#!/usr/bin/env python3
"""Consolidate duplicate and overlapping definitions and formulas in Physics (9702).

Performs controlled merges:
- 11 formula groups (reducing 133 -> 122)
- 5 definition groups (reducing 122 -> 116)
- Corrects semantic definition of gravitational field vs gravitational field strength
- Preserves aliases (merged_ids) and combined evidence/topic sets.

Rule: Strictly ZERO em dashes anywhere in code, markdown, logs, or outputs.
"""

from __future__ import annotations

import json
from pathlib import Path

PHY_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = PHY_ROOT / "knowledge/knowledge-base"
DEFS_PATH = KB_DIR / "definitions.json"
FORMS_PATH = KB_DIR / "formulas.json"

def sanitize(text: str) -> str:
    return text.replace(chr(8212), "-").replace("\u2014", "-")

def main():
    print("Consolidating Physics (9702) Knowledge Base Registries...")

    defs_data = json.loads(DEFS_PATH.read_text(encoding="utf-8"))
    forms_data = json.loads(FORMS_PATH.read_text(encoding="utf-8"))

    raw_defs = defs_data["definitions"]
    raw_forms = forms_data["formulas"]

    defs_by_id = {d["definition_id"]: d for d in raw_defs}
    forms_by_id = {f["formula_id"]: f for f in raw_forms}

    # ================= FORMULA MERGES =================
    formula_merges = [
        {
            "target_id": "9702_formula_attenuation_intensity",
            "source_ids": ["9702_formula_xray_attenuation"],
            "name": "Exponential Attenuation of Radiation",
            "latex": "I = I_0 e^{-\\mu x}",
            "latex_aliases": ["I = I_0 \\exp(-\\mu x)", "I = I_0 e^{-\\mu x}"],
            "name_aliases": ["X-ray and radiation attenuation", "exponential attenuation"],
        },
        {
            "target_id": "9702_formula_specific_heat_capacity",
            "source_ids": ["9702_formula_thermal_energy_shc"],
            "name": "Specific heat capacity",
            "latex": "\\Delta E = mc\\Delta T",
            "latex_aliases": ["q = mc\\Delta T", "\\Delta E = mc\\Delta T"],
            "name_aliases": ["Thermal energy change from specific heat capacity"],
        },
        {
            "target_id": "9702_formula_angular_speed_period",
            "source_ids": ["9702_formula_ac_period_angular_frequency"],
            "name": "Angular speed and period relationship",
            "latex": "\\omega = \\frac{2\\pi}{T} = 2\\pi f",
            "latex_aliases": ["\\omega = \\frac{2\\pi}{T}", "T = \\frac{2\\pi}{\\omega}"],
            "name_aliases": ["Period of alternating voltage from angular frequency"],
        },
        {
            "target_id": "9702_formula_capacitor_energy",
            "source_ids": ["9702_formula_capacitor_energy_cv2", "9702_formula_capacitor_energy_qv"],
            "name": "Energy stored in a capacitor",
            "latex": "W = \\frac{1}{2}QV = \\frac{1}{2}CV^2 = \\frac{Q^2}{2C}",
            "latex_aliases": ["E = \\frac{1}{2} C V^2", "E = \\frac{1}{2}QV", "W = \\frac{1}{2}QV", "E = \\frac{1}{2}CV^2"],
            "name_aliases": ["Capacitor energy in terms of charge and voltage", "Energy stored in a capacitor"],
        },
        {
            "target_id": "9702_formula_newtons_second_law",
            "source_ids": ["9702_formula_force_momentum_rate"],
            "name": "Newton's second law of motion",
            "latex": "F = \\frac{\\Delta p}{\\Delta t} = ma",
            "latex_aliases": ["F = ma", "F = \\frac{\\Delta p}{\\Delta t}"],
            "name_aliases": ["Force as rate of momentum change", "Newton's second law"],
        },
        {
            "target_id": "9702_formula_gravitational_potential_energy_potential",
            "source_ids": ["9702_formula_gravitational_potential_energy_point_masses"],
            "name": "Gravitational potential energy in a radial field",
            "latex": "E_{\\mathrm{p}} = m\\phi = -\\frac{GMm}{r}",
            "latex_aliases": ["E_{\\mathrm{p}} = -\\frac{GMm}{r}", "E_{\\mathrm{p}} = m\\phi"],
            "name_aliases": ["Gravitational potential energy of two point masses", "Gravitational potential energy from potential"],
        },
        {
            "target_id": "9702_formula_photon_energy",
            "source_ids": ["9702_formula_photon_wavelength_energy"],
            "name": "Photon energy and wavelength equation",
            "latex": "E = hf = \\frac{hc}{\\lambda}",
            "latex_aliases": ["E = hf", "\\lambda = \\frac{hc}{E}"],
            "name_aliases": ["Photon wavelength from energy"],
        },
        {
            "target_id": "9702_formula_sinusoidal_ac",
            "source_ids": ["9702_formula_sinusoidal_ac_voltage", "9702_formula_sinusoidal_ac_current"],
            "name": "Sinusoidal alternating voltage and current",
            "latex": "x = x_0 \\sin(\\omega t) \\quad (x = V \\text{ or } I)",
            "latex_aliases": ["V = V_0 \\sin \\omega t", "I = I_0 \\cos(\\omega t)"],
            "name_aliases": ["Sinusoidal alternating voltage", "Sinusoidal alternating current"],
        },
        {
            "target_id": "9702_formula_rms_values",
            "source_ids": ["9702_formula_v_rms", "9702_formula_i_rms"],
            "name": "Root-mean-square values for sinusoidal AC",
            "latex": "I_{\\mathrm{r.m.s.}} = \\frac{I_0}{\\sqrt{2}};\\quad V_{\\mathrm{r.m.s.}} = \\frac{V_0}{\\sqrt{2}}",
            "latex_aliases": ["V_{\\mathrm{r.m.s.}} = \\frac{V_0}{\\sqrt{2}}", "I_{\\mathrm{r.m.s.}} = \\frac{I_0}{\\sqrt{2}}"],
            "name_aliases": ["Root-mean-square voltage for sinusoidal AC", "Root-mean-square current for sinusoidal AC"],
        },
        {
            "target_id": "9702_formula_mass_energy_equivalence",
            "source_ids": ["9702_formula_annihilation_energy"],
            "name": "Mass-energy equivalence and pair annihilation",
            "latex": "\\Delta E = \\Delta m c^2 \\quad (\\text{annihilation: } E = 2mc^2)",
            "latex_aliases": ["E = mc^2", "E = 2mc^2", "\\Delta E = \\Delta m c^2"],
            "name_aliases": ["Energy released in pair annihilation", "Mass-energy equivalence"],
        },
        {
            "target_id": "9702_formula_uniform_motion_displacement",
            "source_ids": ["9702_formula_displacement_velocity_time_graph"],
            "name": "Displacement in uniform motion",
            "latex": "s = vt",
            "latex_aliases": ["s = vt"],
            "name_aliases": ["Displacement from a velocity-time graph"],
        },
    ]

    merged_form_sources = set()
    consolidated_forms = []

    for m in formula_merges:
        target_id = m["target_id"]
        source_ids = m["source_ids"]
        merged_form_sources.update(source_ids)

        # Retrieve or initialize target
        if target_id in forms_by_id:
            target_item = dict(forms_by_id[target_id])
        else:
            # New composite ID (like 9702_formula_capacitor_energy, 9702_formula_sinusoidal_ac, 9702_formula_rms_values)
            comp_top = "9702_t19" if "capacitor" in target_id else "9702_t21"
            target_item = {
                "formula_id": target_id,
                "canonical_topic_id": comp_top,
                "name": m["name"],
                "latex": m["latex"],
                "topic_ids": [comp_top],
                "evidence_question_ids": [],
            }

        target_item["name"] = m["name"]
        target_item["latex"] = m["latex"]
        target_item["latex_aliases"] = m["latex_aliases"]
        target_item["name_aliases"] = m["name_aliases"]
        target_item["merged_ids"] = list(source_ids)

        # Combine topics and evidence
        topics = set(target_item.get("topic_ids", []))
        ev_ids = set(target_item.get("evidence_question_ids", []))

        for sid in source_ids:
            if sid in forms_by_id:
                s_item = forms_by_id[sid]
                topics.update(s_item.get("topic_ids", []))
                ev_ids.update(s_item.get("evidence_question_ids", []))

        target_item["topic_ids"] = sorted(list(topics))
        target_item["evidence_question_ids"] = sorted(list(ev_ids))
        forms_by_id[target_id] = target_item

    # Reassemble formula list excluding merged source IDs
    for fid, f_item in forms_by_id.items():
        if fid not in merged_form_sources:
            consolidated_forms.append(f_item)

    print(f"Formulas consolidated from {len(raw_forms)} to {len(consolidated_forms)}.")

    # ================= DEFINITION MERGES =================
    # 1. Semantic correction for gravitational_field vs gravitational_field_strength
    if "9702_def_gravitational_field" in defs_by_id:
        defs_by_id["9702_def_gravitational_field"]["accepted_definition"] = (
            "a region of space where a mass experiences a gravitational force"
        )
        defs_by_id["9702_def_gravitational_field"]["accepted_alternatives"] = [
            "field of force surrounding a mass where another mass experiences an attractive force",
            "region where a force acts on any mass placed within it"
        ]
        defs_by_id["9702_def_gravitational_field"]["topic_ids"] = ["9702_t13"]

    if "9702_def_gravitational_field_strength" in defs_by_id:
        defs_by_id["9702_def_gravitational_field_strength"]["accepted_definition"] = (
            "gravitational force per unit mass acting on a small test mass"
        )
        defs_by_id["9702_def_gravitational_field_strength"]["accepted_alternatives"] = [
            "force per unit mass",
            "g = F / m"
        ]

    definition_merges = [
        {
            "target_id": "9702_def_force",
            "source_ids": ["9702_def_newtons_second_law"],
            "term": "force (Newton's second law)",
            "term_aliases": ["force", "Newton's second law of motion", "Newton's second law"],
            "accepted_definition": "the rate of change of momentum of a body",
            "accepted_alternatives": [
                "resultant force is equal to the rate of change of momentum and acts in the direction of the force",
                "rate of change of momentum",
                "F = delta p / delta t",
                "product of mass and acceleration (for constant mass)"
            ],
        },
        {
            "target_id": "9702_def_specific_latent_heat",
            "source_ids": ["9702_def_specific_latent_heat_of_vaporisation"],
            "term": "specific latent heat",
            "term_aliases": [
                "specific latent heat",
                "specific latent heat of vaporisation",
                "latent heat of vaporisation",
                "latent heat of fusion"
            ],
            "accepted_definition": "thermal energy per unit mass required to change the state of a substance at constant temperature",
            "accepted_alternatives": [
                "thermal energy per unit mass required to change state from solid to liquid at constant temperature (latent heat of fusion)",
                "thermal energy per unit mass required to change state from liquid to gas at constant temperature (latent heat of vaporisation)",
                "energy per unit mass transferred during change of phase without temperature change"
            ],
        },
        {
            "target_id": "9702_def_radioactive_decay",
            "source_ids": ["9702_def_spontaneous_decay", "9702_def_random_decay"],
            "term": "radioactive decay",
            "term_aliases": [
                "radioactive decay",
                "spontaneous radioactive decay",
                "random radioactive decay",
                "spontaneous decay",
                "random decay"
            ],
            "accepted_definition": "the spontaneous and random emission of ionising radiation from an unstable nucleus",
            "accepted_alternatives": [
                "spontaneous: decay not affected by external environmental factors (temperature, pressure, chemical environment)",
                "random: impossible to predict when a particular nucleus will decay / constant probability of decay per unit time",
                "decay of unstable nuclei to form more stable nuclei with emission of alpha, beta or gamma radiation"
            ],
        },
        {
            "target_id": "9702_def_threshold_frequency",
            "source_ids": ["9702_def_threshold_wavelength"],
            "term": "threshold frequency",
            "term_aliases": [
                "threshold frequency",
                "threshold wavelength"
            ],
            "accepted_definition": "the minimum frequency of electromagnetic radiation required to cause the emission of photoelectrons from a metal surface",
            "accepted_alternatives": [
                "threshold wavelength: the maximum wavelength of electromagnetic radiation that causes photoelectric emission from a metal surface",
                "minimum frequency for photoelectric emission",
                "f_0 = Phi / h or lambda_0 = hc / Phi"
            ],
        },
    ]

    merged_def_sources = set()
    consolidated_defs = []

    for m in definition_merges:
        target_id = m["target_id"]
        source_ids = m["source_ids"]
        merged_def_sources.update(source_ids)

        target_item = dict(defs_by_id[target_id])
        target_item["term"] = m["term"]
        target_item["term_aliases"] = m["term_aliases"]
        target_item["accepted_definition"] = m["accepted_definition"]
        target_item["accepted_alternatives"] = m["accepted_alternatives"]
        target_item["merged_ids"] = list(source_ids)

        # Combine topics and evidence
        topics = set(target_item.get("topic_ids", []))
        ev_ids = set(target_item.get("evidence_question_ids", []))

        for sid in source_ids:
            if sid in defs_by_id:
                s_item = defs_by_id[sid]
                topics.update(s_item.get("topic_ids", []))
                ev_ids.update(s_item.get("evidence_question_ids", []))

        target_item["topic_ids"] = sorted(list(topics))
        target_item["evidence_question_ids"] = sorted(list(ev_ids))
        defs_by_id[target_id] = target_item

    # Reassemble definitions list excluding merged source IDs
    for did, d_item in defs_by_id.items():
        if did not in merged_def_sources:
            consolidated_defs.append(d_item)

    print(f"Definitions consolidated from {len(raw_defs)} to {len(consolidated_defs)}.")

    # Write updated knowledge-base JSON files
    defs_data["definitions"] = consolidated_defs
    forms_data["formulas"] = consolidated_forms

    defs_text = sanitize(json.dumps(defs_data, indent=2, ensure_ascii=False) + "\n")
    forms_text = sanitize(json.dumps(forms_data, indent=2, ensure_ascii=False) + "\n")

    DEFS_PATH.write_text(defs_text, encoding="utf-8")
    FORMS_PATH.write_text(forms_text, encoding="utf-8")
    print("Successfully saved consolidated knowledge base registries.")

if __name__ == "__main__":
    main()
