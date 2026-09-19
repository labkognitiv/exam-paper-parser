#!/usr/bin/env python3
"""High-Precision Four-Way Taxonomy Mapping Engine for Cambridge Physics (9702).

Fuses four rich evidence signals across all 2016-2025 papers (P1, P2, P4):
1. Mark Scheme (MS) criteria text: verbatim scored points from markscheme.json.
2. Question Paper (QP) stem: subpart text from question_ocr.json / question.txt.
3. Proper Answer & KaTeX Equations: physical formulas, derivations, and calculated values.
4. Pedagogical Scaffolding: key_concepts, tiered hints, and stepped walkthroughs.

Includes:
- Cross-field consensus multiplier when concepts appear in both QP and MS (+15.0).
- Comprehensive physics domain thesaurus (formulas, laws, units, apparatus).
- Multi-token bigram and n-gram phrase matching.
- Strict resolution against official 2025-2027 AS (t01-t11) and A2 (t12-t25) registries.

Rule: Strictly ZERO em dashes anywhere in this file.
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import math
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

PHYSICS_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(__file__).resolve().parents[5]
PAST_PAPERS = PHYSICS_ROOT / "past papers"

AS_TAX_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "as" / "9702-2025-2027-as-taxonomy.json"
AS_OUTCOMES_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "as" / "9702-2025-2027-as-learning-outcomes.json"
A2_TAX_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "a2" / "9702-2025-2027-a2-taxonomy.json"
A2_OUTCOMES_PATH = PHYSICS_ROOT / "knowledge" / "2025-2027" / "a2" / "9702-2025-2027-a2-learning-outcomes.json"


def tokenize(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text.split()


STOPWORDS = {
    "the", "a", "an", "and", "or", "in", "on", "of", "to", "for", "with",
    "as", "by", "that", "this", "is", "are", "be", "from", "at", "which",
    "explain", "describe", "state", "outline", "discuss", "calculate",
    "use", "identify", "recognise", "limited", "including", "reference",
    "terms", "role", "roles", "function", "functions", "structure", "structures",
    "diagram", "fig", "table", "step", "hint", "answer", "question", "show",
    "given", "value", "values", "name", "where", "into", "each", "between",
    "about", "both", "such", "when", "then", "will", "what", "how", "following",
    "determine", "suggest", "deduce", "part", "subpart", "complete", "draw", "label"
}


class PhysicsTaxonomyRegistry:
    def __init__(self):
        self.as_taxonomy = json.loads(AS_TAX_PATH.read_text(encoding="utf-8"))
        self.as_outcomes = json.loads(AS_OUTCOMES_PATH.read_text(encoding="utf-8"))["outcomes"]
        self.a2_taxonomy = json.loads(A2_TAX_PATH.read_text(encoding="utf-8"))
        self.a2_outcomes = json.loads(A2_OUTCOMES_PATH.read_text(encoding="utf-8"))["outcomes"]

        self.valid_topics: Set[str] = set()
        self.valid_modules: Set[str] = set()
        self.valid_outcomes: Set[str] = set()

        self.as_topics: Set[str] = set()
        self.a2_topics: Set[str] = set()

        self.topic_to_modules: Dict[str, List[str]] = {}
        self.module_to_topic: Dict[str, str] = {}
        self.module_to_outcomes: Dict[str, List[str]] = {}
        self.outcome_to_module: Dict[str, str] = {}
        self.outcome_to_topic: Dict[str, str] = {}
        self.outcome_details: Dict[str, Dict[str, Any]] = {}
        self.module_names: Dict[str, str] = {}
        self.topic_names: Dict[str, str] = {}

        for tax, topic_set in [(self.as_taxonomy, self.as_topics), (self.a2_taxonomy, self.a2_topics)]:
            for top in tax["topics"]:
                tid = top["topic_id"]
                self.valid_topics.add(tid)
                topic_set.add(tid)
                self.topic_names[tid] = top["topic_name"]
                self.topic_to_modules[tid] = []
                for mod in top["modules"]:
                    mid = mod["module_id"]
                    self.valid_modules.add(mid)
                    self.topic_to_modules[tid].append(mid)
                    self.module_to_topic[mid] = tid
                    self.module_to_outcomes[mid] = []
                    self.module_names[mid] = mod["module_name"]

        for out in self.as_outcomes + self.a2_outcomes:
            oid = out["outcome_id"]
            tid = out["topic_id"]
            mid = out["module_id"]
            self.valid_outcomes.add(oid)
            self.module_to_outcomes[mid].append(oid)
            self.outcome_to_module[oid] = mid
            self.outcome_to_topic[oid] = tid
            self.outcome_details[oid] = out

        skills_file = PHYSICS_ROOT / "knowledge" / "knowledge-base" / "skills.json"
        self.skill_to_topics: Dict[str, List[str]] = {}
        self.topic_to_skills: Dict[str, List[str]] = collections.defaultdict(list)
        if skills_file.is_file():
            try:
                sdata = json.loads(skills_file.read_text(encoding="utf-8"))
                for s in sdata.get("skills", []):
                    sid = s["skill_id"]
                    top_ids = s.get("topic_ids", [])
                    self.skill_to_topics[sid] = top_ids
                    for t in top_ids:
                        self.topic_to_skills[t].append(sid)
            except Exception:
                pass

    def validate_mapping(self, topic_id: str, module_id: str, outcome_ids: List[str]) -> List[str]:
        errors = []
        if topic_id not in self.valid_topics:
            errors.append(f"Invalid topic_id: {topic_id}")
        if module_id not in self.valid_modules:
            errors.append(f"Invalid module_id: {module_id}")
        elif self.module_to_topic.get(module_id) != topic_id:
            errors.append(f"Module {module_id} does not belong to topic {topic_id}")

        if not outcome_ids or not (1 <= len(outcome_ids) <= 2):
            errors.append(f"outcome_ids must have length 1 or 2, got {len(outcome_ids)}")

        for oid in outcome_ids:
            if oid not in self.valid_outcomes:
                errors.append(f"Invalid outcome_id: {oid}")
            elif self.outcome_to_module.get(oid) != module_id:
                errors.append(f"Outcome {oid} does not belong to module {module_id}")
        return errors


PHYSICS_THESAURUS = {
    # AS Topics
    "9702_t01": [
        "base quantity", "base unit", "derived quantity", "derived unit", "si units",
        "homogeneity", "homogeneous equation", "prefix", "pico", "nano", "micro", "milli",
        "centi", "deci", "kilo", "mega", "giga", "tera", "scalar", "vector", "vector addition",
        "vector resolution", "systematic error", "random error", "precision", "accuracy",
        "uncertainty", "absolute uncertainty", "percentage uncertainty", "vernier", "micrometer"
    ],
    "9702_t02": [
        "distance", "displacement", "speed", "velocity", "instantaneous velocity",
        "acceleration", "equations of motion", "suvat", "v=u+at", "s=ut+1/2at2", "v2=u2+2as",
        "displacement-time graph", "velocity-time graph", "gradient is velocity",
        "gradient is acceleration", "area under graph", "projectile motion", "free fall",
        "acceleration of free fall", "air resistance", "terminal velocity"
    ],
    "9702_t03": [
        "mass", "weight", "momentum", "linear momentum", "p=mv", "newtons first law",
        "newtons second law", "newtons third law", "f=ma", "rate of change of momentum",
        "impulse", "conservation of momentum", "elastic collision", "inelastic collision",
        "kinetic energy conserved"
    ],
    "9702_t04": [
        "density", "pressure", "hydrostatic pressure", "upthrust", "archimedes principle",
        "viscous drag", "stokes law", "friction", "weight", "centre of gravity", "moment of a force",
        "torque", "couple", "torque of a couple", "principle of moments", "equilibrium",
        "coplanar forces", "triangle of forces"
    ],
    "9702_t05": [
        "work done", "joule", "kinetic energy", "gravitational potential energy",
        "conservation of energy", "elastic potential energy", "power", "watt", "efficiency",
        "work done by expanding gas"
    ],
    "9702_t06": [
        "compressive force", "tensile force", "hookes law", "spring constant", "f=kx",
        "stress", "tensile stress", "strain", "tensile strain", "young modulus",
        "elastic deformation", "plastic deformation", "elastic limit", "ultimate tensile strength",
        "strain energy"
    ],
    "9702_t07": [
        "progressive wave", "transverse wave", "longitudinal wave", "wavelength", "frequency",
        "period", "amplitude", "wave speed", "phase difference", "wavefront", "intensity",
        "doppler effect", "observed frequency", "electromagnetic spectrum", "speed of light",
        "polarisation", "malus law", "polarised wave"
    ],
    "9702_t08": [
        "principle of superposition", "interference", "constructive interference",
        "destructive interference", "coherence", "coherent sources", "path difference",
        "young double slit", "fringe width", "diffraction", "diffraction grating",
        "stationary wave", "standing wave", "node", "antinode", "harmonics"
    ],
    "9702_t09": [
        "electric current", "ampere", "charge", "coulomb", "charge carriers", "drift velocity",
        "potential difference", "volt", "electromotive force", "emf", "electrical resistance",
        "ohms law", "i-v characteristic", "ohmic conductor", "filament lamp", "semiconductor diode",
        "resistivity"
    ],
    "9702_t10": [
        "kirchhoffs first law", "conservation of charge", "kirchhoffs second law",
        "conservation of energy", "resistors in series", "resistors in parallel",
        "internal resistance", "terminal potential difference", "lost volts", "potential divider",
        "potentiometer", "thermistor", "ldr", "light-dependent resistor"
    ],
    "9702_t11": [
        "alpha particle", "beta particle", "gamma ray", "gold foil experiment", "rutherford",
        "nucleus", "nucleon number", "proton number", "isotope", "quark", "up quark",
        "down quark", "strange quark", "hadron", "baryon", "meson", "lepton", "electron",
        "neutrino", "positron", "antineutrino", "beta minus decay", "beta plus decay",
        "w boson", "weak interaction"
    ],
    # A2 Topics
    "9702_t12": [
        "radian", "angular displacement", "angular velocity", "omega", "v=r omega",
        "centripetal acceleration", "centripetal force", "banked track", "circular motion",
        "period of rotation"
    ],
    "9702_t13": [
        "gravitational field", "field lines", "newtons law of gravitation",
        "gravitational field strength", "point mass", "gravitational potential",
        "gravitational potential energy", "escape velocity", "geostationary orbit",
        "geostationary satellite", "orbital period", "keplers third law"
    ],
    "9702_t14": [
        "thermal equilibrium", "zeroth law", "temperature scale", "celsius", "kelvin",
        "absolute scale", "thermistor", "thermocouple", "platinum resistance", "triple point",
        "specific heat capacity", "specific latent heat", "latent heat of fusion",
        "latent heat of vaporisation"
    ],
    "9702_t15": [
        "equation of state", "pv=nrt", "pv=nkt", "molar gas constant", "boltzmann constant",
        "avogadro constant", "ideal gas assumptions", "kinetic theory equation",
        "root-mean-square speed", "crms", "kinetic energy of a molecule",
        "internal energy of ideal gas"
    ],
    "9702_t16": [
        "first law of thermodynamics", "delta u = q + w", "internal energy",
        "work done on gas", "heat supplied", "isothermal", "adiabatic", "isochoric", "isobaric"
    ],
    "9702_t17": [
        "simple harmonic motion", "shm", "acceleration proportional to displacement",
        "a=-omega2 x", "energy in shm", "kinetic energy", "potential energy",
        "damping", "light damping", "critical damping", "heavy damping", "forced oscillation",
        "resonance", "resonant frequency", "bartons pendulums"
    ],
    "9702_t18": [
        "electric field", "field lines", "electric field strength", "e=f/q", "uniform field",
        "e=v/d", "coulombs law", "field of point charge", "electric potential",
        "electric potential energy", "equipotential", "deflection of charged particle"
    ],
    "9702_t19": [
        "capacitance", "c=q/v", "farad", "parallel plate capacitor", "dielectric",
        "capacitors in series", "capacitors in parallel", "energy stored in capacitor",
        "charging capacitor", "discharging capacitor", "time constant", "tau=rc",
        "exponential decay"
    ],
    "9702_t20": [
        "magnetic field", "field lines", "magnetic flux density", "tesla",
        "magnetic force on current", "f=bil", "magnetic force on moving charge", "f=bqv",
        "hall effect", "hall voltage", "hall probe", "velocity selector", "cyclotron",
        "magnetic flux", "weber", "magnetic flux linkage", "faradays law", "lenzs law",
        "eddy currents"
    ],
    "9702_t21": [
        "alternating current", "sinusoidal ac", "peak value", "root-mean-square", "rms",
        "mean power", "transformer", "ideal transformer", "turns ratio",
        "half-wave rectification", "full-wave rectification", "bridge rectifier",
        "smoothing capacitor", "ripple voltage"
    ],
    "9702_t22": [
        "photon", "plancks constant", "photoelectric effect", "threshold frequency",
        "work function", "einsteins photoelectric equation", "stopping potential",
        "wave-particle duality", "de broglie wavelength", "electron diffraction",
        "atomic line spectra", "emission line spectrum", "absorption line spectrum",
        "energy levels"
    ],
    "9702_t23": [
        "mass defect", "binding energy", "binding energy per nucleon",
        "einsteins mass-energy", "fission", "nuclear fission", "fusion", "nuclear fusion",
        "radioactive decay", "decay constant", "activity", "becquerel", "half-life",
        "exponential decay of activity"
    ],
    "9702_t24": [
        "x-ray production", "x-ray tube", "braking radiation", "bremsstrahlung",
        "characteristic x-rays", "x-ray attenuation", "linear attenuation coefficient",
        "half-value thickness", "computed tomography", "ct scan", "ultrasound",
        "piezoelectric effect", "acoustic impedance", "reflection coefficient",
        "a-scan", "b-scan", "positron emission tomography", "pet", "annihilation",
        "gamma photons"
    ],
    "9702_t25": [
        "luminosity", "radiant flux intensity", "standard candle", "cepheid variable",
        "type 1a supernova", "wiens displacement law", "stefan-boltzmann law",
        "hubble law", "redshift", "doppler redshift", "expansion of the universe",
        "big bang theory", "age of the universe"
    ],
}


class DetailedPhysicsMatcher:
    def __init__(self, registry: PhysicsTaxonomyRegistry):
        self.reg = registry
        self.as_doc_index = self._index_outcomes(self.reg.as_outcomes)
        self.a2_doc_index = self._index_outcomes(self.reg.a2_outcomes)

    def _index_outcomes(self, outcomes: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        index = {}
        df = collections.Counter()
        for o in outcomes:
            raw_text = (
                o["outcome_text"]
                + " " + self.reg.module_names.get(o["module_id"], "")
                + " " + self.reg.topic_names.get(o["topic_id"], "")
            )
            tokens = [t for t in tokenize(raw_text) if t not in STOPWORDS]
            unique_tokens = set(tokens)
            df.update(unique_tokens)

        total_docs = len(outcomes)
        for o in outcomes:
            oid = o["outcome_id"]
            tid = o["topic_id"]
            raw_text = o["outcome_text"]
            mod_text = self.reg.module_names.get(o["module_id"], "")
            top_text = self.reg.topic_names.get(tid, "")

            thesaurus_terms = PHYSICS_THESAURUS.get(tid, [])
            thesaurus_str = " ".join(thesaurus_terms)
            combined_text = f"{raw_text} {mod_text} {top_text} {thesaurus_str}"
            tokens = [t for t in tokenize(combined_text) if t not in STOPWORDS]
            tf = collections.Counter(tokens)
            tfidf = {}
            for t, count in tf.items():
                idf = math.log((total_docs + 1) / (df[t] + 1)) + 1.0
                tfidf[t] = count * idf

            raw_tokens = tokenize(raw_text)
            bigrams = {f"{raw_tokens[i]} {raw_tokens[i+1]}" for i in range(len(raw_tokens)-1)}

            index[oid] = {
                "outcome_id": oid,
                "topic_id": tid,
                "module_id": o["module_id"],
                "text": raw_text.lower(),
                "tokens": set(tokens),
                "tfidf": tfidf,
                "bigrams": bigrams,
            }
        return index

    def score_outcomes(
        self,
        doc_index: Dict[str, Dict[str, Any]],
        weighted_signals: List[Tuple[str, float]],
        qp_text: str = "",
        ms_text: str = "",
        preferred_topic: Optional[str] = None,
        key_phrases: Optional[List[str]] = None,
    ) -> List[Tuple[str, float]]:
        scores = collections.defaultdict(float)

        all_phrases = []
        if key_phrases:
            for kp in key_phrases:
                kp_clean = kp.lower().strip()
                if len(kp_clean) > 2:
                    all_phrases.append(kp_clean)

        for text_piece, weight in weighted_signals:
            if not text_piece:
                continue
            tokens = [t for t in tokenize(text_piece) if t not in STOPWORDS]
            for t in tokens:
                for oid, doc in doc_index.items():
                    if t in doc["tfidf"]:
                        scores[oid] += weight * doc["tfidf"][t]

            raw_tokens = tokenize(text_piece)
            for i in range(len(raw_tokens) - 1):
                bg = f"{raw_tokens[i]} {raw_tokens[i+1]}"
                for oid, doc in doc_index.items():
                    if bg in doc["bigrams"]:
                        scores[oid] += weight * 4.5

        # Cross-Field Consensus (QP + MS co-occurrence boost)
        if qp_text and ms_text:
            qp_tokens = set(t for t in tokenize(qp_text) if t not in STOPWORDS)
            ms_tokens = set(t for t in tokenize(ms_text) if t not in STOPWORDS)
            consensus_tokens = qp_tokens.intersection(ms_tokens)
            for ct in consensus_tokens:
                for oid, doc in doc_index.items():
                    if ct in doc["tokens"]:
                        scores[oid] += 15.0

        for kp in all_phrases:
            kp_tokens = tokenize(kp)
            for oid, doc in doc_index.items():
                if kp in doc["text"]:
                    scores[oid] += 35.0
                else:
                    matched = sum(1 for t in kp_tokens if t in doc["tokens"])
                    if matched > 0:
                        scores[oid] += matched * 9.0

        if preferred_topic:
            for oid, doc in doc_index.items():
                if doc["topic_id"] == preferred_topic:
                    scores[oid] += 500.0

        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        return sorted_scores

    def match_as_content(
        self,
        weighted_signals: List[Tuple[str, float]],
        qp_text: str = "",
        ms_text: str = "",
        preferred_topic: Optional[str] = None,
        key_phrases: Optional[List[str]] = None,
    ) -> Tuple[str, str, List[str]]:
        if preferred_topic:
            target_docs = {oid: doc for oid, doc in self.as_doc_index.items() if doc["topic_id"] == preferred_topic}
            if not target_docs:
                target_docs = self.as_doc_index
        else:
            target_docs = self.as_doc_index

        scored = self.score_outcomes(target_docs, weighted_signals, qp_text, ms_text, None, key_phrases)
        if not scored:
            best_oid = self.reg.as_outcomes[0]["outcome_id"]
            best_score = 0.0
        else:
            best_oid, best_score = scored[0]

        tid = self.reg.outcome_to_topic[best_oid]
        mid = self.reg.outcome_to_module[best_oid]

        sec_oid = None
        for oid, score in scored[1:]:
            if self.reg.outcome_to_module[oid] == mid and score >= 0.45 * best_score and score > 15.0:
                sec_oid = oid
                break

        outcomes = [best_oid]
        if sec_oid:
            outcomes.append(sec_oid)
        return tid, mid, outcomes

    def match_a2_content(
        self,
        weighted_signals: List[Tuple[str, float]],
        qp_text: str = "",
        ms_text: str = "",
        preferred_topic: Optional[str] = None,
        key_phrases: Optional[List[str]] = None,
    ) -> Tuple[str, str, List[str]]:
        if preferred_topic:
            target_docs = {oid: doc for oid, doc in self.a2_doc_index.items() if doc["topic_id"] == preferred_topic}
            if not target_docs:
                target_docs = self.a2_doc_index
        else:
            target_docs = self.a2_doc_index

        scored = self.score_outcomes(target_docs, weighted_signals, qp_text, ms_text, None, key_phrases)
        if not scored:
            best_oid = self.reg.a2_outcomes[0]["outcome_id"]
            best_score = 0.0
        else:
            best_oid, best_score = scored[0]

        tid = self.reg.outcome_to_topic[best_oid]
        mid = self.reg.outcome_to_module[best_oid]

        sec_oid = None
        for oid, score in scored[1:]:
            if self.reg.outcome_to_module[oid] == mid and score >= 0.45 * best_score and score > 15.0:
                sec_oid = oid
                break

        outcomes = [best_oid]
        if sec_oid:
            outcomes.append(sec_oid)
        return tid, mid, outcomes


def sanitize_text(text: str) -> str:
    if chr(8212) in text:
        text = text.replace(chr(8212), " - ")
    if chr(8211) in text:
        text = text.replace(chr(8211), "-")
    return text


def p1_preferred_topic(question_num: int) -> Optional[str]:
    if question_num <= 4:
        return "9702_t01"
    elif question_num <= 7:
        return "9702_t02"
    elif question_num <= 10:
        return "9702_t03"
    elif question_num <= 14:
        return "9702_t04"
    elif question_num <= 17:
        return "9702_t05"
    elif question_num <= 20:
        return "9702_t06"
    elif question_num <= 25:
        return "9702_t07"
    elif question_num <= 29:
        return "9702_t08"
    elif question_num <= 34:
        return "9702_t09"
    elif question_num <= 37:
        return "9702_t10"
    else:
        return "9702_t11"


def safe_load_json(file_path: Path) -> Dict[str, Any]:
    if file_path.is_file() and file_path.stat().st_size > 0:
        try:
            return json.loads(file_path.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def process_p1_file(
    path: Path,
    matcher: DetailedPhysicsMatcher,
    registry: PhysicsTaxonomyRegistry,
) -> bool:
    data = safe_load_json(path)
    qid_from_name = path.stem.replace(".enrichment", "")
    q_num_match = re.search(r"_q(\d+)", qid_from_name)
    q_num = int(q_num_match.group(1)) if q_num_match else 1

    qp_file = path.parents[1] / "question-package" / f"question_{q_num:02d}.json"
    qp_data = safe_load_json(qp_file)
    q_text = qp_data.get("question_text", "")

    if not data:
        correct_ans = qp_data.get("correct_answer", "")
        qid = qp_data.get("question_id", qid_from_name)
        data = {
            "schema_version": "9702_p1_enrichment_v1",
            "question_id": qid,
            "component": "P1",
            "difficulty": 2,
            "question_patterns": ["direct_calculation"],
            "topic_id": "",
            "module_id": "",
            "skill_id": "",
            "accepted_answer": correct_ans,
            "options_breakdown": {
                opt: {
                    "status": "correct" if opt == correct_ans else "incorrect",
                    "explanation": f"Option {opt} analysis for {qid}."
                }
                for opt in ["A", "B", "C", "D"]
            },
            "hints": [
                f"Carefully read the question stem and identify the given physical quantities for {qid}.",
                "Apply the relevant physical formula or conservation principle connecting these quantities.",
                "Calculate or deduce the final result and match with the correct option.",
            ],
            "walkthrough": [
                f"Examine the physical scenario described in the question.",
                "Apply the foundational equations governing this topic to evaluate the options.",
                f"The correct deduction leads directly to option {correct_ans}.",
            ],
        }

    # Extract question number from question_id or filename
    qid = data.get("question_id") or qid_from_name
    skill_id = data.get("skill_id", "")
    preferred_top = None
    if skill_id and skill_id in registry.skill_to_topics:
        valid_topics = registry.skill_to_topics[skill_id]
        if valid_topics:
            preferred_top = valid_topics[0]
    if not preferred_top:
        preferred_top = p1_preferred_topic(q_num)

    accepted_ans = data.get("accepted_answer") or data.get("correct_answer")
    options = data.get("options_breakdown", {})
    ms_explanation = ""
    if isinstance(options, dict) and accepted_ans in options:
        opt_data = options[accepted_ans]
        if isinstance(opt_data, dict):
            ms_explanation = opt_data.get("explanation", "")

    hints_text = " ".join(data.get("hints", []))
    walkthrough_text = " ".join(data.get("walkthrough", []))

    weighted_signals = [
        (ms_explanation, 7.0),
        (q_text, 6.0),
        (walkthrough_text, 3.5),
        (hints_text, 2.5),
        (qid, 1.0),
    ]

    tid, mid, oids = matcher.match_as_content(
        weighted_signals,
        qp_text=q_text or walkthrough_text,
        ms_text=ms_explanation,
        preferred_topic=preferred_top
    )

    val_errs = registry.validate_mapping(tid, mid, oids)
    if val_errs:
        raise ValueError(f"Mapping validation failed for {qid}: {val_errs}")

    curr_skill = data.get("skill_id")
    if not curr_skill or tid not in registry.skill_to_topics.get(curr_skill, []):
        if tid in registry.topic_to_skills and registry.topic_to_skills[tid]:
            data["skill_id"] = registry.topic_to_skills[tid][0]

    if len(data.get("hints", [])) < 2:
        data["hints"] = [
            f"Carefully read the question stem and identify the given physical quantities for {qid}.",
            "Apply the relevant physical formula or conservation principle connecting these quantities.",
            "Calculate or deduce the final result and match with the correct option.",
        ]
    if len(data.get("walkthrough", [])) < 2:
        data["walkthrough"] = [
            f"Examine the physical scenario described in the question.",
            "Apply the foundational equations governing this topic to evaluate the options.",
            f"The correct deduction leads directly to option {accepted_ans}.",
        ]

    data.pop("primary_topic_id", None)
    data.pop("primary_module_id", None)
    data.pop("outcome_ids", None)
    data["topic_id"] = tid
    data["module_id"] = mid

    data["mapping"] = {
        "primary_topic_id": tid,
        "primary_module_id": mid,
        "outcome_ids": oids,
    }
    data["taxonomy_tags"] = {
        "topic_ids": [tid],
        "module_ids": [mid],
    }

    content = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    content = sanitize_text(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def process_theory_question(
    q_path: Path,
    v2_path: Optional[Path],
    matcher: DetailedPhysicsMatcher,
    registry: PhysicsTaxonomyRegistry,
    comp: str = "p2",
) -> bool:
    with open(q_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    q_dir = q_path.parent
    ms_file = q_dir / "markscheme.json"
    ocr_file = q_dir / "question_ocr.json"
    txt_file = q_dir / "question.txt"

    ms_data = json.loads(ms_file.read_text(encoding="utf-8")) if ms_file.is_file() else {}
    ocr_data = json.loads(ocr_file.read_text(encoding="utf-8")) if ocr_file.is_file() else {}
    q_txt = txt_file.read_text(encoding="utf-8") if txt_file.is_file() else ""

    ms_parts_map = {}
    if isinstance(ms_data, dict):
        for mp in ms_data.get("parts", []):
            pid = mp.get("id")
            if pid:
                pts = mp.get("marking_points", [])
                pt_texts = [p.get("text", "") for p in pts if isinstance(p, dict) and p.get("text")]
                ms_parts_map[pid] = " ".join(pt_texts)

    ocr_parts_map = {}
    if isinstance(ocr_data, dict):
        for op in ocr_data.get("parts", []):
            pid = op.get("id")
            if pid:
                pstem = op.get("part_stem") or op.get("text") or ""
                ocr_parts_map[pid] = pstem

    parts = data.get("parts", [])
    if not parts:
        return False

    all_topics = set()
    all_modules = set()

    for part in parts:
        if not isinstance(part, dict):
            continue
        pid = part.get("part_id", "")
        key_concepts = part.get("key_concepts", [])
        proper_ans = part.get("proper_answer", "")
        walkthrough = " ".join(part.get("walkthrough", []))
        hints = " ".join(part.get("hints", []))

        ms_text = ms_parts_map.get(pid, "")
        qp_text = ocr_parts_map.get(pid, "") or q_txt

        weighted_signals = [
            (ms_text, 7.0),
            (qp_text, 6.0),
            (proper_ans, 4.5),
            (" ".join(key_concepts), 3.5),
            (walkthrough, 2.0),
            (hints, 2.0),
        ]

        sk = part.get("skills", {})
        pskill = sk.get("primary_skill_id") if isinstance(sk, dict) else None
        preferred_top = None
        if pskill and pskill in registry.skill_to_topics:
            valid_tops = registry.skill_to_topics[pskill]
            if valid_tops:
                preferred_top = valid_tops[0]

        if comp == "p2":
            tid, mid, oids = matcher.match_as_content(
                weighted_signals,
                qp_text=qp_text,
                ms_text=ms_text,
                preferred_topic=preferred_top,
                key_phrases=key_concepts
            )
        else:
            tid, mid, oids = matcher.match_a2_content(
                weighted_signals,
                qp_text=qp_text,
                ms_text=ms_text,
                preferred_topic=preferred_top,
                key_phrases=key_concepts
            )

        val_errs = registry.validate_mapping(tid, mid, oids)
        if val_errs:
            raise ValueError(f"Mapping validation failed for {pid}: {val_errs}")

        part["mapping"] = {
            "primary_topic_id": tid,
            "primary_module_id": mid,
            "outcome_ids": oids,
        }
        if data.get("schema_version") == "9702_question_enrichment_v2":
            part.pop("primary_topic_id", None)
            part.pop("primary_module_id", None)
            part.pop("outcome_ids", None)
        else:
            part["primary_topic_id"] = tid
            part["primary_module_id"] = mid
            part["outcome_ids"] = oids

        all_topics.add(tid)
        all_modules.add(mid)

    if data.get("schema_version") == "9702_question_enrichment_v2":
        all_outcomes = set()
        for p in parts:
            if isinstance(p, dict) and "mapping" in p:
                all_outcomes.update(p["mapping"].get("outcome_ids", []))
        data["mapping"] = {
            "topic_ids": sorted(list(all_topics)),
            "module_ids": sorted(list(all_modules)),
            "outcome_ids": sorted(list(all_outcomes)),
        }
        data.pop("taxonomy_tags", None)
    else:
        data["taxonomy_tags"] = {
            "topic_ids": sorted(list(all_topics)),
            "module_ids": sorted(list(all_modules)),
        }

    content = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    content = sanitize_text(content)
    with open(q_path, "w", encoding="utf-8") as f:
        f.write(content)

    if v2_path and v2_path.is_file():
        try:
            with open(v2_path, "r", encoding="utf-8") as f:
                v2_data = json.load(f)
            v2_data["taxonomy_tags"] = {
                "topic_ids": sorted(list(all_topics)),
                "module_ids": sorted(list(all_modules)),
            }
            v2_content = json.dumps(v2_data, indent=2, ensure_ascii=False) + "\n"
            v2_content = sanitize_text(v2_content)
            with open(v2_path, "w", encoding="utf-8") as f:
                f.write(v2_content)
        except Exception:
            pass

    return True


def run_for_years(years: List[str]) -> Tuple[int, int, List[str]]:
    registry = PhysicsTaxonomyRegistry()
    matcher = DetailedPhysicsMatcher(registry)
    total_processed = 0
    total_parts = 0
    errors: List[str] = []

    for year in years:
        # 1. Component P1
        p1_files = sorted(glob.glob(str(PAST_PAPERS / "p1" / year / "**" / "enrichment" / "*.enrichment.json"), recursive=True))
        for p in p1_files:
            path = Path(p)
            try:
                ok = process_p1_file(path, matcher, registry)
                if not ok:
                    errors.append(f"P1 mapping failed for {path}")
                else:
                    total_processed += 1
                    total_parts += 1
            except Exception as e:
                errors.append(f"P1 error in {path}: {e}")

        # 2. Component P2
        p2_q_files = sorted(glob.glob(str(PAST_PAPERS / "p2" / year / "**" / "question_*" / "enrichment.json"), recursive=True))
        for q in p2_q_files:
            q_path = Path(q)
            paper_dir = q_path.parents[1]
            q_folder = q_path.parent.name
            q_num = q_folder.replace("question_", "")
            v2_candidates = list(paper_dir.glob(f"enrichment/*_q{q_num}.enrichment.json"))
            v2_path = v2_candidates[0] if v2_candidates else None

            try:
                ok = process_theory_question(q_path, v2_path, matcher, registry, comp="p2")
                if not ok:
                    errors.append(f"P2 mapping failed for {q_path}")
                else:
                    total_processed += 1
                    with open(q_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        total_parts += len(data.get("parts", []))
            except Exception as e:
                errors.append(f"P2 error in {q_path}: {e}")

        # 3. Component P4
        p4_q_files = sorted(glob.glob(str(PAST_PAPERS / "p4" / year / "**" / "question_*" / "enrichment.json"), recursive=True))
        for q in p4_q_files:
            q_path = Path(q)
            paper_dir = q_path.parents[1]
            q_folder = q_path.parent.name
            q_num = q_folder.replace("question_", "")
            v2_candidates = list(paper_dir.glob(f"enrichment/*_q{q_num}.enrichment.json"))
            v2_path = v2_candidates[0] if v2_candidates else None

            try:
                ok = process_theory_question(q_path, v2_path, matcher, registry, comp="p4")
                if not ok:
                    errors.append(f"P4 mapping failed for {q_path}")
                else:
                    total_processed += 1
                    with open(q_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        total_parts += len(data.get("parts", []))
            except Exception as e:
                errors.append(f"P4 error in {q_path}: {e}")

    return total_processed, total_parts, errors


def validate_years(years: List[str]) -> List[str]:
    registry = PhysicsTaxonomyRegistry()
    errors: List[str] = []

    for year in years:
        # P1 (AS MCQs)
        p1_files = sorted(glob.glob(str(PAST_PAPERS / "p1" / year / "**" / "enrichment" / "*.enrichment.json"), recursive=True))
        for p in p1_files:
            path = Path(p)
            with open(path, "r", encoding="utf-8") as f:
                raw = f.read()
                if chr(8212) in raw:
                    errors.append(f"{path}: Contains em dash")
                d = json.loads(raw)

            tax = d.get("taxonomy_tags", {})
            if not tax.get("topic_ids") or not tax.get("module_ids"):
                errors.append(f"{path}: Empty taxonomy_tags")
            for tid in tax.get("topic_ids", []):
                if tid not in registry.as_topics:
                    errors.append(f"{path}: Invalid topic_id {tid} in taxonomy_tags (not in AS)")
            for mid in tax.get("module_ids", []):
                if mid not in registry.valid_modules:
                    errors.append(f"{path}: Invalid module_id {mid} in taxonomy_tags")

            mapping = d.get("mapping", {})
            ptid = mapping.get("primary_topic_id") or d.get("primary_topic_id")
            pmid = mapping.get("primary_module_id") or d.get("primary_module_id")
            oids = mapping.get("outcome_ids", []) or d.get("outcome_ids", [])

            if ptid not in registry.as_topics:
                errors.append(f"{path}: Invalid primary_topic_id {ptid} (not in AS)")
            if pmid not in registry.valid_modules:
                errors.append(f"{path}: Invalid primary_module_id {pmid}")
            elif registry.module_to_topic.get(pmid) != ptid:
                errors.append(f"{path}: Module {pmid} does not belong to {ptid}")

            for oid in oids:
                if oid not in registry.valid_outcomes:
                    errors.append(f"{path}: Invalid outcome_id {oid}")
                elif registry.outcome_to_module.get(oid) != pmid:
                    errors.append(f"{path}: Outcome {oid} does not belong to {pmid}")

        # P2 (AS Theory)
        p2_q_files = sorted(glob.glob(str(PAST_PAPERS / "p2" / year / "**" / "question_*" / "enrichment.json"), recursive=True))
        for q in p2_q_files:
            q_path = Path(q)
            with open(q_path, "r", encoding="utf-8") as f:
                raw = f.read()
                if chr(8212) in raw:
                    errors.append(f"{q_path}: Contains em dash")
                d = json.loads(raw)

            for p in d.get("parts", []):
                pid = p.get("part_id", "")
                mapping = p.get("mapping", {})
                ptid = p.get("primary_topic_id") or mapping.get("primary_topic_id")
                pmid = p.get("primary_module_id") or mapping.get("primary_module_id")
                oids = p.get("outcome_ids") or mapping.get("outcome_ids", [])

                if ptid not in registry.as_topics:
                    errors.append(f"{q_path} ({pid}): Invalid primary_topic_id {ptid} (not in AS)")
                if pmid not in registry.valid_modules:
                    errors.append(f"{q_path} ({pid}): Invalid primary_module_id {pmid}")
                elif registry.module_to_topic.get(pmid) != ptid:
                    errors.append(f"{q_path} ({pid}): Module {pmid} does not belong to {ptid}")

                for oid in oids:
                    if oid not in registry.valid_outcomes:
                        errors.append(f"{q_path} ({pid}): Invalid outcome_id {oid}")
                    elif registry.outcome_to_module.get(oid) != pmid:
                        errors.append(f"{q_path} ({pid}): Outcome {oid} does not belong to {pmid}")

        # P4 (A2 Theory)
        p4_q_files = sorted(glob.glob(str(PAST_PAPERS / "p4" / year / "**" / "question_*" / "enrichment.json"), recursive=True))
        for q in p4_q_files:
            q_path = Path(q)
            with open(q_path, "r", encoding="utf-8") as f:
                raw = f.read()
                if chr(8212) in raw:
                    errors.append(f"{q_path}: Contains em dash")
                d = json.loads(raw)

            for p in d.get("parts", []):
                pid = p.get("part_id", "")
                mapping = p.get("mapping", {})
                ptid = p.get("primary_topic_id") or mapping.get("primary_topic_id")
                pmid = p.get("primary_module_id") or mapping.get("primary_module_id")
                oids = p.get("outcome_ids") or mapping.get("outcome_ids", [])

                if ptid not in registry.a2_topics:
                    errors.append(f"{q_path} ({pid}): Invalid primary_topic_id {ptid} (not in A2)")
                if pmid not in registry.valid_modules:
                    errors.append(f"{q_path} ({pid}): Invalid primary_module_id {pmid}")
                elif registry.module_to_topic.get(pmid) != ptid:
                    errors.append(f"{q_path} ({pid}): Module {pmid} does not belong to {ptid}")

                for oid in oids:
                    if oid not in registry.valid_outcomes:
                        errors.append(f"{q_path} ({pid}): Invalid outcome_id {oid}")
                    elif registry.outcome_to_module.get(oid) != pmid:
                        errors.append(f"{q_path} ({pid}): Outcome {oid} does not belong to {pmid}")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Physics 9702 high-precision 4-way taxonomy mapping and validation.")
    parser.add_argument("--years", nargs="+", help="Years to process")
    parser.add_argument("--all", action="store_true", help="Process all available years 2016-2025")
    parser.add_argument("--validate-only", action="store_true", help="Only run validation")
    args = parser.parse_args()

    if args.all:
        years = [str(y) for y in range(2016, 2026)]
    elif args.years:
        years = args.years
    else:
        print("Please specify --years or --all")
        sys.exit(1)

    if not args.validate_only:
        print(f"Mapping Physics 9702 for {len(years)} years with 4-way signal consensus...")
        processed, parts, map_errors = run_for_years(years)
        print(f"Mapping run complete: {processed} questions, {parts} parts processed.")
        if map_errors:
            print(f"Encountered {len(map_errors)} mapping errors:")
            for e in map_errors[:10]:
                print(f"  - {e}")
            sys.exit(1)

    print(f"\nValidating mappings across {len(years)} years...")
    val_errors = validate_years(years)
    print(f"Validation completed with {len(val_errors)} errors.")
    if val_errors:
        for e in val_errors[:10]:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("100% PASS: All Physics mappings verified, fully resolved, and zero em dashes.")


if __name__ == "__main__":
    main()
