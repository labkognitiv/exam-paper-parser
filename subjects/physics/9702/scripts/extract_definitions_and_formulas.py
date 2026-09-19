#!/usr/bin/env python3
"""Authoritative Cambridge Physics (9702) Definition & Formula Extraction Engine.

Extracts verbatim mark scheme definitions and mathematical formulas across the complete
2016-2025 past paper archive (Paper 1 MCQ, Paper 2 AS Theory, Paper 4 A2 Theory: 8,335 items).

Architectural Principles:
1. Canonical Topic Anchoring: Every definition and formula has a single authoritative
   primary syllabus topic (canonical_topic_id). Multi-topic coordinates exist strictly for
   verified cross-topic concepts.
2. Target-Specific Definition Extraction: Authentically mines definition questions from
   Paper 2 and Paper 4 using command triggers (define, state what is meant by, state [law])
   and exact longest-match term targeting, eliminating false-positive keyword pollution.
3. Bounded Formula Extraction: Matches mathematical formulas within valid topic scopes,
   capturing authentic calculation problems across Papers 1, 2, and 4.
4. Clean Topic-by-Topic Reference Guide: The markdown catalog groups entries strictly by
   canonical topic, eliminating repetition of generic terms across topics.
5. Zero Em Dashes: Strictly enforces zero em dashes across all code, logs, JSON, and markdown.
"""

from __future__ import annotations

import collections
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

PHY_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_ROOT = PHY_ROOT / "knowledge/2025-2027"
KB_DIR = PHY_ROOT / "knowledge/knowledge-base"
PAPERS_ROOT = PHY_ROOT / "past papers"

AS_TAX_PATH = KNOWLEDGE_ROOT / "as/9702-2025-2027-as-taxonomy.json"
A2_TAX_PATH = KNOWLEDGE_ROOT / "a2/9702-2025-2027-a2-taxonomy.json"
BASE_DEFS_PATH = KB_DIR / "definitions.json"
BASE_FORMS_PATH = KB_DIR / "formulas.json"

# ================= CANONICAL SYLLABUS TOPIC MAPPINGS =================

