// Title-only preview fixture. Generated 2026-09-12 from the active authored maps below.
// The product UI intentionally does not display these developer-facing source paths.
// Two empty Physics course-module JSON files use their existing course-module directory names as title fallbacks:
// 9702_t07_cm05 Doppler effect for sound; 9702_t10_cm04 Potential dividers and sensing circuits.
export const curriculumFixtureProvenance = [
  'subjects/physics/9702/study/topics/*/{syllabus.json,lesson-knowledge-map.json,course-modules/*/module.json}',
  'subjects/biology/9700/study/topics/*/{syllabus.json,lesson-knowledge-map.json,module-lesson-structure.md}',
  'subjects/chemistry/9701/study/topics/*/{syllabus.json,lesson-knowledge-map.json,module-lesson-structure.md}',
] as const;

export type CurriculumLesson = { id: string; title: string };
export type CurriculumModule = { id: string; title: string; lessons: CurriculumLesson[] };
export type CurriculumTopic = { id: string; title: string; level: 'AS' | 'A2'; modules: CurriculumModule[] };
