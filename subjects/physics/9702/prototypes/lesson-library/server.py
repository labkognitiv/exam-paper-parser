#!/usr/bin/env python3
"""Local unified viewer for active and preserved HTML lessons."""

from __future__ import annotations

import argparse
import json
import mimetypes
import re
from html import unescape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

REPO_ROOT = Path(__file__).resolve().parents[5]
APP_ROOT = Path(__file__).resolve().parent
LESSON_ID = re.compile(r"^(9700|9701|9702)_t\d+_cm\d+_l\d+$")
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
HEADING = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
TAGS = re.compile(r"<[^>]+>")

SOURCES = (
    ("Biology", "9700", REPO_ROOT / "subjects/biology/9700/study"),
    ("Chemistry", "9701", REPO_ROOT / "subjects/chemistry/9701/study"),
    (
        "Physics",
        "9702",
        REPO_ROOT
        / "archive/2026-09-08-root-slimming/artifacts/physics/scroll-lessons/2026-09-08",
    ),
)


def clean_html(value: str) -> str:
    return " ".join(unescape(TAGS.sub(" ", value)).split())


def display_name(path: Path, lesson_id: str) -> str:
    try:
        source = path.read_text(encoding="utf-8", errors="replace")[:100_000]
    except OSError:
        return lesson_id
    for pattern in (TITLE, HEADING):
        match = pattern.search(source)
        if match:
            title = clean_html(match.group(1))
            title = re.sub(r"\s*[|·-]\s*(Kognitiv|Cambridge|Physics|Biology|Chemistry).*$", "", title, flags=re.I)
            if title and title.lower() not in {"lesson", "preview"}:
                return title
    return lesson_id


def topic_name(path: Path) -> str:
    for part in path.parts:
        if re.match(r"^97\d\d_t\d+_", part):
            return re.sub(r"^97\d\d_t\d+_", "", part).replace("_", " ").title()
    return "Other"


def scan_lessons() -> list[dict[str, str]]:
    lessons: list[dict[str, str]] = []
    for subject, code, base in SOURCES:
        if not base.exists():
            continue
        directories = (
            p
            for p in base.rglob("*")
            if p.is_dir()
            and LESSON_ID.fullmatch(p.name)
            and (subject == "Physics" or "archive" not in p.relative_to(base).parts)
        )
        for directory in sorted(directories):
            candidates = [directory / "index.html", directory / "preview.html"]
            candidates.extend(sorted(directory.glob("*.html")))
            page = next((candidate for candidate in candidates if candidate.is_file()), None)
            if page is None:
                continue
            lessons.append(
                {
                    "id": directory.name,
                    "subject": subject,
                    "code": code,
                    "topic": topic_name(directory),
                    "title": display_name(page, directory.name),
                    "source": "Preserved archive" if subject == "Physics" else "Active study",
                    "url": f"/lesson/{directory.name}/{page.name}",
                }
            )
            LESSON_PATHS[directory.name] = directory.resolve()
    return sorted(lessons, key=lambda item: (item["subject"], item["topic"], item["id"]))


LESSON_PATHS: dict[str, Path] = {}
LESSONS = scan_lessons()


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        path = unquote(urlparse(self.path).path)
        if path == "/api/lessons":
            payload = json.dumps(LESSONS, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        if path.startswith("/lesson/"):
            parts = path.split("/")
            if len(parts) < 4 or parts[2] not in LESSON_PATHS:
                self.send_error(404)
                return
            root = LESSON_PATHS[parts[2]]
            requested = root.joinpath(*parts[3:]).resolve()
            if requested != root and root not in requested.parents:
                self.send_error(403)
                return
            if not requested.is_file():
                self.send_error(404)
                return
            mime = mimetypes.guess_type(requested.name)[0] or "application/octet-stream"
            body = requested.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if path in {"/", "/index.html"}:
            self.path = "/dist/index.html"
        super().do_GET()

    def translate_path(self, path: str) -> str:
        clean = urlparse(path).path.lstrip("/")
        return str((APP_ROOT / clean).resolve())

    def log_message(self, format: str, *args: object) -> None:
        if args and str(args[0]).startswith("GET /api"):
            return
        super().log_message(format, *args)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8790)
    args = parser.parse_args()
    print(f"Lesson library: {len(LESSONS)} lessons")
    print(f"Open http://localhost:{args.port}")
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