CANONICAL_DEF_TOPICS: Dict[str, str] = {
    # Topic 1: Physical quantities and units
    "9702_def_precision": "9702_t01",
    "9702_def_accuracy": "9702_t01",
    "9702_def_systematic_error": "9702_t01",
    "9702_def_random_error": "9702_t01",
    "9702_def_scalar_quantity": "9702_t01",
    "9702_def_vector_quantity": "9702_t01",
    "9702_def_instrument_resolution": "9702_t01",

    # Topic 2: Kinematics
    "9702_def_displacement": "9702_t02",
    "9702_def_velocity": "9702_t02",
    "9702_def_acceleration": "9702_t02",

    # Topic 3: Dynamics
    "9702_def_mass": "9702_t03",
    "9702_def_linear_momentum": "9702_t03",
    "9702_def_force": "9702_t03",
    "9702_def_newtons_first_law": "9702_t03",
    "9702_def_newtons_third_law": "9702_t03",
    "9702_def_conservation_of_momentum": "9702_t03",
    "9702_def_elastic_collision": "9702_t03",

    # Topic 4: Forces, density and pressure
    "9702_def_centre_of_gravity": "9702_t04",
    "9702_def_moment_of_force": "9702_t04",
    "9702_def_principle_of_moments": "9702_t04",
    "9702_def_torque_of_a_couple": "9702_t04",
    "9702_def_density": "9702_t04",
    "9702_def_pressure": "9702_t04",

    # Topic 5: Work, energy and power
    "9702_def_work_done": "9702_t05",
    "9702_def_kinetic_energy": "9702_t05",
    "9702_def_gravitational_potential_energy": "9702_t05",
    "9702_def_power": "9702_t05",

    # Topic 6: Deformation of solids
    "9702_def_hookes_law": "9702_t06",
    "9702_def_stress": "9702_t06",
    "9702_def_strain": "9702_t06",
    "9702_def_young_modulus": "9702_t06",
    "9702_def_elastic_potential_energy": "9702_t06",

    # Topic 7: Waves
    "9702_def_progressive_wave": "9702_t07",
    "9702_def_transverse_wave": "9702_t07",
    "9702_def_longitudinal_wave": "9702_t07",
    "9702_def_wavelength": "9702_t07",
    "9702_def_frequency": "9702_t07",
    "9702_def_period": "9702_t07",
    "9702_def_amplitude": "9702_t07",
    "9702_def_doppler_effect": "9702_t07",

    # Topic 8: Superposition
    "9702_def_superposition": "9702_t08",
    "9702_def_diffraction": "9702_t08",
    "9702_def_coherence": "9702_t08",
    "9702_def_node": "9702_t08",
    "9702_def_antinode": "9702_t08",

    # Topic 9: Current electricity
    "9702_def_electric_current": "9702_t09",
    "9702_def_charge_quantisation": "9702_t09",
    "9702_def_coulomb": "9702_t09",
    "9702_def_potential_difference": "9702_t09",
    "9702_def_electromotive_force": "9702_t09",
    "9702_def_volt": "9702_t09",
    "9702_def_resistance": "9702_t09",
    "9702_def_ohm": "9702_t09",
    "9702_def_ohms_law": "9702_t09",

    # Topic 10: D.C. circuits
    "9702_def_kirchhoffs_first_law": "9702_t10",
    "9702_def_kirchhoffs_second_law": "9702_t10",

    # Topic 11: Particle physics
    "9702_def_fundamental_particle": "9702_t11",

    # Topic 12: Motion in a circle
    "9702_def_radian": "9702_t12",

    # Topic 13: Gravitational fields
    "9702_def_gravitational_field": "9702_t13",
    "9702_def_gravitational_field_strength": "9702_t13",
    "9702_def_gravitational_potential": "9702_t13",
    "9702_def_newtons_law_of_gravitation": "9702_t13",

    # Topic 14: Temperature
    "9702_def_thermal_equilibrium": "9702_t14",
    "9702_def_absolute_zero": "9702_t14",

    # Topic 15: Ideal gases
    "9702_def_ideal_gas": "9702_t15",
    "9702_def_mole": "9702_t15",
    "9702_def_avogadro_constant": "9702_t15",

    # Topic 16: Thermodynamics
    "9702_def_internal_energy": "9702_t16",
    "9702_def_first_law_of_thermodynamics": "9702_t16",
    "9702_def_specific_heat_capacity": "9702_t16",
    "9702_def_specific_latent_heat": "9702_t16",

    # Topic 17: Oscillations
    "9702_def_simple_harmonic_motion": "9702_t17",
    "9702_def_damping": "9702_t17",
    "9702_def_resonance": "9702_t17",

    # Topic 18: Electric fields
    "9702_def_electric_field_strength": "9702_t18",
    "9702_def_coulombs_law": "9702_t18",
    "9702_def_electric_potential": "9702_t18",
    "9702_def_electric_field_line": "9702_t18",

    # Topic 19: Capacitance
    "9702_def_capacitance": "9702_t19",
    "9702_def_time_constant": "9702_t19",

    # Topic 20: Magnetic fields
    "9702_def_magnetic_field": "9702_t20",
    "9702_def_magnetic_flux_density": "9702_t20",
    "9702_def_magnetic_flux": "9702_t20",
    "9702_def_magnetic_flux_linkage": "9702_t20",
    "9702_def_faradays_law": "9702_t20",
    "9702_def_lenzs_law": "9702_t20",

    # Topic 21: Alternating currents
    "9702_def_rectification": "9702_t21",

    # Topic 22: Quantum physics
    "9702_def_photon": "9702_t22",
    "9702_def_photoelectric_effect": "9702_t22",
    "9702_def_work_function": "9702_t22",
    "9702_def_threshold_frequency": "9702_t22",
    "9702_def_de_broglie_wavelength": "9702_t22",

    # Topic 23: Nuclear physics
    "9702_def_mass_defect": "9702_t23",
    "9702_def_nuclear_binding_energy": "9702_t23",
    "9702_def_nuclear_fission": "9702_t23",
    "9702_def_nuclear_fusion": "9702_t23",
    "9702_def_radioactive_decay": "9702_t23",
    "9702_def_activity": "9702_t23",
    "9702_def_decay_constant": "9702_t23",
    "9702_def_half_life": "9702_t23",
    "9702_def_annihilation": "9702_t23",

    # Topic 24: Medical physics
    "9702_def_specific_acoustic_impedance": "9702_t24",
    "9702_def_linear_attenuation_coefficient": "9702_t24",
    "9702_def_contrast": "9702_t24",
    "9702_def_tracer": "9702_t24",

    # Topic 25: Astronomy and cosmology
    "9702_def_luminosity": "9702_t25",
    "9702_def_radiant_flux_intensity": "9702_t25",
    "9702_def_standard_candle": "9702_t25",
    "9702_def_wiens_displacement_law": "9702_t25",
    "9702_def_hubbles_law": "9702_t25",
    "9702_def_redshift": "9702_t25",

    # Legacy syllabus items (operational amplifiers & telecommunications)
    "9702_def_bandwidth": "9702_t24",
    "9702_def_digital_signal": "9702_t24",
    "9702_def_amplitude_modulation": "9702_t24",
    "9702_def_slew_rate": "9702_t21",
    "9702_def_voltage_gain": "9702_t21",
    "9702_def_virtual_earth": "9702_t21",
}

