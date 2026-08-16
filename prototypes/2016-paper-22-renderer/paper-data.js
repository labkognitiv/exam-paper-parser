window.PAPER_DATA = [
  {
    "schema_version": "1.1",
    "question_id": "9702_m16_22_q01",
    "source_filename": "9702_m16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "February/March",
    "session_code": "m",
    "variant": 22,
    "paper_code": "9702_m16_22",
    "metadata_confidence": 1.0,
    "question_num": 1,
    "source_pages": [
      5
    ],
    "total_marks": 6,
    "detected_part_marks": 6,
    "marks_validation_passed": true,
    "question_stem": "The speed v of a transverse wave on a uniform string is given by the expression\nv = √(Tl/m)\nwhere T is the tension in the string, l is its length and m is its mass.\nAn experiment is performed to determine the speed v of the wave. The measurements are shown\nin Fig. 1.1.",
    "question_stem_latex": "The speed v of a transverse wave on a uniform string is given by the expression\n$v = \\sqrt{\\frac{Tl}{m}}$\nwhere $T$ is the tension in the string, $l$ is its length and $m$ is its mass.\nAn experiment is performed to determine the speed $v$ of the wave. The measurements are shown\nin Fig. 1.1.",
    "content_flow": [
      {
        "type": "stem"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q01_a"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q01_b"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q01_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q01_b_ii"
      }
    ],
    "question_image": "question_01.png",
    "question_image_with_figures": "question_01_with_figures.png",
    "question_text_file": "question_01.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_1_1",
        "label": "Fig. 1.1",
        "file": "figure_1_1.png",
        "placement": {
          "scope": "question",
          "position": "after_stem"
        },
        "introduced_by": "9702_m16_22_q01_b_i",
        "referenced_by": [
          "9702_m16_22_q01_b_i",
          "9702_m16_22_q01_b_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_1_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_m16_22_q01_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State an appropriate instrument to measure the length l.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State an appropriate instrument to measure the length l.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q01_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q01_a_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "label": "Instrument",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q01_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q01_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_m16_22_q01_b",
        "display_order": 3,
        "question_text": "Use the data in Fig. 1.1 to calculate the speed v.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m s^-1",
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "Use the data in Fig. 1.1 to calculate the speed $v$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q01_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q01_b_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q01_b_i_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "v",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q01_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_m16_22_q01_b",
        "display_order": 4,
        "question_text": "Use your answer in (b)(i) and the data in Fig. 1.1 to determine the value of v, with its\nabsolute uncertainty, to an appropriate number of significant figures.",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m s^-1",
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "Use your answer in (b)(i) and the data in Fig. 1.1 to determine the value of $v$, with its\nabsolute uncertainty, to an appropriate number of significant figures.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q01_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q01_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q01_b_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q01_b_ii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "v",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q01_b_ii_field_03",
                  "control": "quantity",
                  "role": "uncertainty",
                  "label": "Absolute uncertainty in v",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "prototype_image": "../../output/physics/p2/questions/9702_m16_qp_22/question_01_with_figures.png",
    "prototype_paper": "9702_m16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_m16_ms_22.pdf",
      "paper_code": "9702_m16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "February/March",
      "session_code": "m",
      "variant": 22,
      "question_id": "9702_m16_22_q01",
      "question_num": 1,
      "total_marks": 6,
      "parts": [
        {
          "id": "9702_m16_22_q01_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q01_a_mp01",
              "text": "metre rule / tape measure",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q01_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q01_b_i_mp01",
              "text": "v = [(1.8 × 126 × 10^-2) / (5.1 × 10^-3)]^(1/2)",
              "text_latex": "$v = \\left[\\frac{1.8 \\times 126 \\times 10^{-2}}{5.1 \\times 10^{-3}}\\right]^{1/2}$",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q01_b_i_mp02",
              "text": "v = 21.1 m s^-1",
              "text_latex": "$v = 21.1\\,\\mathrm{m\\,s^{-1}}$",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q01_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_m16_22_q01_b_ii_mp01",
              "text": "percentage uncertainty = 4% or fractional uncertainty = 0.04",
              "text_latex": "$\\text{percentage uncertainty} = 4\\%$ or $\\text{fractional uncertainty} = 0.04$",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q01_b_ii_mp02",
              "text": "Δv = 0.04 × 21.1 = 0.84 m s^-1",
              "text_latex": "$\\Delta v = 0.04 \\times 21.1 = 0.84\\,\\mathrm{m\\,s^{-1}}$",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q01_b_ii_mp03",
              "text": "v = 21.1 ± 0.8 m s^-1",
              "text_latex": "$v = (21.1 \\pm 0.8)\\,\\mathrm{m\\,s^{-1}}$",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_m16_22_q02",
    "source_filename": "9702_m16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "February/March",
    "session_code": "m",
    "variant": 22,
    "paper_code": "9702_m16_22",
    "metadata_confidence": 1.0,
    "question_num": 2,
    "source_pages": [
      6,
      7
    ],
    "total_marks": 13,
    "detected_part_marks": 13,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_a"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_b"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_b_iv"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_c"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_c_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q02_d"
      }
    ],
    "question_image": "question_02.png",
    "question_image_with_figures": "question_02_with_figures.png",
    "question_text_file": "question_02.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_2_1",
        "label": "Fig. 2.1",
        "file": "figure_2_1.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q02_b",
          "position": "after_text",
          "anchor": "as shown in Fig. 2.1."
        },
        "introduced_by": "9702_m16_22_q02_b",
        "referenced_by": [
          "9702_m16_22_q02_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_2_1.png"
      },
      {
        "id": "fig_2_2",
        "label": "Fig. 2.2",
        "file": "figure_2_2.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q02_b_iv",
          "position": "response_background"
        },
        "introduced_by": "9702_m16_22_q02_b_iv",
        "referenced_by": [
          "9702_m16_22_q02_b_iv"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_2_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_m16_22_q02_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define acceleration.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define acceleration.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q02_a_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q02_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A ball is kicked from horizontal ground towards the top of a vertical wall, as shown in Fig. 2.1.\nThe horizontal distance between the initial position of the ball and the base of the wall is 24 m.\nThe ball is kicked with an initial velocity v at an angle of 28° to the horizontal. The ball hits the\ntop of the wall after a time of 1.5 s. Air resistance may be assumed to be negligible.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_2_1"
        ],
        "figure_references": [
          "Fig. 2.1"
        ],
        "question_text_latex": "A ball is kicked from horizontal ground towards the top of a vertical wall, as shown in Fig. 2.1.\nThe horizontal distance between the initial position of the ball and the base of the wall is 24 m.\nThe ball is kicked with an initial velocity v at an angle of 28° to the horizontal. The ball hits the\ntop of the wall after a time of 1.5 s. Air resistance may be assumed to be negligible.",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q02_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_m16_22_q02_b",
        "display_order": 3,
        "question_text": "Calculate the initial horizontal component vₓ of the velocity of the ball.",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m s⁻¹",
        "unit_latex": "\\mathrm{m\\,s^{-1}}",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the initial horizontal component $v_x$ of the velocity of the ball.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q02_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q02_b_i_field_01",
                  "control": "quantity",
                  "role": "value",
                  "label": "vₓ",
                  "label_latex": "v_x",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q02_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_m16_22_q02_b",
        "display_order": 4,
        "question_text": "Show that the initial vertical component vᵧ of the velocity of the ball is 8.5 m s⁻¹.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the initial vertical component $v_y$ of the velocity of the ball is $8.5\\,\\mathrm{m\\,s^{-1}}$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q02_b_i"
          },
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q02_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q02_b_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q02_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_m16_22_q02_b",
        "display_order": 5,
        "question_text": "Calculate the time taken for the ball to reach its maximum height above the ground.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the time taken for the ball to reach its maximum height above the ground.",
        "marks_source": "reconciled_from_printed_total",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q02_b_ii"
          },
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q02_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q02_b_iii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q02_b_iii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Time",
                  "unit": "s",
                  "unit_latex": "\\mathrm{s}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q02_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_m16_22_q02_b",
        "display_order": 6,
        "question_text": "The ball is kicked at time t = 0. On Fig. 2.2, sketch the variation with time t of the vertical\ncomponent vᵧ of the velocity of the ball until it hits the wall. It may be assumed that\nvelocity is positive when in the upwards direction.",
        "marks": 2,
        "answer_type": "graph",
        "answer_type_confidence": 0.95,
        "unit": null,
        "figure_ids": [
          "fig_2_2"
        ],
        "figure_references": [
          "Fig. 2.2"
        ],
        "question_text_latex": "The ball is kicked at time $t = 0$. On Fig. 2.2, sketch the variation with time $t$ of the vertical\ncomponent $v_y$ of the velocity of the ball until it hits the wall. It may be assumed that\nvelocity is positive when in the upwards direction.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q02_b_ii"
          },
          {
            "type": "figure",
            "id": "fig_2_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_b_iv_block_01",
              "type": "canvas",
              "mode": "draw_on_scaffold",
              "background_figure_id": "fig_2_2",
              "tools": [
                "line",
                "freehand",
                "eraser"
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q02_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 7,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q02_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_m16_22_q02_c",
        "display_order": 8,
        "question_text": "Use the information in (b) to determine the maximum height of the ball above the ground.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use the information in (b) to determine the maximum height of the ball above the ground.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "part_context",
            "part_id": "9702_m16_22_q02_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q02_c_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q02_c_i_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Maximum height",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q02_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_m16_22_q02_c",
        "display_order": 9,
        "question_text": "The maximum gravitational potential energy of the ball above the ground is 22 J. Calculate\nthe mass of the ball.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "kg",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The maximum gravitational potential energy of the ball above the ground is 22 J. Calculate\nthe mass of the ball.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q02_c_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q02_c_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q02_c_ii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Mass",
                  "unit": "kg",
                  "unit_latex": "\\mathrm{kg}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q02_d",
        "path": [
          "d"
        ],
        "label": "(d)",
        "parent_id": null,
        "display_order": 10,
        "question_text": "A ball of greater mass is kicked with the same velocity as the ball in (b).\nState and explain the effect, if any, of the increased mass on the maximum height reached by\nthe ball. Air resistance is still assumed to be negligible.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "A ball of greater mass is kicked with the same velocity as the ball in (b).\nState and explain the effect, if any, of the increased mass on the maximum height reached by\nthe ball. Air resistance is still assumed to be negligible.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "part_context",
            "part_id": "9702_m16_22_q02_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q02_d_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q02_d_field_01",
                  "control": "long_text",
                  "role": "explanation",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "prototype_image": "../../output/physics/p2/questions/9702_m16_qp_22/question_02_with_figures.png",
    "prototype_paper": "9702_m16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_m16_ms_22.pdf",
      "paper_code": "9702_m16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "February/March",
      "session_code": "m",
      "variant": 22,
      "question_id": "9702_m16_22_q02",
      "question_num": 2,
      "total_marks": 13,
      "parts": [
        {
          "id": "9702_m16_22_q02_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_a_mp01",
              "text": "change in velocity / time (taken) or rate of change of velocity",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q02_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_b_i_mp01",
              "text": "vX = (24 / 1.5) = 16 (m s–1)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q02_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_b_ii_mp01",
              "text": "tan 28° = vY / vX or vX = v cos 28° and vY = v sin 28°",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q02_b_ii_mp02",
              "text": "vY = 16 tan 28° or vY = 16 × (sin 28° / cos 28°) so vY = 8.5 (m s–1)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q02_b_iii",
          "label": "(b)(iii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_b_iii_mp01",
              "text": "v = u + at",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q02_b_iii_mp02",
              "text": "t = (0 – 8.5) / (–9.81) = 0.87 (s)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q02_b_iv",
          "label": "(b)(iv)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_b_iv_mp01",
              "text": "straight line from positive vY at t = 0 to negative vY at t =1.5 s",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q02_b_iv_mp02",
              "text": "line starts at (0, 8.5) and crosses t-axis at (0.87, 0) and does not go beyond t = 1.5 s.",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q02_c_i",
          "label": "(c)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_c_i_mp01",
              "text": "(v 2 = u 2 + 2as) 0 = 8.52 + 2(–9.81)s or (s = ut + ½at 2) s = 8.5×0.87 + ½ × (–9.81) × 0.872 or (s = vt – ½at 2) s = 0 – ½×(–9.81)×0.872 or (s = ½(u + v)t or area under graph) s = 0.5 × 8.5 × 0.87",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q02_c_i_mp02",
              "text": "s = 3.7 (m)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q02_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_c_ii_mp01",
              "text": "∆EP = mg∆h (allow E = mgh)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q02_c_ii_mp02",
              "text": "m = 22 / (9.81 × 3.7) = 0.61 (kg)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q02_d",
          "label": "(d)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q02_d_mp01",
              "text": "acceleration of free fall is unchanged / independent of mass, so there is no effect on maximum height; or: initial kinetic energy ∝ mass, ΔKE = ΔPE, maximum PE ∝ mass, so there is no effect on maximum height",
              "text_latex": "$g$ is independent of mass, so the maximum height is unchanged; or: initial $E_{\\mathrm{K}} \\propto m$, $\\Delta E_{\\mathrm{K}} = \\Delta E_{\\mathrm{P}}$, and maximum $E_{\\mathrm{P}} \\propto m$",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_m16_22_q03",
    "source_filename": "9702_m16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "February/March",
    "session_code": "m",
    "variant": 22,
    "paper_code": "9702_m16_22",
    "metadata_confidence": 1.0,
    "question_num": 3,
    "source_pages": [
      8,
      9,
      10
    ],
    "total_marks": 12,
    "detected_part_marks": 12,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_a"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_b"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_b_iv"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q03_c"
      }
    ],
    "question_image": "question_03.png",
    "question_image_with_figures": "question_03_with_figures.png",
    "question_text_file": "question_03.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_3_1",
        "label": "Fig. 3.1",
        "file": "figure_3_1.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q03_b",
          "position": "after_text",
          "anchor": "as shown in Fig. 3.1."
        },
        "introduced_by": "9702_m16_22_q03_b",
        "referenced_by": [
          "9702_m16_22_q03_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_3_1.png"
      },
      {
        "id": "fig_3_2",
        "label": "Fig. 3.2",
        "file": "figure_3_2.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q03_b_ii",
          "position": "after_text",
          "anchor": "shown in Fig. 3.2."
        },
        "introduced_by": "9702_m16_22_q03_b_ii",
        "referenced_by": [
          "9702_m16_22_q03_b_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_3_2.png"
      },
      {
        "id": "fig_3_3",
        "label": "Fig. 3.3",
        "file": "figure_3_3.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q03_c",
          "position": "response_background"
        },
        "introduced_by": "9702_m16_22_q03_c",
        "referenced_by": [
          "9702_m16_22_q03_c"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_3_3.png"
      }
    ],
    "parts": [
      {
        "id": "9702_m16_22_q03_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State what is meant by",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q03_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_m16_22_q03_a",
        "display_order": 2,
        "question_text": "work done,",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "work done,",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q03_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q03_a_i_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q03_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_m16_22_q03_a",
        "display_order": 3,
        "question_text": "elastic potential energy.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "elastic potential energy.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q03_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q03_a_ii_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q03_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "A block of mass 0.40 kg slides in a straight line with a constant speed of 0.30 m s⁻¹ along a\nhorizontal surface, as shown in Fig. 3.1.\nThe block hits a spring and decelerates. The speed of the block becomes zero when the\nspring is compressed by 8.0 cm.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_3_1"
        ],
        "figure_references": [
          "Fig. 3.1"
        ],
        "question_text_latex": "A block of mass $0.40\\,\\mathrm{kg}$ slides in a straight line with a constant speed of $0.30\\,\\mathrm{m\\,s^{-1}}$ along a\nhorizontal surface, as shown in Fig. 3.1.\nThe block hits a spring and decelerates. The speed of the block becomes zero when the\nspring is compressed by $8.0\\,\\mathrm{cm}$.",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q03_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_m16_22_q03_b",
        "display_order": 5,
        "question_text": "Calculate the initial kinetic energy of the block.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "J",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the initial kinetic energy of the block.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q03_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q03_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q03_b_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q03_b_i_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Kinetic energy",
                  "unit": "J",
                  "unit_latex": "\\mathrm{J}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q03_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_m16_22_q03_b",
        "display_order": 6,
        "question_text": "The variation of the compression x of the spring with the force F applied to the spring is\nshown in Fig. 3.2.\nUse your answer in (b)(i) to determine the maximum force Fₘₐₓ exerted on the spring by\nthe block.\nExplain your working.",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [
          "fig_3_2"
        ],
        "figure_references": [
          "Fig. 3.2"
        ],
        "question_text_latex": "The variation of the compression $x$ of the spring with the force $F$ applied to the spring is\nshown in Fig. 3.2.\nUse your answer in (b)(i) to determine the maximum force $F_{\\mathrm{MAX}}$ exerted on the spring by\nthe block.\nExplain your working.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q03_b_i"
          },
          {
            "type": "figure",
            "id": "fig_3_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q03_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q03_b_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q03_b_ii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Fₘₐₓ",
                  "label_latex": "F_{\\max}",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q03_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_m16_22_q03_b",
        "display_order": 7,
        "question_text": "Calculate the maximum deceleration of the block.",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m s^-2",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the maximum deceleration of the block.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q03_b_ii"
          },
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q03_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q03_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q03_b_iii_field_01",
                  "control": "quantity",
                  "role": "value",
                  "label": "Maximum deceleration",
                  "unit": "m s⁻²",
                  "unit_latex": "\\mathrm{m\\,s^{-2}}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q03_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_m16_22_q03_b",
        "display_order": 8,
        "question_text": "State and explain whether the block is in equilibrium\n1.\nbefore it hits the spring,\n2.\nwhen its speed becomes zero.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State and explain whether the block is in equilibrium\n1.\nbefore it hits the spring,\n2.\nwhen its speed becomes zero.",
        "marks_source": "reconciled_from_printed_total",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q03_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q03_b_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q03_b_iv_field_01",
                  "control": "short_text",
                  "role": "explanation",
                  "label": "Before hitting the spring",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q03_b_iv_field_02",
                  "control": "short_text",
                  "role": "explanation",
                  "label": "When its speed becomes zero",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q03_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 9,
        "question_text": "The energy E stored in a spring is given by\nE = ½kx²\nwhere k is the spring constant of the spring and x is its compression.\nThe mass m of the block in (b) is now varied. The initial speed of the block remains constant\nand the spring continues to obey Hooke’s law.\nOn Fig. 3.3, sketch the variation of the maximum compression x₀ of the spring with mass m.",
        "marks": 2,
        "answer_type": "graph",
        "answer_type_confidence": 0.95,
        "unit": null,
        "figure_ids": [
          "fig_3_3"
        ],
        "figure_references": [
          "Fig. 3.3"
        ],
        "question_text_latex": "The energy $E$ stored in a spring is given by\n$E = \\frac{1}{2}kx^2$\nwhere $k$ is the spring constant of the spring and $x$ is its compression.\nThe mass $m$ of the block in (b) is now varied. The initial speed of the block remains constant\nand the spring continues to obey Hooke’s law.\nOn Fig. 3.3, sketch the variation of the maximum compression $x_0$ of the spring with mass $m$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_3"
          },
          {
            "type": "part_context",
            "part_id": "9702_m16_22_q03_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q03_c_block_01",
              "type": "canvas",
              "mode": "draw_on_scaffold",
              "background_figure_id": "fig_3_3",
              "tools": [
                "curve",
                "freehand",
                "eraser"
              ]
            }
          ]
        }
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "prototype_image": "../../output/physics/p2/questions/9702_m16_qp_22/question_03_with_figures.png",
    "prototype_paper": "9702_m16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_m16_ms_22.pdf",
      "paper_code": "9702_m16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "February/March",
      "session_code": "m",
      "variant": 22,
      "question_id": "9702_m16_22_q03",
      "question_num": 3,
      "total_marks": 12,
      "parts": [
        {
          "id": "9702_m16_22_q03_a_i",
          "label": "(a)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q03_a_i_mp01",
              "text": "(work = ) force × distance moved in the direction of the force.",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q03_a_ii",
          "label": "(a)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q03_a_ii_mp01",
              "text": "the energy stored (in an object) due to extension / compression / change of shape",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q03_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q03_b_i_mp01",
              "text": "E_K = ½mv^2",
              "text_latex": "$E_{\\mathrm{K}} = \\frac{1}{2}mv^2$",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q03_b_i_mp02",
              "text": "= 0.5 × 0.40 × 0.30^2 = 1.8 × 10^-2 J",
              "text_latex": "$= 0.5 \\times 0.40 \\times 0.30^2 = 1.8 \\times 10^{-2}\\,\\mathrm{J}$",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q03_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_m16_22_q03_b_ii_mp01",
              "text": "(change in) kinetic energy = work done on spring / (change in) elastic potential energy",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q03_b_ii_mp02",
              "text": "1.8 × 10–2 = ½ × F × 0.080",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q03_b_ii_mp03",
              "text": "FMAX = 0.45 (N)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q03_b_iii",
          "label": "(b)(iii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q03_b_iii_mp01",
              "text": "a = F / m = 0.45 / 0.40 = 1.1 (m s–2)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q03_b_iv",
          "label": "(b)(iv)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q03_b_iv_mp01",
              "text": "1. constant velocity / resultant force is zero, so in equilibrium",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q03_b_iv_mp02",
              "text": "2. decelerating / resultant force is not zero, so not in equilibrium",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q03_c",
          "label": "(c)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q03_c_mp01",
              "text": "curved line from the origin",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q03_c_mp02",
              "text": "with decreasing gradient",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_m16_22_q04",
    "source_filename": "9702_m16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "February/March",
    "session_code": "m",
    "variant": 22,
    "paper_code": "9702_m16_22",
    "metadata_confidence": 1.0,
    "question_num": 4,
    "source_pages": [
      12,
      13
    ],
    "total_marks": 11,
    "detected_part_marks": 11,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_a"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_b"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_c"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q04_c_ii"
      }
    ],
    "question_image": "question_04.png",
    "question_image_with_figures": "question_04_with_figures.png",
    "question_text_file": "question_04.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_4_1",
        "label": "Fig. 4.1",
        "file": "figure_4_1.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q04_b",
          "position": "after_text",
          "anchor": "Fig. 4.1."
        },
        "introduced_by": "9702_m16_22_q04_b",
        "referenced_by": [
          "9702_m16_22_q04_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_4_1.png"
      },
      {
        "id": "fig_4_2",
        "label": "Fig. 4.2",
        "file": "figure_4_2.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q04_c",
          "position": "after_text",
          "anchor": "shown in Fig. 4.2."
        },
        "introduced_by": "9702_m16_22_q04_c",
        "referenced_by": [
          "9702_m16_22_q04_c"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_4_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_m16_22_q04_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q04_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_m16_22_q04_a",
        "display_order": 2,
        "question_text": "By reference to the direction of propagation of energy, state what is meant by a transverse\nwave.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "By reference to the direction of propagation of energy, state what is meant by a transverse\nwave.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q04_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q04_a_i_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q04_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_m16_22_q04_a",
        "display_order": 3,
        "question_text": "State the principle of superposition.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the principle of superposition.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q04_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q04_a_ii_field_01",
                  "control": "long_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q04_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "Circular water waves may be produced by vibrating dippers at points P and Q, as illustrated in\nFig. 4.1.\nThe waves from P alone have the same amplitude at point R as the waves from Q alone.\nDistance PR is 44 cm and distance QR is 29 cm.\nThe dippers vibrate in phase with a period of 1.5 s to produce waves of speed 4.0 cm s⁻¹.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_4_1"
        ],
        "figure_references": [
          "Fig. 4.1"
        ],
        "question_text_latex": "Circular water waves may be produced by vibrating dippers at points P and Q, as illustrated in\nFig. 4.1.\nThe waves from P alone have the same amplitude at point R as the waves from Q alone.\nDistance PR is $44\\,\\mathrm{cm}$ and distance QR is $29\\,\\mathrm{cm}$.\nThe dippers vibrate in phase with a period of $1.5\\,\\mathrm{s}$ to produce waves of speed $4.0\\,\\mathrm{cm\\,s^{-1}}$.",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q04_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_m16_22_q04_b",
        "display_order": 5,
        "question_text": "Determine the wavelength of the waves.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "cm",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the wavelength of the waves.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q04_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q04_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q04_b_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q04_b_i_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Wavelength",
                  "unit": "cm",
                  "unit_latex": "\\mathrm{cm}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q04_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_m16_22_q04_b",
        "display_order": 6,
        "question_text": "By reference to the distances PR and QR, explain why the water particles are at rest at\npoint R.",
        "marks": 3,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "By reference to the distances PR and QR, explain why the water particles are at rest at\npoint R.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q04_b_i"
          },
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q04_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q04_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q04_b_ii_field_01",
                  "control": "long_text",
                  "role": "explanation",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q04_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 7,
        "question_text": "A wave is produced on the surface of a different liquid. At one particular time, the variation of\nthe vertical displacement y with distance x along the surface of the liquid is shown in Fig. 4.2.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_4_2"
        ],
        "figure_references": [
          "Fig. 4.2"
        ],
        "question_text_latex": "A wave is produced on the surface of a different liquid. At one particular time, the variation of\nthe vertical displacement y with distance x along the surface of the liquid is shown in Fig. 4.2.",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q04_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_m16_22_q04_c",
        "display_order": 8,
        "question_text": "The wave has intensity I₁ at distance x = 2.0 cm and intensity I₂ at x = 10.0 cm.\nDetermine the ratio I₂/I₁.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The wave has intensity $I_1$ at distance $x = 2.0\\,\\mathrm{cm}$ and intensity $I_2$ at $x = 10.0\\,\\mathrm{cm}$.\nDetermine the ratio $I_2/I_1$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q04_c"
          },
          {
            "type": "figure",
            "id": "fig_4_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q04_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q04_c_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q04_c_i_field_02",
                  "control": "number",
                  "role": "value",
                  "label": "I₂/I₁",
                  "label_latex": "I_2/I_1",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q04_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_m16_22_q04_c",
        "display_order": 9,
        "question_text": "State the phase difference, with its unit, between the oscillations of the liquid particles at\ndistances x = 3.0 cm and x = 4.0 cm.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the phase difference, with its unit, between the oscillations of the liquid particles at\ndistances $x = 3.0\\,\\mathrm{cm}$ and $x = 4.0\\,\\mathrm{cm}$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q04_c"
          },
          {
            "type": "figure",
            "id": "fig_4_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q04_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q04_c_ii_field_01",
                  "control": "number",
                  "role": "value",
                  "label": "Phase difference",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q04_c_ii_field_02",
                  "control": "short_text",
                  "role": "unit",
                  "label": "Unit",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "prototype_image": "../../output/physics/p2/questions/9702_m16_qp_22/question_04_with_figures.png",
    "prototype_paper": "9702_m16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_m16_ms_22.pdf",
      "paper_code": "9702_m16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "February/March",
      "session_code": "m",
      "variant": 22,
      "question_id": "9702_m16_22_q04",
      "question_num": 4,
      "total_marks": 11,
      "parts": [
        {
          "id": "9702_m16_22_q04_a_i",
          "label": "(a)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q04_a_i_mp01",
              "text": "Displacement of particles perpendicular to direction of energy propagation",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q04_a_ii",
          "label": "(a)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q04_a_ii_mp01",
              "text": "waves meet / overlap (at a point)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q04_a_ii_mp02",
              "text": "resultant displacement is the sum of the individual displacements",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q04_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q04_b_i_mp01",
              "text": "λ = vT or λ = v / f and f = 1 / T",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q04_b_i_mp02",
              "text": "λ = 4.0 × 1.5 λ = 6.0 (cm)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q04_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_m16_22_q04_b_ii_mp01",
              "text": "path difference [= (44 cm – 29 cm) / 6 cm] = 2.5λ",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q04_b_ii_mp02",
              "text": "either waves have path difference = (n + ½)λ or waves have phase difference = 180°",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q04_b_ii_mp03",
              "text": "so destructive interference",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q04_c_i",
          "label": "(c)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q04_c_i_mp01",
              "text": "intensity ∝ (amplitude)2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q04_c_i_mp02",
              "text": "ratio = (0.602 / 0.902) = 0.44",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q04_c_ii",
          "label": "(c)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q04_c_ii_mp01",
              "text": "phase difference = 90°",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_m16_22_q05",
    "source_filename": "9702_m16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "February/March",
    "session_code": "m",
    "variant": 22,
    "paper_code": "9702_m16_22",
    "metadata_confidence": 1.0,
    "question_num": 5,
    "source_pages": [
      14,
      15
    ],
    "total_marks": 12,
    "detected_part_marks": 12,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_a"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_b"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q05_b_iv"
      }
    ],
    "question_image": "question_05.png",
    "question_image_with_figures": "question_05_with_figures.png",
    "question_text_file": "question_05.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_5_1",
        "label": "Fig. 5.1",
        "file": "figure_5_1.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q05_b",
          "position": "after_text",
          "anchor": "as shown in Fig. 5.1."
        },
        "introduced_by": "9702_m16_22_q05_b",
        "referenced_by": [
          "9702_m16_22_q05_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_5_1.png"
      },
      {
        "id": "fig_5_2",
        "label": "Fig. 5.2",
        "file": "figure_5_2.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m16_22_q05_b",
          "position": "after_text",
          "anchor": "Fig. 5.2."
        },
        "introduced_by": "9702_m16_22_q05_b",
        "referenced_by": [
          "9702_m16_22_q05_b",
          "9702_m16_22_q05_b_ii"
        ],
        "mapping_method": "ai_repair_from_complete_question_image",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m16_qp_22/figure_5_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_m16_22_q05_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q05_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_m16_22_q05_a",
        "display_order": 2,
        "question_text": "State what is meant by an electric current.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by an electric current.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q05_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q05_a_i_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q05_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_m16_22_q05_a",
        "display_order": 3,
        "question_text": "Define electric potential difference (p.d.).",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define electric potential difference (p.d.).",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q05_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q05_a_ii_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q05_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "A power supply of electromotive force (e.m.f.) 8.7 V and negligible internal resistance is\nconnected by two identical wires to three filament lamps, as shown in Fig. 5.1.\nThe power supply provides a current of 0.30 A to the circuit.\nThe filament lamps are identical. The I–V characteristic for one of the lamps is shown in\nFig. 5.2.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_5_1",
          "fig_5_2"
        ],
        "figure_references": [
          "Fig. 5.1",
          "Fig. 5.2"
        ],
        "question_text_latex": "A power supply of electromotive force (e.m.f.) 8.7 V and negligible internal resistance is\nconnected by two identical wires to three filament lamps, as shown in Fig. 5.1.\nThe power supply provides a current of 0.30 A to the circuit.\nThe filament lamps are identical. The I–V characteristic for one of the lamps is shown in\nFig. 5.2.",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q05_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_m16_22_q05_b",
        "display_order": 5,
        "question_text": "Show that the resistance of each connecting wire is 2.0 Ω.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the resistance of each connecting wire is 2.0 $\\Omega$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q05_b"
          },
          {
            "type": "figure",
            "id": "fig_5_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q05_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q05_b_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q05_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_m16_22_q05_b",
        "display_order": 6,
        "question_text": "The resistivity of the metal of the connecting wires does not vary with temperature.\nOn Fig. 5.2, sketch the I–V characteristic for one of the connecting wires.",
        "marks": 2,
        "answer_type": "drawing",
        "answer_type_confidence": 0.95,
        "unit": null,
        "figure_ids": [
          "fig_5_2"
        ],
        "figure_references": [
          "Fig. 5.2"
        ],
        "question_text_latex": "The resistivity of the metal of the connecting wires does not vary with temperature.\nOn Fig. 5.2, sketch the I–V characteristic for one of the connecting wires.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q05_b_ii_block_01",
              "type": "canvas",
              "mode": "draw_on_scaffold",
              "background_figure_id": "fig_5_2",
              "tools": [
                "line",
                "freehand",
                "eraser"
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q05_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_m16_22_q05_b",
        "display_order": 7,
        "question_text": "Calculate the power loss in one of the connecting wires.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "W",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the power loss in one of the connecting wires.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q05_b_i"
          },
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q05_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q05_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q05_b_iii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q05_b_iii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Power loss",
                  "unit": "W",
                  "unit_latex": "\\mathrm{W}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q05_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_m16_22_q05_b",
        "display_order": 8,
        "question_text": "Some data for the connecting wires are given below.\ncross-sectional area = 0.40 mm²\nresistivity = 1.7 × 10⁻⁸ Ω m\nnumber density of free electrons = 8.5 × 10²⁸ m⁻³\nCalculate\n1. the length of one of the connecting wires,\n2. the drift speed of a free electron in the connecting wires.",
        "marks": 4,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Some data for the connecting wires are given below.\n$\\text{cross-sectional area} = 0.40\\,\\mathrm{mm^2}$\n$\\text{resistivity} = 1.7 \\times 10^{-8}\\,\\Omega\\,\\mathrm{m}$\n$\\text{number density of free electrons} = 8.5 \\times 10^{28}\\,\\mathrm{m^{-3}}$\nCalculate\n1. the length of one of the connecting wires,\n2. the drift speed of a free electron in the connecting wires.",
        "marks_source": "reconciled_from_printed_subpart_marks",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_m16_22_q05_b_i"
          },
          {
            "type": "question_context",
            "part_id": "9702_m16_22_q05_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q05_b_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q05_b_iv_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working for length",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q05_b_iv_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Length",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q05_b_iv_field_03",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working for drift speed",
                  "required": true
                },
                {
                  "field_id": "9702_m16_22_q05_b_iv_field_04",
                  "control": "quantity",
                  "role": "value",
                  "label": "Drift speed",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "prototype_image": "../../output/physics/p2/questions/9702_m16_qp_22/question_05_with_figures.png",
    "prototype_paper": "9702_m16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_m16_ms_22.pdf",
      "paper_code": "9702_m16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "February/March",
      "session_code": "m",
      "variant": 22,
      "question_id": "9702_m16_22_q05",
      "question_num": 5,
      "total_marks": 12,
      "parts": [
        {
          "id": "9702_m16_22_q05_a_i",
          "label": "(a)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q05_a_i_mp01",
              "text": "movement / flow of charge carriers",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q05_a_ii",
          "label": "(a)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q05_a_ii_mp01",
              "text": "work done or energy transformed per unit charge",
              "text_latex": "$\\text{potential difference} = \\frac{\\text{work done or energy transformed}}{\\text{charge}}$",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q05_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q05_b_i_mp01",
              "text": "p.d. across one lamp = 2.5 V",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q05_b_i_mp02",
              "text": "resistance = [(8.7 – 7.5) / 0.3] / 2 = 2.0 (Ω)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q05_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q05_b_ii_mp01",
              "text": "straight line through the origin",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q05_b_ii_mp02",
              "text": "with gradient of 0.5",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q05_b_iii",
          "label": "(b)(iii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q05_b_iii_mp01",
              "text": "P = I^2R or P = VI with V = IR or P = V^2/R with V = IR",
              "text_latex": "$P = I^2R$ or $P = VI$ with $V = IR$ or $P = V^2/R$ with $V = IR$",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q05_b_iii_mp02",
              "text": "= 0.30^2 × 2.0 = 0.60 × 0.30 = 0.60^2 / 2.0 = 0.18 W",
              "text_latex": "$= 0.30^2 \\times 2.0 = 0.60 \\times 0.30 = 0.60^2/2.0 = 0.18\\,\\mathrm{W}$",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q05_b_iv",
          "label": "(b)(iv)",
          "marks": 4,
          "marking_points": [
            {
              "id": "9702_m16_22_q05_b_iv_mp01",
              "text": "1 R = ρl / A",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q05_b_iv_mp02",
              "text": "l = (2.0 × 0.40 × 10–6) / 1.7 × 10–8 = 47 (m)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q05_b_iv_mp03",
              "text": "2 I = Anvq v = 0.30 / (0.40 × 10–6 × 8.5 × 1028 × 1.6 × 10–19)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q05_b_iv_mp04",
              "text": "= 5.5 × 10–5 (m s–1)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_m16_22_q06",
    "source_filename": "9702_m16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "February/March",
    "session_code": "m",
    "variant": 22,
    "paper_code": "9702_m16_22",
    "metadata_confidence": 1.0,
    "question_num": 6,
    "source_pages": [
      16
    ],
    "total_marks": 6,
    "detected_part_marks": 6,
    "marks_validation_passed": true,
    "question_stem": "A neutron decays by emitting a β⁻ particle.",
    "question_stem_latex": "A neutron decays by emitting a $\\beta^-$ particle.",
    "content_flow": [
      {
        "type": "stem"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q06_a"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q06_b"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q06_c"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q06_d"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q06_d_i"
      },
      {
        "type": "part",
        "part_id": "9702_m16_22_q06_d_ii"
      }
    ],
    "question_image": "question_06.png",
    "question_image_with_figures": null,
    "question_text_file": "question_06.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_m16_22_q06_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Complete the equation below for this decay.\n¹₀n →",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Complete the equation below for this decay.\n${}^{1}_{0}\\mathrm{n} \\rightarrow$",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q06_a_block_01",
              "type": "fields",
              "segments": [
                {
                  "type": "static_latex",
                  "value": "{}^{1}_{0}\\mathrm{n} \\rightarrow"
                },
                {
                  "type": "field_ref",
                  "field_id": "9702_m16_22_q06_a_field_01"
                }
              ],
              "fields": [
                {
                  "field_id": "9702_m16_22_q06_a_field_01",
                  "control": "math_expression",
                  "role": "equation",
                  "label": "Complete right-hand side",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q06_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "State the name of the particle represented by the symbol ν̄.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the name of the particle represented by the symbol $\\bar{\\nu}$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q06_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q06_b_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q06_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "State the name of the class (group) of particles that includes β⁻ and ν̄.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the name of the class (group) of particles that includes $\\beta^-$ and $\\bar{\\nu}$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q06_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q06_c_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q06_d",
        "path": [
          "d"
        ],
        "label": "(d)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "State",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State",
        "marks_source": null
      },
      {
        "id": "9702_m16_22_q06_d_i",
        "path": [
          "d",
          "i"
        ],
        "label": "(d)(i)",
        "parent_id": "9702_m16_22_q06_d",
        "display_order": 5,
        "question_text": "the quark structure of the neutron,",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the quark structure of the neutron,",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q06_d_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q06_d_i_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m16_22_q06_d_ii",
        "path": [
          "d",
          "ii"
        ],
        "label": "(d)(ii)",
        "parent_id": "9702_m16_22_q06_d",
        "display_order": 6,
        "question_text": "the change to the quark structure when the neutron decays.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the change to the quark structure when the neutron decays.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m16_22_q06_d_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m16_22_q06_d_ii_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "prototype_image": "../../output/physics/p2/questions/9702_m16_qp_22/question_06.png",
    "prototype_paper": "9702_m16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_m16_ms_22.pdf",
      "paper_code": "9702_m16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "February/March",
      "session_code": "m",
      "variant": 22,
      "question_id": "9702_m16_22_q06",
      "question_num": 6,
      "total_marks": 6,
      "parts": [
        {
          "id": "9702_m16_22_q06_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m16_22_q06_a_mp01",
              "text": "proton: ^1_1 p",
              "text_latex": "${}^{1}_{1}\\mathrm{p}$",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m16_22_q06_a_mp02",
              "text": "beta particle and electron antineutrino: ^0_-1 β^- + ^0_0 ν̄",
              "text_latex": "${}^{0}_{-1}\\beta^- + {}^{0}_{0}\\bar{\\nu}$",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q06_b",
          "label": "(b)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q06_b_mp01",
              "text": "an (electron) antineutrino",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q06_c",
          "label": "(c)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q06_c_mp01",
              "text": "lepton(s)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q06_d_i",
          "label": "(d)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q06_d_i_mp01",
              "text": "down, down, up / ddu",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m16_22_q06_d_ii",
          "label": "(d)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m16_22_q06_d_ii_mp01",
              "text": "a down / d (quark) changes to an up / u (quark) or ddu → uud",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_s16_21_q01",
    "source_filename": "9702_s16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 21,
    "paper_code": "9702_s16_21",
    "metadata_confidence": 1.0,
    "question_num": 1,
    "source_pages": [
      4
    ],
    "total_marks": 7,
    "detected_part_marks": 7,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_01.png",
    "question_image_with_figures": "question_01_with_figures.png",
    "question_text_file": "question_01.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_1_1",
        "label": "Fig. 1.1",
        "file": "figure_1_1.png",
        "introduced_by": "9702_s16_21_q01_b",
        "referenced_by": [
          "9702_s16_21_q01_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_21_q01_b",
          "position": "after_text",
          "anchor": "as shown in Fig. 1.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_1_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_21_q01_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Make estimates of",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Make estimates of",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q01_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_s16_21_q01_a",
        "display_order": 2,
        "question_text": "the mass, in kg, of a wooden metre rule,",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": "kg",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the mass, in $\\mathrm{kg}$, of a wooden metre rule,",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q01_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q01_a_i_field_01",
                  "control": "quantity",
                  "role": "value",
                  "label": "Mass",
                  "unit": "kg",
                  "unit_latex": "\\mathrm{kg}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q01_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_s16_21_q01_a",
        "display_order": 3,
        "question_text": "the volume, in cm³, of a cricket ball or a tennis ball.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the volume, in $\\mathrm{cm^3}$, of a cricket ball or a tennis ball.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q01_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q01_a_ii_field_01",
                  "control": "quantity",
                  "role": "value",
                  "label": "Volume",
                  "unit": "cm³",
                  "unit_latex": "\\mathrm{cm^3}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q01_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "A metal wire of length L has a circular cross-section of diameter d, as shown in Fig. 1.1.\nThe volume V of the wire is given by the expression\nV = πd²L/4.\nThe diameter, length and mass M are measured to determine the density of the metal of the\nwire. The measured values are:\nd = 0.38 ± 0.01 mm,\nL = 25.0 ± 0.1 cm,\nM = 0.225 ± 0.001 g.\nCalculate the density of the metal, with its absolute uncertainty. Give your answer to an\nappropriate number of significant figures.",
        "marks": 5,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "A metal wire of length $L$ has a circular cross-section of diameter $d$, as shown in Fig. 1.1.\nThe volume $V$ of the wire is given by the expression\n$V = \\frac{\\pi d^2L}{4}$.\nThe diameter, length and mass $M$ are measured to determine the density of the metal of the\nwire. The measured values are:\n$d = (0.38 \\pm 0.01)\\,\\mathrm{mm}$,\n$L = (25.0 \\pm 0.1)\\,\\mathrm{cm}$,\n$M = (0.225 \\pm 0.001)\\,\\mathrm{g}$.\nCalculate the density of the metal, with its absolute uncertainty. Give your answer to an\nappropriate number of significant figures.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q01_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q01_b_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q01_b_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Density",
                  "unit": "kg m⁻³",
                  "unit_latex": "\\mathrm{kg\\,m^{-3}}",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q01_b_field_03",
                  "control": "quantity",
                  "role": "uncertainty",
                  "label": "Absolute uncertainty",
                  "unit": "kg m⁻³",
                  "unit_latex": "\\mathrm{kg\\,m^{-3}}",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_21_q01_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q01_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q01_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q01_b"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_21/question_01_with_figures.png",
    "prototype_paper": "9702_s16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_21.pdf",
      "paper_code": "9702_s16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 21,
      "question_id": "9702_s16_21_q01",
      "question_num": 1,
      "total_marks": 7,
      "parts": [
        {
          "id": "9702_s16_21_q01_a_i",
          "label": "(a)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q01_a_i_mp01",
              "text": "(50 to 200) × 10–3 kg or (0.05 to 0.2) kg",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q01_a_ii",
          "label": "(a)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q01_a_ii_mp01",
              "text": "(50 to 300) cm3",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q01_b",
          "label": "(b)",
          "marks": 5,
          "marking_points": [
            {
              "id": "9702_s16_21_q01_b_mp01",
              "text": "density = mass / volume or ρ = M / V",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q01_b_mp02",
              "text": "V = [π(0.38 × 10–3)2 × 25.0 × 10–2] / 4 (= 2.835 × 10–8 m3)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q01_b_mp03",
              "text": "ρ = (0.225 × 10–3) / 2.835 × 10–8 = 7940 (kg m–3)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q01_b_mp04",
              "text": "∆ρ / ρ = 2(0.01/0.38) + (0.1/25.0) + (0.001/0.225) [= 0.061] or %ρ = 5.3% + 0.40% + 0.44% (= 6.1%)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q01_b_mp05",
              "text": "∆ρ = 0.061 × 7940 = 480 (kg m–3) density = (7.9 ± 0.5) × 103 kg m–3 or (7900 ± 500) kg m–3",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_s16_21_q02",
    "source_filename": "9702_s16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 21,
    "paper_code": "9702_s16_21",
    "metadata_confidence": 1.0,
    "question_num": 2,
    "source_pages": [
      5
    ],
    "total_marks": 8,
    "detected_part_marks": 8,
    "marks_validation_passed": true,
    "question_stem": "A ball is thrown from a point P with an initial velocity u of 12 m s⁻¹ at 50° to the horizontal, as\nillustrated in Fig. 2.1.\nThe ball reaches maximum height at Q.\nAir resistance is negligible.",
    "question_stem_latex": "A ball is thrown from a point P with an initial velocity $u$ of $12\\,\\mathrm{m\\,s^{-1}}$ at $50^\\circ$ to the horizontal, as\nillustrated in Fig. 2.1.\nThe ball reaches maximum height at Q.\nAir resistance is negligible.",
    "question_image": "question_02.png",
    "question_image_with_figures": "question_02_with_figures.png",
    "question_text_file": "question_02.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_2_1",
        "label": "Fig. 2.1",
        "file": "figure_2_1.png",
        "introduced_by": null,
        "referenced_by": [],
        "mapping_method": "caption_proximity",
        "mapping_confidence": 0.6,
        "placement": {
          "scope": "question",
          "position": "after_stem_text",
          "anchor": "illustrated in Fig. 2.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_2_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_21_q02_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Calculate",
        "marks": null,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q02_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_s16_21_q02_a",
        "display_order": 2,
        "question_text": "the horizontal component of u,",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the horizontal component of $u$,",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q02_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q02_a_i_field_01",
                  "control": "quantity",
                  "role": "value",
                  "label": "Horizontal component",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q02_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_s16_21_q02_a",
        "display_order": 3,
        "question_text": "the vertical component of u.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the vertical component of $u$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q02_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q02_a_ii_field_01",
                  "control": "quantity",
                  "role": "value",
                  "label": "Vertical component",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q02_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "Show that the maximum height reached by the ball is 4.3 m.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the maximum height reached by the ball is $4.3\\,\\mathrm{m}$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q02_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q02_b_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q02_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "Determine the magnitude of the displacement PQ.",
        "marks": 4,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the magnitude of the displacement PQ.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q02_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q02_c_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q02_c_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Displacement",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [
      "figure_without_explicit_part_reference"
    ],
    "human_review_status": "pending",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "stem"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q02_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q02_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q02_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q02_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q02_c"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_21/question_02_with_figures.png",
    "prototype_paper": "9702_s16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_21.pdf",
      "paper_code": "9702_s16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 21,
      "question_id": "9702_s16_21_q02",
      "question_num": 2,
      "total_marks": 8,
      "parts": [
        {
          "id": "9702_s16_21_q02_a_i",
          "label": "(a)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q02_a_i_mp01",
              "text": "horizontal component (= 12 cos 50°) = 7.7 m s–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q02_a_ii",
          "label": "(a)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q02_a_ii_mp01",
              "text": "vertical component (= 12 sin 50° or 7.7 tan 50°) = 9.2 m s–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q02_b",
          "label": "(b)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_21_q02_b_mp01",
              "text": "v2 = u2 + 2as and v = 0 or mgh = ½mv2 or s = v2 sin2θ / 2g",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q02_b_mp02",
              "text": "9.22 = 2 × 9.81 × h hence h = 4.3 (4.31) m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "alternative methods using time to maximum height of 0.94 s: s = ut + ½at2 and t = 0.94 (s)",
            "2(C1) s = 9.2 × 0.94 – ½ × 9.81 × 0.942 hence s = 4.3 m",
            "2(A1) or s = vt – ½at2 and t = 0.94 (s)",
            "2(C1) s = ½ × 9.81 × 0.942 hence s = 4.3 m",
            "2(A1) or s = ½(u + v)t and t = 0.94 (s)",
            "2(C1) s = ½ × 9.2 × 0.94 hence s = 4.3 m"
          ]
        },
        {
          "id": "9702_s16_21_q02_c",
          "label": "(c)",
          "marks": 4,
          "marking_points": [
            {
              "id": "9702_s16_21_q02_c_mp01",
              "text": "t (= 9.2 / 9.81) = 0.94 (0.938) s",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q02_c_mp02",
              "text": "horizontal distance = 0.938 × 7.7 (= 7.23 m)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q02_c_mp03",
              "text": "displacement = [4.32 + 7.232]1/2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q02_c_mp04",
              "text": "= 8.4 m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 21"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_s16_21_q03",
    "source_filename": "9702_s16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 21,
    "paper_code": "9702_s16_21",
    "metadata_confidence": 1.0,
    "question_num": 3,
    "source_pages": [
      6,
      7
    ],
    "total_marks": 8,
    "detected_part_marks": 8,
    "marks_validation_passed": true,
    "question_stem": "A ball of mass 150 g is at rest on a horizontal floor, as shown in Fig. 3.1.",
    "question_stem_latex": "A ball of mass $150\\,\\mathrm{g}$ is at rest on a horizontal floor, as shown in Fig. 3.1.",
    "question_image": "question_03.png",
    "question_image_with_figures": "question_03_with_figures.png",
    "question_text_file": "question_03.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_3_1",
        "label": "Fig. 3.1",
        "file": "figure_3_1.png",
        "introduced_by": null,
        "referenced_by": [],
        "mapping_method": "caption_proximity",
        "mapping_confidence": 0.6,
        "placement": {
          "scope": "question",
          "position": "after_stem"
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_3_1.png"
      },
      {
        "id": "fig_3_2",
        "label": "Fig. 3.2",
        "file": "figure_3_2.png",
        "introduced_by": "9702_s16_21_q03_b",
        "referenced_by": [
          "9702_s16_21_q03_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_21_q03_b",
          "position": "after_text",
          "anchor": "Fig. 3.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_3_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_21_q03_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q03_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_s16_21_q03_a",
        "display_order": 2,
        "question_text": "Calculate the magnitude of the normal contact force from the floor acting on the ball.",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the magnitude of the normal contact force from the floor acting on the ball.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q03_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q03_a_i_field_01",
                  "control": "quantity",
                  "role": "value",
                  "label": "Force",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q03_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_s16_21_q03_a",
        "display_order": 3,
        "question_text": "Explain your working in (i).",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Explain your working in (i).",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q03_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q03_a_ii_field_01",
                  "control": "short_text",
                  "role": "explanation",
                  "required": true
                }
              ]
            }
          ]
        },
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_s16_21_q03_a_i"
          }
        ]
      },
      {
        "id": "9702_s16_21_q03_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "The ball is now lifted above the floor and dropped so that it falls vertically, as illustrated in\nFig. 3.2.\nJust before contact with the floor, the ball has velocity 6.2 m s⁻¹ downwards. The ball bounces\nfrom the floor and its velocity just after losing contact with the floor is 2.5 m s⁻¹ upwards. The\nball is in contact with the floor for 0.12 s.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_3_2"
        ],
        "figure_references": [
          "Fig. 3.2"
        ],
        "question_text_latex": "The ball is now lifted above the floor and dropped so that it falls vertically, as illustrated in\nFig. 3.2.\nJust before contact with the floor, the ball has velocity $6.2\\,\\mathrm{m\\,s^{-1}}$ downwards. The ball bounces\nfrom the floor and its velocity just after losing contact with the floor is $2.5\\,\\mathrm{m\\,s^{-1}}$ upwards. The\nball is in contact with the floor for $0.12\\,\\mathrm{s}$.",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q03_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_21_q03_b",
        "display_order": 5,
        "question_text": "State Newton’s second law of motion.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State Newton’s second law of motion.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q03_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q03_b_i_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q03_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_21_q03_b",
        "display_order": 6,
        "question_text": "Calculate the average resultant force on the ball when it is in contact with the floor.",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the average resultant force on the ball when it is in contact with the floor.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q03_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q03_b_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q03_b_ii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Average resultant force",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q03_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_s16_21_q03_b",
        "display_order": 7,
        "question_text": "State and explain whether linear momentum is conserved during the collision of the ball\nwith the floor.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State and explain whether linear momentum is conserved during the collision of the ball\nwith the floor.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q03_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q03_b_iii_field_01",
                  "control": "long_text",
                  "role": "explanation",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [
      "figure_without_explicit_part_reference"
    ],
    "human_review_status": "pending",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "stem"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q03_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q03_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q03_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q03_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q03_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q03_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q03_b_iii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_21/question_03_with_figures.png",
    "prototype_paper": "9702_s16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_21.pdf",
      "paper_code": "9702_s16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 21,
      "question_id": "9702_s16_21_q03",
      "question_num": 3,
      "total_marks": 8,
      "parts": [
        {
          "id": "9702_s16_21_q03_a_i",
          "label": "(a)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q03_a_i_mp01",
              "text": "force (= mg = 0.15 × 9.81) = 1.5 (1.47) N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q03_a_ii",
          "label": "(a)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q03_a_ii_mp01",
              "text": "resultant force (on ball) is zero so normal contact force = weight or the forces are in opposite directions so normal contact force = weight or normal contact force up = weight down",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q03_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q03_b_i_mp01",
              "text": "force proportional/equal to rate of change of momentum",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q03_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_21_q03_b_ii_mp01",
              "text": "change in momentum = 0.15 × (6.2 + 2.5) (= 1.305 N s)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q03_b_ii_mp02",
              "text": "magnitude of force = 1.305 / 0.12 = 11 (10.9) N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q03_b_ii_mp03",
              "text": "(direction of force is) upwards/up",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or",
            "average acceleration = (6.2 + 2.5) / 0.12 (= 72.5 m s–2)",
            "magnitude of force = 0.15 × 72.5 = 11 (10.9) N"
          ]
        },
        {
          "id": "9702_s16_21_q03_b_iii",
          "label": "(b)(iii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_21_q03_b_iii_mp01",
              "text": "there is a change/gain in momentum of the floor",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q03_b_iii_mp02",
              "text": "this is equal (and opposite) to the change/loss in momentum of the ball so momentum is conserved",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or change of (total) momentum of ball and floor is zero",
            "so momentum is conserved",
            "or total momentum of ball and floor before is equal to the (total) momentum of ball and floor after",
            "so momentum is conserved"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_s16_21_q04",
    "source_filename": "9702_s16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 21,
    "paper_code": "9702_s16_21",
    "metadata_confidence": 1.0,
    "question_num": 4,
    "source_pages": [
      8,
      9
    ],
    "total_marks": 9,
    "detected_part_marks": 7,
    "marks_validation_passed": false,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_04.png",
    "question_image_with_figures": "question_04_with_figures.png",
    "question_text_file": "question_04.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_4_1",
        "label": "Fig. 4.1",
        "file": "figure_4_1.png",
        "introduced_by": "9702_s16_21_q04_b",
        "referenced_by": [
          "9702_s16_21_q04_b",
          "9702_s16_21_q04_b_i",
          "9702_s16_21_q04_b_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_21_q04_b",
          "position": "after_text",
          "anchor": "shown in Fig. 4.1 for the range of values of x from 20 cm to 40 cm."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_4_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_21_q04_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State what is meant by elastic potential energy.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by elastic potential energy.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q04_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q04_a_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q04_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A spring is extended by applying a force. The variation with extension x of the force F is\nshown in Fig. 4.1 for the range of values of x from 20 cm to 40 cm.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_4_1"
        ],
        "figure_references": [
          "Fig. 4.1"
        ],
        "question_text_latex": "A spring is extended by applying a force. The variation with extension x of the force F is\nshown in Fig. 4.1 for the range of values of x from 20 cm to 40 cm.",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q04_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_21_q04_b",
        "display_order": 3,
        "question_text": "Use data from Fig. 4.1 to show that the spring obeys Hooke’s law for this range of\nextensions.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [
          "fig_4_1"
        ],
        "figure_references": [
          "Fig. 4.1"
        ],
        "question_text_latex": "Use data from Fig. 4.1 to show that the spring obeys Hooke’s law for this range of\nextensions.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q04_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q04_b_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                }
              ]
            }
          ]
        },
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ]
      },
      {
        "id": "9702_s16_21_q04_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_21_q04_b",
        "display_order": 4,
        "question_text": "Use Fig. 4.1 to calculate\n1. the spring constant,\n2. the work done extending the spring from x = 20 cm to x = 40 cm.",
        "marks": 5,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "J",
        "figure_ids": [
          "fig_4_1"
        ],
        "figure_references": [
          "Fig. 4.1"
        ],
        "question_text_latex": "Use Fig. 4.1 to calculate\n1. the spring constant,\n2. the work done extending the spring from $x = 20\\,\\mathrm{cm}$ to $x = 40\\,\\mathrm{cm}$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q04_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q04_b_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working for spring constant",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q04_b_ii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Spring constant",
                  "unit": "N m⁻¹",
                  "unit_latex": "\\mathrm{N\\,m^{-1}}",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q04_b_ii_field_03",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working for work done",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q04_b_ii_field_04",
                  "control": "quantity",
                  "role": "value",
                  "label": "Work done",
                  "unit": "J",
                  "unit_latex": "\\mathrm{J}",
                  "required": true
                }
              ]
            }
          ]
        },
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ]
      },
      {
        "id": "9702_s16_21_q04_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "A force is applied to the spring in (b) to give an extension of 50 cm.\nState how you would check that the spring has not exceeded its elastic limit.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "A force is applied to the spring in (b) to give an extension of 50 cm.\nState how you would check that the spring has not exceeded its elastic limit.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q04_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q04_c_field_01",
                  "control": "short_text",
                  "role": "explanation",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [
      "part_marks_do_not_match_total"
    ],
    "human_review_status": "pending",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_21_q04_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q04_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q04_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q04_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q04_c"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_21/question_04_with_figures.png",
    "prototype_paper": "9702_s16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_21.pdf",
      "paper_code": "9702_s16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 21,
      "question_id": "9702_s16_21_q04",
      "question_num": 4,
      "total_marks": 9,
      "parts": [
        {
          "id": "9702_s16_21_q04_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q04_a_mp01",
              "text": "the energy (stored) in a body due to its extension/compression/deformation/ change in shape/size",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q04_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_21_q04_b_i_mp01",
              "text": "two values of F/x are calculated which are the same e.g. 10.4 / 40 = 0.26 and 6.5 / 25 = 0.26",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q04_b_i_mp02",
              "text": "force is proportional to extension (and so Hooke’s law obeyed)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or ratio of two forces and the ratio of the corresponding two extensions are calculated which are the same e.g. 5.2 / 10.4 = 0.5 and 20 / 40 = 0.5",
            "4(B1) or gradient of graph line calculated and coordinates of one point on the line used with straight line equation y = mx + c to show c = 0"
          ]
        },
        {
          "id": "9702_s16_21_q04_b_ii",
          "label": "(b)(ii)",
          "marks": 5,
          "marking_points": [
            {
              "id": "9702_s16_21_q04_b_ii_mp01",
              "text": "1. k = F / x or k = gradient",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q04_b_ii_mp02",
              "text": "gradient or values from a single point used e.g. k = 10.4 / (40 × 10–2) k = 26 N m–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q04_b_ii_mp03",
              "text": "2. work done = area under graph or ½Fx or ½(F2 + F1)(x2 – x1) or ½kx2 or ½k(x2 2 – x1 2)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q04_b_ii_mp04",
              "text": "= ½ × 10.4 × 0.4 – ½ × 5.2 × 0.2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q04_b_ii_mp05",
              "text": "or ½ × (5.2 + 10.4) × 20 × 10–2 or ½ × 26 × (0.42 − 0.22) = 1.6 J",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q04_c",
          "label": "(c)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q04_c_mp01",
              "text": "remove the force and the spring goes back to its original length",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_s16_21_q05",
    "source_filename": "9702_s16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 21,
    "paper_code": "9702_s16_21",
    "metadata_confidence": 1.0,
    "question_num": 5,
    "source_pages": [
      11,
      12,
      13
    ],
    "total_marks": 11,
    "detected_part_marks": 11,
    "marks_validation_passed": true,
    "question_stem": "The variation with time t of the displacement y of a wave X, as it passes a point P, is shown in\nFig. 5.1.\nThe intensity of wave X is I.",
    "question_stem_latex": "The variation with time $t$ of the displacement $y$ of a wave X, as it passes a point P, is shown in\nFig. 5.1.\nThe intensity of wave X is $I$.",
    "question_image": "question_05.png",
    "question_image_with_figures": "question_05_with_figures.png",
    "question_text_file": "question_05.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_5_1",
        "label": "Fig. 5.1",
        "file": "figure_5_1.png",
        "introduced_by": "9702_s16_21_q05_a",
        "referenced_by": [
          "9702_s16_21_q05_a",
          "9702_s16_21_q05_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "question",
          "position": "after_stem_text",
          "anchor": "Fig. 5.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_5_1.png"
      },
      {
        "id": "fig_5_2",
        "label": "Fig. 5.2",
        "file": "figure_5_2.png",
        "introduced_by": "9702_s16_21_q05_c",
        "referenced_by": [
          "9702_s16_21_q05_c"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_21_q05_c",
          "position": "after_text",
          "anchor": "as shown in Fig. 5.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_5_2.png"
      },
      {
        "id": "fig_5_3",
        "label": "Fig. 5.3",
        "file": "figure_5_3.png",
        "introduced_by": "9702_s16_21_q05_c",
        "referenced_by": [
          "9702_s16_21_q05_c",
          "9702_s16_21_q05_c_i",
          "9702_s16_21_q05_c_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_21_q05_c",
          "position": "after_text",
          "anchor": "shown in\nFig. 5.3."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_5_3.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_21_q05_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Use Fig. 5.1 to determine the frequency of wave X.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "Hz",
        "figure_ids": [
          "fig_5_1"
        ],
        "figure_references": [
          "Fig. 5.1"
        ],
        "question_text_latex": "Use Fig. 5.1 to determine the frequency of wave X.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q05_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q05_a_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q05_a_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Frequency",
                  "unit": "Hz",
                  "unit_latex": "\\mathrm{Hz}",
                  "required": true
                }
              ]
            }
          ]
        },
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_1"
          }
        ]
      },
      {
        "id": "9702_s16_21_q05_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A second wave Z with the same frequency as wave X also passes point P.\nWave Z has intensity 2I. The phase difference between the two waves is 90°.\nOn Fig. 5.1, sketch the variation with time t of the displacement y of wave Z.\nShow your working.",
        "marks": 3,
        "answer_type": "graph",
        "answer_type_confidence": 0.95,
        "unit": null,
        "figure_ids": [
          "fig_5_1"
        ],
        "figure_references": [
          "Fig. 5.1"
        ],
        "question_text_latex": "A second wave Z with the same frequency as wave X also passes point P.\nWave Z has intensity 2I. The phase difference between the two waves is 90°.\nOn Fig. 5.1, sketch the variation with time t of the displacement y of wave Z.\nShow your working.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q05_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q05_b_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                }
              ]
            },
            {
              "block_id": "9702_s16_21_q05_b_block_02",
              "type": "canvas",
              "mode": "annotate_figure",
              "background_figure_id": "fig_5_1",
              "tools": [
                "curve",
                "freehand",
                "eraser"
              ]
            }
          ]
        },
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_1"
          }
        ]
      },
      {
        "id": "9702_s16_21_q05_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "A double-slit interference experiment is used to determine the wavelength of light emitted\nfrom a laser, as shown in Fig. 5.2.\nThe separation of the slits is 0.45 mm. The fringes are viewed on a screen at a distance D\nfrom the double slit.\nThe fringe width x is measured for different distances D. The variation with D of x is shown in\nFig. 5.3.",
        "marks": null,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_5_2",
          "fig_5_3"
        ],
        "figure_references": [
          "Fig. 5.2",
          "Fig. 5.3"
        ],
        "question_text_latex": "A double-slit interference experiment is used to determine the wavelength of light emitted\nfrom a laser, as shown in Fig. 5.2.\nThe separation of the slits is 0.45 mm. The fringes are viewed on a screen at a distance D\nfrom the double slit.\nThe fringe width x is measured for different distances D. The variation with D of x is shown in\nFig. 5.3.",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q05_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_s16_21_q05_c",
        "display_order": 4,
        "question_text": "Use the gradient of the line in Fig. 5.3 to determine the wavelength, in nm, of the laser\nlight.",
        "marks": 4,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_5_3"
        ],
        "figure_references": [
          "Fig. 5.3"
        ],
        "question_text_latex": "Use the gradient of the line in Fig. 5.3 to determine the wavelength, in nm, of the laser\nlight.",
        "marks_source": "reconciled_from_printed_total",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q05_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q05_c_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q05_c_i_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Wavelength",
                  "unit": "nm",
                  "unit_latex": "\\mathrm{nm}",
                  "required": true
                }
              ]
            }
          ]
        },
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_3"
          }
        ]
      },
      {
        "id": "9702_s16_21_q05_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_s16_21_q05_c",
        "display_order": 5,
        "question_text": "The separation of the slits is increased. State and explain the effects, if any, on the graph\nof Fig. 5.3.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_5_3"
        ],
        "figure_references": [
          "Fig. 5.3"
        ],
        "question_text_latex": "The separation of the slits is increased. State and explain the effects, if any, on the graph\nof Fig. 5.3.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q05_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q05_c_ii_field_01",
                  "control": "long_text",
                  "role": "explanation",
                  "required": true
                }
              ]
            }
          ]
        },
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_3"
          }
        ]
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "stem"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q05_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q05_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q05_c"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q05_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q05_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_21/question_05_with_figures.png",
    "prototype_paper": "9702_s16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_21.pdf",
      "paper_code": "9702_s16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 21,
      "question_id": "9702_s16_21_q05",
      "question_num": 5,
      "total_marks": 11,
      "parts": [
        {
          "id": "9702_s16_21_q05_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_21_q05_a_mp01",
              "text": "T = 4 (ms) or 4 × 10–3 s",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q05_a_mp02",
              "text": "f = 1 / T = 1 / 0.004 = 250 Hz",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q05_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_21_q05_b_mp01",
              "text": "intensity ∝ (amplitude)2 and amplitude = 2.8 (2.83) (cm)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q05_b_mp02",
              "text": "curve with same period and with amplitude 2.8 cm",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q05_b_mp03",
              "text": "curve shifted 1.0 ms to left or to right of wave X",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 21"
          ]
        },
        {
          "id": "9702_s16_21_q05_c_i",
          "label": "(c)(i)",
          "marks": 4,
          "marking_points": [
            {
              "id": "9702_s16_21_q05_c_i_mp01",
              "text": "gradient = (4.5 – 2.4) × 10–3 / (3.25 – 1.75) [= 1.4 × 10–3]",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q05_c_i_mp02",
              "text": "wavelength = 0.45 × 10–3 × 1.4 × 10–3",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q05_c_i_mp03",
              "text": "= 6.30 × 10–7 m",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q05_c_i_mp04",
              "text": "= 630 nm",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q05_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_21_q05_c_ii_mp01",
              "text": "(gradient is equal to λ / a therefore) gradient of line is reduced",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q05_c_ii_mp02",
              "text": "value of x will be reduced for all values of D or new line is completely below old line or intercept is less",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_s16_21_q06",
    "source_filename": "9702_s16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 21,
    "paper_code": "9702_s16_21",
    "metadata_confidence": 1.0,
    "question_num": 6,
    "source_pages": [
      14,
      15
    ],
    "total_marks": 12,
    "detected_part_marks": 12,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_06.png",
    "question_image_with_figures": "question_06_with_figures.png",
    "question_text_file": "question_06.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_6_1",
        "label": "Fig. 6.1",
        "file": "figure_6_1.png",
        "introduced_by": "9702_s16_21_q06_b",
        "referenced_by": [
          "9702_s16_21_q06_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_21_q06_b",
          "position": "after_text",
          "anchor": "as shown in Fig. 6.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_6_1.png"
      },
      {
        "id": "fig_6_2",
        "label": "Fig. 6.2",
        "file": "figure_6_2.png",
        "introduced_by": "9702_s16_21_q06_c",
        "referenced_by": [
          "9702_s16_21_q06_c"
        ],
        "mapping_method": "ai_repair_from_complete_question_image",
        "mapping_confidence": 1.0,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_21_q06_c",
          "position": "after_text",
          "anchor": "shown in Fig. 6.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_21/figure_6_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_21_q06_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define the coulomb.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define the coulomb.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q06_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q06_a_field_01",
                  "control": "short_text",
                  "role": "definition",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q06_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A resistor X is connected to a cell as shown in Fig. 6.1.\nThe resistor is a wire of cross-sectional area A and length l. The current in the wire is I.\nShow that the average drift speed v of the charge carriers in X is given by the equation\nv = I/(nAe)\nwhere e is the charge on a charge carrier and n is the number of charge carriers per unit\nvolume in X.",
        "marks": 3,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [
          "fig_6_1"
        ],
        "figure_references": [
          "Fig. 6.1"
        ],
        "question_text_latex": "A resistor X is connected to a cell as shown in Fig. 6.1.\nThe resistor is a wire of cross-sectional area $A$ and length $l$. The current in the wire is $I$.\nShow that the average drift speed $v$ of the charge carriers in X is given by the equation\n$v = \\frac{I}{nAe}$\nwhere $e$ is the charge on a charge carrier and $n$ is the number of charge carriers per unit\nvolume in X.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q06_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q06_b_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q06_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "A 12 V battery with negligible internal resistance is connected to two resistors Y and Z, as\nshown in Fig. 6.2.\nThe resistors are made from wires of the same material. The wire of Y has a diameter d and\nlength l. The wire of Z has a diameter 2d and length 2l.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_6_2"
        ],
        "figure_references": [
          "Fig. 6.2"
        ],
        "question_text_latex": "A $12\\,\\mathrm{V}$ battery with negligible internal resistance is connected to two resistors Y and Z, as\nshown in Fig. 6.2.\nThe resistors are made from wires of the same material. The wire of Y has a diameter $d$ and\nlength $l$. The wire of Z has a diameter $2d$ and length $2l$.",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q06_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_s16_21_q06_c",
        "display_order": 4,
        "question_text": "Determine the ratio\naverage drift speed of the charge carriers in Y / average drift speed of the charge carriers in Z.",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the ratio\n$\\frac{\\text{average drift speed of the charge carriers in Y}}{\\text{average drift speed of the charge carriers in Z}}$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q06_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q06_c_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q06_c_i_field_02",
                  "control": "number",
                  "role": "value",
                  "label": "Ratio",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q06_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_s16_21_q06_c",
        "display_order": 5,
        "question_text": "Show that\nresistance of Y / resistance of Z = 2.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that\n$\\frac{\\text{resistance of Y}}{\\text{resistance of Z}} = 2$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q06_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q06_c_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q06_c_iii",
        "path": [
          "c",
          "iii"
        ],
        "label": "(c)(iii)",
        "parent_id": "9702_s16_21_q06_c",
        "display_order": 6,
        "question_text": "Determine the potential difference across Y.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "V",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the potential difference across Y.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q06_c_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q06_c_iii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "label": "Working",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q06_c_iii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Potential difference",
                  "unit": "V",
                  "unit_latex": "\\mathrm{V}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q06_c_iv",
        "path": [
          "c",
          "iv"
        ],
        "label": "(c)(iv)",
        "parent_id": "9702_s16_21_q06_c",
        "display_order": 7,
        "question_text": "Determine the ratio\npower dissipated in Y / power dissipated in Z.",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the ratio\n$\\frac{\\text{power dissipated in Y}}{\\text{power dissipated in Z}}$.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q06_c_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q06_c_iv_field_01",
                  "control": "number",
                  "role": "value",
                  "label": "Ratio",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_21_q06_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q06_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q06_c"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q06_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q06_c_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q06_c_iii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q06_c_iv"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_21/question_06_with_figures.png",
    "prototype_paper": "9702_s16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_21.pdf",
      "paper_code": "9702_s16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 21,
      "question_id": "9702_s16_21_q06",
      "question_num": 6,
      "total_marks": 12,
      "parts": [
        {
          "id": "9702_s16_21_q06_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q06_a_mp01",
              "text": "(coulomb is) ampere second",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q06_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_21_q06_b_mp01",
              "text": "charge or Q = nAle",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q06_b_mp02",
              "text": "I = Q / t and l / t = v",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q06_b_mp03",
              "text": "I = nAle / t = nAve therefore v = I / nAe",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q06_c_i",
          "label": "(c)(i)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_21_q06_c_i_mp01",
              "text": "ratio = (I / nAYe) / (I / nAZe)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q06_c_i_mp02",
              "text": "= AZ / AY or 4A / A or πd2 / (πd2 / 4)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q06_c_i_mp03",
              "text": "= 4",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q06_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_21_q06_c_ii_mp01",
              "text": "R = ρl / A or R = 4ρl / πd2",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q06_c_ii_mp02",
              "text": "RY = ρl / A and RZ = ρ(2l) / 4A so RY / RZ = 2 or RY = 4ρl /πd2 and RZ = 4ρ(2l) /π4d2 or 2ρl / πd2 so RY / RZ = 2",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q06_c_iii",
          "label": "(c)(iii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_21_q06_c_iii_mp01",
              "text": "V = 12RY / (RY + RZ) or I = 12 / (RY + RZ) and V = IRY",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_21_q06_c_iii_mp02",
              "text": "V = 12 × 2/3 = 8(.0) V",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q06_c_iv",
          "label": "(c)(iv)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q06_c_iv_mp01",
              "text": "ratio = I2RY / I2RZ or (VY 2 / RY) / (VZ 2 / RZ) or (VYI) / (VZI) = 2",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 21"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_s16_21_q07",
    "source_filename": "9702_s16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 21,
    "paper_code": "9702_s16_21",
    "metadata_confidence": 1.0,
    "question_num": 7,
    "source_pages": [
      16
    ],
    "total_marks": 5,
    "detected_part_marks": 5,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_07.png",
    "question_image_with_figures": null,
    "question_text_file": "question_07.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_s16_21_q07_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Give one example of a hadron and one example of a lepton.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Give one example of a hadron and one example of a lepton.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q07_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q07_a_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "label": "A hadron",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q07_a_field_02",
                  "control": "short_text",
                  "role": "answer",
                  "label": "A lepton",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q07_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "Describe, in terms of the simple quark model,",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Describe, in terms of the simple quark model,",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q07_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_21_q07_b",
        "display_order": 3,
        "question_text": "a proton,",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "a proton,",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q07_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q07_b_i_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q07_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_21_q07_b",
        "display_order": 4,
        "question_text": "a neutron.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "a neutron.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q07_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q07_b_ii_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q07_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "Beta particles may be emitted during the decay of an unstable nucleus of an atom. The\nemission of a beta particle is due to the decay of a neutron.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Beta particles may be emitted during the decay of an unstable nucleus of an atom. The\nemission of a beta particle is due to the decay of a neutron.",
        "marks_source": null
      },
      {
        "id": "9702_s16_21_q07_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_s16_21_q07_c",
        "display_order": 6,
        "question_text": "Complete the following word equation for the particles produced in this reaction.\nneutron → ___ + ___ + ___",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Complete the following word equation for the particles produced in this reaction.\nneutron $\\rightarrow$ ___ + ___ + ___",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q07_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q07_c_i_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "label": "First particle",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q07_c_i_field_02",
                  "control": "short_text",
                  "role": "answer",
                  "label": "Second particle",
                  "required": true
                },
                {
                  "field_id": "9702_s16_21_q07_c_i_field_03",
                  "control": "short_text",
                  "role": "answer",
                  "label": "Third particle",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_21_q07_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_s16_21_q07_c",
        "display_order": 7,
        "question_text": "State the change in quark composition of the particles during this reaction.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the change in quark composition of the particles during this reaction.",
        "marks_source": "compacted_text",
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_21_q07_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_21_q07_c_ii_field_01",
                  "control": "short_text",
                  "role": "answer",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_21_q07_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q07_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q07_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q07_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q07_c"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q07_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_21_q07_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_21/question_07.png",
    "prototype_paper": "9702_s16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_21.pdf",
      "paper_code": "9702_s16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 21,
      "question_id": "9702_s16_21_q07",
      "question_num": 7,
      "total_marks": 5,
      "parts": [
        {
          "id": "9702_s16_21_q07_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q07_a_mp01",
              "text": "hadron: neutron/proton and lepton: electron/(electron) neutrino",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "(allow other correct particles)"
          ]
        },
        {
          "id": "9702_s16_21_q07_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q07_b_i_mp01",
              "text": "proton: up up down or uud",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q07_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q07_b_ii_mp01",
              "text": "neutron: up down down or udd",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q07_c_i",
          "label": "(c)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q07_c_i_mp01",
              "text": "neutron → proton + electron + (electron) antineutrino",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_21_q07_c_ii",
          "label": "(c)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_21_q07_c_ii_mp01",
              "text": "up down down (quarks) change to up up down (quarks) or down (quark) changes to up (quark)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_22_q01",
    "source_filename": "9702_s16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 22,
    "paper_code": "9702_s16_22",
    "metadata_confidence": 1,
    "question_num": 1,
    "source_pages": [
      4,
      5
    ],
    "total_marks": 12,
    "detected_part_marks": 12,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_01.png",
    "question_image_with_figures": "question_01_with_figures.png",
    "question_text_file": "question_01.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_1_1",
        "label": "Fig. 1.1",
        "file": "figure_1_1.png",
        "introduced_by": "9702_s16_22_q01_b",
        "referenced_by": [
          "9702_s16_22_q01_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_22_q01_b",
          "position": "after_text",
          "anchor": "The path is illustrated in Fig. 1.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_22/figure_1_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_22_q01_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define acceleration.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define acceleration.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q01_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q01_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q01_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A man travels on a toboggan down a slope covered with snow from point A to point B and\nthen to point C. The path is illustrated in Fig. 1.1.\nThe slope AB makes an angle of 40°with the horizontal and the slope BC makes an angle of\n20°with the horizontal. Friction is not negligible.\nThe man and toboggan have a combined mass of 95 kg.\nThe man starts from rest at A and has constant acceleration between A and B. The man\ntakes 19 s to reach B. His speed is 36 m s⁻¹ at B.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "A man travels on a toboggan down a slope covered with snow from point A to point B and\nthen to point C. The path is illustrated in Fig. 1.1.\nThe slope AB makes an angle of $40^\\circ$ with the horizontal and the slope BC makes an angle of\n$20^\\circ$ with the horizontal. Friction is not negligible.\nThe man and toboggan have a combined mass of $95\\,\\mathrm{kg}$.\nThe man starts from rest at A and has constant acceleration between A and B. The man\ntakes $19\\,\\mathrm{s}$ to reach B. His speed is $36\\,\\mathrm{m\\,s^{-1}}$ at B.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_22_q01_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_22_q01_b",
        "display_order": 3,
        "question_text": "Calculate the acceleration from A to B.\nacceleration = m s⁻²",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the acceleration from A to B.\n$acceleration = m s^{-2}$",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q01_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q01_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q01_b_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "acceleration",
                  "unit": "m s⁻²",
                  "unit_latex": "\\mathrm{m\\,s^{-2}}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q01_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_22_q01_b",
        "display_order": 4,
        "question_text": "Show that the distance moved from A to B is 340 m.",
        "marks": 1,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the distance moved from A to B is 340 m.",
        "marks_source": "reconciled_from_printed_total",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q01_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q01_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q01_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_s16_22_q01_b",
        "display_order": 5,
        "question_text": "For the man and toboggan moving from A to B, calculate\n1. the change in kinetic energy,\nchange in kinetic energy = J\n2. the change in potential energy.\nchange in potential energy = J",
        "marks": 4,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "J",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "For the man and toboggan moving from A to B, calculate\n1. the change in kinetic energy,\nchange in kinetic energy = J\n2. the change in potential energy.\nchange in potential energy = J",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q01_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q01_b_iii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q01_b_iii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "change in kinetic energy",
                  "unit": "J",
                  "unit_latex": "\\mathrm{J}"
                },
                {
                  "field_id": "9702_s16_22_q01_b_iii_field_03",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "change in potential energy",
                  "unit": "J",
                  "unit_latex": "\\mathrm{J}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q01_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_s16_22_q01_b",
        "display_order": 6,
        "question_text": "Use your answers in (iii) to determine the average frictional force that acts on the\ntoboggan between A and B.\nfrictional force = N",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use your answers in (iii) to determine the average frictional force that acts on the\ntoboggan between A and B.\n$frictional force = N $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_s16_22_q01_b_iii"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q01_b_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q01_b_iv_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q01_b_iv_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "frictional force",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q01_b_v",
        "path": [
          "b",
          "v"
        ],
        "label": "(b)(v)",
        "parent_id": "9702_s16_22_q01_b",
        "display_order": 7,
        "question_text": "A parachute opens on the toboggan as it passes point B. There is a constant deceleration\nof 3.0 m s⁻² from B to C.\nCalculate the frictional force that produces this deceleration between B and C.\nfrictional force = N",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "A parachute opens on the toboggan as it passes point B. There is a constant deceleration\nof 3.0 m $s^{-2}$ from B to C.\nCalculate the frictional force that produces this deceleration between B and C.\n$frictional force = N $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q01_b_v_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q01_b_v_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q01_b_v_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "frictional force",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_22_q01_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q01_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q01_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q01_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q01_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q01_b_iv"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q01_b_v"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_22/question_01_with_figures.png",
    "prototype_paper": "9702_s16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_22.pdf",
      "paper_code": "9702_s16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 22,
      "question_id": "9702_s16_22_q01",
      "question_num": 1,
      "total_marks": 12,
      "parts": [
        {
          "id": "9702_s16_22_q01_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q01_a_mp01",
              "text": "acceleration = change in velocity / time (taken) or rate of change of velocity",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q01_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q01_b_i_mp01",
              "text": "v = 0 + at or v = at",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q01_b_i_mp02",
              "text": "(a = 36 / 19 =) 1.9 (1.8947) m s–2",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q01_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q01_b_ii_mp01",
              "text": "s = ½(u + v)t or s = v2 / 2a or s = ½at2 = ½ × 36 × 19 = 362 / (2 × 1.89) = ½ × 1.89 × 192 = 340 m (342 m / 343 m / 341 m)",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q01_b_iii",
          "label": "(b)(iii)",
          "marks": 4,
          "marking_points": [
            {
              "id": "9702_s16_22_q01_b_iii_mp01",
              "text": "1. (∆KE =) ½ × 95 × (36)2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q01_b_iii_mp02",
              "text": "= 62 000 (61 560) J",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q01_b_iii_mp03",
              "text": "2. (∆PE =) 95 × 9.81 × 340 sin 40° or 95 × 9.81 × 218.5",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q01_b_iii_mp04",
              "text": "= 200 000 J",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q01_b_iv",
          "label": "(b)(iv)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q01_b_iv_mp01",
              "text": "work done (by frictional force) = ∆PE – ∆KE or work done = 200 000 – 62 000 (values from 1b(iii) 1. and 2.)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q01_b_iv_mp02",
              "text": "(frictional force = 138 000 / 340 =) 410 (406) N [420 N if full figures used]",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q01_b_v",
          "label": "(b)(v)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q01_b_v_mp01",
              "text": "–ma = mg sin 20° – f or ma = –mg sin 20° + f",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q01_b_v_mp02",
              "text": "–95 × 3.0 = 95 × 3.36 – f f = 600 (604) N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_22_q02",
    "source_filename": "9702_s16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 22,
    "paper_code": "9702_s16_22",
    "metadata_confidence": 1,
    "question_num": 2,
    "source_pages": [
      6,
      7
    ],
    "total_marks": 6,
    "detected_part_marks": 6,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_02.png",
    "question_image_with_figures": "question_02_with_figures.png",
    "question_text_file": "question_02.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_2_1",
        "label": "Fig. 2.1",
        "file": "figure_2_1.png",
        "introduced_by": "9702_s16_22_q02_a",
        "referenced_by": [
          "9702_s16_22_q02_a"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_22_q02_a",
          "position": "after_text",
          "anchor": "Fig. 2.1 shows a liquid in a cylindrical container."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_22/figure_2_1.png"
      },
      {
        "id": "fig_2_2",
        "label": "Fig. 2.2",
        "file": "figure_2_2.png",
        "introduced_by": "9702_s16_22_q02_b",
        "referenced_by": [
          "9702_s16_22_q02_b",
          "9702_s16_22_q02_b_i",
          "9702_s16_22_q02_b_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_22_q02_b",
          "position": "after_text",
          "anchor": "Fig. 2.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_22/figure_2_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_22_q02_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Fig. 2.1 shows a liquid in a cylindrical container.\nThe cross-sectional area of the container is A. The height of the column of liquid is h and the\ndensity of the liquid is ρ.\nShow that the pressure p due to the liquid on the base of the cylinder is given by\np = ρ gh.",
        "marks": 3,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": "ρ gh.",
        "figure_ids": [
          "fig_2_1"
        ],
        "figure_references": [
          "Fig. 2.1"
        ],
        "question_text_latex": "Fig. 2.1 shows a liquid in a cylindrical container.\nThe cross-sectional area of the container is A. The height of the column of liquid is h and the\ndensity of the liquid is $\\rho$.\nShow that the pressure p due to the liquid on the base of the cylinder is given by\n$p = \\rho gh.$",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q02_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q02_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q02_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "The variation with height h of the total pressure P on the base of the cylinder in (a) is shown in\nFig. 2.2.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_2_2"
        ],
        "figure_references": [
          "Fig. 2.2"
        ],
        "question_text_latex": "The variation with height h of the total pressure P on the base of the cylinder in (a) is shown in\nFig. 2.2.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_22_q02_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_22_q02_b",
        "display_order": 3,
        "question_text": "Explain why the line of the graph in Fig. 2.2 does not pass through the origin (0,0).",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_2_2"
        ],
        "figure_references": [
          "Fig. 2.2"
        ],
        "question_text_latex": "Explain why the line of the graph in Fig. 2.2 does not pass through the origin (0,0).",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_2_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q02_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q02_b_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q02_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_22_q02_b",
        "display_order": 4,
        "question_text": "Use data from Fig. 2.2 to calculate the density of the liquid in the cylinder.\ndensity = kg m⁻³",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_2_2"
        ],
        "figure_references": [
          "Fig. 2.2"
        ],
        "question_text_latex": "Use data from Fig. 2.2 to calculate the density of the liquid in the cylinder.\n$density = kg m^{-3} $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_2_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q02_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q02_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q02_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "density",
                  "unit": "kg m⁻³",
                  "unit_latex": "\\mathrm{kg\\,m^{-3}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_22_q02_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q02_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q02_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q02_b_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_22/question_02_with_figures.png",
    "prototype_paper": "9702_s16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_22.pdf",
      "paper_code": "9702_s16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 22,
      "question_id": "9702_s16_22_q02",
      "question_num": 2,
      "total_marks": 6,
      "parts": [
        {
          "id": "9702_s16_22_q02_a",
          "label": "(a)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_22_q02_a_mp01",
              "text": "p = F / A",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q02_a_mp02",
              "text": "use of m = ρV and use of V = Ah and use of F = mg",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q02_a_mp03",
              "text": "correct substitution to obtain p = ρgh",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q02_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q02_b_i_mp01",
              "text": "(when h is zero the pressure is not zero due to) pressure from the air/atmosphere",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q02_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q02_b_ii_mp01",
              "text": "gradient = ρg or P – 1.0 × 105 = ρgh",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q02_b_ii_mp02",
              "text": "e.g. ρg = 1.0 × 105 / 0.75 (= 133333) ρ = 133 333 / 9.81 = 14 000 (13 592) kg m–3",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 22"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_22_q03",
    "source_filename": "9702_s16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 22,
    "paper_code": "9702_s16_22",
    "metadata_confidence": 1,
    "question_num": 3,
    "source_pages": [
      8
    ],
    "total_marks": 5,
    "detected_part_marks": 5,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_03.png",
    "question_image_with_figures": "question_03_with_figures.png",
    "question_text_file": "question_03.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_3_1",
        "label": "Fig. 3.1",
        "file": "figure_3_1.png",
        "introduced_by": "9702_s16_22_q03_b_ii",
        "referenced_by": [
          "9702_s16_22_q03_b_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_22_q03_b_ii",
          "position": "response_background"
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_22/figure_3_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_22_q03_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define the Young modulus.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define the Young modulus.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q03_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q03_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q03_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "The Young modulus of steel is 1.9 × 10¹¹ Pa. The Young modulus of copper is 1.2 × 10¹¹ Pa.\nA steel wire and a copper wire each have the same cross-sectional area and length. The two\nwires are each extended by equal forces.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The Young modulus of steel is $1.9 \\times 10^{11}$ Pa. The Young modulus of copper is $1.2 \\times 10^{11}$ Pa.\nA steel wire and a copper wire each have the same cross-sectional area and length. The two\nwires are each extended by equal forces.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_22_q03_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_22_q03_b",
        "display_order": 3,
        "question_text": "Use the definition of the Young modulus to determine the ratio\nextension of the copper wire / extension of the steel wire.\nratio =",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use the definition of the Young modulus to determine the ratio $\\frac{\\text{extension of the copper wire}}{\\text{extension of the steel wire}}$.\n$\\text{ratio} =$",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q03_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q03_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q03_b_i_field_02",
                  "required": true,
                  "control": "number",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q03_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_22_q03_b",
        "display_order": 4,
        "question_text": "The two wires are each extended by a force. Both wires obey Hooke’s law.\nOn Fig. 3.1, sketch a graph for each wire to show the variation with extension of the\nforce.\nLabel the line for steel with the letter S and the line for copper with the letter C.",
        "marks": 1,
        "answer_type": "graph",
        "answer_type_confidence": 0.95,
        "unit": null,
        "figure_ids": [
          "fig_3_1"
        ],
        "figure_references": [
          "Fig. 3.1"
        ],
        "question_text_latex": "The two wires are each extended by a force. Both wires obey Hooke’s law.\nOn Fig. 3.1, sketch a graph for each wire to show the variation with extension of the\nforce.\nLabel the line for steel with the letter S and the line for copper with the letter C.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q03_b_ii_block_01",
              "type": "canvas",
              "mode": "draw_on_scaffold",
              "background_figure_id": "fig_3_1",
              "tools": [
                "line",
                "text"
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_22_q03_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q03_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q03_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q03_b_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_22/question_03_with_figures.png",
    "prototype_paper": "9702_s16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_22.pdf",
      "paper_code": "9702_s16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 22,
      "question_id": "9702_s16_22_q03",
      "question_num": 3,
      "total_marks": 5,
      "parts": [
        {
          "id": "9702_s16_22_q03_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q03_a_mp01",
              "text": "Young modulus = stress / strain",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q03_b_i",
          "label": "(b)(i)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_22_q03_b_i_mp01",
              "text": "E = (F × l) / (A × e) or e = (F × l) / (A × E)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q03_b_i_mp02",
              "text": "e ∝ 1 / E or ratio eC / eS = ES / EC or (1.9 × 1011) / (1.2 × 1011) or 19 / 12",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q03_b_i_mp03",
              "text": "(ratio =) 1.6 (1.58)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q03_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q03_b_ii_mp01",
              "text": "two straight lines from (0,0) with S having the steepest gradient",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_22_q04",
    "source_filename": "9702_s16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 22,
    "paper_code": "9702_s16_22",
    "metadata_confidence": 1,
    "question_num": 4,
    "source_pages": [
      9,
      10
    ],
    "total_marks": 10,
    "detected_part_marks": 10,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_04.png",
    "question_image_with_figures": null,
    "question_text_file": "question_04.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_s16_22_q04_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "By reference to the direction of the propagation of energy, state what is meant by a longitudinal\nwave and by a transverse wave.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "By reference to the direction of the propagation of energy, state what is meant by a longitudinal\nwave and by a transverse wave.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q04_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q04_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q04_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "The intensity of a sound wave passing through air is given by\nI = Kvρf²A²\nwhere I is the intensity (power per unit area),\nK is a constant without units,\nv is the speed of sound,\nρ is the density of air,\nf is the frequency of the wave\nand A is the amplitude of the wave.\nShow that both sides of the equation have the same SI base units.",
        "marks": 3,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The intensity of a sound wave passing through air is given by\n$I = Kv\\rho f^2 A^2$\nwhere $I$ is the intensity (power per unit area),\n$K$ is a constant without units,\n$v$ is the speed of sound,\n$\\rho$ is the density of air,\n$f$ is the frequency of the wave\nand $A$ is the amplitude of the wave.\nShow that both sides of the equation have the same SI base units.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q04_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q04_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q04_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_22_q04_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_s16_22_q04_c",
        "display_order": 4,
        "question_text": "Describe the Doppler effect.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Describe the Doppler effect.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q04_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q04_c_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q04_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_s16_22_q04_c",
        "display_order": 5,
        "question_text": "A distant star is moving away from a stationary observer.\nState the effect of the motion on the light observed from the star.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "A distant star is moving away from a stationary observer.\nState the effect of the motion on the light observed from the star.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q04_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q04_c_ii_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q04_d",
        "path": [
          "d"
        ],
        "label": "(d)",
        "parent_id": null,
        "display_order": 6,
        "question_text": "A car travels at a constant speed towards a stationary observer. The horn of the car sounds at\na frequency of 510 Hz and the observer hears a frequency of 550 Hz. The speed of sound in\nair is 340 m s⁻¹.\nCalculate the speed of the car.\nspeed = m s⁻¹",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "A car travels at a constant speed towards a stationary observer. The horn of the car sounds at\na frequency of 510 Hz and the observer hears a frequency of 550 Hz. The speed of sound in\nair is 340 m $s^{-1}$.\nCalculate the speed of the car.\n$speed = m s^{-1} $",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q04_d_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q04_d_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q04_d_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "speed",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_22_q04_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q04_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q04_c"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q04_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q04_c_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q04_d"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_22/question_04.png",
    "prototype_paper": "9702_s16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_22.pdf",
      "paper_code": "9702_s16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 22,
      "question_id": "9702_s16_22_q04",
      "question_num": 4,
      "total_marks": 10,
      "parts": [
        {
          "id": "9702_s16_22_q04_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q04_a_mp01",
              "text": "longitudinal: vibrations/oscillations (of the particles/wave) are parallel to the direction or in the same direction (of the propagation of energy)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q04_a_mp02",
              "text": "transverse: vibrations/oscillations (of the particles/wave) are perpendicular to the direction (of the propagation of energy)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q04_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_22_q04_b_mp01",
              "text": "LHS: intensity = power / area units: kg m s–2 × m × s–1 × m–2 or kg m2 s–3 × m–2",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q04_b_mp02",
              "text": "RHS: units: m s–1 × kg m–3 × s–2 × m2",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q04_b_mp03",
              "text": "LHS and RHS both kg s–3",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q04_c_i",
          "label": "(c)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q04_c_i_mp01",
              "text": "change/difference in the observed/apparent frequency when the source is moving (relative to the observer)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q04_c_ii",
          "label": "(c)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q04_c_ii_mp01",
              "text": "wavelength increases/frequency decreases/red shift",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q04_d",
          "label": "(d)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_22_q04_d_mp01",
              "text": "observed frequency = vfS / (v – vS)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q04_d_mp02",
              "text": "550 = (340 × 510) / (340 – vS)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q04_d_mp03",
              "text": "vS = 25 (24.7) m s–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_22_q05",
    "source_filename": "9702_s16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 22,
    "paper_code": "9702_s16_22",
    "metadata_confidence": 1,
    "question_num": 5,
    "source_pages": [
      11
    ],
    "total_marks": 6,
    "detected_part_marks": 6,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_05.png",
    "question_image_with_figures": "question_05_with_figures.png",
    "question_text_file": "question_05.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_5_1",
        "label": "Fig. 5.1",
        "file": "figure_5_1.png",
        "introduced_by": "9702_s16_22_q05_b",
        "referenced_by": [
          "9702_s16_22_q05_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_22_q05_b",
          "position": "after_text",
          "anchor": "The diffraction grating illustrated in Fig. 5.1 is used with light of wavelength 486 nm."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_22/figure_5_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_22_q05_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Light of a single wavelength is incident on a diffraction grating. Explain the part played by\ndiffraction and interference in the production of the first order maximum by the diffraction\ngrating.",
        "marks": 3,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Light of a single wavelength is incident on a diffraction grating. Explain the part played by\ndiffraction and interference in the production of the first order maximum by the diffraction\ngrating.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q05_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q05_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q05_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "The diffraction grating illustrated in Fig. 5.1 is used with light of wavelength 486 nm.\nThe orders of the maxima produced are shown on the screen in Fig. 5.1. The angle between\nthe two second order maxima is 59.4°.\nCalculate the number of lines per millimetre of the grating.\nnumber of lines per millimetre = mm⁻¹",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_5_1"
        ],
        "figure_references": [
          "Fig. 5.1"
        ],
        "question_text_latex": "The diffraction grating illustrated in Fig. 5.1 is used with light of wavelength 486 nm.\nThe orders of the maxima produced are shown on the screen in Fig. 5.1. The angle between\nthe two second order maxima is 59.4°.\nCalculate the number of lines per millimetre of the grating.\nnumber of lines per millimetre = mm^{-1}",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q05_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q05_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q05_b_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "number of lines per millimetre",
                  "unit": "mm⁻¹",
                  "unit_latex": "\\mathrm{mm^{-1}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_22_q05_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q05_b"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_22/question_05_with_figures.png",
    "prototype_paper": "9702_s16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_22.pdf",
      "paper_code": "9702_s16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 22,
      "question_id": "9702_s16_22_q05",
      "question_num": 5,
      "total_marks": 6,
      "parts": [
        {
          "id": "9702_s16_22_q05_a",
          "label": "(a)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_22_q05_a_mp01",
              "text": "diffraction: spreading/diverging of waves/light (takes place) at (each) slit/ element/gap/aperture",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q05_a_mp02",
              "text": "interference: overlapping of waves (from coherent sources at each element)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q05_a_mp03",
              "text": "path difference λ/phase difference of 360(°)/2π (produces the first order)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q05_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_22_q05_b_mp01",
              "text": "d sinθ = nλ or sinθ = Nnλ",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q05_b_mp02",
              "text": "d = (2 × 486 × 10–9) / sin 29.7° (= 1.962 × 10–6)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q05_b_mp03",
              "text": "number of lines = 510 (509.7) mm–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 22"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_22_q06",
    "source_filename": "9702_s16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 22,
    "paper_code": "9702_s16_22",
    "metadata_confidence": 1,
    "question_num": 6,
    "source_pages": [
      13
    ],
    "total_marks": 5,
    "detected_part_marks": 5,
    "marks_validation_passed": true,
    "question_stem": "Two parallel vertical metal plates are connected to a power supply, as shown in Fig. 6.1.\nThe separation of the plates is 16 mm.",
    "question_stem_latex": "Two parallel vertical metal plates are connected to a power supply, as shown in Fig. 6.1.\nThe separation of the plates is 16 mm.",
    "question_image": "question_06.png",
    "question_image_with_figures": "question_06_with_figures.png",
    "question_text_file": "question_06.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_6_1",
        "label": "Fig. 6.1",
        "file": "figure_6_1.png",
        "introduced_by": "9702_s16_22_q06_a",
        "referenced_by": [
          "9702_s16_22_q06_a"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_22_q06_a",
          "position": "response_background"
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_22/figure_6_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_22_q06_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "On Fig. 6.1, draw at least six field lines to represent the electric field between the plates.",
        "marks": 1,
        "answer_type": "drawing",
        "answer_type_confidence": 0.95,
        "unit": null,
        "figure_ids": [
          "fig_6_1"
        ],
        "figure_references": [
          "Fig. 6.1"
        ],
        "question_text_latex": "On Fig. 6.1, draw at least six field lines to represent the electric field between the plates.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_6_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q06_a_block_01",
              "type": "canvas",
              "mode": "draw_on_scaffold",
              "background_figure_id": "fig_6_1",
              "tools": [
                "line",
                "arrow"
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q06_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "An α-particle travels in a vacuum between the two plates.\nThe electric field does work on the α-particle. The gain in kinetic energy of the α-particle is\n15 keV.\nCalculate the electric field strength between the plates.\nelectric field strength = V m⁻¹",
        "marks": 4,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "An α-particle travels in a vacuum between the two plates.\nThe electric field does work on the α-particle. The gain in kinetic energy of the α-particle is\n15 keV.\nCalculate the electric field strength between the plates.\n$electric field strength = V m^{-1} $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_6_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q06_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q06_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q06_b_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "electric field strength",
                  "unit": "V m⁻¹",
                  "unit_latex": "\\mathrm{V\\,m^{-1}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "stem"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q06_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q06_b"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_22/question_06_with_figures.png",
    "prototype_paper": "9702_s16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_22.pdf",
      "paper_code": "9702_s16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 22,
      "question_id": "9702_s16_22_q06",
      "question_num": 6,
      "total_marks": 5,
      "parts": [
        {
          "id": "9702_s16_22_q06_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q06_a_mp01",
              "text": "at least six horizontal lines equally spaced and arrow to the right",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q06_b",
          "label": "(b)",
          "marks": 4,
          "marking_points": [
            {
              "id": "9702_s16_22_q06_b_mp01",
              "text": "charge used 2e",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q06_b_mp02",
              "text": "gain in KE = 15 × 1.6 × 10–19 × 103 = 2 × 1.6 × 10–19 × V (p.d.across plates) or F (= W / d) = 15 × 1.6 × 10–19 × 103 / 16 × 10–3",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q06_b_mp03",
              "text": "(hence V = 7500 V or F = 1.5 × 10–13 N) E = V / d or E = F / Q",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q06_b_mp04",
              "text": "E = (7500 / 16 × 10–3) or E = (1.5 × 10–13 / 3.2 × 10–19) E = 4.7 × 105 (468 750) V m–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or KE (= ½mv2) = 15 × 103 × 1.6 × 10–19 v = [(2 × 15 × 103 × 1.6 × 10–19) / (6.68 × 10–27)]1/2 = 8.5 × 105 m s–1",
            "6(C1) a (= v2 / 2s) = (8.5 × 105)2 / 2 × 16 × 10–3 = 2.25 × 1013 m s–2 F (= 6.68 × 10–27 × 2.25 × 10–13) = 1.5 × 10–13 N E = F / Q",
            "Q = 2e",
            "E = 4.7 × 105 V m–1",
            "6(A1) 9702 22"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_22_q07",
    "source_filename": "9702_s16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 22,
    "paper_code": "9702_s16_22",
    "metadata_confidence": 1,
    "question_num": 7,
    "source_pages": [
      14,
      15
    ],
    "total_marks": 10,
    "detected_part_marks": 10,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_07.png",
    "question_image_with_figures": "question_07_with_figures.png",
    "question_text_file": "question_07.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_7_1",
        "label": "Fig. 7.1",
        "file": "figure_7_1.png",
        "introduced_by": "9702_s16_22_q07_b",
        "referenced_by": [
          "9702_s16_22_q07_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_22_q07_b",
          "position": "after_text",
          "anchor": "A battery of electromotive force (e.m.f.) 9.0 V and internal resistance 0.25 Ω is connected in\nseries with two identical resistors X and a resistor Y, as shown in Fig. 7.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_22/figure_7_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_22_q07_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Electric current is a flow of charge carriers. The charge on the carriers is quantised. Explain\nwhat is meant by quantised.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Electric current is a flow of charge carriers. The charge on the carriers is quantised. Explain\nwhat is meant by quantised.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q07_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q07_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q07_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A battery of electromotive force (e.m.f.) 9.0 V and internal resistance 0.25 Ω is connected in\nseries with two identical resistors X and a resistor Y, as shown in Fig. 7.1.\nThe resistance of each resistor X is 0.15 Ω and the resistance of resistor Y is 2.7 Ω.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_7_1"
        ],
        "figure_references": [
          "Fig. 7.1"
        ],
        "question_text_latex": "A battery of electromotive force (e.m.f.) 9.0 V and internal resistance 0.25 $\\Omega$ is connected in\nseries with two identical resistors X and a resistor Y, as shown in Fig. 7.1.\nThe resistance of each resistor X is 0.15 $\\Omega$ and the resistance of resistor Y is 2.7 $\\Omega$.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_22_q07_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_22_q07_b",
        "display_order": 3,
        "question_text": "Show that the current in the circuit is 2.8 A.",
        "marks": 3,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the current in the circuit is 2.8 A.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_7_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q07_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q07_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q07_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_22_q07_b",
        "display_order": 4,
        "question_text": "Calculate the potential difference across the battery.\npotential difference = V",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "V",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the potential difference across the battery.\n$potential difference = V $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_7_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_s16_22_q07_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q07_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q07_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q07_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "potential difference",
                  "unit": "V",
                  "unit_latex": "\\mathrm{V}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q07_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "Each resistor X connected in the circuit in (b) is made from a wire with a cross-sectional area\nof 2.5 mm². The number of free electrons per unit volume in the wire is 8.5 × 10²⁹ m⁻³.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Each resistor X connected in the circuit in (b) is made from a wire with a cross-sectional area\nof 2.5 mm^{2}. The number of free electrons per unit volume in the wire is $8.5 \\times 10^{29}\\,\\mathrm{m}^{-3}$.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_22_q07_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_s16_22_q07_c",
        "display_order": 6,
        "question_text": "Calculate the average drift speed of the electrons in X.\ndrift speed = m s⁻¹",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the average drift speed of the electrons in X.\n$drift speed = m s^{-1} $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_s16_22_q07_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q07_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q07_c_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_22_q07_c_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "drift speed",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_22_q07_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_s16_22_q07_c",
        "display_order": 7,
        "question_text": "The two resistors X are replaced by two resistors Z made of the same material and\nlength but with half the diameter.\nDescribe and explain the difference between the average drift speed in Z and that in X.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The two resistors X are replaced by two resistors Z made of the same material and\nlength but with half the diameter.\nDescribe and explain the difference between the average drift speed in Z and that in X.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_s16_22_q07_c_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_22_q07_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_22_q07_c_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_22_q07_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q07_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q07_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q07_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q07_c"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q07_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_22_q07_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_22/question_07_with_figures.png",
    "prototype_paper": "9702_s16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_22.pdf",
      "paper_code": "9702_s16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 22,
      "question_id": "9702_s16_22_q07",
      "question_num": 7,
      "total_marks": 10,
      "parts": [
        {
          "id": "9702_s16_22_q07_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_22_q07_a_mp01",
              "text": "charge exists only in discrete amounts",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q07_b_i",
          "label": "(b)(i)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_22_q07_b_i_mp01",
              "text": "E = I(R + r) or V = IR",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q07_b_i_mp02",
              "text": "(total resistance =) 2.7 + 0.30 + 0.25 (= 3.25 Ω)",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q07_b_i_mp03",
              "text": "I = 9.0 / (2.7 + 0.30 + 0.25) or 9.0 / 3.25 = 2.8 A",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q07_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q07_b_ii_mp01",
              "text": "V = IRext",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q07_b_ii_mp02",
              "text": "7(C1) = 9.0 – 2.77 × 0.25 or 9.0 – 2.8 × 0.25 V = 8.3 (8.31) V or 8.4 V",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "= 2.77 × 3.0 or 2.8 × 3.0 or V = E – Ir"
          ]
        },
        {
          "id": "9702_s16_22_q07_c_i",
          "label": "(c)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q07_c_i_mp01",
              "text": "I = nevA v = 2.77 / (8.5 × 1029 × 1.6 × 10–19 × 2.5 × 10–6)",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q07_c_i_mp02",
              "text": "= 8.1 (8.147) × 10–6 m s–1 or 8.2 × 10–6 m s–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_22_q07_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_22_q07_c_ii_mp01",
              "text": "A reduces by a factor 4 (1/4 less) or resistance of Z goes up by 4×",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_22_q07_c_ii_mp02",
              "text": "current goes down but by less than a factor of 4 (as total resistance does not go up by a factor of 4) so drift speed goes up",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_23_q02",
    "source_filename": "9702_s16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 23,
    "paper_code": "9702_s16_23",
    "metadata_confidence": 1,
    "question_num": 2,
    "source_pages": [
      5
    ],
    "total_marks": 4,
    "detected_part_marks": 4,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_02.png",
    "question_image_with_figures": null,
    "question_text_file": "question_02.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_s16_23_q02_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Describe the effects, one in each case, of systematic errors and random errors when using a\nmicrometer screw gauge to take readings for the diameter of a wire.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Describe the effects, one in each case, of systematic errors and random errors when using a\nmicrometer screw gauge to take readings for the diameter of a wire.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q02_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q02_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q02_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "Distinguish between precision and accuracy when measuring the diameter of a wire.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Distinguish between precision and accuracy when measuring the diameter of a wire.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q02_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q02_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_23_q02_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q02_b"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_23/question_02.png",
    "prototype_paper": "9702_s16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_23.pdf",
      "paper_code": "9702_s16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 23,
      "question_id": "9702_s16_23_q02",
      "question_num": 2,
      "total_marks": 4,
      "parts": [
        {
          "id": "9702_s16_23_q02_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q02_a_mp01",
              "text": "systematic: the reading is larger or smaller than (or varying from) the true reading by a constant amount",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q02_a_mp02",
              "text": "random: scatter in readings about the true reading",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q02_b",
          "label": "(b)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q02_b_mp01",
              "text": "precision: the size of the smallest division (on the measuring instrument) or 0.01 mm for the micrometer",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q02_b_mp02",
              "text": "accuracy: how close (diameter) value is to the true (diameter) value",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_23_q03",
    "source_filename": "9702_s16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 23,
    "paper_code": "9702_s16_23",
    "metadata_confidence": 1,
    "question_num": 3,
    "source_pages": [
      6,
      7,
      8
    ],
    "total_marks": 12,
    "detected_part_marks": 12,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_03.png",
    "question_image_with_figures": "question_03_with_figures.png",
    "question_text_file": "question_03.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_3_1",
        "label": "Fig. 3.1",
        "file": "figure_3_1.png",
        "introduced_by": "9702_s16_23_q03_b",
        "referenced_by": [
          "9702_s16_23_q03_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_23_q03_b",
          "position": "after_text",
          "anchor": "as illustrated in Fig. 3.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_23/figure_3_1.png"
      },
      {
        "id": "fig_3_2",
        "label": "Fig. 3.2",
        "file": "figure_3_2.png",
        "introduced_by": "9702_s16_23_q03_b",
        "referenced_by": [
          "9702_s16_23_q03_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_23_q03_b",
          "position": "after_text",
          "anchor": "The variation with time t of the velocity v of the ball as it falls from A to B is shown in Fig. 3.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_23/figure_3_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_23_q03_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Explain what is meant by gravitational potential energy and by kinetic energy.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Explain what is meant by gravitational potential energy and by kinetic energy.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q03_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q03_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q03_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A motion sensor is used to measure the velocity of a ball falling vertically towards the ground,\nas illustrated in Fig. 3.1.\nThe ball passes through points A and B as it falls. The ball has a mass of 1.5 kg.\nThe variation with time t of the velocity v of the ball as it falls from A to B is shown in Fig. 3.2.\nUse Fig. 3.2 to calculate, for the ball falling from A to B,",
        "marks": null,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_3_1",
          "fig_3_2"
        ],
        "figure_references": [
          "Fig. 3.1",
          "Fig. 3.2"
        ],
        "question_text_latex": "A motion sensor is used to measure the velocity of a ball falling vertically towards the ground,\nas illustrated in Fig. 3.1.\nThe ball passes through points A and B as it falls. The ball has a mass of 1.5 kg.\nThe variation with time t of the velocity v of the ball as it falls from A to B is shown in Fig. 3.2.\nUse Fig. 3.2 to calculate, for the ball falling from A to B,",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_23_q03_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_23_q03_b",
        "display_order": 3,
        "question_text": "the displacement,\ndisplacement = m",
        "marks": 3,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the displacement,\n$displacement = m $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q03_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q03_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q03_b_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "displacement",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q03_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_23_q03_b",
        "display_order": 4,
        "question_text": "the acceleration,",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the acceleration,",
        "marks_source": "reconciled_from_printed_total",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q03_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q03_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q03_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "acceleration",
                  "unit": "m s⁻²",
                  "unit_latex": "\\mathrm{m\\,s^{-2}}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q03_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_s16_23_q03_b",
        "display_order": 5,
        "question_text": "the change in kinetic energy.\nchange in kinetic energy = J",
        "marks": 3,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": "J",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the change in kinetic energy.\nchange in kinetic energy = J",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q03_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q03_b_iii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q03_b_iii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "change in kinetic energy",
                  "unit": "J",
                  "unit_latex": "\\mathrm{J}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q03_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 6,
        "question_text": "Show that the work done by the gravitational field on the ball in (b) as it moves from A to B is\nequal to the change in kinetic energy.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the work done by the gravitational field on the ball in (b) as it moves from A to B is\nequal to the change in kinetic energy.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_s16_23_q03_b_i"
          },
          {
            "type": "previous_response",
            "part_id": "9702_s16_23_q03_b_iii"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q03_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q03_c_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_23_q03_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q03_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q03_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q03_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q03_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q03_c"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_23/question_03_with_figures.png",
    "prototype_paper": "9702_s16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_23.pdf",
      "paper_code": "9702_s16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 23,
      "question_id": "9702_s16_23_q03",
      "question_num": 3,
      "total_marks": 12,
      "parts": [
        {
          "id": "9702_s16_23_q03_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q03_a_mp01",
              "text": "(gravitational potential energy is) the energy/ability to do work of a mass that it has or is stored due to its position/height in a gravitational field",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q03_a_mp02",
              "text": "kinetic energy is energy/ability to do work a object/body/mass has due to its speed/velocity/motion/movement",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q03_b_i",
          "label": "(b)(i)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q03_b_i_mp01",
              "text": "s = [(u + v) t] / 2 or acceleration = 9.8/9.75 (using gradient)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q03_b_i_mp02",
              "text": "= [(7.8 + 3.9) × 0.4] / 2 or s = 3.9 × 0.4 + 1 2 × 9.75 × (0.4)2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q03_b_i_mp03",
              "text": "s = 2.3(4) m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q03_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q03_b_ii_mp01",
              "text": "a = (v – u) / t or gradient of line",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q03_b_ii_mp02",
              "text": "= (7.8 – 3.9) / 0.4 = 9.8 (9.75) m s–2 (allow ± 1 2 small square in readings)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 23"
          ]
        },
        {
          "id": "9702_s16_23_q03_b_iii",
          "label": "(b)(iii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q03_b_iii_mp01",
              "text": "KE = 1 2 mv2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q03_b_iii_mp02",
              "text": "change in kinetic energy = 1 2 mv2 – 1 2 mu2 = 1 2 × 1.5 × (7.82 – 3.92)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q03_b_iii_mp03",
              "text": "= 34 (34.22) J",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q03_c",
          "label": "(c)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q03_c_mp01",
              "text": "work done = force × distance (moved) or Fd or Fx or mgh or mgd or mgx",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q03_c_mp02",
              "text": "= 1.5 × 9.8 × 2.3 = 34 (33.8) J (equals the change in KE)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_23_q04",
    "source_filename": "9702_s16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 23,
    "paper_code": "9702_s16_23",
    "metadata_confidence": 1,
    "question_num": 4,
    "source_pages": [
      9
    ],
    "total_marks": 4,
    "detected_part_marks": 4,
    "marks_validation_passed": true,
    "question_stem": "A spring balance is used to weigh a cylinder that is immersed in oil, as shown in Fig. 4.1.\nThe reading on the spring balance is 4.8 N. The length of the cylinder is 5.0 cm and the cross-\nsectional area of the cylinder is 13 cm². The weight of the cylinder is 5.3 N.",
    "question_stem_latex": "A spring balance is used to weigh a cylinder that is immersed in oil, as shown in Fig. 4.1.\nThe reading on the spring balance is $4.8\\,\\mathrm{N}$. The length of the cylinder is $5.0\\,\\mathrm{cm}$ and the cross-\nsectional area of the cylinder is $13\\,\\mathrm{cm^2}$. The weight of the cylinder is $5.3\\,\\mathrm{N}$.",
    "question_image": "question_04.png",
    "question_image_with_figures": "question_04_with_figures.png",
    "question_text_file": "question_04.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_4_1",
        "label": "Fig. 4.1",
        "file": "figure_4_1.png",
        "introduced_by": null,
        "referenced_by": [],
        "mapping_method": "caption_proximity",
        "mapping_confidence": 0.6,
        "placement": {
          "scope": "question",
          "position": "after_stem_text",
          "anchor": "A spring balance is used to weigh a cylinder that is immersed in oil, as shown in Fig. 4.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_23/figure_4_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_23_q04_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "The cylinder is in equilibrium when it is immersed in the oil. Explain this in terms of the forces\nacting on the cylinder.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The cylinder is in equilibrium when it is immersed in the oil. Explain this in terms of the forces\nacting on the cylinder.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q04_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q04_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q04_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "Calculate the density of the oil.\ndensity = kg m⁻³",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the density of the oil.\n$density = kg m^{-3} $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q04_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q04_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q04_b_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "density",
                  "unit": "kg m⁻³",
                  "unit_latex": "\\mathrm{kg\\,m^{-3}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [
      "figure_without_explicit_part_reference"
    ],
    "human_review_status": "pending",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "stem"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q04_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q04_b"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_23/question_04_with_figures.png",
    "prototype_paper": "9702_s16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_23.pdf",
      "paper_code": "9702_s16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 23,
      "question_id": "9702_s16_23_q04",
      "question_num": 4,
      "total_marks": 4,
      "parts": [
        {
          "id": "9702_s16_23_q04_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_23_q04_a_mp01",
              "text": "(resultant force = 0) (equilibrium) therefore: weight – upthrust = force from thin wire (allow tension in wire) or 5.3 (N) – upthrust = 4.8 (N)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q04_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q04_b_mp01",
              "text": "difference in weight = upthrust or upthrust = 0.5 (N) 0.5 = ρghA or m = 0.5 / 9.81 and V = 5.0 × 13 × 10–6 (m3)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q04_b_mp02",
              "text": "ρ = 0.5 / (9.81 × 5.0 × 13 × 10–6)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q04_b_mp03",
              "text": "= 780 (784) kg m–3",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_23_q05",
    "source_filename": "9702_s16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 23,
    "paper_code": "9702_s16_23",
    "metadata_confidence": 1,
    "question_num": 5,
    "source_pages": [
      10,
      11
    ],
    "total_marks": 9,
    "detected_part_marks": 9,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_05.png",
    "question_image_with_figures": "question_05_with_figures.png",
    "question_text_file": "question_05.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_5_1",
        "label": "Fig. 5.1",
        "file": "figure_5_1.png",
        "introduced_by": "9702_s16_23_q05_b",
        "referenced_by": [
          "9702_s16_23_q05_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_23_q05_b",
          "position": "after_text",
          "anchor": "Two particles A and B collide elastically, as illustrated in Fig. 5.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_23/figure_5_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_23_q05_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State the law of conservation of momentum.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the law of conservation of momentum.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q05_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q05_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q05_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "Two particles A and B collide elastically, as illustrated in Fig. 5.1.\nThe initial velocity of A is 500 m s⁻¹ in the x-direction and B is at rest.\nThe velocity of A after the collision is vₐ at 60° to the x-direction. The velocity of B after the\ncollision is vᵦ at 30° to the x-direction.\nThe mass m of each particle is 1.67 × 10⁻²⁷ kg.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_5_1"
        ],
        "figure_references": [
          "Fig. 5.1"
        ],
        "question_text_latex": "Two particles A and B collide elastically, as illustrated in Fig. 5.1.\nThe initial velocity of A is $500\\,\\mathrm{m\\,s^{-1}}$ in the $x$-direction and B is at rest.\nThe velocity of A after the collision is $v_A$ at $60^\\circ$ to the $x$-direction. The velocity of B after the\ncollision is $v_B$ at $30^\\circ$ to the $x$-direction.\nThe mass $m$ of each particle is $1.67 \\times 10^{-27}\\,\\mathrm{kg}$.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_23_q05_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_23_q05_b",
        "display_order": 3,
        "question_text": "Explain what is meant by the particles colliding elastically.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Explain what is meant by the particles colliding elastically.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q05_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q05_b_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q05_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_23_q05_b",
        "display_order": 4,
        "question_text": "Calculate the total initial momentum of A and B.\nmomentum = N s",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N s",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the total initial momentum of A and B.\n$momentum = N s $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q05_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q05_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q05_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "momentum",
                  "unit": "N s",
                  "unit_latex": "\\mathrm{N\\,s}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q05_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_s16_23_q05_b",
        "display_order": 5,
        "question_text": "State an expression in terms of m, vₐ and vᵦ for the total momentum of A and B after the\ncollision\n1. in the x-direction,\n2. in the y-direction.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State an expression in terms of m, $v_{\\mathrm{A}}$ and $v_{\\mathrm{B}}$ for the total momentum of A and B after the\ncollision\n1. in the x-direction,\n2. in the y-direction.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q05_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q05_b_iii_field_01",
                  "required": true,
                  "control": "math_expression",
                  "role": "equation",
                  "label": "x-direction"
                },
                {
                  "field_id": "9702_s16_23_q05_b_iii_field_02",
                  "required": true,
                  "control": "math_expression",
                  "role": "equation",
                  "label": "y-direction"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q05_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_s16_23_q05_b",
        "display_order": 6,
        "question_text": "Calculate the magnitudes of the velocities vₐ and vᵦ after the collision.",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the magnitudes of the velocities $v_{\\mathrm{A}}$ and $v_{\\mathrm{B}}$ after the collision.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q05_b_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q05_b_iv_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q05_b_iv_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "v_A",
                  "label_latex": "v_A",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}"
                },
                {
                  "field_id": "9702_s16_23_q05_b_iv_field_03",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "v_B",
                  "label_latex": "v_B",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_23_q05_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q05_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q05_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q05_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q05_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q05_b_iv"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_23/question_05_with_figures.png",
    "prototype_paper": "9702_s16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_23.pdf",
      "paper_code": "9702_s16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 23,
      "question_id": "9702_s16_23_q05",
      "question_num": 5,
      "total_marks": 9,
      "parts": [
        {
          "id": "9702_s16_23_q05_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q05_a_mp01",
              "text": "the total momentum of a system (of colliding particles) remains constant",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q05_a_mp02",
              "text": "provided there is no resultant external force acting on the system/ isolated or closed system",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q05_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_23_q05_b_i_mp01",
              "text": "the total kinetic energy before (the collision) is equal to the total kinetic energy after (the collision)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q05_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_23_q05_b_ii_mp01",
              "text": "p (= mv = 1.67 × 10–27 × 500) = 8.4 (8.35) × 10–25 N s",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q05_b_iii",
          "label": "(b)(iii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q05_b_iii_mp01",
              "text": "1. mvA cos 60° + mvB cos 30° or m(vA 2 + vB 2)1/2",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q05_b_iii_mp02",
              "text": "2. mvA sin 60° + mvB sin 30°",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q05_b_iv",
          "label": "(b)(iv)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q05_b_iv_mp01",
              "text": "8.35 × 10–25 or 500m = mvA cos 60° + mvB cos 30° and 0 = mvA sin 60° + mvB sin 30° or using a vector triangle",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q05_b_iv_mp02",
              "text": "vA = 250 m s–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q05_b_iv_mp03",
              "text": "vB = 430 (433) m s–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 23"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_23_q06",
    "source_filename": "9702_s16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 23,
    "paper_code": "9702_s16_23",
    "metadata_confidence": 1,
    "question_num": 6,
    "source_pages": [
      12,
      13
    ],
    "total_marks": 10,
    "detected_part_marks": 10,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_06.png",
    "question_image_with_figures": "question_06_with_figures.png",
    "question_text_file": "question_06.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_6_1",
        "label": "Fig. 6.1",
        "file": "figure_6_1.png",
        "introduced_by": "9702_s16_23_q06_b",
        "referenced_by": [
          "9702_s16_23_q06_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_23_q06_b",
          "position": "after_text",
          "anchor": "shown in Fig. 6.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_23/figure_6_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_23_q06_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define the ohm.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define the ohm.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q06_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q06_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q06_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A 15 V battery with negligible internal resistance is connected to two resistors P and Q, as\nshown in Fig. 6.1.\nThe resistors are made of wires of the same material. The wire of P has diameter d and\nlength 2l. The wire of Q has diameter 2d and length l.\nThe resistance of P is 12 Ω.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_6_1"
        ],
        "figure_references": [
          "Fig. 6.1"
        ],
        "question_text_latex": "A 15 V battery with negligible internal resistance is connected to two resistors P and Q, as\nshown in Fig. 6.1.\nThe resistors are made of wires of the same material. The wire of P has diameter d and\nlength 2l. The wire of Q has diameter 2d and length l.\nThe resistance of P is 12 $\\Omega$.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_23_q06_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_23_q06_b",
        "display_order": 3,
        "question_text": "Show that the resistance of Q is 1.5 Ω.",
        "marks": 3,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the resistance of Q is 1.5 $\\Omega$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_6_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q06_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q06_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q06_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_23_q06_b",
        "display_order": 4,
        "question_text": "Calculate the total power dissipated in the resistors P and Q.\npower = W",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "W",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the total power dissipated in the resistors P and Q.\n$power = W $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_6_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_s16_23_q06_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q06_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q06_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q06_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "power",
                  "unit": "W",
                  "unit_latex": "\\mathrm{W}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q06_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_s16_23_q06_b",
        "display_order": 5,
        "question_text": "Determine the ratio\naverage drift speed of the charge carriers in P / average drift speed of the charge carriers in Q.\nratio =",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the ratio $\\frac{\\text{average drift speed of the charge carriers in P}}{\\text{average drift speed of the charge carriers in Q}}$.\n$\\text{ratio} =$",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_6_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_s16_23_q06_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q06_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q06_b_iii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q06_b_iii_field_02",
                  "required": true,
                  "control": "number",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_23_q06_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q06_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q06_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q06_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q06_b_iii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_23/question_06_with_figures.png",
    "prototype_paper": "9702_s16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_23.pdf",
      "paper_code": "9702_s16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 23,
      "question_id": "9702_s16_23_q06",
      "question_num": 6,
      "total_marks": 10,
      "parts": [
        {
          "id": "9702_s16_23_q06_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_23_q06_a_mp01",
              "text": "ohm is volt per ampere or volt / ampere",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q06_b_i",
          "label": "(b)(i)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q06_b_i_mp01",
              "text": "R = ρl / A",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q06_b_i_mp02",
              "text": "RP = 4ρ(2l) / πd2 or 8ρl / πd2 or RQ = ρl / πd2 or ratio idea e.g. length is halved hence R halved and diameter is halved hence R is 1/4",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q06_b_i_mp03",
              "text": "RQ (= 4ρl / π4d2) = ρl / πd2 = RP / 8 (= 12 / 8) = 1.5 Ω",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q06_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q06_b_ii_mp01",
              "text": "power = I 2R or V 2 / R or VI",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q06_b_ii_mp02",
              "text": "= (1.25)2 × 12 + (10)2 × 1.5 or (15)2/12 + (15)2/1.5 or 15 × 11.25",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q06_b_ii_mp03",
              "text": "= (18.75 + 150 =) 170 (168.75) W",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q06_b_iii",
          "label": "(b)(iii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q06_b_iii_mp01",
              "text": "IP = (15 / 12 =) 1.25 (A) and IQ = (15 / 1.5 =) 10 (A)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q06_b_iii_mp02",
              "text": "vP / vQ = IPnAQe / IQnAPe or (1.25 × πd 2) / (10 × πd 2/4)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q06_b_iii_mp03",
              "text": "= 0.5",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_23_q07",
    "source_filename": "9702_s16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 23,
    "paper_code": "9702_s16_23",
    "metadata_confidence": 1,
    "question_num": 7,
    "source_pages": [
      14,
      15
    ],
    "total_marks": 6,
    "detected_part_marks": 6,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_07.png",
    "question_image_with_figures": "question_07_with_figures.png",
    "question_text_file": "question_07.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_7_1",
        "label": "Fig. 7.1",
        "file": "figure_7_1.png",
        "introduced_by": "9702_s16_23_q07_a",
        "referenced_by": [
          "9702_s16_23_q07_a"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_23_q07_a",
          "position": "after_text",
          "anchor": "Apparatus used to produce stationary waves on a stretched string is shown in Fig. 7.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_23/figure_7_1.png"
      },
      {
        "id": "fig_7_2",
        "label": "Fig. 7.2",
        "file": "figure_7_2.png",
        "introduced_by": "9702_s16_23_q07_b",
        "referenced_by": [
          "9702_s16_23_q07_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_s16_23_q07_b",
          "position": "after_text",
          "anchor": "by a second wave S is also shown in Fig. 7.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_s16_qp_23/figure_7_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_s16_23_q07_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Apparatus used to produce stationary waves on a stretched string is shown in Fig. 7.1.\nThe frequency generator is switched on.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_7_1"
        ],
        "figure_references": [
          "Fig. 7.1"
        ],
        "question_text_latex": "Apparatus used to produce stationary waves on a stretched string is shown in Fig. 7.1.\nThe frequency generator is switched on.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_23_q07_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_s16_23_q07_a",
        "display_order": 2,
        "question_text": "Describe two adjustments that can be made to the apparatus to produce stationary\nwaves on the string.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Describe two adjustments that can be made to the apparatus to produce stationary\nwaves on the string.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_7_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q07_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q07_a_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q07_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_s16_23_q07_a",
        "display_order": 3,
        "question_text": "Describe the features that are seen on the stretched string that indicate stationary waves\nhave been produced.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Describe the features that are seen on the stretched string that indicate stationary waves\nhave been produced.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_7_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q07_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q07_a_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q07_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "The variation with time t of the displacement x of a particle caused by a progressive wave R is\nshown in Fig. 7.2. For the same particle, the variation with time t of the displacement x caused\nby a second wave S is also shown in Fig. 7.2.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_7_2"
        ],
        "figure_references": [
          "Fig. 7.2"
        ],
        "question_text_latex": "The variation with time t of the displacement x of a particle caused by a progressive wave R is\nshown in Fig. 7.2. For the same particle, the variation with time t of the displacement x caused\nby a second wave S is also shown in Fig. 7.2.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_23_q07_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_s16_23_q07_b",
        "display_order": 5,
        "question_text": "Determine the phase difference between wave R and wave S. Include an appropriate\nunit.\nphase difference =",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the phase difference between wave R and wave S. Include an appropriate\nunit.\n$phase difference = $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_7_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q07_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q07_b_i_field_01",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "phase difference",
                  "unit": "°",
                  "unit_latex": "^\\circ"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q07_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_s16_23_q07_b",
        "display_order": 6,
        "question_text": "Calculate the ratio\nintensity of wave R / intensity of wave S.\nratio =",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the ratio $\\frac{\\text{intensity of wave R}}{\\text{intensity of wave S}}$.\n$\\text{ratio} =$",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_7_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q07_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q07_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_s16_23_q07_b_ii_field_02",
                  "required": true,
                  "control": "number",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_23_q07_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q07_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q07_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q07_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q07_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q07_b_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_23/question_07_with_figures.png",
    "prototype_paper": "9702_s16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_23.pdf",
      "paper_code": "9702_s16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 23,
      "question_id": "9702_s16_23_q07",
      "question_num": 7,
      "total_marks": 6,
      "parts": [
        {
          "id": "9702_s16_23_q07_a_i",
          "label": "(a)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q07_a_i_mp01",
              "text": "alter distance from vibrator to pulley alter frequency of generator (change tension in string by) changing value of the masses any two",
              "tag": "B2",
              "marks": 2,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q07_a_ii",
          "label": "(a)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_23_q07_a_ii_mp01",
              "text": "points on string have amplitudes varying from maximum to zero/minimum",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q07_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_23_q07_b_i_mp01",
              "text": "60° or π / 3 rad",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q07_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q07_b_ii_mp01",
              "text": "ratio = [3.4 / 2.2]2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q07_b_ii_mp02",
              "text": "= 2.4 (2.39)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 23"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_s16_23_q08",
    "source_filename": "9702_s16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "May/June",
    "session_code": "s",
    "variant": 23,
    "paper_code": "9702_s16_23",
    "metadata_confidence": 1,
    "question_num": 8,
    "source_pages": [
      16
    ],
    "total_marks": 8,
    "detected_part_marks": 8,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_08.png",
    "question_image_with_figures": null,
    "question_text_file": "question_08.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_s16_23_q08_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Distinguish between an α-particle and a β⁺-particle.",
        "marks": 3,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Distinguish between an α-particle and a $β^{+}$-particle.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q08_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q08_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q08_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "State the equation that shows the decay of a particle in a nucleus that results in β⁺ emission.\nAll particles in the equation should be shown in the notation that is usually used for the\nrepresentation of nuclides.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the equation that shows the decay of a particle in a nucleus that results in $β^{+}$ emission.\nAll particles in the equation should be shown in the notation that is usually used for the\nrepresentation of nuclides.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q08_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q08_b_field_01",
                  "required": true,
                  "control": "math_expression",
                  "role": "equation"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q08_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_s16_23_q08_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_s16_23_q08_c",
        "display_order": 4,
        "question_text": "State the quark composition of\n1. a proton,\n2. a neutron.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the quark composition of\n1. a proton,\n2. a neutron.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q08_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q08_c_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "proton quark composition"
                },
                {
                  "field_id": "9702_s16_23_q08_c_i_field_02",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "neutron quark composition"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_s16_23_q08_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_s16_23_q08_c",
        "display_order": 5,
        "question_text": "Use the quark model to explain the charge on a proton.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use the quark model to explain the charge on a proton.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_s16_23_q08_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_s16_23_q08_c_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_s16_23_q08_a"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q08_b"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q08_c"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q08_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_s16_23_q08_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_s16_qp_23/question_08.png",
    "prototype_paper": "9702_s16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_s16_ms_23.pdf",
      "paper_code": "9702_s16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "May/June",
      "session_code": "s",
      "variant": 23,
      "question_id": "9702_s16_23_q08",
      "question_num": 8,
      "total_marks": 8,
      "parts": [
        {
          "id": "9702_s16_23_q08_a",
          "label": "(a)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_s16_23_q08_a_mp01",
              "text": "α-particle is 2 protons and 2 neutrons; β+-particle is positive electron/positron α-particle has charge +2e; β+-particle has +e charge α-particle has mass 4u; β-particle has mass (1/2000)u α-particle made up of hadrons; β+-particle a lepton any three",
              "tag": "B3",
              "marks": 3,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q08_b",
          "label": "(b)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q08_b_mp01",
              "text": "ν β 0 0 0 1 1 0 1 1 n p + + → all terms correct",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q08_b_mp02",
              "text": "all numerical values correct (ignore missing values on ν)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q08_c_i",
          "label": "(c)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_s16_23_q08_c_i_mp01",
              "text": "1. proton: up, up, down / uud",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_s16_23_q08_c_i_mp02",
              "text": "2. neutron: up, down, down / udd",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_s16_23_q08_c_ii",
          "label": "(c)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_s16_23_q08_c_ii_mp01",
              "text": "up quark has charge +2 / 3 (e) and down quark has charge –1 / 3 (e) total is +1(e)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_21_q01",
    "source_filename": "9702_w16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 21,
    "paper_code": "9702_w16_21",
    "metadata_confidence": 1,
    "question_num": 1,
    "source_pages": [
      5
    ],
    "total_marks": 5,
    "detected_part_marks": 5,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_01.png",
    "question_image_with_figures": "question_01_with_figures.png",
    "question_text_file": "question_01.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_1_1",
        "label": "Fig. 1.1",
        "file": "figure_1_1.png",
        "introduced_by": "9702_w16_21_q01_b",
        "referenced_by": [
          "9702_w16_21_q01_b",
          "9702_w16_21_q01_b_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_w16_21_q01_b",
          "position": "after_text",
          "anchor": "Data for the density and the mass are given in Fig. 1.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_21/figure_1_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_21_q01_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define density.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define density.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q01_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q01_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q01_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "The mass m of a metal sphere is given by the expression\nm = πd³ρ / 6\nwhere ρ is the density of the metal and d is the diameter of the sphere.\nData for the density and the mass are given in Fig. 1.1.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "The mass $m$ of a metal sphere is given by the expression\n$m = \\frac{\\pi d^3\\rho}{6}$\nwhere $\\rho$ is the density of the metal and $d$ is the diameter of the sphere.\nData for the density and the mass are given in Fig. 1.1.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_21_q01_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_21_q01_b",
        "display_order": 3,
        "question_text": "Calculate the diameter d.\nd = m",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the diameter d.\n$d = m $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q01_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q01_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q01_b_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "d",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q01_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_21_q01_b",
        "display_order": 4,
        "question_text": "Use your answer in (i) and the data in Fig. 1.1 to determine the value of d, with its\nabsolute uncertainty, to an appropriate number of significant figures.\nd = ± m",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "± m",
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "Use your answer in (i) and the data in Fig. 1.1 to determine the value of d, with its\nabsolute uncertainty, to an appropriate number of significant figures.\n$d = \\pm m $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_w16_21_q01_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q01_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q01_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q01_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "d",
                  "label_latex": "d",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                },
                {
                  "field_id": "9702_w16_21_q01_b_ii_field_03",
                  "required": true,
                  "control": "quantity",
                  "role": "uncertainty",
                  "label": "absolute uncertainty",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_21_q01_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q01_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q01_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q01_b_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_21/question_01_with_figures.png",
    "prototype_paper": "9702_w16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_21.pdf",
      "paper_code": "9702_w16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 21,
      "question_id": "9702_w16_21_q01",
      "question_num": 1,
      "total_marks": 5,
      "parts": [
        {
          "id": "9702_w16_21_q01_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_21_q01_a_mp01",
              "text": "(density =) mass / volume",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q01_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_21_q01_b_i_mp01",
              "text": "d = [(6 × 7.5) / (π × 8100)]1/3 = 0.12(1) m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q01_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_21_q01_b_ii_mp01",
              "text": "percentage uncertainty = (4 + 5) / 3 (= 3%) or fractional uncertainty = (0.04 + 0.05) / 3 (= 0.03)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q01_b_ii_mp02",
              "text": "absolute uncertainty (= 0.03 × 0.121) = 0.0036",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q01_b_ii_mp03",
              "text": "d = 0.121 ± 0.004 m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_21_q03",
    "source_filename": "9702_w16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 21,
    "paper_code": "9702_w16_21",
    "metadata_confidence": 1,
    "question_num": 3,
    "source_pages": [
      8,
      9
    ],
    "total_marks": 12,
    "detected_part_marks": 10,
    "marks_validation_passed": false,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_03.png",
    "question_image_with_figures": "question_03_with_figures.png",
    "question_text_file": "question_03.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_3_1",
        "label": "Fig. 3.1",
        "file": "figure_3_1.png",
        "introduced_by": "9702_w16_21_q03_b",
        "referenced_by": [
          "9702_w16_21_q03_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_w16_21_q03_b",
          "position": "after_text",
          "anchor": "The variation with compression x of the force F acting on a spring is shown in Fig. 3.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_21/figure_3_1.png"
      },
      {
        "id": "fig_3_2",
        "label": "Fig. 3.2",
        "file": "figure_3_2.png",
        "introduced_by": "9702_w16_21_q03_b",
        "referenced_by": [
          "9702_w16_21_q03_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_w16_21_q03_b",
          "position": "after_text",
          "anchor": "that the spring is compressed, as shown in Fig. 3.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_21/figure_3_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_21_q03_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State Hooke’s law.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State Hooke’s law.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q03_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q03_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q03_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "The variation with compression x of the force F acting on a spring is shown in Fig. 3.1.\nThe spring is fixed to the closed end of a horizontal tube. A block is pushed into the tube so\nthat the spring is compressed, as shown in Fig. 3.2.\nThe compression of the spring is 4.0 cm. The mass of the block is 0.025 kg.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_3_1",
          "fig_3_2"
        ],
        "figure_references": [
          "Fig. 3.1",
          "Fig. 3.2"
        ],
        "question_text_latex": "The variation with compression x of the force F acting on a spring is shown in Fig. 3.1.\nThe spring is fixed to the closed end of a horizontal tube. A block is pushed into the tube so\nthat the spring is compressed, as shown in Fig. 3.2.\nThe compression of the spring is 4.0 cm. The mass of the block is 0.025 kg.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_21_q03_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_21_q03_b",
        "display_order": 3,
        "question_text": "Calculate the spring constant of the spring.\nspring constant = N m⁻¹",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the spring constant of the spring.\n$spring constant = N m^{-1} $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_1"
          },
          {
            "type": "figure",
            "id": "fig_3_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q03_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q03_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q03_b_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "spring constant",
                  "unit": "N m⁻¹",
                  "unit_latex": "\\mathrm{N\\,m^{-1}}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q03_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_21_q03_b",
        "display_order": 4,
        "question_text": "Show that the work done to compress the spring by 4.0 cm is 0.48 J.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the work done to compress the spring by 4.0 cm is 0.48 J.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_w16_21_q03_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q03_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q03_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q03_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_w16_21_q03_b",
        "display_order": 5,
        "question_text": "The block is now released and accelerates along the tube as the spring returns to its\noriginal length. The block leaves the end of the tube with a speed of 6.0 m s⁻¹.\n1. Calculate the kinetic energy of the block as it leaves the end of the tube.\nkinetic energy = J\n2.\nAssume that the spring has negligible kinetic energy as the block leaves the tube.\nDetermine the average resistive force acting against the block as it moves along the\ntube.\nresistive force = N",
        "marks": 5,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The block is now released and accelerates along the tube as the spring returns to its\noriginal length. The block leaves the end of the tube with a speed of 6.0 m $s^{-1}$.\n1. Calculate the kinetic energy of the block as it leaves the end of the tube.\n$kinetic energy = J $\n2.\nAssume that the spring has negligible kinetic energy as the block leaves the tube.\nDetermine the average resistive force acting against the block as it moves along the\ntube.\n$resistive force = N $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_21_q03_b_ii"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q03_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q03_b_iii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q03_b_iii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "kinetic energy",
                  "unit": "J",
                  "unit_latex": "\\mathrm{J}"
                },
                {
                  "field_id": "9702_w16_21_q03_b_iii_field_03",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "resistive force",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q03_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_w16_21_q03_b",
        "display_order": 6,
        "question_text": "Determine the efficiency of the transfer of elastic potential energy from the spring to the\nkinetic energy of the block.\nefficiency =",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the efficiency of the transfer of elastic potential energy from the spring to the\nkinetic energy of the block.\n$\\text{efficiency} =$",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_21_q03_b_iii"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q03_b_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q03_b_iv_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q03_b_iv_field_02",
                  "required": true,
                  "control": "number",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [
      "part_marks_do_not_match_total"
    ],
    "human_review_status": "pending",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_21_q03_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q03_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q03_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q03_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q03_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q03_b_iv"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_21/question_03_with_figures.png",
    "prototype_paper": "9702_w16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_21.pdf",
      "paper_code": "9702_w16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 21,
      "question_id": "9702_w16_21_q03",
      "question_num": 3,
      "total_marks": 12,
      "parts": [
        {
          "id": "9702_w16_21_q03_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_21_q03_a_mp01",
              "text": "force/load is proportional to extension/compression (provided proportionality limit is not exceeded)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q03_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q03_b_i_mp01",
              "text": "k = F / x or k = gradient",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q03_b_i_mp02",
              "text": "k = 600 N m–1",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q03_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q03_b_ii_mp01",
              "text": "(W =) ½kx2 or (W =) ½Fx or (W =) area under graph",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q03_b_ii_mp02",
              "text": "(W =) 0.5 × 600 × (0.040)2 = 0.48 J or (W =) 0.5 × 24 × 0.040 = 0.48 J",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q03_b_iii",
          "label": "(b)(iii)",
          "marks": 5,
          "marking_points": [
            {
              "id": "9702_w16_21_q03_b_iii_mp01",
              "text": "1. (EK =) ½mv2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q03_b_iii_mp02",
              "text": "= ½ × 0.025 × 6.02 = 0.45 J",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q03_b_iii_mp03",
              "text": "2. (work done against resistive force =) 0.48 – 0.45 [= 0.03(0) J]",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q03_b_iii_mp04",
              "text": "average resistive force = 0.030 / 0.040",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q03_b_iii_mp05",
              "text": "= 0.75 N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q03_b_iv",
          "label": "(b)(iv)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q03_b_iv_mp01",
              "text": "efficiency = [useful energy out / total energy in] (×100)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q03_b_iv_mp02",
              "text": "= [0.45 / 0.48] (×100) = 0.94 or 94%",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_21_q04",
    "source_filename": "9702_w16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 21,
    "paper_code": "9702_w16_21",
    "metadata_confidence": 1,
    "question_num": 4,
    "source_pages": [
      10,
      11
    ],
    "total_marks": 8,
    "detected_part_marks": 8,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_04.png",
    "question_image_with_figures": "question_04_with_figures.png",
    "question_text_file": "question_04.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_4_1",
        "label": "Fig. 4.1",
        "file": "figure_4_1.png",
        "introduced_by": "9702_w16_21_q04_b",
        "referenced_by": [
          "9702_w16_21_q04_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_w16_21_q04_b",
          "position": "after_text",
          "anchor": "The trace produced on the screen of the c.r.o. is shown in Fig. 4.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_21/figure_4_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_21_q04_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State what is meant by the frequency of a progressive wave.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by the frequency of a progressive wave.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q04_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q04_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q04_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A cathode-ray oscilloscope (c.r.o.) is used to determine the frequency of the sound emitted by\na loudspeaker. The trace produced on the screen of the c.r.o. is shown in Fig. 4.1.\nThe time-base setting of the c.r.o. is 250 μs cm⁻¹.\nShow that the frequency of the sound wave is 1600 Hz.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_4_1"
        ],
        "figure_references": [
          "Fig. 4.1"
        ],
        "question_text_latex": "A cathode-ray oscilloscope (c.r.o.) is used to determine the frequency of the sound emitted by\na loudspeaker. The trace produced on the screen of the c.r.o. is shown in Fig. 4.1.\nThe time-base setting of the c.r.o. is 250 $\\mu$s cm^{-1}.\nShow that the frequency of the sound wave is 1600 Hz.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q04_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q04_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q04_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "The loudspeaker in (b) emits the sound in all directions. A person attaches the loudspeaker to\na string and then swings the loudspeaker at a constant speed in a horizontal circle above his\nhead.\nAn observer, standing a large distance away from the loudspeaker, hears sound of maximum\nfrequency 1640 Hz. The speed of sound in air is 330 m s⁻¹.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The loudspeaker in (b) emits the sound in all directions. A person attaches the loudspeaker to\na string and then swings the loudspeaker at a constant speed in a horizontal circle above his\nhead.\nAn observer, standing a large distance away from the loudspeaker, hears sound of maximum\nfrequency 1640 Hz. The speed of sound in air is 330 m $s^{-1}$.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_21_q04_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_w16_21_q04_c",
        "display_order": 4,
        "question_text": "Determine the speed of the loudspeaker.\nspeed = m s⁻¹",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the speed of the loudspeaker.\n$speed = m s^{-1} $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_21_q04_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q04_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q04_c_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q04_c_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "speed",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q04_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_w16_21_q04_c",
        "display_order": 5,
        "question_text": "Describe and explain, qualitatively, the variation in the frequency of the sound heard by\nthe observer.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Describe and explain, qualitatively, the variation in the frequency of the sound heard by\nthe observer.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q04_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q04_c_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_21_q04_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q04_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q04_c"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q04_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q04_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_21/question_04_with_figures.png",
    "prototype_paper": "9702_w16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_21.pdf",
      "paper_code": "9702_w16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 21,
      "question_id": "9702_w16_21_q04",
      "question_num": 4,
      "total_marks": 8,
      "parts": [
        {
          "id": "9702_w16_21_q04_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q04_a_mp01",
              "text": "the number of oscillations per unit time",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q04_a_mp02",
              "text": "of the source/of a point on the wave/of a particle (in the medium)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or the number of wavelengths/wavefronts per unit time",
            "4(M1) passing a (fixed) point"
          ]
        },
        {
          "id": "9702_w16_21_q04_b",
          "label": "(b)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q04_b_mp01",
              "text": "T or period = 2.5 × 250 (µs) (= 625 µs)",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q04_b_mp02",
              "text": "frequency = 1 / (6.25 × 10–4) or 1 / (2.5 × 250 × 10–6) = 1600 Hz",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q04_c_i",
          "label": "(c)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q04_c_i_mp01",
              "text": "for maximum frequency: fo = fsv / (v – vs) 1640 = (1600 × 330) / (330 – vs)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q04_c_i_mp02",
              "text": "vs = 8(.0) m s–1 (8.049 m s–1)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q04_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q04_c_ii_mp01",
              "text": "loudspeaker moving towards observer causes rise in/higher frequency",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q04_c_ii_mp02",
              "text": "loudspeaker moving away from observer causes fall in/lower frequency",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or repeated rise and fall/higher and then lower frequency",
            "4(M1) caused by loudspeaker moving towards and away from observer",
            "4(A1) 9702 21 © UCLES 2016"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_21_q05",
    "source_filename": "9702_w16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 21,
    "paper_code": "9702_w16_21",
    "metadata_confidence": 1,
    "question_num": 5,
    "source_pages": [
      11
    ],
    "total_marks": 7,
    "detected_part_marks": 7,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_05.png",
    "question_image_with_figures": null,
    "question_text_file": "question_05.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_w16_21_q05_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State what is meant by the diffraction of a wave.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by the diffraction of a wave.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q05_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q05_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q05_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "Laser light of wavelength 500 nm is incident normally on a diffraction grating. The resulting\ndiffraction pattern has diffraction maxima up to and including the fourth-order maximum.\nCalculate, for the diffraction grating, the minimum possible line spacing.\nline spacing = m",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Laser light of wavelength 500 nm is incident normally on a diffraction grating. The resulting\ndiffraction pattern has diffraction maxima up to and including the fourth-order maximum.\nCalculate, for the diffraction grating, the minimum possible line spacing.\n$line spacing = m $",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q05_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q05_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q05_b_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "line spacing",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q05_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "The light in (b) is now replaced with red light. State and explain whether this is likely to result\nin the formation of a fifth-order diffraction maximum.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The light in (b) is now replaced with red light. State and explain whether this is likely to result\nin the formation of a fifth-order diffraction maximum.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q05_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q05_c_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_21_q05_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q05_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q05_c"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_21/question_05.png",
    "prototype_paper": "9702_w16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_21.pdf",
      "paper_code": "9702_w16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 21,
      "question_id": "9702_w16_21_q05",
      "question_num": 5,
      "total_marks": 7,
      "parts": [
        {
          "id": "9702_w16_21_q05_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q05_a_mp01",
              "text": "wave incident on/passes by or through an aperture/edge",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q05_a_mp02",
              "text": "wave spreads (into geometrical shadow)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q05_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_21_q05_b_mp01",
              "text": "nλ = d sinθ",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q05_b_mp02",
              "text": "substitution of θ = 90° or sinθ = 1",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q05_b_mp03",
              "text": "4 × 500 × 10–9 = d × sin 90° line spacing = 2.0 × 10–6 m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q05_c",
          "label": "(c)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q05_c_mp01",
              "text": "wavelength of red light is longer (than 500 nm)",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q05_c_mp02",
              "text": "(each order/fourth order is now at a greater angle so) the fifth-order maximum cannot be formed/not formed",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_21_q06",
    "source_filename": "9702_w16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 21,
    "paper_code": "9702_w16_21",
    "metadata_confidence": 1,
    "question_num": 6,
    "source_pages": [
      12,
      13
    ],
    "total_marks": 9,
    "detected_part_marks": 7,
    "marks_validation_passed": false,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_06.png",
    "question_image_with_figures": "question_06_with_figures.png",
    "question_text_file": "question_06.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_6_1",
        "label": "Fig. 6.1",
        "file": "figure_6_1.png",
        "introduced_by": "9702_w16_21_q06_b",
        "referenced_by": [
          "9702_w16_21_q06_b",
          "9702_w16_21_q06_c"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_w16_21_q06_b",
          "position": "after_text",
          "anchor": "a resistor network, as shown in Fig. 6.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_21/figure_6_1.png"
      },
      {
        "id": "fig_6_2",
        "label": "Fig. 6.2",
        "file": "figure_6_2.png",
        "introduced_by": "9702_w16_21_q06_c",
        "referenced_by": [
          "9702_w16_21_q06_c"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "scope": "part",
          "part_id": "9702_w16_21_q06_c",
          "position": "after_text",
          "anchor": "Fig. 6.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_21/figure_6_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_21_q06_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define electric potential difference (p.d.).",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define electric potential difference (p.d.).",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q06_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q06_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q06_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A battery of electromotive force (e.m.f.) 14 V and negligible internal resistance is connected to\na resistor network, as shown in Fig. 6.1.\nR₁ and R₂ are fixed resistors of resistances 6.0 Ω and 12 Ω respectively. R₃ is a variable\nresistor.\nSwitch S is closed.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_6_1"
        ],
        "figure_references": [
          "Fig. 6.1"
        ],
        "question_text_latex": "A battery of electromotive force (e.m.f.) 14 V and negligible internal resistance is connected to\na resistor network, as shown in Fig. 6.1.\n$R_{1}$ and $R_{2}$ are fixed resistors of resistances 6.0 $\\Omega$ and 12 $\\Omega$ respectively. $R_{3}$ is a variable\nresistor.\nSwitch S is closed.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_21_q06_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_21_q06_b",
        "display_order": 3,
        "question_text": "Calculate the current in the battery when the resistance of R₃ is set\n1.\nat zero,\ncurrent = A\n2.\nat 24 Ω.\ncurrent = A",
        "marks": 4,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "A",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the current in the battery when the resistance of $R_{3}$ is set\n1.\nat zero,\n$current = A $\n2.\nat 24 $\\Omega$.\n$current = A $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_6_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q06_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q06_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q06_b_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "current when R₃ is zero",
                  "unit": "A",
                  "unit_latex": "\\mathrm{A}"
                },
                {
                  "field_id": "9702_w16_21_q06_b_i_field_03",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "current when R₃ is 24 Ω",
                  "unit": "A",
                  "unit_latex": "\\mathrm{A}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q06_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_21_q06_b",
        "display_order": 4,
        "question_text": "Use your answers in (b)(i) to calculate the change in the total power produced by the\nbattery when the resistance of R₃ is changed from zero to 24 Ω.\nchange in power = W",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "W",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use your answers in (b)(i) to calculate the change in the total power produced by the\nbattery when the resistance of $R_{3}$ is changed from zero to 24 $\\Omega$.\n$change in power = W $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_21_q06_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q06_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q06_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q06_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "change in power",
                  "unit": "W",
                  "unit_latex": "\\mathrm{W}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q06_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "Switch S in Fig. 6.1 is now opened.\nResistors R₁ and R₂ are made from metal wires. Some data for these resistors are shown in\nFig. 6.2.\nDetermine the ratio\naverage drift speed of free electrons in R₁ / average drift speed of free electrons in R₂.\nratio =",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_6_1",
          "fig_6_2"
        ],
        "figure_references": [
          "Fig. 6.1",
          "Fig. 6.2"
        ],
        "question_text_latex": "Switch S in Fig. 6.1 is now opened.\nResistors $R_1$ and $R_2$ are made from metal wires. Some data for these resistors are shown in\nFig. 6.2.\nDetermine the ratio $\\frac{\\text{average drift speed of free electrons in }R_1}{\\text{average drift speed of free electrons in }R_2}$.\n$\\text{ratio} =$",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_6_1"
          },
          {
            "type": "figure",
            "id": "fig_6_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q06_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q06_c_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_21_q06_c_field_02",
                  "required": true,
                  "control": "number",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [
      "part_marks_do_not_match_total"
    ],
    "human_review_status": "pending",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_21_q06_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q06_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q06_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q06_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q06_c"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_21/question_06_with_figures.png",
    "prototype_paper": "9702_w16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_21.pdf",
      "paper_code": "9702_w16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 21,
      "question_id": "9702_w16_21_q06",
      "question_num": 6,
      "total_marks": 9,
      "parts": [
        {
          "id": "9702_w16_21_q06_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_21_q06_a_mp01",
              "text": "charge forms) other to electrical (from ed) (transform energy or done work",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q06_b_i",
          "label": "(b)(i)",
          "marks": 4,
          "marking_points": [
            {
              "id": "9702_w16_21_q06_b_i_mp01",
              "text": "1. V = IR or E = IR",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q06_b_i_mp02",
              "text": "I = 14 / 6.0 = 2.3 (2.33) A",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q06_b_i_mp03",
              "text": "2. total resistance of parallel resistors = 8.0 Ω",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q06_b_i_mp04",
              "text": "current = 14 / (6.0 + 8.0) = 1.0 A",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q06_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q06_b_ii_mp01",
              "text": "P = EI (allow P = VI) or P = V2 / R or P = I2R",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q06_b_ii_mp02",
              "text": "change in power = (14 × 2.33) – (14 × 1.0) or (142 / 6.0) – (142 / 14) or (2.332 × 6.0) – (1.02 × 14) = 19 W (18 W if 2.3 A used)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q06_c",
          "label": "(c)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q06_c_mp01",
              "text": "I = Anvq ratio = (0.50n / n) × (1.8 A / A) or ratio = 0.50 × 1.8",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q06_c_mp02",
              "text": "= 0.90",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 21 © UCLES 2016"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_21_q07",
    "source_filename": "9702_w16_qp_21.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 21,
    "paper_code": "9702_w16_21",
    "metadata_confidence": 1,
    "question_num": 7,
    "source_pages": [
      14
    ],
    "total_marks": 7,
    "detected_part_marks": 7,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_07.png",
    "question_image_with_figures": null,
    "question_text_file": "question_07.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_w16_21_q07_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State one difference between a hadron and a lepton.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State one difference between a hadron and a lepton.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q07_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q07_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q07_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_21_q07_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_21_q07_b",
        "display_order": 3,
        "question_text": "State the quark composition of a proton and of a neutron.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the quark composition of a proton and of a neutron.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q07_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q07_b_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "proton quark composition"
                },
                {
                  "field_id": "9702_w16_21_q07_b_i_field_02",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "neutron quark composition"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q07_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_21_q07_b",
        "display_order": 4,
        "question_text": "Use your answer in (i) to determine the quark composition of an α-particle.\nquark composition:",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use your answer in (i) to determine the quark composition of an α-particle.\nquark composition:",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_21_q07_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q07_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q07_b_ii_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q07_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "The results of the α-particle scattering experiment provide evidence for the structure of the\natom.\nresult 1:\nThe vast majority of α-particles pass straight through the metal foil or are\ndeviated by small angles.\nresult 2:\nA very small minority of α-particles are scattered through angles greater\nthan 90°.\nState what may be inferred from",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The results of the α-particle scattering experiment provide evidence for the structure of the\natom.\nresult 1:\nThe vast majority of α-particles pass straight through the metal foil or are\ndeviated by small angles.\nresult 2:\nA very small minority of α-particles are scattered through angles greater\nthan 90°.\nState what may be inferred from",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_21_q07_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_w16_21_q07_c",
        "display_order": 6,
        "question_text": "result 1,",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "result 1,",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q07_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q07_c_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_21_q07_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_w16_21_q07_c",
        "display_order": 7,
        "question_text": "result 2.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "result 2.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_21_q07_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_21_q07_c_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_21_q07_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q07_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q07_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q07_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q07_c"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q07_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_21_q07_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_21/question_07.png",
    "prototype_paper": "9702_w16_qp_21",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_21.pdf",
      "paper_code": "9702_w16_21",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 21,
      "question_id": "9702_w16_21_q07",
      "question_num": 7,
      "total_marks": 7,
      "parts": [
        {
          "id": "9702_w16_21_q07_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_21_q07_a_mp01",
              "text": "hadron not a fundamental particle/lepton is fundamental particle or hadron made of quarks/lepton not made of quarks or strong force/interaction acts on hadrons/does not act on leptons",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q07_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q07_b_i_mp01",
              "text": "proton: up, up, down / uud",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q07_b_i_mp02",
              "text": "neutron: up, down, down / udd",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q07_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_21_q07_b_ii_mp01",
              "text": "composition: 2(uud) + 2(udd) = 6 up, 6 down / 6u, 6d",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q07_c_i",
          "label": "(c)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_21_q07_c_i_mp01",
              "text": "most of the atom is empty space or the nucleus (volume) is (very) small compared to the atom",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_21_q07_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_21_q07_c_ii_mp01",
              "text": "nucleus is (positively) charged",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_21_q07_c_ii_mp02",
              "text": "the mass is concentrated in (very small) nucleus/small region/small volume/small core or the majority of mass in (very small) nucleus/small region/small volume/small core",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_22_q01",
    "source_filename": "9702_w16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 22,
    "paper_code": "9702_w16_22",
    "metadata_confidence": 1,
    "question_num": 1,
    "source_pages": [
      5
    ],
    "total_marks": 5,
    "detected_part_marks": 5,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_01.png",
    "question_image_with_figures": null,
    "question_text_file": "question_01.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_w16_22_q01_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_22_q01_a_i",
        "path": [
          "a",
          "i"
        ],
        "label": "(a)(i)",
        "parent_id": "9702_w16_22_q01_a",
        "display_order": 2,
        "question_text": "Define pressure.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define pressure.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q01_a_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q01_a_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q01_a_ii",
        "path": [
          "a",
          "ii"
        ],
        "label": "(a)(ii)",
        "parent_id": "9702_w16_22_q01_a",
        "display_order": 3,
        "question_text": "Show that the SI base units of pressure are kg m⁻¹ s⁻².",
        "marks": 1,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the SI base units of pressure are $\\mathrm{kg\\,m^{-1}\\,s^{-2}}$.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q01_a_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q01_a_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q01_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 4,
        "question_text": "Gas flows through the narrow end (nozzle) of a pipe. Under certain conditions, the mass m of gas that flows through the nozzle in a short time t is given by m / t = kC√(ρP), where k is a constant with no units, C is a quantity that depends on the nozzle size, ρ is the density of the gas arriving at the nozzle, and P is the pressure of the gas arriving at the nozzle. Determine the base units of C.",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Gas flows through the narrow end (nozzle) of a pipe. Under certain conditions, the mass $m$ of gas that flows through the nozzle in a short time $t$ is given by $\\frac{m}{t} = kC\\sqrt{\\rho P}$, where $k$ is a constant with no units, $C$ is a quantity that depends on the nozzle size, $\\rho$ is the density of the gas arriving at the nozzle, and $P$ is the pressure of the gas arriving at the nozzle. Determine the base units of $C$.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q01_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q01_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q01_b_field_02",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "base units"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_22_q01_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q01_a_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q01_a_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q01_b"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_22/question_01.png",
    "prototype_paper": "9702_w16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_22.pdf",
      "paper_code": "9702_w16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 22,
      "question_id": "9702_w16_22_q01",
      "question_num": 1,
      "total_marks": 5,
      "parts": [
        {
          "id": "9702_w16_22_q01_a_i",
          "label": "(a)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_22_q01_a_i_mp01",
              "text": "force / area (normal to the force)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q01_a_ii",
          "label": "(a)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_22_q01_a_ii_mp01",
              "text": "(p = F / A so) units: kg m s–2 / m2 = kg m–1 s–2",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "allow use of other correct equations: e.g. (∆p = ρg∆h so) kg m–3 m s–2 m = kg m–1 s–2 e.g. (p = W / ∆V so) kg m s–2 m / m3 = kg m–1 s–2"
          ]
        },
        {
          "id": "9702_w16_22_q01_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_22_q01_b_mp01",
              "text": "units for m: kg, t: s and ρ: kg m–3",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q01_b_mp02",
              "text": "units of C: kg / s (kg m–3 kg m–1 s–2)1/2 or units of C2: kg2 / s2 kg m–3 kg m–1 s–2",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q01_b_mp03",
              "text": "units of C: m2",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_22_q03",
    "source_filename": "9702_w16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 22,
    "paper_code": "9702_w16_22",
    "metadata_confidence": 1,
    "question_num": 3,
    "source_pages": [
      8,
      9
    ],
    "total_marks": 11,
    "detected_part_marks": 11,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_03.png",
    "question_image_with_figures": "question_03_with_figures.png",
    "question_text_file": "question_03.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_3_1",
        "label": "Fig. 3.1",
        "file": "figure_3_1.png",
        "introduced_by": "9702_w16_22_q03_b",
        "referenced_by": [
          "9702_w16_22_q03_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "position": "after_text",
          "scope": "part",
          "part_id": "9702_w16_22_q03_b",
          "anchor": "rigid bar BD, as shown in Fig. 3.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_22/figure_3_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_22_q03_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State the two conditions for an object to be in equilibrium.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the two conditions for an object to be in equilibrium.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q03_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q03_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q03_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A uniform beam AC is attached to a vertical wall at end A. The beam is held horizontal by a\nrigid bar BD, as shown in Fig. 3.1.\nThe beam is of length 0.40 m and weight W. An empty bucket of weight 12 N is suspended\nby a light metal wire from end C. The bar exerts a force on the beam of 33 N at 52° to the\nhorizontal. The beam is in equilibrium.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_3_1"
        ],
        "figure_references": [
          "Fig. 3.1"
        ],
        "question_text_latex": "A uniform beam AC is attached to a vertical wall at end A. The beam is held horizontal by a\nrigid bar BD, as shown in Fig. 3.1.\nThe beam is of length 0.40 m and weight W. An empty bucket of weight 12 N is suspended\nby a light metal wire from end C. The bar exerts a force on the beam of 33 N at 52° to the\nhorizontal. The beam is in equilibrium.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_22_q03_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_22_q03_b",
        "display_order": 3,
        "question_text": "Calculate the vertical component of the force exerted by the bar on the beam.\ncomponent of the force = N",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the vertical component of the force exerted by the bar on the beam.\ncomponent of the force = N",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q03_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q03_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q03_b_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "component of the force",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q03_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_22_q03_b",
        "display_order": 4,
        "question_text": "By taking moments about A, calculate the weight W of the beam.\nW = N",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "By taking moments about A, calculate the weight W of the beam.\n$W = N $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_3_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_w16_22_q03_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q03_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q03_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q03_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "W",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q03_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "The metal of the wire in (b) has a Young modulus of 2.0 × 10¹¹ Pa.\nInitially the bucket is empty. When the bucket is filled with paint of weight 78 N, the strain of\nthe wire increases by 7.5 × 10⁻⁴. The wire obeys Hooke’s law.\nCalculate, for the wire,",
        "marks": null,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The metal of the wire in (b) has a Young modulus of $2.0 \\times 10^{11}$ Pa.\nInitially the bucket is empty. When the bucket is filled with paint of weight 78 N, the strain of\nthe wire increases by $7.5 \\times 10^{-4}$. The wire obeys Hooke’s law.\nCalculate, for the wire,",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_22_q03_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_w16_22_q03_c",
        "display_order": 6,
        "question_text": "the increase in stress due to the addition of the paint,\nincrease in stress = Pa",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.5,
        "unit": "Pa",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "the increase in stress due to the addition of the paint,\n$increase in stress = Pa $",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q03_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q03_c_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q03_c_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "increase in stress",
                  "unit": "Pa",
                  "unit_latex": "\\mathrm{Pa}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q03_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_w16_22_q03_c",
        "display_order": 7,
        "question_text": "its diameter.\ndiameter = m",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.5,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "its diameter.\n$diameter = m $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_22_q03_c_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q03_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q03_c_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q03_c_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "diameter",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_22_q03_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q03_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q03_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q03_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q03_c"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q03_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q03_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_22/question_03_with_figures.png",
    "prototype_paper": "9702_w16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_22.pdf",
      "paper_code": "9702_w16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 22,
      "question_id": "9702_w16_22_q03",
      "question_num": 3,
      "total_marks": 11,
      "parts": [
        {
          "id": "9702_w16_22_q03_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q03_a_mp01",
              "text": "resultant force (in any direction) is zero",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q03_a_mp02",
              "text": "resultant moment/torque (about any point) is zero",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q03_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_22_q03_b_i_mp01",
              "text": "force = 33 sin 52° or 33 cos 38° = 26 N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q03_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_22_q03_b_ii_mp01",
              "text": "26 × 0.30 or W × 0.20 or 12 × 0.40",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q03_b_ii_mp02",
              "text": "26 × 0.30 = (W × 0.20) + (12 × 0.40)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q03_b_ii_mp03",
              "text": "W = 15 N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q03_c_i",
          "label": "(c)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q03_c_i_mp01",
              "text": "E = ∆σ / ∆ε or E = σ / ε",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q03_c_i_mp02",
              "text": "∆σ = 2.0 × 1011 × 7.5 × 10–4 = 1.5 × 108 Pa",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q03_c_ii",
          "label": "(c)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_22_q03_c_ii_mp01",
              "text": "∆σ = ∆F / A or σ = F / A",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q03_c_ii_mp02",
              "text": "A = 78 / 1.5 × 108 (= 5.2 × 10–7 m2)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q03_c_ii_mp03",
              "text": "5.2 × 10–7 = πd 2 / 4 d = 8.1 × 10–4 m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_22_q04",
    "source_filename": "9702_w16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 22,
    "paper_code": "9702_w16_22",
    "metadata_confidence": 1,
    "question_num": 4,
    "source_pages": [
      10,
      11
    ],
    "total_marks": 10,
    "detected_part_marks": 10,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_04.png",
    "question_image_with_figures": "question_04_with_figures.png",
    "question_text_file": "question_04.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_4_1",
        "label": "Fig. 4.1",
        "file": "figure_4_1.png",
        "introduced_by": "9702_w16_22_q04_b",
        "referenced_by": [
          "9702_w16_22_q04_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "position": "after_text",
          "scope": "part",
          "part_id": "9702_w16_22_q04_b",
          "anchor": "An arrangement for demonstrating the interference of light is shown in Fig. 4.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_22/figure_4_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_22_q04_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State what is meant by the diffraction of a wave.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by the diffraction of a wave.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q04_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q04_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q04_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "An arrangement for demonstrating the interference of light is shown in Fig. 4.1.\nThe wavelength of the light from the laser is 580 nm. The separation of the slits is 0.41 mm.\nThe perpendicular distance between the double slit and the screen is D.\nCoherent light emerges from the slits and an interference pattern is observed on the screen.\nThe central bright fringe is produced at point X. The closest dark fringes to point X are\nproduced at points Y and Z. The distance XY is 2.0 mm.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_4_1"
        ],
        "figure_references": [
          "Fig. 4.1"
        ],
        "question_text_latex": "An arrangement for demonstrating the interference of light is shown in Fig. 4.1.\nThe wavelength of the light from the laser is 580 nm. The separation of the slits is 0.41 mm.\nThe perpendicular distance between the double slit and the screen is D.\nCoherent light emerges from the slits and an interference pattern is observed on the screen.\nThe central bright fringe is produced at point X. The closest dark fringes to point X are\nproduced at points Y and Z. The distance XY is 2.0 mm.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_22_q04_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_22_q04_b",
        "display_order": 3,
        "question_text": "Explain why a bright fringe is produced at point X.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Explain why a bright fringe is produced at point X.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q04_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q04_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q04_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_22_q04_b",
        "display_order": 4,
        "question_text": "State the difference in the distances, in nm, from each slit to point Y.\ndistance = nm",
        "marks": 1,
        "answer_type": "numeric",
        "answer_type_confidence": 0.85,
        "unit": "nm",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the difference in the distances, in nm, from each slit to point Y.\n$distance = nm $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q04_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q04_b_ii_field_01",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "distance",
                  "unit": "nm",
                  "unit_latex": "\\mathrm{nm}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q04_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_w16_22_q04_b",
        "display_order": 5,
        "question_text": "Calculate the distance D.\nD = m",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the distance D.\n$D = m $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q04_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q04_b_iii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q04_b_iii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "D",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q04_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_w16_22_q04_b",
        "display_order": 6,
        "question_text": "The intensity of the light passing through the two slits was initially the same. The intensity\nof the light through one of the slits is now reduced. Compare the appearance of the\nfringes before and after the change of intensity.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The intensity of the light passing through the two slits was initially the same. The intensity\nof the light through one of the slits is now reduced. Compare the appearance of the\nfringes before and after the change of intensity.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q04_b_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q04_b_iv_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_22_q04_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q04_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q04_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q04_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q04_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q04_b_iv"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_22/question_04_with_figures.png",
    "prototype_paper": "9702_w16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_22.pdf",
      "paper_code": "9702_w16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 22,
      "question_id": "9702_w16_22_q04",
      "question_num": 4,
      "total_marks": 10,
      "parts": [
        {
          "id": "9702_w16_22_q04_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q04_a_mp01",
              "text": "wave incident on/passes by or through an aperture/edge",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q04_a_mp02",
              "text": "wave spreads (into geometrical shadow)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q04_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q04_b_i_mp01",
              "text": "waves (from slits) overlap (at point X)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q04_b_i_mp02",
              "text": "path difference (from slits to X) is zero/ phase difference (between the two waves) is zero (so constructive interference gives bright fringe)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q04_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_22_q04_b_ii_mp01",
              "text": "difference in distances = λ / 2 = 580 / 2 = 290 nm",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q04_b_iii",
          "label": "(b)(iii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_22_q04_b_iii_mp01",
              "text": "λ = ax / D",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q04_b_iii_mp02",
              "text": "D = [0.41 × 10–3 × (2 × 2.0 × 10–3)] / 580 × 10–9",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q04_b_iii_mp03",
              "text": "= 2.8 m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q04_b_iv",
          "label": "(b)(iv)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q04_b_iv_mp01",
              "text": "same separation/fringe width/number of fringes bright fringe(s)/central bright fringe/(fringe at) X less bright dark fringe(s)/(fringe at) Y/(fringe at) Z brighter contrast between fringes decreases Any two of the above four points, 1 mark each",
              "tag": "B2",
              "marks": 2,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 22 © UCLES 2016"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_22_q05",
    "source_filename": "9702_w16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 22,
    "paper_code": "9702_w16_22",
    "metadata_confidence": 1,
    "question_num": 5,
    "source_pages": [
      12,
      13,
      14
    ],
    "total_marks": 12,
    "detected_part_marks": 10,
    "marks_validation_passed": false,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_05.png",
    "question_image_with_figures": "question_05_with_figures.png",
    "question_text_file": "question_05.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_5_1",
        "label": "Fig. 5.1",
        "file": "figure_5_1.png",
        "introduced_by": "9702_w16_22_q05_b",
        "referenced_by": [
          "9702_w16_22_q05_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "position": "after_text",
          "scope": "part",
          "part_id": "9702_w16_22_q05_b",
          "anchor": "A battery is connected in parallel with two lamps A and B, as shown in Fig. 5.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_22/figure_5_1.png"
      },
      {
        "id": "fig_5_2",
        "label": "Fig. 5.2",
        "file": "figure_5_2.png",
        "introduced_by": "9702_w16_22_q05_b",
        "referenced_by": [
          "9702_w16_22_q05_b",
          "9702_w16_22_q05_b_i"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "position": "after_text",
          "scope": "part",
          "part_id": "9702_w16_22_q05_b",
          "anchor": "The I–V characteristics of lamps A and B are shown in Fig. 5.2."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_22/figure_5_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_22_q05_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State Kirchhoff’s second law.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State Kirchhoff’s second law.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q05_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q05_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q05_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A battery is connected in parallel with two lamps A and B, as shown in Fig. 5.1.\nThe battery has electromotive force (e.m.f.) 6.8 V and internal resistance r.\nThe I–V characteristics of lamps A and B are shown in Fig. 5.2.\nThe potential difference across the battery terminals is 6.0 V.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_5_1",
          "fig_5_2"
        ],
        "figure_references": [
          "Fig. 5.1",
          "Fig. 5.2"
        ],
        "question_text_latex": "A battery is connected in parallel with two lamps A and B, as shown in Fig. 5.1.\nThe battery has electromotive force (e.m.f.) 6.8 V and internal resistance r.\nThe I–V characteristics of lamps A and B are shown in Fig. 5.2.\nThe potential difference across the battery terminals is 6.0 V.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_22_q05_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_22_q05_b",
        "display_order": 3,
        "question_text": "Use Fig. 5.2 to show that the current in the battery is 0.40 A.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [
          "fig_5_2"
        ],
        "figure_references": [
          "Fig. 5.2"
        ],
        "question_text_latex": "Use Fig. 5.2 to show that the current in the battery is 0.40 A.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q05_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q05_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q05_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_22_q05_b",
        "display_order": 4,
        "question_text": "Calculate the internal resistance r of the battery.\nr = Ω",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "Ω",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the internal resistance r of the battery.\n$r = \\Omega $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_22_q05_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q05_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q05_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q05_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "r",
                  "unit": "Ω",
                  "unit_latex": "\\Omega"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q05_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_w16_22_q05_b",
        "display_order": 5,
        "question_text": "Determine the ratio\nresistance of lamp A\nresistance of lamp B .\nratio =",
        "marks": 2,
        "answer_type": "numeric",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the ratio\nresistance of lamp A\nresistance of lamp B .\n$ratio = $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_5_2"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q05_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q05_b_iii_field_01",
                  "required": true,
                  "control": "number",
                  "role": "answer",
                  "label": "ratio"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q05_b_iv",
        "path": [
          "b",
          "iv"
        ],
        "label": "(b)(iv)",
        "parent_id": "9702_w16_22_q05_b",
        "display_order": 6,
        "question_text": "Determine\n1.\nthe total power produced by the battery,\npower = W\n2.\nthe efficiency of the battery in the circuit.\nefficiency =",
        "marks": 4,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine\n1.\nthe total power produced by the battery,\n$power = W $\n2.\nthe efficiency of the battery in the circuit.\n$efficiency = $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_22_q05_b_i"
          },
          {
            "type": "previous_response",
            "part_id": "9702_w16_22_q05_b_ii"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q05_b_iv_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q05_b_iv_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_22_q05_b_iv_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "power",
                  "unit": "W",
                  "unit_latex": "\\mathrm{W}"
                },
                {
                  "field_id": "9702_w16_22_q05_b_iv_field_03",
                  "required": true,
                  "control": "number",
                  "role": "answer",
                  "label": "efficiency"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [
      "part_marks_do_not_match_total"
    ],
    "human_review_status": "pending",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_22_q05_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q05_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q05_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q05_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q05_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q05_b_iv"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_22/question_05_with_figures.png",
    "prototype_paper": "9702_w16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_22.pdf",
      "paper_code": "9702_w16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 22,
      "question_id": "9702_w16_22_q05",
      "question_num": 5,
      "total_marks": 12,
      "parts": [
        {
          "id": "9702_w16_22_q05_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q05_a_mp01",
              "text": "total/sum of electromotive forces or e.m.f.s = total/sum of potential differences or p.d.s",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q05_a_mp02",
              "text": "around a loop/(closed) circuit",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q05_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q05_b_i_mp01",
              "text": "(current in battery =) current in A + current in B or IA + IB",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q05_b_i_mp02",
              "text": "(I =) 0.14 + 0.26 = 0.40 A",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q05_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q05_b_ii_mp01",
              "text": "E = V + Ir 6.8 = 6.0 + 0.40r or 6.8 = 0.40 (15 + r)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q05_b_ii_mp02",
              "text": "r = 2.0 Ω",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q05_b_iii",
          "label": "(b)(iii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q05_b_iii_mp01",
              "text": "R = V / I",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q05_b_iii_mp02",
              "text": "ratio (= RA / RB) = (6.0 / 0.14) / (6.0 / 0.26) = 42.9 / 23.1 or 0.26 / 0.14 = 1.9 (1.86)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q05_b_iv",
          "label": "(b)(iv)",
          "marks": 4,
          "marking_points": [
            {
              "id": "9702_w16_22_q05_b_iv_mp01",
              "text": "1. P = EI or VI or P = I 2R or P = V 2 / R",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q05_b_iv_mp02",
              "text": "= 6.8 × 0.40 = 0.402 × 17 = 6.82 / 17 = 2.7 W (2.72 W)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q05_b_iv_mp03",
              "text": "2. output power = VI = 6.0 × 0.40 (= 2.40 W)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q05_b_iv_mp04",
              "text": "efficiency = (6.0 × 0.40) / (6.8 × 0.40) = 2.40 / 2.72 = 0.88 or 88% (allow 0.89 or 89%)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "9702 22 © UCLES 2016"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_22_q06",
    "source_filename": "9702_w16_qp_22.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 22,
    "paper_code": "9702_w16_22",
    "metadata_confidence": 1,
    "question_num": 6,
    "source_pages": [
      15
    ],
    "total_marks": 10,
    "detected_part_marks": 10,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_06.png",
    "question_image_with_figures": null,
    "question_text_file": "question_06.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_w16_22_q06_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State one difference between a hadron and a lepton.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State one difference between a hadron and a lepton.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q06_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q06_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q06_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A proton within a nucleus decays to form a neutron and two other particles. A partial equation to represent this decay is ¹₁p → ¹₀n + _____ + _____.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "A proton within a nucleus decays to form a neutron and two other particles. A partial equation to represent this decay is $^{1}_{1}\\mathrm{p} \\to {}^{1}_{0}\\mathrm{n} + \\ldots + \\ldots$.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_22_q06_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_22_q06_b",
        "display_order": 3,
        "question_text": "Complete the equation.",
        "marks": 2,
        "answer_type": "math",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Complete the equation.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q06_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q06_b_i_field_01",
                  "required": true,
                  "control": "math_expression",
                  "role": "answer",
                  "label": "completed equation"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q06_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_22_q06_b",
        "display_order": 4,
        "question_text": "State the name of the interaction or force that gives rise to this decay.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the name of the interaction or force that gives rise to this decay.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q06_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q06_b_ii_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q06_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_w16_22_q06_b",
        "display_order": 5,
        "question_text": "State three quantities that are conserved in the decay.",
        "marks": 3,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State three quantities that are conserved in the decay.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q06_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q06_b_iii_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "quantity 1"
                },
                {
                  "field_id": "9702_w16_22_q06_b_iii_field_02",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "quantity 2"
                },
                {
                  "field_id": "9702_w16_22_q06_b_iii_field_03",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "quantity 3"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_22_q06_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 6,
        "question_text": "Use the quark composition of a proton to show that it has a charge of +e, where e is the\nelementary charge.\nExplain your working.",
        "marks": 3,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use the quark composition of a proton to show that it has a charge of +e, where e is the\nelementary charge.\nExplain your working.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_22_q06_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_22_q06_c_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_22_q06_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q06_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q06_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q06_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q06_b_iii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_22_q06_c"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_22/question_06.png",
    "prototype_paper": "9702_w16_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_22.pdf",
      "paper_code": "9702_w16_22",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 22,
      "question_id": "9702_w16_22_q06",
      "question_num": 6,
      "total_marks": 10,
      "parts": [
        {
          "id": "9702_w16_22_q06_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_22_q06_a_mp01",
              "text": "hadron not a fundamental particle/lepton is fundamental particle or hadron made of quarks/lepton not made of quarks or strong force/interaction acts on hadrons/does not act on leptons",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q06_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_22_q06_b_i_mp01",
              "text": "e 0 1 ) (+ or ) + (β 0 1",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q06_b_i_mp02",
              "text": ") (e 0 0ν",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q06_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_22_q06_b_ii_mp01",
              "text": "weak (nuclear force / interaction)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q06_b_iii",
          "label": "(b)(iii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_22_q06_b_iii_mp01",
              "text": "• mass-energy • momentum • proton number • nucleon number • charge Any three of the above quantities, 1 mark each",
              "tag": "B3",
              "marks": 3,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_22_q06_c",
          "label": "(c)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_22_q06_c_mp01",
              "text": "(quark structure of proton is) up, up, down or uud",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q06_c_mp02",
              "text": "up/u (quark charge) is (+)⅔(e), down/d (quark charge) is –⅓(e)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_22_q06_c_mp03",
              "text": "⅔e + ⅔e – ⅓e = (+)e",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_23_q01",
    "source_filename": "9702_w16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 23,
    "paper_code": "9702_w16_23",
    "metadata_confidence": 1,
    "question_num": 1,
    "source_pages": [
      5
    ],
    "total_marks": 5,
    "detected_part_marks": 5,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_01.png",
    "question_image_with_figures": "question_01_with_figures.png",
    "question_text_file": "question_01.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_1_1",
        "label": "Fig. 1.1",
        "file": "figure_1_1.png",
        "introduced_by": "9702_w16_23_q01_b",
        "referenced_by": [
          "9702_w16_23_q01_b",
          "9702_w16_23_q01_b_ii"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "position": "after_text",
          "scope": "part",
          "part_id": "9702_w16_23_q01_b",
          "anchor": "Data for the density and the mass are given in Fig. 1.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_23/figure_1_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_23_q01_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Define density.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Define density.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q01_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q01_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q01_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "The mass m of a metal sphere is given by m = πd³ρ / 6, where ρ is the density of the metal and d is the diameter of the sphere. Data for the density and the mass are given in Fig. 1.1.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "The mass $m$ of a metal sphere is given by $m = \\frac{\\pi d^3\\rho}{6}$, where $\\rho$ is the density of the metal and $d$ is the diameter of the sphere. Data for the density and the mass are given in Fig. 1.1.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_23_q01_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_23_q01_b",
        "display_order": 3,
        "question_text": "Calculate the diameter d.\nd = m",
        "marks": 1,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Calculate the diameter d.\n$d = m $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q01_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q01_b_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_23_q01_b_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "d",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q01_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_23_q01_b",
        "display_order": 4,
        "question_text": "Use your answer in (i) and the data in Fig. 1.1 to determine the value of d, with its\nabsolute uncertainty, to an appropriate number of significant figures.\nd = ± m",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "± m",
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "Use your answer in (i) and the data in Fig. 1.1 to determine the value of d, with its\nabsolute uncertainty, to an appropriate number of significant figures.\n$d = \\pm m $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          },
          {
            "type": "previous_response",
            "part_id": "9702_w16_23_q01_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q01_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q01_b_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_23_q01_b_ii_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "value",
                  "label": "d",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                },
                {
                  "field_id": "9702_w16_23_q01_b_ii_field_03",
                  "required": true,
                  "control": "quantity",
                  "role": "uncertainty",
                  "label": "absolute uncertainty",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_23_q01_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q01_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q01_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q01_b_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_23/question_01_with_figures.png",
    "prototype_paper": "9702_w16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_23.pdf",
      "paper_code": "9702_w16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 23,
      "question_id": "9702_w16_23_q01",
      "question_num": 1,
      "total_marks": 5,
      "parts": [
        {
          "id": "9702_w16_23_q01_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_23_q01_a_mp01",
              "text": "(density =) mass / volume",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q01_b_i",
          "label": "(b)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_23_q01_b_i_mp01",
              "text": "d = [(6 × 7.5) / (π × 8100)]1/3 = 0.12(1) m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q01_b_ii",
          "label": "(b)(ii)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_23_q01_b_ii_mp01",
              "text": "percentage uncertainty = (4 + 5) / 3 (= 3%) or fractional uncertainty = (0.04 + 0.05) / 3 (= 0.03)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q01_b_ii_mp02",
              "text": "absolute uncertainty (= 0.03 × 0.121) = 0.0036",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q01_b_ii_mp03",
              "text": "d = 0.121 ± 0.004 m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_23_q04",
    "source_filename": "9702_w16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 23,
    "paper_code": "9702_w16_23",
    "metadata_confidence": 1,
    "question_num": 4,
    "source_pages": [
      10,
      11
    ],
    "total_marks": 8,
    "detected_part_marks": 8,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_04.png",
    "question_image_with_figures": "question_04_with_figures.png",
    "question_text_file": "question_04.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_4_1",
        "label": "Fig. 4.1",
        "file": "figure_4_1.png",
        "introduced_by": "9702_w16_23_q04_b",
        "referenced_by": [
          "9702_w16_23_q04_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1,
        "placement": {
          "position": "after_text",
          "scope": "part",
          "part_id": "9702_w16_23_q04_b",
          "anchor": "shown in Fig. 4.1."
        },
        "prototype_file": "../../output/physics/p2/questions/9702_w16_qp_23/figure_4_1.png"
      }
    ],
    "parts": [
      {
        "id": "9702_w16_23_q04_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State what is meant by the frequency of a progressive wave.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by the frequency of a progressive wave.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q04_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q04_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q04_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A cathode-ray oscilloscope (c.r.o.) is used to determine the frequency of the sound emitted by\na loudspeaker. The trace produced on the screen of the c.r.o. is shown in Fig. 4.1.\nThe time-base setting of the c.r.o. is 250 µs cm⁻¹.\nShow that the frequency of the sound wave is 1600 Hz.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [
          "fig_4_1"
        ],
        "figure_references": [
          "Fig. 4.1"
        ],
        "question_text_latex": "A cathode-ray oscilloscope (c.r.o.) is used to determine the frequency of the sound emitted by\na loudspeaker. The trace produced on the screen of the c.r.o. is shown in Fig. 4.1.\nThe time-base setting of the c.r.o. is 250 µs cm^{-1}.\nShow that the frequency of the sound wave is 1600 Hz.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_4_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q04_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q04_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q04_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "The loudspeaker in (b) emits the sound in all directions. A person attaches the loudspeaker to\na string and then swings the loudspeaker at a constant speed in a horizontal circle above his\nhead.\nAn observer, standing a large distance away from the loudspeaker, hears sound of maximum\nfrequency 1640 Hz. The speed of sound in air is 330 m s⁻¹.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The loudspeaker in (b) emits the sound in all directions. A person attaches the loudspeaker to\na string and then swings the loudspeaker at a constant speed in a horizontal circle above his\nhead.\nAn observer, standing a large distance away from the loudspeaker, hears sound of maximum\nfrequency 1640 Hz. The speed of sound in air is 330 m $s^{-1}$.",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_23_q04_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_w16_23_q04_c",
        "display_order": 4,
        "question_text": "Determine the speed of the loudspeaker.\nspeed = m s⁻¹",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Determine the speed of the loudspeaker.\n$speed = m s^{-1} $",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_23_q04_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q04_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q04_c_i_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_23_q04_c_i_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "speed",
                  "unit": "m s⁻¹",
                  "unit_latex": "\\mathrm{m\\,s^{-1}}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q04_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_w16_23_q04_c",
        "display_order": 5,
        "question_text": "Describe and explain, qualitatively, the variation in the frequency of the sound heard by\nthe observer.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Describe and explain, qualitatively, the variation in the frequency of the sound heard by\nthe observer.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q04_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q04_c_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_23_q04_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q04_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q04_c"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q04_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q04_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_23/question_04_with_figures.png",
    "prototype_paper": "9702_w16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_23.pdf",
      "paper_code": "9702_w16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 23,
      "question_id": "9702_w16_23_q04",
      "question_num": 4,
      "total_marks": 8,
      "parts": [
        {
          "id": "9702_w16_23_q04_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q04_a_mp01",
              "text": "the number of oscillations per unit time",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q04_a_mp02",
              "text": "of the source/of a point on the wave/of a particle (in the medium)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or the number of wavelengths/wavefronts per unit time",
            "4(M1) passing a (fixed) point"
          ]
        },
        {
          "id": "9702_w16_23_q04_b",
          "label": "(b)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q04_b_mp01",
              "text": "T or period = 2.5 × 250 (µs) (= 625 µs)",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q04_b_mp02",
              "text": "frequency = 1 / (6.25 × 10–4) or 1 / (2.5 × 250 × 10–6) = 1600 Hz",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q04_c_i",
          "label": "(c)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q04_c_i_mp01",
              "text": "for maximum frequency: fo = fsv / (v – vs) 1640 = (1600 × 330) / (330 – vs)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q04_c_i_mp02",
              "text": "vs = 8(.0) m s–1 (8.049 m s–1)",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q04_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q04_c_ii_mp01",
              "text": "loudspeaker moving towards observer causes rise in/higher frequency",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q04_c_ii_mp02",
              "text": "loudspeaker moving away from observer causes fall in/lower frequency",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ],
          "notes": [
            "or repeated rise and fall/higher and then lower frequency",
            "4(M1) caused by loudspeaker moving towards and away from observer",
            "4(A1) 9702 23 © UCLES 2016"
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_23_q05",
    "source_filename": "9702_w16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 23,
    "paper_code": "9702_w16_23",
    "metadata_confidence": 1,
    "question_num": 5,
    "source_pages": [
      11
    ],
    "total_marks": 7,
    "detected_part_marks": 7,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_05.png",
    "question_image_with_figures": null,
    "question_text_file": "question_05.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_w16_23_q05_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State what is meant by the diffraction of a wave.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State what is meant by the diffraction of a wave.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q05_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q05_a_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q05_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "Laser light of wavelength 500 nm is incident normally on a diffraction grating. The resulting\ndiffraction pattern has diffraction maxima up to and including the fourth-order maximum.\nCalculate, for the diffraction grating, the minimum possible line spacing.\nline spacing = m",
        "marks": 3,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "m",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Laser light of wavelength 500 nm is incident normally on a diffraction grating. The resulting\ndiffraction pattern has diffraction maxima up to and including the fourth-order maximum.\nCalculate, for the diffraction grating, the minimum possible line spacing.\n$line spacing = m $",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q05_b_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q05_b_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "working"
                },
                {
                  "field_id": "9702_w16_23_q05_b_field_02",
                  "required": true,
                  "control": "quantity",
                  "role": "answer",
                  "label": "line spacing",
                  "unit": "m",
                  "unit_latex": "\\mathrm{m}"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q05_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 3,
        "question_text": "The light in (b) is now replaced with red light. State and explain whether this is likely to result\nin the formation of a fifth-order diffraction maximum.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The light in (b) is now replaced with red light. State and explain whether this is likely to result\nin the formation of a fifth-order diffraction maximum.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q05_c_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q05_c_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_23_q05_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q05_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q05_c"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_23/question_05.png",
    "prototype_paper": "9702_w16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_23.pdf",
      "paper_code": "9702_w16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 23,
      "question_id": "9702_w16_23_q05",
      "question_num": 5,
      "total_marks": 7,
      "parts": [
        {
          "id": "9702_w16_23_q05_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q05_a_mp01",
              "text": "wave incident on/passes by or through an aperture/edge",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q05_a_mp02",
              "text": "wave spreads (into geometrical shadow)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q05_b",
          "label": "(b)",
          "marks": 3,
          "marking_points": [
            {
              "id": "9702_w16_23_q05_b_mp01",
              "text": "nλ = d sinθ",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q05_b_mp02",
              "text": "substitution of θ = 90° or sinθ = 1",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q05_b_mp03",
              "text": "4 × 500 × 10–9 = d × sin 90° line spacing = 2.0 × 10–6 m",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q05_c",
          "label": "(c)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q05_c_mp01",
              "text": "wavelength of red light is longer (than 500 nm)",
              "tag": "M1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q05_c_mp02",
              "text": "(each order/fourth order is now at a greater angle so) the fifth-order maximum cannot be formed/not formed",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.0",
    "question_id": "9702_w16_23_q07",
    "source_filename": "9702_w16_qp_23.pdf",
    "subject_code": "9702",
    "year": 2016,
    "session": "October/November",
    "session_code": "w",
    "variant": 23,
    "paper_code": "9702_w16_23",
    "metadata_confidence": 1,
    "question_num": 7,
    "source_pages": [
      14
    ],
    "total_marks": 7,
    "detected_part_marks": 7,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "question_image": "question_07.png",
    "question_image_with_figures": null,
    "question_text_file": "question_07.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": false,
    "figures": [],
    "parts": [
      {
        "id": "9702_w16_23_q07_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "State one difference between a hadron and a lepton.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State one difference between a hadron and a lepton.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q07_a_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q07_a_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q07_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_23_q07_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_w16_23_q07_b",
        "display_order": 3,
        "question_text": "State the quark composition of a proton and of a neutron.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "State the quark composition of a proton and of a neutron.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q07_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q07_b_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "proton"
                },
                {
                  "field_id": "9702_w16_23_q07_b_i_field_02",
                  "required": true,
                  "control": "short_text",
                  "role": "answer",
                  "label": "neutron"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q07_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_w16_23_q07_b",
        "display_order": 4,
        "question_text": "Use your answer in (i) to determine the quark composition of an α-particle.\nquark composition:",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Use your answer in (i) to determine the quark composition of an α-particle.\nquark composition:",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "previous_response",
            "part_id": "9702_w16_23_q07_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q07_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q07_b_ii_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q07_c",
        "path": [
          "c"
        ],
        "label": "(c)",
        "parent_id": null,
        "display_order": 5,
        "question_text": "The results of the α-particle scattering experiment provide evidence for the structure of the\natom.\nresult 1:\nThe vast majority of α-particles pass straight through the metal foil or are\ndeviated by small angles.\nresult 2:\nA very small minority of α-particles are scattered through angles greater\nthan 90°.\nState what may be inferred from",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The results of the α-particle scattering experiment provide evidence for the structure of the\natom.\nresult 1:\nThe vast majority of α-particles pass straight through the metal foil or are\ndeviated by small angles.\nresult 2:\nA very small minority of α-particles are scattered through angles greater\nthan 90°.\nState what may be inferred from",
        "marks_source": null,
        "dependencies": []
      },
      {
        "id": "9702_w16_23_q07_c_i",
        "path": [
          "c",
          "i"
        ],
        "label": "(c)(i)",
        "parent_id": "9702_w16_23_q07_c",
        "display_order": 6,
        "question_text": "result 1,",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "result 1,",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q07_c_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q07_c_i_field_01",
                  "required": true,
                  "control": "short_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_w16_23_q07_c_ii",
        "path": [
          "c",
          "ii"
        ],
        "label": "(c)(ii)",
        "parent_id": "9702_w16_23_q07_c",
        "display_order": 7,
        "question_text": "result 2.",
        "marks": 2,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "result 2.",
        "marks_source": "compacted_text",
        "dependencies": [],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_w16_23_q07_c_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_w16_23_q07_c_ii_field_01",
                  "required": true,
                  "control": "long_text",
                  "role": "answer"
                }
              ]
            }
          ]
        }
      }
    ],
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_w16_23_q07_a"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q07_b"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q07_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q07_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q07_c"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q07_c_i"
      },
      {
        "type": "part",
        "part_id": "9702_w16_23_q07_c_ii"
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "prototype_image": "../../output/physics/p2/questions/9702_w16_qp_23/question_07.png",
    "prototype_paper": "9702_w16_qp_23",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_w16_ms_23.pdf",
      "paper_code": "9702_w16_23",
      "subject_code": "9702",
      "year": 2016,
      "session": "October/November",
      "session_code": "w",
      "variant": 23,
      "question_id": "9702_w16_23_q07",
      "question_num": 7,
      "total_marks": 7,
      "parts": [
        {
          "id": "9702_w16_23_q07_a",
          "label": "(a)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_23_q07_a_mp01",
              "text": "hadron not a fundamental particle/lepton is fundamental particle or hadron made of quarks/lepton not made of quarks or strong force/interaction acts on hadrons/does not act on leptons",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q07_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q07_b_i_mp01",
              "text": "proton: up, up, down / uud",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q07_b_i_mp02",
              "text": "neutron: up, down, down / udd",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q07_b_ii",
          "label": "(b)(ii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_23_q07_b_ii_mp01",
              "text": "composition: 2(uud) + 2(udd) = 6 up, 6 down / 6u, 6d",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q07_c_i",
          "label": "(c)(i)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_w16_23_q07_c_i_mp01",
              "text": "most of the atom is empty space or the nucleus (volume) is (very) small compared to the atom",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_w16_23_q07_c_ii",
          "label": "(c)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_w16_23_q07_c_ii_mp01",
              "text": "nucleus is (positively) charged",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_w16_23_q07_c_ii_mp02",
              "text": "the mass is concentrated in (very small) nucleus/small region/small volume/small core or the majority of mass in (very small) nucleus/small region/small volume/small core",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  },
  {
    "schema_version": "1.1",
    "question_id": "9702_m17_22_q01",
    "source_filename": "9702_m17_qp_22.pdf",
    "subject_code": "9702",
    "year": 2017,
    "session": "February/March",
    "session_code": "m",
    "variant": 22,
    "paper_code": "9702_m17_22",
    "metadata_confidence": 1.0,
    "question_num": 1,
    "source_pages": [
      4,
      5
    ],
    "total_marks": 7,
    "detected_part_marks": 7,
    "marks_validation_passed": true,
    "question_stem": "",
    "question_stem_latex": "",
    "content_flow": [
      {
        "type": "part",
        "part_id": "9702_m17_22_q01_a"
      },
      {
        "type": "part",
        "part_id": "9702_m17_22_q01_b"
      },
      {
        "type": "part",
        "part_id": "9702_m17_22_q01_b_i"
      },
      {
        "type": "part",
        "part_id": "9702_m17_22_q01_b_ii"
      },
      {
        "type": "part",
        "part_id": "9702_m17_22_q01_b_iii"
      }
    ],
    "question_image": "question_01.png",
    "question_image_with_figures": "question_01_with_figures.png",
    "question_text_file": "question_01.txt",
    "question_text_format": "markdown-with-inline-latex",
    "has_diagram": true,
    "figures": [
      {
        "id": "fig_1_1",
        "label": "Fig. 1.1",
        "file": "figure_1_1.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m17_22_q01_a",
          "position": "after_text",
          "anchor": "quantities are scalars or vectors."
        },
        "introduced_by": "9702_m17_22_q01_a",
        "referenced_by": [
          "9702_m17_22_q01_a"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m17_qp_22/figure_1_1.png"
      },
      {
        "id": "fig_1_2",
        "label": "Fig. 1.2",
        "file": "figure_1_2.png",
        "placement": {
          "scope": "part",
          "part_id": "9702_m17_22_q01_b",
          "position": "after_text",
          "anchor": "as shown in Fig. 1.2."
        },
        "introduced_by": "9702_m17_22_q01_b",
        "referenced_by": [
          "9702_m17_22_q01_b"
        ],
        "mapping_method": "explicit_text_reference",
        "mapping_confidence": 1.0,
        "prototype_file": "../../output/physics/p2/questions/9702_m17_qp_22/figure_1_2.png"
      }
    ],
    "parts": [
      {
        "id": "9702_m17_22_q01_a",
        "path": [
          "a"
        ],
        "label": "(a)",
        "parent_id": null,
        "display_order": 1,
        "question_text": "Complete Fig. 1.1 by putting a tick (✓) in the appropriate column to indicate whether the listed quantities are scalars or vectors.",
        "marks": 2,
        "answer_type": "selection",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [
          "fig_1_1"
        ],
        "figure_references": [
          "Fig. 1.1"
        ],
        "question_text_latex": "Complete Fig. 1.1 by putting a tick (✓) in the appropriate column to indicate whether the listed quantities are scalars or vectors.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "figure",
            "id": "fig_1_1"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m17_22_q01_a_block_01",
              "type": "table",
              "columns": [
                {
                  "column_id": "quantity",
                  "label": "quantity"
                },
                {
                  "column_id": "scalar",
                  "label": "scalar"
                },
                {
                  "column_id": "vector",
                  "label": "vector"
                }
              ],
              "rows": [
                {
                  "row_id": "acceleration"
                },
                {
                  "row_id": "force"
                },
                {
                  "row_id": "kinetic_energy"
                },
                {
                  "row_id": "momentum"
                },
                {
                  "row_id": "power"
                },
                {
                  "row_id": "work"
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m17_22_q01_b",
        "path": [
          "b"
        ],
        "label": "(b)",
        "parent_id": null,
        "display_order": 2,
        "question_text": "A floating sphere is attached by a cable to the bottom of a river, as shown in Fig. 1.2.\nThe sphere is in equilibrium, with the cable at an angle of 75° to the horizontal. Assume that the force on the sphere due to the water flow is in the horizontal direction.\nThe radius of the sphere is 23 cm. The sphere is solid and is made from a material of density 82 kg m⁻³.",
        "marks": null,
        "answer_type": "text",
        "answer_type_confidence": 0.5,
        "unit": null,
        "figure_ids": [
          "fig_1_2"
        ],
        "figure_references": [
          "Fig. 1.2"
        ],
        "question_text_latex": "A floating sphere is attached by a cable to the bottom of a river, as shown in Fig. 1.2.\nThe sphere is in equilibrium, with the cable at an angle of $75^\\circ$ to the horizontal. Assume that the force on the sphere due to the water flow is in the horizontal direction.\nThe radius of the sphere is $23\\,\\mathrm{cm}$. The sphere is solid and is made from a material of density $82\\,\\mathrm{kg\\,m^{-3}}$.",
        "marks_source": null
      },
      {
        "id": "9702_m17_22_q01_b_i",
        "path": [
          "b",
          "i"
        ],
        "label": "(b)(i)",
        "parent_id": "9702_m17_22_q01_b",
        "display_order": 3,
        "question_text": "Show that the weight of the sphere is 41 N.",
        "marks": 2,
        "answer_type": "working",
        "answer_type_confidence": 0.9,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Show that the weight of the sphere is $41\\,\\mathrm{N}$.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m17_22_q01_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m17_22_q01_b_i_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m17_22_q01_b_i_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m17_22_q01_b_ii",
        "path": [
          "b",
          "ii"
        ],
        "label": "(b)(ii)",
        "parent_id": "9702_m17_22_q01_b",
        "display_order": 4,
        "question_text": "The tension in the cable is 290 N.\nDetermine the upthrust acting on the sphere.",
        "marks": 2,
        "answer_type": "numeric-with-working",
        "answer_type_confidence": 0.85,
        "unit": "N",
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "The tension in the cable is $290\\,\\mathrm{N}$.\nDetermine the upthrust acting on the sphere.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m17_22_q01_b"
          },
          {
            "type": "previous_response",
            "part_id": "9702_m17_22_q01_b_i"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m17_22_q01_b_ii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m17_22_q01_b_ii_field_01",
                  "control": "long_text",
                  "role": "working",
                  "required": true
                },
                {
                  "field_id": "9702_m17_22_q01_b_ii_field_02",
                  "control": "quantity",
                  "role": "value",
                  "label": "Upthrust",
                  "unit": "N",
                  "unit_latex": "\\mathrm{N}",
                  "required": true
                }
              ]
            }
          ]
        }
      },
      {
        "id": "9702_m17_22_q01_b_iii",
        "path": [
          "b",
          "iii"
        ],
        "label": "(b)(iii)",
        "parent_id": "9702_m17_22_q01_b",
        "display_order": 5,
        "question_text": "Explain the origin of the upthrust acting on the sphere.",
        "marks": 1,
        "answer_type": "text",
        "answer_type_confidence": 0.85,
        "unit": null,
        "figure_ids": [],
        "figure_references": [],
        "question_text_latex": "Explain the origin of the upthrust acting on the sphere.",
        "marks_source": "compacted_text",
        "dependencies": [
          {
            "type": "question_context",
            "part_id": "9702_m17_22_q01_b"
          }
        ],
        "response_schema": {
          "version": "0.1",
          "blocks": [
            {
              "block_id": "9702_m17_22_q01_b_iii_block_01",
              "type": "fields",
              "fields": [
                {
                  "field_id": "9702_m17_22_q01_b_iii_field_01",
                  "control": "long_text",
                  "role": "explanation",
                  "required": true
                }
              ]
            }
          ]
        }
      }
    ],
    "verification": {
      "content_structure_checked": true,
      "marks_reconciled": true,
      "numerical_values_checked": false
    },
    "review_flags": [],
    "human_review_status": "not_required",
    "enrichment": {
      "difficulty": null,
      "topic_id": null,
      "primary_skill": null,
      "skill_tags": [],
      "ai_rubric": null
    },
    "prototype_image": "../../output/physics/p2/questions/9702_m17_qp_22/question_01_with_figures.png",
    "prototype_paper": "9702_m17_qp_22",
    "prototype_mark_scheme": {
      "schema_version": "1.0",
      "source_filename": "9702_m17_ms_22.pdf",
      "paper_code": "9702_m17_22",
      "subject_code": "9702",
      "year": 2017,
      "session": "February/March",
      "session_code": "m",
      "variant": 22,
      "question_id": "9702_m17_22_q01",
      "question_num": 1,
      "total_marks": 7,
      "parts": [
        {
          "id": "9702_m17_22_q01_a",
          "label": "(a)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m17_22_q01_a_mp01",
              "text": "scalars: kinetic energy, power, work",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m17_22_q01_a_mp02",
              "text": "vectors: acceleration, force, momentum",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m17_22_q01_b_i",
          "label": "(b)(i)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m17_22_q01_b_i_mp01",
              "text": "mass = volume × density or m = V × ρ = 4/3 π (23 × 10–2)3 × 82",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m17_22_q01_b_i_mp02",
              "text": "weight = 4/3 π (23 × 10–2)3 × 82 × 9.8 = 41 N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m17_22_q01_b_ii",
          "label": "(b)(ii)",
          "marks": 2,
          "marking_points": [
            {
              "id": "9702_m17_22_q01_b_ii_mp01",
              "text": "vertical component of tension = 290 sin75° or 290 cos15° (= 280)",
              "tag": "C1",
              "marks": 1,
              "is_alternative": false
            },
            {
              "id": "9702_m17_22_q01_b_ii_mp02",
              "text": "upthrust = 290 sin75° + 41 = 320 (321) N",
              "tag": "A1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        },
        {
          "id": "9702_m17_22_q01_b_iii",
          "label": "(b)(iii)",
          "marks": 1,
          "marking_points": [
            {
              "id": "9702_m17_22_q01_b_iii_mp01",
              "text": "the water pressure is greater than the air pressure or the pressure on lower surface (of sphere) is greater than the pressure on upper surface (of sphere)",
              "tag": "B1",
              "marks": 1,
              "is_alternative": false
            }
          ]
        }
      ]
    }
  }
];
