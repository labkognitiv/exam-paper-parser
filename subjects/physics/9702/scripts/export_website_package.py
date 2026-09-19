#!/usr/bin/env python3
"""Build a self-contained, development-only Physics website export.

Source files are read-only. Repeat builds are deterministic; changed releases
replace the output only after validation, with the previous package archived.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import tempfile
from datetime import datetime, timezone
from collections import Counter
from urllib.parse import unquote, urlsplit

from validate_migration_selection import (
    audit_questions_and_mappings, collect_active_lessons, canonical_question_paths,
    preferred_markscheme_path, resolve_part_ids,
)

SUBJECT = Path(__file__).resolve().parents[1]
REPO = SUBJECT.parents[2]
OUTPUT = REPO / "migration/physics"
TEMPLATE_ID = "9702_t01_cm02_l05"
HTML_TEMPLATE = REPO / (
    "archive/2026-09-08-root-slimming/artifacts/physics/scroll-lessons/2026-09-08/"
    f"9702_t01_physical_quantities_and_units/{TEMPLATE_ID}/index.html"
)
SCHEMA = "kognitiv_website_test_v1"
SUBJECT_ID = "physics:9702"
ALLOWED_EXTENSIONS = {".json", ".html", ".css", ".js", ".png", ".svg", ".jpg", ".jpeg", ".webp", ".woff", ".woff2", ".ttf"}
URL_RE = re.compile(r"url\(\s*(['\"]?)([^)'\"]+)\1\s*\)")
FIGURE_RE = re.compile(r"\{\{figure:([\w.-]+)\}\}")
BAD_JOIN = {"unresolved", "ambiguous", "invalid_explicit"}


def normalize_question_parts(question):
    """Disambiguate two known OCR identities without changing text or marks."""
    question = copy.deepcopy(question)
    qid = question["question_id"]
    joins = {}
    if qid == "9702_s19_23_q02":
        for index, suffix in [(0, "ai1"), (1, "ai2")]:
            part = question["parts"][index]
            assert part["id"] == qid + "_ai"
            part["source_part_id"] = part["id"]
            part["id"] = qid + "_" + suffix
        joins[qid + "_a_i"] = [qid + "_ai1", qid + "_ai2"]
    elif qid == "9702_s19_23_q06":
        for index, suffix, old in [(3, "bi1", "1."), (4, "bi2", "2."),
                                   (5, "bi3", "3."), (7, "bii1", "1."), (8, "bii2", "2.")]:
            part = question["parts"][index]
            assert part["id"] == qid + "_" + old
            part["source_part_id"] = part["id"]
            part["id"] = qid + "_" + suffix
        joins[qid + "_b_i"] = [qid + "_bi" + str(n) for n in (1, 2, 3)]
        joins[qid + "_b_ii"] = [qid + "_bii" + str(n) for n in (1, 2)]
    question["export_part_joins"] = joins
    return question


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strings(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)
    elif isinstance(value, str):
        yield value


def transform(value, fn):
    if isinstance(value, dict):
        return {key: transform(child, fn) for key, child in value.items()}
    if isinstance(value, list):
        return [transform(child, fn) for child in value]
    return fn(value) if isinstance(value, str) else value


def strip_registry_links(value):
    """Skip formula/definition library links, not instructional prose or maths."""
    if isinstance(value, dict):
        return {
            key: strip_registry_links(child) for key, child in value.items()
            if not (("formula" in key.lower() or "definition" in key.lower())
                    and isinstance(child, (dict, list)))
        }
    if isinstance(value, list):
        return [strip_registry_links(v) for v in value
                if not (isinstance(v, str) and v.startswith(("9702_def_", "9702_formula_")))]
    return value


def strip_old_mapping(value):
    if isinstance(value, dict):
        return {k: strip_old_mapping(v) for k, v in value.items()
                if k not in {"mapping", "taxonomy_tags", "topic_id", "topic_ids", "module_id", "module_ids",
                             "primary_topic_id", "primary_module_id", "lesson_id", "outcome_ids"}}
    if isinstance(value, list):
        return [strip_old_mapping(v) for v in value]
    return value


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for name in ("src", "href"):
            if attrs.get(name):
                (self.links if tag == "a" else self.assets).append(attrs[name])


class Package:
    def __init__(self, root):
        self.root = root
        self.sources = {}
        self.files = {}
        self.counts = Counter()
        self.asset_aliases = []
        self.translations = read_json(SUBJECT / "migration/part-id-translations.json")
        self.overrides = {x["question_id"]: x for x in read_json(SUBJECT / "migration/mapping-overrides.json")["records"]}
        self.lesson_info = {}
        self.outcome_lessons = {}
        self.mappings = []

    def source(self, path):
        path = Path(path)
        key = path.relative_to(REPO).as_posix()
        self.sources.setdefault(key, digest(path))
        return path

    def load(self, path):
        return read_json(self.source(path))

    def save(self, relative, value, kind, identity):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(value, (dict, list)):
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        elif isinstance(value, str):
            path.write_text(value, encoding="utf-8")
        else:
            path.write_bytes(value)
        key = Path(relative).as_posix()
        assert key not in self.files, f"Duplicate output path: {key}"
        self.files[key] = {"path": key, "kind": kind, "id": identity, "sha256": digest(path), "bytes": path.stat().st_size}
        return key

    def copy_asset(self, source, relative, identity):
        return self.save(relative, self.source(source).read_bytes(), "asset", identity)

    def curriculum(self):
        topics, modules, outcomes, lessons = [], [], [], []
        aliases = self.load(SUBJECT / "study/lesson-id-redirects.json")["aliases"]
        for topic_dir in sorted((SUBJECT / "study/topics").iterdir()):
            if not (topic_dir / "syllabus.json").is_file():
                continue
            syllabus = self.load(topic_dir / "syllabus.json")
            topic = syllabus["topic"]
            tid = topic["topic_id"]
            topics.append({"id": tid, "title": topic["topic_name"], "sequence": topic["topic_number"], "level": syllabus["level"]})
            for outcome in syllabus["learning_outcomes"]:
                outcomes.append({"id": outcome["outcome_id"], "title": outcome["outcome_text"], "topic_id": tid,
                                 "module_id": outcome["module_id"], "sequence": outcome["outcome_number"]})
            for mp in sorted(topic_dir.glob("modules/*/module.json")):
                m = self.load(mp)
                modules.append({"id": m["module_id"], "title": m["module_name"], "kind": "syllabus",
                                "parent_id": tid, "sequence": m["module_number"], "outcome_ids": m["learning_outcome_ids"]})
            for mp in sorted(topic_dir.glob("course-modules/*/module.json")):
                m = self.load(mp)
                modules.append({"id": m["course_module_id"], "title": m["title"], "kind": "teaching",
                                "parent_id": tid, "sequence": m["sequence"], "lesson_ids": m["lesson_ids"],
                                "outcome_ids": m["learning_outcome_ids"]})
            lesson_map = self.load(topic_dir / "lesson-knowledge-map.json")
            for index, lesson in enumerate(lesson_map["lessons"], 1):
                lid = lesson["lesson_id"]
                paths = list(topic_dir.glob(f"course-modules/*/lessons/{lid}/lesson.json"))
                assert len(paths) == 1, lid
                spec = self.load(paths[0])
                mid = spec["course_module_id"]
                directory = Path("study") / tid / mid / lid
                previous = list(dict.fromkeys(aliases.get(x, x) for x in spec.get("prerequisites", {}).get("previous_lesson_ids", [])))
                previous = [x for x in previous if x != lid]
                info = {"id": lid, "title": lesson["title"], "sequence": index, "parent_id": mid,
                        "topic_id": tid, "level": syllabus["level"], "outcome_ids": lesson["outcome_ids"],
                        "prerequisite_lesson_ids": previous, "status": "test_fixture",
                        "path": (directory / f"{lid}.lesson.json").as_posix()}
                lessons.append(info)
                self.lesson_info[lid] = (info, directory)
                for outcome in info["outcome_ids"]:
                    self.outcome_lessons.setdefault(outcome, set()).add(lid)
        references = {}
        for filename, key, id_key in [("skills", "skills", "skill_id"), ("question-patterns", "patterns", "pattern_id")]:
            records = self.load(SUBJECT / f"knowledge/knowledge-base/{filename}.json")[key]
            references[key] = [{"id": x[id_key], "title": x["name"], "description": x.get("description", "")} for x in records]
        self.counts.update(topics=len(topics), syllabus_modules=sum(m["kind"] == "syllabus" for m in modules),
                           teaching_modules=sum(m["kind"] == "teaching" for m in modules), lessons=len(lessons), outcomes=len(outcomes))
        self.save("curriculum.json", {"schema_version": SCHEMA, "subject_id": SUBJECT_ID, "title": "Physics",
                  "syllabus_code": "9702", "syllabus_years": "2025-2027", "levels": ["AS", "A2"],
                  "components": ["p1", "p2", "p4"], "topics": topics, "modules": modules, "lessons": lessons,
                  "learning_outcomes": outcomes, "lesson_redirects": aliases, **references}, "curriculum", SUBJECT_ID)

    def html_lesson(self, info, directory):
        lid, title = info["id"], info["title"]
        original = self.source(HTML_TEMPLATE).read_text(encoding="utf-8")
        parser = LinkParser()
        parser.feed(original)
        dependencies = {}

        def dependency(source):
            source = Path(source)
            assert source.is_file(), source
            if source in dependencies:
                return dependencies[source]
            assert source.suffix in ALLOWED_EXTENSIONS and source.suffix not in {".html", ".json"}
            source_relative = source.relative_to(HTML_TEMPLATE.parent)
            filename = lid + "_" + re.sub(r"[^a-zA-Z0-9._-]", "_", source_relative.as_posix())
            relative = directory / "assets" / filename
            dependencies[source] = relative
            if source.suffix == ".css":
                css = self.source(source).read_text()
                def replace_url(match):
                    url = match.group(2).strip()
                    assert not urlsplit(url).scheme, url
                    target = dependency(source.parent / unquote(urlsplit(url).path))
                    return f'url("{target.name}")'
                css = URL_RE.sub(replace_url, css)
                self.save(relative, css, "asset", filename)
            else:
                self.copy_asset(source, relative, filename)
            return relative

        for url in parser.assets:
            assert not urlsplit(url).scheme, url
            dest = dependency(HTML_TEMPLATE.parent / unquote(urlsplit(url).path))
            original = original.replace(f'"{url}"', f'"assets/{dest.name}"')
        document = original.replace(TEMPLATE_ID, lid)
        document = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)} | Test lesson</title>", document, flags=re.S)
        document = re.sub(r"<h1>.*?</h1>", f"<h1>{html.escape(title)}</h1>", document, count=1, flags=re.S)
        document = re.sub(r'<nav\b[^>]*class="[^"]*(?:topic-navigation|lesson-nav)[^"]*"[^>]*>.*?</nav>', "", document, flags=re.S)
        # Original cross-lesson links must never escape this independently copied package.
        document = re.sub(r'<a\b[^>]*href="\.\.[^"]*"[^>]*>.*?</a>', "", document, flags=re.S)
        document = re.sub(r'<div class="top">.*?</div>', '<div class="top"><strong>Kognitiv · Physics 9702</strong><span>Development test</span></div>', document, count=1, flags=re.S)
        document = re.sub(r'<p class="kicker">.*?</p>', f'<p class="kicker">{html.escape(lid)}</p>', document, count=1, flags=re.S)
        banner = ('<aside role="note" style="padding:12px 18px;background:#fff3cd;color:#533f03;border:1px solid #d6b854;">'
                  '<strong>Test content.</strong> This lesson contains a copied example: Checking equation homogeneity. '
                  'It is not the finished lesson for this topic.</aside>')
        document = document.replace("<body>", '<body data-content-status="test_fixture">' + banner, 1)
        html_path = self.save(directory / f"{lid}.html", document, "lesson_html", lid)
        return html_path, [p.as_posix() for p in dependencies.values()]

    def lessons(self):
        source_manifest = next((SUBJECT / "study/topics").glob(f"*/course-modules/*/lessons/{TEMPLATE_ID}/practice-questions/manifest.json"))
        template = self.load(source_manifest)
        source_questions = [self.load(source_manifest.parent / f"{qid}.json") for qid in template["question_ids"]]
        assert len(source_questions) == 20
        assert not any("FIGURE PLACEHOLDER" in s for q in source_questions for s in strings(q))
        for lid, (info, directory) in self.lesson_info.items():
            html_path, assets = self.html_lesson(info, directory)
            practice_ids = []
            for source in source_questions:
                data = transform(copy.deepcopy(source), lambda s: s.replace(TEMPLATE_ID, lid))
                qid = data["question_id"]
                practice_ids.append(qid)
                qdir = directory / "practice" / qid
                fixture = {"status": "test_fixture", "template_lesson_id": TEMPLATE_ID,
                           "template_question_id": source["question_id"], "curriculum_alignment": "not_asserted"}
                parts = []
                for n, part in enumerate(data.get("response_structure", {}).get("parts", []), 1):
                    parts.append({"id": f"{qid}_part{n:02}", "label": part.get("part", part.get("part_id")), "marks": part["marks"],
                                  "text": part.get("description", "")})
                q = {"schema_version": SCHEMA, "id": qid, "subject_id": SUBJECT_ID, "kind": "lesson_practice",
                     "lesson_id": lid, "sequence": data["sequence"], "question_type": data["question_type"],
                     "difficulty": data["difficulty"], "total_marks": data["marks"], "prompt": data["prompt"],
                     "parts": parts, "figures": [], "fixture": fixture}
                if "options" in data:
                    q["options"] = [{"id": str(i), "label": chr(64+i), "text": text} for i, text in enumerate(data["options"], 1)]
                    q["response_schema"] = {"type": "single-choice", "required": True, "option_ids": [x["id"] for x in q["options"]]}
                label_ids = {p["label"]: p["id"] for p in parts}
                ms = {"schema_version": SCHEMA, "id": qid, "question_id": qid, "total_marks": data["marks"],
                      "answer": data.get("answer"), "marking_points": data.get("mark_scheme", []),
                      "parts": [{"question_part_ids": [p["id"]], "label": p["label"], "marks": p["marks"]} for p in parts],
                      "fixture": fixture}
                if data["question_type"] == "mcq":
                    ms["correct_option_id"] = str(data["answer"]["correct_option"])
                e = {"schema_version": SCHEMA, "id": qid, "question_id": qid, "hints": data.get("hints", []),
                     "solution": data.get("solution"), "teacher_walkthrough": data.get("teacher_walkthrough", []),
                     "distractor_explanations": data.get("distractor_explanations", []),
                     "parts": [{"label": part.get("part", part.get("part_id")),
                                **{k: v for k, v in part.items() if k not in {"part", "part_id"}},
                                "question_part_ids": [label_ids[part.get("part", part.get("part_id"))]]}
                               for part in data.get("part_enrichment", [])],
                     "fixture": fixture}
                for suffix, record in [("question", q), ("markscheme", ms), ("enrichment", e)]:
                    self.save(qdir / f"{qid}.{suffix}.json", record, suffix, qid)
                self.counts["practice_questions"] += 1
            self.save(directory / f"{lid}.lesson.json", {"schema_version": SCHEMA, "subject_id": SUBJECT_ID,
                      **{k: v for k, v in info.items() if k != "path"}, "html_path": html_path, "asset_paths": assets,
                      "practice_question_ids": practice_ids, "fixture_template_lesson_id": TEMPLATE_ID}, "lesson", lid)

    def linked_parts(self, source_parts, question, kind):
        result = []
        ids = {p["id"] for p in question.get("parts", [])}
        for part in source_parts:
            source_id = part.get("id") if kind == "markscheme" else part.get("part_id", part.get("id"))
            if kind == "enrichment" and source_id in self.translations.get("excluded_enrichment_parts", {}):
                continue
            method, targets = resolve_part_ids(source_id, ids, {**self.translations["translations"], **question.get("export_part_joins", {})})
            assert method not in BAD_JOIN, (question["question_id"], source_id, method)
            record = copy.deepcopy(part)
            record.pop("id", None)
            record.pop("part_id", None)
            result.append({**record, "source_part_id": source_id, "question_part_ids": targets})
        return result

    def mapping(self, component, qid, question, enrichment):
        if component == "p1":
            mapping = enrichment["mapping"]
            candidates = set()
            for oid in mapping.get("outcome_ids", []):
                candidates.update(self.outcome_lessons.get(oid, []))
            return {"question_id": qid, "authority": "canonical_p1_enrichment", **mapping,
                    "lesson_candidate_ids": sorted(candidates), "primary_lesson_id": None,
                    "lesson_assignment_status": "candidates_only"}
        review = self.load(SUBJECT / f"reviews/question-primary-lesson-mapping/{component}/{qid}.json")
        override = self.overrides.get(qid)
        selected = override or review
        primary = selected["primary_lesson_id"]
        assert primary in self.lesson_info
        source_parts = ([{"part_id": p, "lesson_id": l} for p, l in override["part_lesson_ids"].items()]
                        if override else review["part_lesson_mappings_unchanged"])
        mapped = self.linked_parts(source_parts, question, "mapping")
        for part in mapped:
            lid = part["lesson_id"]
            lesson, _ = self.lesson_info[lid]
            part["topic_id"] = lesson["topic_id"]
            part["course_module_id"] = lesson["parent_id"]
        return {"question_id": qid, "authority": "development_override" if override else "reviewed_primary_lesson_mapping",
                "primary_lesson_id": primary, "primary_topic_id": self.lesson_info[primary][0]["topic_id"],
                "confidence": selected.get("confidence"), "review_required": bool(override) or selected.get("confidence") == "low",
                "parts": mapped}

    def question_assets(self, source, directory, qid, component):
        compact = source.with_suffix(".png") if component == "p1" else source.parent / "question_compact.png"
        image_path = self.copy_asset(compact, directory / f"{qid}.question.png", f"{qid}:question")
        figures = []
        aliases = {}
        for image in (sorted(p for p in source.parent.glob("*.png")
                             if not p.name.startswith(("question", "markscheme"))) if component != "p1" else []):
            short = image.stem.replace("fig_", "figure_", 1) if image.stem.startswith("fig_") else image.stem
            fid = f"{qid}_{short}"
            path = self.copy_asset(image, directory / "assets" / f"{fid}.png", fid)
            figures.append({"id": fid, "path": path})
            aliases[image.stem] = fid
            aliases[image.stem.replace("figure_", "fig_", 1)] = fid
        return image_path, figures, aliases

    def corrected_scheme_image(self, source, output_path, qid):
        """Re-extract the three known faulty images, keeping locked sources intact."""
        import fitz
        from PIL import Image
        crops = {
            "9702_m19_22_q02": [(4, (52, 240, 794, 389)), (5, (52, 49, 794, 356))],
            "9702_m20_22_q04": [(11, (52, 245, 794, 543))],
            "9702_w18_41_q10": [(10, (58, 326, 789, 469))],
        }
        meta = self.load(source.parent / "markscheme_ocr_review_meta.json")
        pdf = self.source(source.parent / meta["source_pdf"])
        images = []
        with fitz.open(pdf) as doc:
            for page_no, box in crops[qid]:
                pixmap = doc[page_no-1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
                page_image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
                images.append(page_image.crop(tuple(round(v*2) for v in box)))
        combined = Image.new("RGB", (max(im.width for im in images), sum(im.height for im in images)+16*(len(images)-1)), "white")
        y = 0
        for im in images:
            combined.paste(im, (0, y))
            y += im.height + 16
        import io
        buffer = io.BytesIO()
        combined.save(buffer, format="PNG")
        return self.save(output_path, buffer.getvalue(), "asset", f"{qid}:markscheme")

    def papers(self):
        paper_records = {}
        for component, paths in canonical_question_paths(SUBJECT).items():
            for source in paths:
                question = normalize_question_parts(self.load(source))
                qid, pid = question["question_id"], question["paper_code"]
                leaf = source.parent.parent
                relative_leaf = leaf.relative_to(SUBJECT / "past papers")
                paper_dir = Path("past-papers") / relative_leaf
                directory = paper_dir / qid
                image_path, figures, aliases = self.question_assets(source, directory, qid, component)

                def rewrite(s):
                    def figure_token(match):
                        old = match.group(1)
                        assert old in aliases, (qid, old)
                        if old.startswith("fig_"):
                            self.asset_aliases.append({"question_id": qid, "source_id": old, "export_id": aliases[old]})
                        return "{{figure:" + aliases[old] + "}}"
                    s = FIGURE_RE.sub(figure_token, s)
                    if s in aliases:
                        return aliases[s]
                    if s.endswith(".png") and not s.startswith("data:"):
                        if Path(s).stem in aliases:
                            return next(f["path"] for f in figures if f["id"] == aliases[Path(s).stem])
                        if Path(s).name.startswith("question"):
                            return image_path
                    return s

                if component == "p1":
                    enrichment = self.load(leaf / "enrichment" / f"{qid}.enrichment.json")
                    record = {"prompt": question["question_text"], "options": question["response_schema"]["options"],
                              "response_schema": question["response_schema"], "parts": [], "total_marks": 1}
                    marks = {"total_marks": 1, "correct_answer": question["correct_answer"], "parts": []}
                    ms_image = None
                    ms_kind = "official_answer_key"
                    self.source(source.parent / "answer_key.json")
                else:
                    enrichment = self.load(source.parent / "enrichment.json")
                    # Preserve question context, nested tables and response data without raw pipeline records.
                    keys = {"question_stem", "question_stem_latex", "parts", "total_marks", "content_flow", "answer_prompt", "response_schema", "review_flags", "numerical_values_checked"}
                    record = {k: v for k, v in question.items() if k in keys}
                    effective = preferred_markscheme_path(source.parent)
                    scheme = self.load(effective)
                    if effective.name == "markscheme_reviewed.json":
                        self.source(source.parent / "markscheme_review_meta.json")
                    marks = {k: v for k, v in scheme.items() if k not in {"schema_version", "parts", "paper_code", "question_id", "question_num"}}
                    marks["parts"] = self.linked_parts(scheme["parts"], question, "markscheme")
                    ms_image = directory / f"{qid}.markscheme.png"
                    if effective.name == "markscheme_ocr_reviewed.json":
                        ms_image = self.corrected_scheme_image(source, ms_image, qid)
                        ms_kind = "source_verified_ocr_reconciliation"
                    else:
                        ms_image = self.copy_asset(source.parent / "markscheme.png", ms_image, f"{qid}:markscheme")
                        ms_kind = "approved_reconciliation" if effective.name != "markscheme.json" else "official_extraction"
                self.mappings.append(self.mapping(component, qid, question, enrichment))
                e = strip_registry_links(strip_old_mapping(copy.deepcopy(enrichment)))
                e.pop("schema_version", None)
                if component != "p1":
                    e["parts"] = self.linked_parts(e.get("parts", []), question, "enrichment")
                record = transform(record, rewrite)
                e = transform(e, rewrite)
                marks = transform(marks, rewrite)
                common = {"schema_version": SCHEMA, "id": qid, "question_id": qid, "subject_id": SUBJECT_ID}
                record = {**record, **common, "kind": "past_paper", "paper_id": pid,
                          "sequence": question["question_num"], "question_image": image_path, "figures": figures}
                marks = {**marks, **common, "image_path": ms_image, "source_kind": ms_kind}
                e = {**e, **common}
                for suffix, data in [("question", record), ("markscheme", marks), ("enrichment", e)]:
                    self.save(directory / f"{qid}.{suffix}.json", data, suffix, qid)
                entry = paper_records.setdefault(pid, {"schema_version": SCHEMA, "id": pid, "subject_id": SUBJECT_ID,
                    "component": component, "year": int(relative_leaf.parts[1]), "session": relative_leaf.parts[2],
                    "variant": int(relative_leaf.parts[3].split("-")[1]), "question_ids": [], "total_marks": 0,
                    "path": paper_dir / f"{pid}.paper.json"})
                entry["question_ids"].append(qid)
                entry["total_marks"] += record["total_marks"]
                self.counts["past_paper_questions"] += 1
        for pid, record in sorted(paper_records.items()):
            path = record.pop("path")
            record["question_ids"].sort()
            assert record["total_marks"] == {"p1": 40, "p2": 60, "p4": 100}[record["component"]], pid
            self.save(path, record, "paper", pid)
        self.counts["papers"] = len(paper_records)
        self.save("mappings.json", {"schema_version": SCHEMA, "subject_id": SUBJECT_ID,
                  "question_mappings": self.mappings,
                  "excluded_enrichment_parts": self.translations.get("excluded_enrichment_parts", {}),
                  "unavailable_enrichment_question_parts": self.translations.get("unavailable_enrichment_question_parts", {})}, "mappings", SUBJECT_ID)

    def finish(self):
        for p in sorted((SUBJECT / "migration").glob("*.json")):
            self.source(p)
        files = sorted(self.files.values(), key=lambda x: x["path"])
        release_hash = hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
        manifest = {"schema_version": SCHEMA, "subject_id": SUBJECT_ID, "release_id": f"physics-9702-test-{release_hash[:16]}",
                    "environment": "development_only", "contains_test_fixtures": True,
                    "fixture_template_lesson_id": TEMPLATE_ID,
                    "excluded_libraries": ["formulas", "definitions"],
                    "counts": dict(self.counts), "files": files,
                    "source_hashes": dict(sorted(self.sources.items())),
                    "figure_aliases_fixed": list({(x["question_id"], x["source_id"]): x for x in self.asset_aliases}.values()),
                    "mapping_review_required": sum(x.get("review_required", False) for x in self.mappings),
                    "storage_paths": "JSON asset paths are relative to this package root; HTML dependencies are relative to their HTML/CSS files.",
                    "update_policy": "Upsert by subject_id + entity kind + stable id; publish a verified release after its assets. Never infer database deletions from absent files.",
                    "database_schema_verified": False}
        (self.root / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")
        return manifest


def validate_package(root):
    manifest = read_json(root / "manifest.json")
    errors = []
    by_kind = {}
    file_paths = {x["path"] for x in manifest["files"]}
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    if actual != file_paths | {"manifest.json"}:
        errors.append("Package files differ from manifest")
    for file in manifest["files"]:
        p = root / file["path"]
        if p.is_symlink() or p.suffix not in ALLOWED_EXTENSIONS:
            errors.append(f"Disallowed file: {p}")
        if not p.is_file() or digest(p) != file["sha256"]:
            errors.append(f"Hash/missing file: {p}")
            continue
        if p.suffix == ".json":
            d = read_json(p)
            if file["kind"] in {"question", "markscheme", "enrichment", "lesson", "paper"}:
                key = (file["kind"], d["id"])
                if key in by_kind:
                    errors.append(f"Duplicate entity {key}")
                by_kind[key] = (p, d)
        elif p.suffix == ".html":
            parser = LinkParser()
            parser.feed(p.read_text())
            for url in parser.assets + parser.links:
                parsed = urlsplit(url)
                if parsed.scheme or parsed.netloc:
                    errors.append(f"External HTML dependency: {url}")
                if parsed.path and not (p.parent / unquote(parsed.path)).is_file():
                    errors.append(f"Broken HTML link: {p}:{url}")
                if not parsed.path and parsed.fragment and parsed.fragment not in parser.ids:
                    errors.append(f"Broken HTML anchor: {p}:{url}")
            if 'data-content-status="test_fixture"' not in p.read_text():
                errors.append(f"Unlabelled fixture HTML: {p}")
        elif p.suffix == ".css":
            for match in URL_RE.finditer(p.read_text()):
                url = match.group(2).strip()
                if urlsplit(url).scheme or not (p.parent / unquote(urlsplit(url).path)).is_file():
                    errors.append(f"Broken CSS dependency: {p}:{url}")
    lessons = {identity for kind, identity in by_kind if kind == "lesson"}
    for (kind, identity), (p, d) in by_kind.items():
        if kind == "lesson":
            if d["html_path"] not in file_paths:
                errors.append(f"Missing lesson HTML: {identity}")
            if len(d["practice_question_ids"]) != 20 or any(("question", x) not in by_kind for x in d["practice_question_ids"]):
                errors.append(f"Missing practice copies: {identity}")
            if any(x not in lessons for x in d["prerequisite_lesson_ids"]):
                errors.append(f"Unknown lesson prerequisite: {identity}")
        if kind != "question":
            continue
        if ("markscheme", identity) not in by_kind or ("enrichment", identity) not in by_kind:
            errors.append(f"Missing question companion: {identity}")
            continue
        parts = [part["id"] for part in d["parts"]]
        if len(parts) != len(set(parts)):
            errors.append(f"Duplicate question part: {identity}")
        if d["parts"] and sum(part.get("marks", 0) or 0 for part in d["parts"]) != d["total_marks"]:
            errors.append(f"Question mark total mismatch: {identity}")
        for name in ("markscheme", "enrichment"):
            companion = by_kind[(name, identity)][1]
            for part in companion.get("parts", []):
                if not part.get("question_part_ids") or any(x != identity and x not in parts for x in part["question_part_ids"]):
                    errors.append(f"Broken {name} part join: {identity}")
            if name == "markscheme" and companion["total_marks"] != d["total_marks"]:
                errors.append(f"Mark-scheme total mismatch: {identity}")
            if companion.get("image_path") and companion["image_path"] not in file_paths:
                errors.append(f"Missing mark-scheme image: {identity}")
        figure_ids = {f["id"] for f in d["figures"]}
        for s in strings(d):
            for fid in FIGURE_RE.findall(s):
                if fid not in figure_ids:
                    errors.append(f"Broken figure token: {identity}:{fid}")
        for asset in ([d["question_image"]] if d.get("question_image") else []) + [f["path"] for f in d["figures"]]:
            if asset not in file_paths:
                errors.append(f"Missing question asset: {asset}")
        if d["kind"] == "lesson_practice" and (d["lesson_id"] not in lessons or d["fixture"]["status"] != "test_fixture"):
            errors.append(f"Invalid fixture ownership: {identity}")
    mappings = read_json(root / "mappings.json")
    for mapping in mappings["question_mappings"]:
        qid = mapping["question_id"]
        if ("question", qid) not in by_kind:
            errors.append(f"Mapping to missing question: {qid}")
        if mapping.get("primary_lesson_id") and mapping["primary_lesson_id"] not in lessons:
            errors.append(f"Mapping to missing lesson: {qid}")
        for part in mapping.get("parts", []):
            valid = {p["id"] for p in by_kind[("question", qid)][1]["parts"]} | {qid}
            if part["lesson_id"] not in lessons or not set(part["question_part_ids"]).issubset(valid):
                errors.append(f"Invalid part mapping: {qid}")
    expected = {"lessons": 147, "practice_questions": 2940, "past_paper_questions": 4016, "papers": 207}
    actual_counts = {
        "lessons": len(lessons),
        "practice_questions": sum(kind == "question" and data[1].get("kind") == "lesson_practice" for (kind, _), data in by_kind.items()),
        "past_paper_questions": sum(kind == "question" and data[1].get("kind") == "past_paper" for (kind, _), data in by_kind.items()),
        "papers": sum(kind == "paper" for kind, _ in by_kind),
    }
    for name, count in expected.items():
        if manifest["counts"].get(name) != count or actual_counts[name] != count:
            errors.append(f"Incorrect {name} count")
    if errors:
        raise ValueError(f"{len(errors)} package errors:\n" + "\n".join(errors[:30]))
    return {"status": "PASS", "release_id": manifest["release_id"], "files": len(file_paths)+1, **manifest["counts"]}


def build():
    active, duplicates = collect_active_lessons(SUBJECT)
    assert not duplicates
    audit = audit_questions_and_mappings(SUBJECT, active)
    for key in ["unreadable", "duplicate_question_ids", "part_id_join_issues", "enrichment_part_id_join_issues", "effective_markscheme_part_id_join_issues"]:
        assert not audit.get(key), (key, audit.get(key))
    testing = SUBJECT / "testing"
    with tempfile.TemporaryDirectory(prefix="website-export-", dir=testing) as temporary:
        staging = Path(temporary) / "physics"
        staging.mkdir()
        package = Package(staging)
        package.curriculum()
        package.lessons()
        package.papers()
        manifest = package.finish()
        report = validate_package(staging)
        # Recheck source hashes at publication: concurrent authoring cannot mix snapshots silently.
        for relative, hashed in package.sources.items():
            assert digest(REPO / relative) == hashed, f"Source changed during export: {relative}"
        if (OUTPUT / "manifest.json").is_file():
            old = read_json(OUTPUT / "manifest.json")
            if old["release_id"] == manifest["release_id"]:
                validate_package(OUTPUT)
                print(json.dumps({**report, "action": "unchanged"}))
                return
        if OUTPUT.exists() and any(OUTPUT.iterdir()):
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M%S-%f")
            backup = REPO / "archive" / f"{stamp}-physics-website-export" / "physics"
            backup.parent.mkdir(parents=True)
            shutil.move(str(OUTPUT), str(backup))
            (backup.parent / "manifest.json").write_text(json.dumps({"reason": "Superseded generated website package", "original_path": "migration/physics", "retained_path": "physics"}, indent=2)+"\n")
        elif OUTPUT.exists():
            OUTPUT.rmdir()  # Empty destination only; no source or package content is deleted.
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(staging), str(OUTPUT))
        print(json.dumps({**report, "action": "built", "output": str(OUTPUT)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.validate_only:
        print(json.dumps(validate_package(OUTPUT)))
    else:
        build()