CANONICAL_FORM_TOPICS: Dict[str, str] = {
    # Topic 2: Kinematics
    "9702_formula_acceleration": "9702_t02",
    "9702_formula_average_speed": "9702_t02",
    "9702_formula_average_velocity": "9702_t02",
    "9702_formula_constant_acceleration_velocity": "9702_t02",
    "9702_formula_constant_acceleration_displacement": "9702_t02",
    "9702_formula_constant_acceleration_velocity_displacement": "9702_t02",
    "9702_formula_uniform_motion_displacement": "9702_t02",

    # Topic 3: Dynamics
    "9702_formula_weight": "9702_t03",
    "9702_formula_newtons_second_law": "9702_t03",
    "9702_formula_momentum": "9702_t03",
    "9702_formula_elastic_collision_relative_speed": "9702_t03",

    # Topic 4: Forces, density and pressure
    "9702_formula_density": "9702_t04",
    "9702_formula_moment": "9702_t04",
    "9702_formula_pressure_force": "9702_t04",
    "9702_formula_hydrostatic_pressure": "9702_t04",
    "9702_formula_upthrust": "9702_t04",

    # Topic 5: Work, energy and power
    "9702_formula_kinetic_energy": "9702_t05",
    "9702_formula_work": "9702_t05",
    "9702_formula_gravitational_potential_energy": "9702_t05",
    "9702_formula_mechanical_power": "9702_t05",
    "9702_formula_power_energy_time": "9702_t05",
    "9702_formula_efficiency": "9702_t05",

    # Topic 6: Deformation of solids
    "9702_formula_hookes_law": "9702_t06",
    "9702_formula_strain": "9702_t06",
    "9702_formula_stress": "9702_t06",
    "9702_formula_young_modulus": "9702_t06",
    "9702_formula_elastic_potential_energy": "9702_t06",

    # Topic 7: Waves
    "9702_formula_wave_speed": "9702_t07",
    "9702_formula_period_frequency": "9702_t07",
    "9702_formula_wave_intensity_amplitude": "9702_t07",
    "9702_formula_wave_intensity_power_area": "9702_t07",
    "9702_formula_doppler_moving_source": "9702_t07",
    "9702_formula_phase_difference_time": "9702_t07",
    "9702_formula_malus_law": "9702_t07",

    # Topic 8: Superposition
    "9702_formula_diffraction_grating": "9702_t08",
    "9702_formula_double_slit_interference": "9702_t08",
    "9702_formula_stationary_wave_spacing": "9702_t08",
    "9702_formula_two_source_interference_path_difference": "9702_t08",

    # Topic 9: Current electricity
    "9702_formula_potential_difference": "9702_t09",
    "9702_formula_ohms_law": "9702_t09",
    "9702_formula_electrical_power": "9702_t09",
    "9702_formula_charge_current_time": "9702_t09",
    "9702_formula_resistivity": "9702_t09",
    "9702_formula_charge_quantisation": "9702_t09",
    "9702_formula_current_drift": "9702_t09",
    "9702_formula_energy_charge_potential_difference": "9702_t09",

    # Topic 10: D.C. circuits
    "9702_formula_potential_divider": "9702_t10",
    "9702_formula_kirchhoff_first_law": "9702_t10",
    "9702_formula_kirchhoff_second_law": "9702_t10",
    "9702_formula_parallel_resistance": "9702_t10",
    "9702_formula_series_resistance": "9702_t10",
    "9702_formula_terminal_potential_difference": "9702_t10",

    # Topic 11: Particle physics
    "9702_formula_nuclear_charge_to_mass_ratio": "9702_t11",

    # Topic 12: Motion in a circle
    "9702_formula_centripetal_force": "9702_t12",
    "9702_formula_angular_speed_period": "9702_t12",
    "9702_formula_centripetal_acceleration": "9702_t12",
    "9702_formula_circular_linear_speed": "9702_t12",
    "9702_formula_angular_displacement_time": "9702_t12",
    "9702_formula_arc_length": "9702_t12",

    # Topic 13: Gravitational fields
    "9702_formula_gravitational_field_strength": "9702_t13",
    "9702_formula_newtons_law_of_gravitation": "9702_t13",
    "9702_formula_gravitational_field_strength_point_mass": "9702_t13",
    "9702_formula_gravitational_potential_point_mass": "9702_t13",
    "9702_formula_gravitational_potential_energy_potential": "9702_t13",
    "9702_formula_escape_speed": "9702_t13",

    # Topic 14: Temperature
    "9702_formula_celsius_to_kelvin": "9702_t14",

    # Topic 15: Ideal gases
    "9702_formula_ideal_gas_equation_moles": "9702_t15",
    "9702_formula_ideal_gas_equation_molecules": "9702_t15",
    "9702_formula_kinetic_theory_pressure": "9702_t15",
    "9702_formula_kinetic_energy_gas_molecule": "9702_t15",

    # Topic 16: Thermodynamics
    "9702_formula_first_law_of_thermodynamics": "9702_t16",
    "9702_formula_specific_heat_capacity": "9702_t16",
    "9702_formula_work_done_gas_expansion": "9702_t16",
    "9702_formula_specific_latent_heat": "9702_t16",

    # Topic 17: Oscillations
    "9702_formula_shm_acceleration": "9702_t17",
    "9702_formula_shm_max_velocity": "9702_t17",
    "9702_formula_shm_energy": "9702_t17",
    "9702_formula_shm_velocity_displacement": "9702_t17",
    "9702_formula_shm_displacement_sine": "9702_t17",

    # Topic 18: Electric fields
    "9702_formula_electric_field_point_charge": "9702_t18",
    "9702_formula_electric_field_force": "9702_t18",
    "9702_formula_electric_potential_point_charge": "9702_t18",
    "9702_formula_coulombs_law": "9702_t18",
    "9702_formula_electric_work_uniform_field": "9702_t18",
    "9702_formula_uniform_electric_field_strength": "9702_t18",
    "9702_formula_electric_potential_energy_point_charges": "9702_t18",

    # Topic 19: Capacitance
    "9702_formula_capacitance_definition": "9702_t19",
    "9702_formula_capacitor_time_constant": "9702_t19",
    "9702_formula_capacitors_series": "9702_t19",
    "9702_formula_capacitors_parallel": "9702_t19",
    "9702_formula_capacitor_energy": "9702_t19",
    "9702_formula_capacitor_discharge_exponential": "9702_t19",

    # Topic 20: Magnetic fields
    "9702_formula_magnetic_flux": "9702_t20",
    "9702_formula_magnetic_flux_linkage": "9702_t20",
    "9702_formula_hall_voltage": "9702_t20",
    "9702_formula_magnetic_force_current_wire": "9702_t20",
    "9702_formula_faradays_law_emf": "9702_t20",
    "9702_formula_magnetic_force_moving_charge": "9702_t20",
    "9702_formula_charged_particle_orbit_radius": "9702_t20",
    "9702_formula_velocity_selector": "9702_t20",

    # Topic 21: Alternating currents
    "9702_formula_sinusoidal_ac": "9702_t21",
    "9702_formula_rms_values": "9702_t21",
    "9702_formula_ac_mean_power": "9702_t21",
    "9702_formula_inverting_amplifier_gain": "9702_t21",
    "9702_formula_non_inverting_amplifier_gain": "9702_t21",

    # Topic 22: Quantum physics
    "9702_formula_photon_energy": "9702_t22",
    "9702_formula_de_broglie_wavelength": "9702_t22",
    "9702_formula_photon_momentum": "9702_t22",
    "9702_formula_photoelectric_equation": "9702_t22",

    # Topic 23: Nuclear physics
    "9702_formula_mass_energy_equivalence": "9702_t23",
    "9702_formula_activity_decay_constant": "9702_t23",
    "9702_formula_half_life_decay_constant": "9702_t23",
    "9702_formula_radioactive_decay_law": "9702_t23",

    # Topic 24: Medical physics
    "9702_formula_attenuation_intensity": "9702_t24",
    "9702_formula_specific_acoustic_impedance": "9702_t24",
    "9702_formula_intensity_reflection_coefficient": "9702_t24",
    "9702_formula_attenuation_decibels": "9702_t24",

    # Topic 25: Astronomy and cosmology
    "9702_formula_hubbles_law": "9702_t25",
    "9702_formula_radiant_flux_intensity": "9702_t25",
    "9702_formula_wiens_displacement_law": "9702_t25",
    "9702_formula_doppler_redshift": "9702_t25",
    "9702_formula_stefan_boltzmann_law": "9702_t25",
}

