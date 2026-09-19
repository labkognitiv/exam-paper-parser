#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const papers = process.argv.slice(2);
if (!papers.length) throw new Error('pass paper IDs');

const uniq = values => [...new Set(values)];
const m16Skills = {
  '9702_m16_22_q01_b_i': '9702_skill_si_units_homogeneity',
  '9702_m16_22_q02_b_i': '9702_skill_projectile_motion',
  '9702_m16_22_q02_b_ii': '9702_skill_projectile_motion',
  '9702_m16_22_q02_b_iii': '9702_skill_kinematics_equations',
  '9702_m16_22_q02_c_i': '9702_skill_kinematics_equations',
  '9702_m16_22_q02_c_ii': '9702_skill_kinetic_potential_energy',
  '9702_m16_22_q02_d': '9702_skill_projectile_motion',
  '9702_m16_22_q03_b_i': '9702_skill_kinetic_potential_energy',
  '9702_m16_22_q03_b_ii': '9702_skill_hookes_law_elastic_energy',
  '9702_m16_22_q03_b_iii': '9702_skill_newtons_laws',
  '9702_m16_22_q03_b_iv': '9702_skill_equilibrium_coplanar_forces',
  '9702_m16_22_q03_c': '9702_skill_hookes_law_elastic_energy',
  '9702_m16_22_q04_b_i': '9702_skill_progressive_wave_properties',
  '9702_m16_22_q05_b_ii': '9702_skill_iv_characteristics',
  '9702_m16_22_q05_b_iii': '9702_skill_potential_difference_power',
  '9702_m16_22_q05_b_iv': '9702_skill_resistivity',
};
const batchSkills = {
  '9702_s16_21_q06_c_iv': '9702_skill_potential_difference_power',
  '9702_s16_22_q04_b': '9702_skill_si_units_homogeneity',
  '9702_s16_23_q04_a': '9702_skill_equilibrium_coplanar_forces',
  '9702_s16_23_q06_b_ii': '9702_skill_potential_difference_power',
  '9702_s16_23_q07_a_i': '9702_skill_stationary_waves',
  '9702_s16_23_q07_a_ii': '9702_skill_stationary_waves',
};
const forceHybrid = new Set([
  '9702_s16_21_q02_a_i',
  '9702_s16_21_q02_a_ii',
  '9702_s16_21_q03_a_i',
  '9702_s16_23_q05_b_ii',
]);
const cleanText = value => {
  if (typeof value === 'string') return value.replace(/([^\n])\n(?=[a-z0-9$])/g, '$1 ');
  if (Array.isArray(value)) return value.map(cleanText);
  if (value && typeof value === 'object') {
    for (const key of Object.keys(value)) value[key] = cleanText(value[key]);
  }
  return value;
};

