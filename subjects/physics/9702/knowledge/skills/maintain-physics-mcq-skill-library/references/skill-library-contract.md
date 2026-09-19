# Physics MCQ skill-library contract

Registry header:

```text
skill_id,skill_name,skill_role,canonical_definition,first_topic_id,first_module_id,first_seen_paper,first_seen_question_id,status,library_version
```

- `skill_id`: stable `9702_mcq_skill_NNN` identifier; never reuse or renumber it.
- `skill_role`: `primary`, `supporting`, or `both`.
- `skill_name`: unique, human-readable canonical label.
- `canonical_definition`: subject-general description of the measurable action, not a single question’s wording.
- `first_topic_id` and `first_module_id`: provenance of first approved use, not a restriction on later reuse.
- `status`: `approved` or `deprecated`; never delete a released skill.
- `library_version`: semantic version of the registry release.

Proposal header:

```text
proposed_skill_name,proposed_role,topic_id,module_id,proposed_definition,source_paper,source_question_id,reason,review_status
```

Allowed review states: `pending`, `approved`, `rejected`.

Change-log header:

```text
change_id,library_version,change_type,skill_id,skill_name,source_paper,source_question_id,notes
```

Normalised duplicate names are forbidden. A spelling variation is not a new skill.