FORMULA_CROSS_TOPICS: Dict[str, Set[str]] = {
    "9702_formula_acceleration": {"9702_t01", "9702_t03"},
    "9702_formula_weight": {"9702_t01", "9702_t04"},
    "9702_formula_newtons_second_law": {"9702_t01", "9702_t02"},
    "9702_formula_density": {"9702_t01"},
    "9702_formula_work": {"9702_t03", "9702_t04"},
    "9702_formula_pressure_force": {"9702_t01"},
    "9702_formula_elastic_potential_energy": {"9702_t05"},
    "9702_formula_gravitational_field_strength": {"9702_t03"},
    "9702_formula_diffraction_grating": {"9702_t07"},
}

EXTRA_DEF_ALIASES: Dict[str, List[str]] = {
    "9702_def_linear_momentum": ["momentum"],
    "9702_def_electric_field_strength": ["electric field"],
    "9702_def_gravitational_field_strength": ["gravitational field"],
    "9702_def_conservation_of_momentum": ["conservation of momentum", "law of conservation of momentum"],
    "9702_def_elastic_collision": ["colliding elastically", "elastic collisions", "elastically"],
    "9702_def_coherence": ["coherent"],
    "9702_def_transverse_wave": ["transverse wave", "transverse waves", "transverse"],
    "9702_def_longitudinal_wave": ["longitudinal wave", "longitudinal waves", "longitudinal"],
}

EXTRA_FORM_ALIASES: Dict[str, List[str]] = {
    "9702_formula_newtons_second_law": ["f=ma", "f=deltap/deltat", "newton's second law", "f = ma"],
    "9702_formula_ohms_law": ["v=ir", "i=v/r", "r=v/i", "ohm's law"],
    "9702_formula_charge_current_time": ["q=it", "i=q/t", "q = it"],
    "9702_formula_uniform_motion_displacement": ["s=vt", "v=s/t", "d=vt"],
    "9702_formula_angular_speed_period": ["omega=2pi/t", "omega=2pif", "2pi/t", "2pif"],
    "9702_formula_mass_energy_equivalence": ["e=mc^2", "deltae=deltamc^2", "e = mc^2", "mass-energy"],
    "9702_formula_specific_latent_heat": ["q=ml", "e=ml", "latent heat"],
    "9702_formula_sinusoidal_ac": ["sin(omegat)", "v_0sin", "i_0sin", "sinusoidal"],
    "9702_formula_gravitational_potential_energy_potential": ["e_p=-gmm/r", "gmm/r", "mphi"],
    "9702_formula_elastic_collision_relative_speed": ["relative speed", "u_1-u_2=v_2-v_1", "elastic collision"],
    "9702_formula_shm_displacement_sine": ["x=x_0sin", "x_0sin(omegat)"],
    "9702_formula_photoelectric_equation": ["hf=phi+e", "hf = phi", "photoelectric equation", "e_max=hf-phi"],
    "9702_formula_celsius_to_kelvin": ["+273", "+ 273.15", "kelvin"],
    "9702_formula_escape_speed": ["2gm/r", "escape speed", "escape velocity"],
    "9702_formula_rms_values": ["v_0/sqrt(2)", "i_0/sqrt(2)", "r.m.s.", "root-mean-square"],
    "9702_formula_electric_work_uniform_field": ["deltae=qed", "qed", "w=qed"],
    "9702_formula_stationary_wave_spacing": ["lambda/2", "lambda/4", "node-node", "node to node"],
    "9702_formula_series_resistance": ["r_1+r_2", "r_total=r_1+r_2", "series resistance", "resistors in series"],
    "9702_formula_power_energy_time": ["p=w/t", "p=deltae/t", "energy transferred per unit time", "work done per unit time"],
    "9702_formula_uniform_electric_field_strength": ["e=v/d", "e=deltav/d", "v/d"],
    "9702_formula_two_source_interference_path_difference": ["path difference", "nlambda", "(n+1/2)lambda"],
    "9702_formula_energy_charge_potential_difference": ["w=vq", "deltae=vq", "vq", "eq"],
    "9702_formula_nuclear_charge_to_mass_ratio": ["q/m", "charge-to-mass", "specific charge"],
    "9702_formula_phase_difference_time": ["2pideltat/t", "phase difference"],
    "9702_formula_electric_potential_energy_point_charges": ["qq/4piepsilont_0r", "electric potential energy"],
    "9702_formula_ac_mean_power": ["mean power", "v_0^2/2r", "i_0^2r/2"],
    "9702_formula_inverting_amplifier_gain": ["-r_f/r_in", "inverting amplifier"],
    "9702_formula_non_inverting_amplifier_gain": ["1+r_f/r_1", "non-inverting amplifier"],
}