for (const paper of papers) {
  const match = paper.match(/^(9702_[msw]\d{2})_(\d{2})$/);
  if (!match) throw new Error(`bad paper: ${paper}`);
  const [, stem, variant] = match;
  const enrichDir = 'subjects/physics/9702/enrichment/p2';
  const files = fs.readdirSync(enrichDir)
    .filter(name => name.startsWith(`${paper}_q`) && name.endsWith('.enrichment.json'))
    .sort();
  for (const name of files) {
    const q = name.match(/_q(\d{2})/)[1];
    const ePath = path.join(enrichDir, name);
    const qPath = `subjects/physics/9702/papers/p2/questions/${stem}_qp_${variant}/question_${q}.json`;
    const enrichment = JSON.parse(fs.readFileSync(ePath, 'utf8'));
    const question = cleanText(JSON.parse(fs.readFileSync(qPath, 'utf8')));

    for (const part of question.parts || []) {
      for (const key of ['question_text', 'question_text_latex']) {
        if (!part[key]) continue;
        part[key] = part[key].replace(/\$([^$]{30,})\$/g, (whole, inner) => {
          const words = inner.split(/\s+/).filter(word => !word.startsWith('\\'));
          return words.length >= 4 && !inner.includes('\\text{') ? inner : whole;
        });
        if (/\b(?:of|the|and|between|with|in|to|from|a|an|is|that|for|or)\s*$/i.test(part[key])) part[key] += ':';
      }
      part.question_text_latex = part.question_text;
    }

    enrichment.numerical_values_checked = false;
    enrichment.question_patterns = uniq(enrichment.parts.flatMap(part => part.question_patterns || []));
    enrichment.mapping.topic_ids = uniq(enrichment.parts.map(part => part.mapping.primary_topic_id));
    enrichment.mapping.module_ids = uniq(enrichment.parts.map(part => part.mapping.primary_module_id));
    enrichment.mapping.outcome_ids = uniq(enrichment.parts.flatMap(part => part.mapping.outcome_ids || []));

    for (const part of enrichment.parts) {
      if (batchSkills[part.part_id]) part.skills.primary_skill_id = batchSkills[part.part_id];
      if (part.checking.mode === 'hybrid') part.checking.full_marks_if_all_deterministic_checks_pass = false;
      if (forceHybrid.has(part.part_id)) {
        part.checking.mode = 'hybrid';
        part.checking.full_marks_if_all_deterministic_checks_pass = false;
      }
      if (part.part_id === '9702_s16_23_q06_a') {
        part.checking.mode = 'ai';
        part.checking.deterministic_checks = [];
        part.checking.full_marks_if_all_deterministic_checks_pass = false;
      }
      if ((part.knowledge_refs.definition_ids || []).length && !part.question_patterns.includes('definition')) {
        part.question_patterns.push('definition');
      }
      part.mapping.outcome_ids = (part.mapping.outcome_ids || []).filter(id => id.startsWith(`${part.mapping.primary_module_id}_`));
      if (part.part_id === '9702_s16_22_q04_b') {
        part.knowledge_refs.formula_empty_justification = 'Uses proportional reasoning from the wave data stated in the question.';
      }
    }

    if (paper === '9702_m16_22') {
      for (const part of enrichment.parts) {
        if (m16Skills[part.part_id]) part.skills.primary_skill_id = m16Skills[part.part_id];
        if (part.checking.mode === 'hybrid') part.checking.full_marks_if_all_deterministic_checks_pass = false;
      }
      const byId = Object.fromEntries(enrichment.parts.map(part => [part.part_id, part]));
      for (const id of ['9702_m16_22_q01_b_i', '9702_m16_22_q01_b_ii', '9702_m16_22_q02_b_i', '9702_m16_22_q02_b_ii', '9702_m16_22_q04_b_ii']) {
        if (byId[id]) byId[id].knowledge_refs.formula_empty_justification = 'Uses a relationship supplied in the question or a direct definition stated in the walkthrough.';
      }
      if (byId['9702_m16_22_q05_b_i']) byId['9702_m16_22_q05_b_i'].mapping.outcome_ids = ['9702_t10_m01_o04'];
      if (byId['9702_m16_22_q05_b_iv']) {
        byId['9702_m16_22_q05_b_iv'].mapping.outcome_ids = ['9702_t09_m03_o06'];
        byId['9702_m16_22_q05_b_iv'].skills.supporting_skill_ids = ['9702_skill_electric_current_drift_speed'];
      }
      enrichment.question_patterns = uniq(enrichment.parts.flatMap(part => part.question_patterns || []));
      enrichment.mapping.topic_ids = uniq(enrichment.parts.map(part => part.mapping.primary_topic_id));
      enrichment.mapping.module_ids = uniq(enrichment.parts.map(part => part.mapping.primary_module_id));
      enrichment.mapping.outcome_ids = uniq(enrichment.parts.flatMap(part => part.mapping.outcome_ids || []));
    }

    enrichment.question_patterns = uniq(enrichment.parts.flatMap(part => part.question_patterns || []));
    enrichment.mapping.topic_ids = uniq(enrichment.parts.map(part => part.mapping.primary_topic_id));
    enrichment.mapping.module_ids = uniq(enrichment.parts.map(part => part.mapping.primary_module_id));
    enrichment.mapping.outcome_ids = uniq(enrichment.parts.flatMap(part => part.mapping.outcome_ids || []));

    for (const figure of question.figures || []) {
      const placement = figure.placement || {};
      if (!['part', 'question'].includes(placement.scope)) placement.scope = 'part';
      if (!['after_text', 'response_background', 'standalone'].includes(placement.position)) {
        placement.position = 'after_text';
      }
      if (placement.scope === 'part' && !placement.part_id) {
        placement.part_id = figure.introduced_by || figure.referenced_by?.[0];
      }
      if (!placement.anchor) placement.anchor = figure.label || figure.id;
      figure.placement = placement;
    }


    fs.writeFileSync(ePath, JSON.stringify(enrichment, null, 2) + '\n');
    fs.writeFileSync(qPath, JSON.stringify(question, null, 2) + '\n');
  }
}