def sanitize(text: str) -> str:
    """Ensure strictly zero em dashes in any text output."""
    return text.replace(chr(8212), "-").replace("\u2014", "-")


def normalize_latex(text: str) -> str:
    return re.sub(r"[\s\\]+", "", text).lower()


def clean_prompt_text(text: str) -> str:
    """Clean markdown formatting and newlines from a question prompt."""
    t = text.replace("\n", " ").strip()
    return t.replace("*", "").replace("$", "").replace("_", "").replace("{", "").replace("}", "")


def main():
    print("Starting Authoritative Cambridge Physics (9702) Extraction Engine...")

    # 1. Load syllabus taxonomies
    as_tax = json.loads(AS_TAX_PATH.read_text(encoding="utf-8"))
    a2_tax = json.loads(A2_TAX_PATH.read_text(encoding="utf-8"))
    topic_names: Dict[str, str] = {}
    topic_levels: Dict[str, str] = {}
    for top in as_tax["topics"]:
        tid = top["topic_id"]
        topic_names[tid] = top["topic_name"]
        topic_levels[tid] = "AS"
    for top in a2_tax["topics"]:
        tid = top["topic_id"]
        topic_names[tid] = top["topic_name"]
        topic_levels[tid] = "A2"

    # 2. Load base definitions and formulas
    base_defs = json.loads(BASE_DEFS_PATH.read_text(encoding="utf-8"))["definitions"]
    base_forms = json.loads(BASE_FORMS_PATH.read_text(encoding="utf-8"))["formulas"]

    print(f"Loaded {len(base_defs)} base definitions and {len(base_forms)} base formulas.")

    # 3. Compile target-specific definition matchers
    def_matchers = []
    for d in base_defs:
        did = d["definition_id"]
        can_top = CANONICAL_DEF_TOPICS.get(did, "9702_t01")
        primary_term = d["term"]
        aliases = list(d.get("term_aliases", [])) + EXTRA_DEF_ALIASES.get(did, [])
        all_terms = [primary_term] + aliases

        clean_terms = []
        for t in all_terms:
            t_clean = t.strip().lower()
            clean_terms.append(t_clean)
            if "(" in t:
                base = re.sub(r"\s*\(.*?\)", "", t).strip().lower()
                if base:
                    clean_terms.append(base)
                inside = re.findall(r"\((.*?)\)", t)
                for ins in inside:
                    clean_terms.append(ins.strip().lower())

        clean_terms = list(set(clean_terms))
        for t in clean_terms:
            def_matchers.append((len(t), t, did, can_top, d))

    def_matchers.sort(key=lambda x: x[0], reverse=True)

    def_command_words = [
        "define", "state what is meant by", "explain what is meant by",
        "state the principle of", "state newton", "state coulomb", "state faraday",
        "state lenz", "state hooke", "state kepler", "state ohm", "state kirchhoff",
        "state wien", "state hubble", "state the law of", "state the relationship"
    ]

    # 4. Compile bounded formula matchers
    form_matchers = []
    for f in base_forms:
        fid = f["formula_id"]
        can_top = CANONICAL_FORM_TOPICS.get(fid, "9702_t01")
        allowed_topics = {can_top}
        if fid in FORMULA_CROSS_TOPICS:
            allowed_topics.update(FORMULA_CROSS_TOPICS[fid])

        names = [f["name"].lower()] + [n.lower() for n in f.get("name_aliases", [])]
        raw_latexes = [f["latex"].strip()] + [l.strip() for l in f.get("latex_aliases", [])]
        norm_latexes = [normalize_latex(l) for l in raw_latexes]

        extra = EXTRA_FORM_ALIASES.get(fid, [])
        for ex in extra:
            ex_low = ex.lower()
            names.append(ex_low)
            norm_latexes.append(normalize_latex(ex_low))

        form_matchers.append((fid, f["name"], can_top, allowed_topics, names, norm_latexes, f))

    # Evidence accumulators
    def_evidence: Dict[str, Dict[str, Any]] = {}
    for d in base_defs:
        did = d["definition_id"]
        can_top = CANONICAL_DEF_TOPICS.get(did, "9702_t01")
        def_evidence[did] = {
            "definition_id": did,
            "canonical_topic_id": can_top,
            "term": d["term"],
            "accepted_definition": d.get("accepted_definition", ""),
            "accepted_alternatives": list(d.get("accepted_alternatives", [])),
            "verbatim_markschemes": [],
            "topic_ids": {can_top},
            "evidence_question_ids": set(),
            "evidence_leaves": [],
            "merged_ids": d.get("merged_ids", []),
        }

    form_evidence: Dict[str, Dict[str, Any]] = {}
    for f in base_forms:
        fid = f["formula_id"]
        can_top = CANONICAL_FORM_TOPICS.get(fid, "9702_t01")
        form_evidence[fid] = {
            "formula_id": fid,
            "canonical_topic_id": can_top,
            "name": f["name"],
            "latex": f["latex"],
            "topic_ids": {can_top},
            "evidence_question_ids": set(),
            "evidence_leaves": [],
            "merged_ids": f.get("merged_ids", []),
        }

    # ================= 5. EXTRACT DEFINITIONS FROM P2 & P4 =================
    print("Extracting authentic definition questions from Paper 2 and Paper 4...")
    for comp in ["p2", "p4"]:
        for q_dir in sorted(PAPERS_ROOT.glob(f"{comp}/**/question_*")):
            if not q_dir.is_dir():
                continue

            leaf_rel = str(q_dir.relative_to(PAPERS_ROOT))

            ms_file = q_dir / "markscheme.json"
            ms_rev = q_dir / "markscheme_reviewed.json"
            target_ms = ms_file if (ms_file.is_file() and ms_file.stat().st_size > 0) else ms_rev
            ms_map = {}
            if target_ms.is_file() and target_ms.stat().st_size > 0:
                try:
                    ms_data = json.loads(target_ms.read_text(encoding="utf-8"))
                    for mp in ms_data.get("parts", []):
                        pts = mp.get("marking_points", [])
                        ms_map[mp.get("id", "").lower()] = " | ".join(
                            [p.get("text", "") for p in pts if isinstance(p, dict) and p.get("text")]
                        )
                except Exception:
                    pass

            ocr_file = q_dir / "question_ocr.json"
            txt_file = q_dir / "question.txt"
            part_prompts: List[Tuple[str, str]] = []
            if ocr_file.is_file() and ocr_file.stat().st_size > 0:
                try:
                    ocr_data = json.loads(ocr_file.read_text(encoding="utf-8"))
                    for op in ocr_data.get("parts", []):
                        pid = op.get("id", "")
                        prompt = op.get("part_stem") or op.get("text") or ""
                        part_prompts.append((pid, prompt))
                except Exception:
                    pass

            if not part_prompts and txt_file.is_file() and txt_file.stat().st_size > 0:
                part_prompts.append(("q", txt_file.read_text(encoding="utf-8")))

            for pid, prompt in part_prompts:
                p_clean = clean_prompt_text(prompt)
                p_clean_lower = p_clean.lower()
                if not any(cmd in p_clean_lower for cmd in def_command_words):
                    continue

                matched_did = None
                for t_len, t_str, did, can_top, d_obj in def_matchers:
                    if t_str == "force" and any(
                        k in p_clean_lower
                        for k in ["electromotive", "centripetal", "gravitational", "moment of", "drag", "magnetic"]
                    ):
                        continue

                    if re.search(rf"\b{re.escape(t_str)}\b", p_clean_lower):
                        matched_did = did
                        break

                if matched_did:
                    ms_note = ms_map.get(pid.lower(), "")
                    def_evidence[matched_did]["evidence_question_ids"].add(pid)
                    def_evidence[matched_did]["evidence_leaves"].append({
                        "part_id": pid,
                        "leaf_path": leaf_rel,
                        "component": comp,
                        "prompt": p_clean[:100],
                    })
                    if ms_note and len(def_evidence[matched_did]["verbatim_markschemes"]) < 4:
                        clean_ms = ms_note.replace("\n", " ").strip()
                        if clean_ms and clean_ms not in def_evidence[matched_did]["verbatim_markschemes"]:
                            def_evidence[matched_did]["verbatim_markschemes"].append(clean_ms)

    # ================= 6. EXTRACT FORMULAS ACROSS P1, P2, P4 =================
    print("Extracting bounded formula questions across Paper 1, Paper 2, and Paper 4...")

    for en_file in sorted(PAPERS_ROOT.glob("p1/**/enrichment/*.enrichment.json")):
        try:
            en_data = json.loads(en_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        tid = en_data.get("topic_id") or en_data.get("mapping", {}).get("primary_topic_id")
        if not tid:
            continue

        qid = en_data.get("question_id", en_file.stem.split(".")[0])
        leaf_rel = str(en_file.parent.parent.relative_to(PAPERS_ROOT))
        acc = en_data.get("accepted_answer", "")
        ms_text = en_data.get("options_breakdown", {}).get(acc, {}).get("explanation", "")
        wt = " ".join(en_data.get("walkthrough", []))
        kc = " ".join(en_data.get("key_concepts", []))

        full_text = f"{wt} {kc} {ms_text}".lower()
        norm_full = normalize_latex(full_text)

        for fid, fname, can_top, allowed_topics, names, norm_latexes, f_obj in form_matchers:
            if tid in allowed_topics:
                matched = False
                if any(n in full_text for n in names):
                    matched = True
                elif any(len(nl) >= 3 and nl in norm_full for nl in norm_latexes):
                    matched = True

                if matched:
                    form_evidence[fid]["topic_ids"].add(tid)
                    form_evidence[fid]["evidence_question_ids"].add(qid)
                    form_evidence[fid]["evidence_leaves"].append({
                        "part_id": qid,
                        "leaf_path": leaf_rel,
                        "component": "p1",
                    })

    for comp in ["p2", "p4"]:
        for q_dir in sorted(PAPERS_ROOT.glob(f"{comp}/**/question_*")):
            if not q_dir.is_dir():
                continue
            en_file = q_dir / "enrichment.json"
            if not en_file.is_file():
                continue
            try:
                en_data = json.loads(en_file.read_text(encoding="utf-8"))
            except Exception:
                continue

            leaf_rel = str(q_dir.relative_to(PAPERS_ROOT))

            for part in en_data.get("parts", []):
                if not isinstance(part, dict):
                    continue
                tid = part.get("primary_topic_id") or part.get("mapping", {}).get("primary_topic_id")
                if not tid:
                    continue

                pid = part.get("part_id", "")
                proper_ans = part.get("proper_answer", "")
                wt = " ".join(part.get("walkthrough", []))
                kc = " ".join(part.get("key_concepts", []))
                text_block = f"{proper_ans} {wt} {kc}".lower()
                norm_text = normalize_latex(text_block)

                for fid, fname, can_top, allowed_topics, names, norm_latexes, f_obj in form_matchers:
                    if tid in allowed_topics:
                        matched = False
                        if any(n in text_block for n in names):
                            matched = True
                        elif any(len(nl) >= 3 and nl in norm_text for nl in norm_latexes):
                            matched = True

                        if matched:
                            form_evidence[fid]["topic_ids"].add(tid)
                            form_evidence[fid]["evidence_question_ids"].add(pid)
                            form_evidence[fid]["evidence_leaves"].append({
                                "part_id": pid,
                                "leaf_path": leaf_rel,
                                "component": comp,
                            })

    # ================= 7. FORMAT & SERIALIZE REGISTRIES =================
    print("Compiling authoritative JSON registries...")

    def_registry_output = []
    for did, data in def_evidence.items():
        seen_parts = set()
        dedup_leaves = []
        for l in sorted(data["evidence_leaves"], key=lambda x: x["part_id"]):
            if l["part_id"] not in seen_parts:
                seen_parts.add(l["part_id"])
                dedup_leaves.append(l)

        def_item = {
            "definition_id": data["definition_id"],
            "canonical_topic_id": data["canonical_topic_id"],
            "term": data["term"],
            "accepted_definition": data["accepted_definition"],
            "accepted_alternatives": data["accepted_alternatives"],
            "verbatim_markschemes": data["verbatim_markschemes"][:4],
            "topic_ids": sorted(list(data["topic_ids"])),
            "testing_count": len(data["evidence_question_ids"]),
            "evidence_question_ids": sorted(list(data["evidence_question_ids"])),
            "evidence_leaves": dedup_leaves,
        }
        if data.get("merged_ids"):
            def_item["merged_ids"] = data["merged_ids"]
        def_registry_output.append(def_item)

    form_registry_output = []
    for fid, data in form_evidence.items():
        seen_parts = set()
        dedup_leaves = []
        for l in sorted(data["evidence_leaves"], key=lambda x: x["part_id"]):
            if l["part_id"] not in seen_parts:
                seen_parts.add(l["part_id"])
                dedup_leaves.append(l)

        form_item = {
            "formula_id": data["formula_id"],
            "canonical_topic_id": data["canonical_topic_id"],
            "name": data["name"],
            "latex": data["latex"],
            "topic_ids": sorted(list(data["topic_ids"])),
            "testing_count": len(data["evidence_question_ids"]),
            "evidence_question_ids": sorted(list(data["evidence_question_ids"])),
            "evidence_leaves": dedup_leaves,
        }
        if data.get("merged_ids"):
            form_item["merged_ids"] = data["merged_ids"]
        form_registry_output.append(form_item)

    def_registry_output.sort(key=lambda x: x["testing_count"], reverse=True)
    form_registry_output.sort(key=lambda x: x["testing_count"], reverse=True)

    def_reg_path = KNOWLEDGE_ROOT / "definitions-registry.json"
    def_reg_text = sanitize(json.dumps(def_registry_output, indent=2, ensure_ascii=False) + "\n")
    def_reg_path.write_text(def_reg_text, encoding="utf-8")
    print(f"Wrote {len(def_registry_output)} definitions to {def_reg_path}")

    form_reg_path = KNOWLEDGE_ROOT / "formulas-registry.json"
    form_reg_text = sanitize(json.dumps(form_registry_output, indent=2, ensure_ascii=False) + "\n")
    form_reg_path.write_text(form_reg_text, encoding="utf-8")
    print(f"Wrote {len(form_registry_output)} formulas to {form_reg_path}")

    print("Updating knowledge-base/definitions.json and formulas.json...")
    enriched_kb_defs = {
        "schema_version": "9702_definitions_v1",
        "subject_code": "9702",
        "definitions": [
            {
                "definition_id": d["definition_id"],
                "canonical_topic_id": d["canonical_topic_id"],
                "term": d["term"],
                "accepted_definition": d["accepted_definition"],
                "accepted_alternatives": d["accepted_alternatives"],
                "topic_ids": d["topic_ids"],
                "testing_count": d["testing_count"],
                "evidence_question_ids": d["evidence_question_ids"],
                **({"merged_ids": d["merged_ids"]} if "merged_ids" in d else {}),
            }
            for d in def_registry_output
        ],
    }
    BASE_DEFS_PATH.write_text(
        sanitize(json.dumps(enriched_kb_defs, indent=2, ensure_ascii=False) + "\n"), encoding="utf-8"
    )

    enriched_kb_forms = {
        "schema_version": "9702_formulas_v1",
        "subject_code": "9702",
        "formulas": [
            {
                "formula_id": f["formula_id"],
                "canonical_topic_id": f["canonical_topic_id"],
                "name": f["name"],
                "latex": f["latex"],
                "topic_ids": f["topic_ids"],
                "testing_count": f["testing_count"],
                "evidence_question_ids": f["evidence_question_ids"],
                **({"merged_ids": f["merged_ids"]} if "merged_ids" in f else {}),
            }
            for f in form_registry_output
        ],
    }
    BASE_FORMS_PATH.write_text(
        sanitize(json.dumps(enriched_kb_forms, indent=2, ensure_ascii=False) + "\n"), encoding="utf-8"
    )

    # ================= 8. GENERATE CLEAN MARKDOWN REFERENCE =================
    print("Generating Clean Master Reference Markdown Document...")
    md = []
    md.append("# Cambridge Physics (9702) Definitions & Formulas Reference Guide")
    md.append("")
    md.append("## Executive Overview")
    md.append("")
    md.append(
        "This authoritative reference catalogs all official Cambridge Physics definitions and mathematical formulas across the complete 2016-2025 archive (8,335 items across Paper 1, Paper 2, and Paper 4)."
    )
    md.append(
        "Definitions are strictly extracted from Paper 2 and Paper 4 definition questions with verbatim mark scheme requirements. Formulas are bounded by their canonical syllabus topics."
    )
    md.append("")
    md.append("Scope Rule: Strictly ZERO em dashes anywhere in this reference.")
    md.append("")

    # Top 25 Most Frequently Tested Definitions
    md.append("## Top 25 Most Frequently Tested Definitions")
    md.append("")
    md.append("Ranked by past paper definition question occurrences across the 10-year examination archive:")
    md.append("")
    md.append("| Rank | Term | Canonical Topic | Official Mark Scheme Definition | Questions | Sample Question Leaf |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")

    for idx, d in enumerate(def_registry_output[:25], 1):
        sample_leaf = d["evidence_leaves"][0]["leaf_path"] if d["evidence_leaves"] else "N/A"
        sample_part = d["evidence_leaves"][0]["part_id"] if d["evidence_leaves"] else "N/A"
        can_tid = d["canonical_topic_id"]
        t_name = topic_names.get(can_tid, can_tid)
        clean_def = d["accepted_definition"].replace("\n", " ").strip()
        if len(clean_def) > 75:
            clean_def = clean_def[:75] + "..."
        md.append(
            f"| {idx} | **{d['term']}** | `{can_tid}` ({t_name}) | {clean_def} | {d['testing_count']} | `{sample_leaf}` ({sample_part}) |"
        )

    md.append("")

    # Top 25 Most Frequently Tested Formulas
    md.append("## Top 25 Most Frequently Tested Formulas")
    md.append("")
    md.append("Ranked by past paper problem occurrences across the 10-year examination archive:")
    md.append("")
    md.append(
        "| Rank | Formula Name | Canonical Topic | LaTeX Mathematical Expression | Questions | Sample Question Leaf |"
    )
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- |")

    for idx, f in enumerate(form_registry_output[:25], 1):
        sample_leaf = f["evidence_leaves"][0]["leaf_path"] if f["evidence_leaves"] else "N/A"
        sample_part = f["evidence_leaves"][0]["part_id"] if f["evidence_leaves"] else "N/A"
        can_tid = f["canonical_topic_id"]
        t_name = topic_names.get(can_tid, can_tid)
        latex_str = f"`${f['latex']}$`"
        md.append(
            f"| {idx} | **{f['name']}** | `{can_tid}` ({t_name}) | {latex_str} | {f['testing_count']} | `{sample_leaf}` ({sample_part}) |"
        )

    md.append("")

    # Topic-by-Topic Complete Catalog
    md.append("## Topic-by-Topic Complete Catalog (Topics 1 to 25)")
    md.append("")

    for tid in sorted(topic_names.keys()):
        t_name = topic_names[tid]
        t_level = topic_levels[tid]

        t_defs = [d for d in def_registry_output if d["canonical_topic_id"] == tid]
        t_forms = [f for f in form_registry_output if f["canonical_topic_id"] == tid]

        md.append(f"### Topic `{tid}`: {t_name} ({t_level})")
        md.append("")
        md.append(f"- **Total Canonical Definitions**: {len(t_defs)}")
        md.append(f"- **Total Canonical Formulas**: {len(t_forms)}")
        md.append("")

        if t_defs:
            md.append("#### Authoritative Mark Scheme Definitions")
            md.append("")
            for d in t_defs:
                md.append(f"- **{d['term']}** (Tested in {d['testing_count']} questions)")
                md.append(f"  - **Official Definition**: {d['accepted_definition']}")
                if d["verbatim_markschemes"]:
                    clean_ms = d["verbatim_markschemes"][0].replace("\n", " ").strip()
                    if len(clean_ms) > 130:
                        clean_ms = clean_ms[:130] + "..."
                    md.append(f"  - **Verbatim Marking Notes**: \"{clean_ms}\"")
                if d["evidence_leaves"]:
                    leaf_sample = d["evidence_leaves"][0]
                    md.append(f"  - **Example Leaf**: `{leaf_sample['leaf_path']}` (Part: `{leaf_sample['part_id']}`)")
            md.append("")

        if t_forms:
            md.append("#### Tested Mathematical Formulas")
            md.append("")
            for f in t_forms:
                md.append(f"- **{f['name']}**: `${f['latex']}$` (Tested in {f['testing_count']} questions)")
                if f["evidence_leaves"]:
                    leaf_sample = f["evidence_leaves"][0]
                    md.append(f"  - **Example Leaf**: `{leaf_sample['leaf_path']}` (Part: `{leaf_sample['part_id']}`)")
            md.append("")

    ref_md_path = KNOWLEDGE_ROOT / "physics-definitions-and-formulas-reference.md"
    clean_md_text = sanitize("\n".join(md) + "\n")
    ref_md_path.write_text(clean_md_text, encoding="utf-8")
    print(f"Successfully generated clean Reference Markdown Guide at {ref_md_path}")

    # ================= 9. VERIFY STRICT ZERO EM DASHES =================
    print("Verifying strictly ZERO em dashes across all outputs...")
    for p in [def_reg_path, form_reg_path, BASE_DEFS_PATH, BASE_FORMS_PATH, ref_md_path]:
        txt = p.read_text(encoding="utf-8")
        assert "\u2014" not in txt and chr(8212) not in txt, f"Em dash detected in {p}!"

    print("All outputs verified: 100% clean and zero em dashes.")


if __name__ == "__main__":
    main()
