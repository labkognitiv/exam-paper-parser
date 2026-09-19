import React, { useEffect, useRef, useState } from 'react';
import { ArrowRight, ChevronDown, SlidersHorizontal, X, CheckCircle2, RotateCcw, Sparkles } from 'lucide-react';

interface ReviewQuestion {
  id: string;
  paperCode: string;
  part: string;
  topic: string;
  component: string;
  tags: ('Incorrect' | 'Bookmarked' | 'Confused' | 'Important')[];
  status: 'active' | 'resolved';
  marks: number;
  questionText: string;
  markSchemeNotes: string;
  studentErrorSummary: string;
}

const initialQuestions: ReviewQuestion[] = [
  {
    id: 'q1',
    paperCode: '9709_M18_42',
    part: 'Q3 (i)',
    topic: 'M1 · Energy, work and power',
    component: 'M1',
    tags: ['Incorrect', 'Confused'],
    status: 'active',
    marks: 4,
    questionText: 'A block of mass 2.5 kg is pulled up a rough slope inclined at 30° to the horizontal by a constant force of magnitude 28 N acting parallel to the slope. The coefficient of friction between the block and the slope is 0.24. Find the work done against friction as the block travels 6 m up the slope.',
    markSchemeNotes: 'M1 for resolving normal reaction R = mg cos 30° = 2.5 * 9.8 * 0.866 = 21.2 N. A1 for F_friction = μ R = 0.24 * 21.2 = 5.09 N. M1 for Work = F_friction * d = 5.09 * 6. A1 for 30.5 J (or 31 J).',
    studentErrorSummary: 'Used mg sin 30° instead of mg cos 30° for normal reaction R. Forgot to multiply friction by distance d.',
  },
  {
    id: 'q2',
    paperCode: '9709_s23_12',
    part: 'Q7 (ii)',
    topic: 'P1 · Trigonometric Equations & Identities',
    component: 'P1',
    tags: ['Bookmarked', 'Important'],
    status: 'active',
    marks: 5,
    questionText: 'Solve the equation 2 sin^2(2θ) - 3 cos(2θ) = 0 for 0° ≤ θ ≤ 180°. Give answers to 1 decimal place.',
    markSchemeNotes: 'M1 for using sin^2(2θ) = 1 - cos^2(2θ) to form quadratic: 2 cos^2(2θ) + 3 cos(2θ) - 2 = 0. M1 for factoring (2 cos 2θ - 1)(cos 2θ + 2) = 0. A1 for cos 2θ = 0.5 (rejecting -2). A1 for 2θ = 60°, 300°. A1 for θ = 30.0°, 150.0°.',
    studentErrorSummary: 'Bookmarked for revision: high probability exam archetype with double angle quadratic factorization.',
  },
  {
    id: 'q3',
    paperCode: '9709_w22_52',
    part: 'Q4',
    topic: 'S1 · The Normal Distribution with Unknown Mean',
    component: 'S1',
    tags: ['Confused'],
    status: 'active',
    marks: 4,
    questionText: 'The length of metal rods produced by a factory is modeled by a normal distribution with mean μ and standard deviation 1.2 cm. Given that 15% of the rods are longer than 24.8 cm, find the value of μ.',
    markSchemeNotes: 'B1 for finding z-score corresponding to upper 15%: Φ(z) = 0.85 => z = +1.036. M1 for standardisation equation: (24.8 - μ) / 1.2 = 1.036. A1 for μ = 24.8 - 1.2 * 1.036 = 23.56 cm.',
    studentErrorSummary: 'Used z = -1.036 instead of +1.036 because upper tail is 15%. Remember: values greater than mean have positive z.',
  },
  {
    id: 'q4',
    paperCode: '9709_m21_32',
    part: 'Q9 (i)',
    topic: 'P3 · Differential Equations by Separation of Variables',
    component: 'P3',
    tags: ['Important'],
    status: 'active',
    marks: 6,
    questionText: 'Find the general solution of the differential equation dy/dx = (y^2 + 1) / (x + 2), expressing y in terms of x.',
    markSchemeNotes: 'M1 for separating variables: ∫ 1/(y^2 + 1) dy = ∫ 1/(x + 2) dx. A1 for tan^-1(y) = ln|x + 2| + c. M1 for taking tangent of both sides: y = tan(ln|x + 2| + c).',
    studentErrorSummary: 'Important standard integral: ∫ 1/(y^2 + 1) dy = arctan(y). Do not forget constant of integration c before taking tangent.',
  },
];

export const ReviewPage: React.FC = () => {
  const [questions, setQuestions] = useState<ReviewQuestion[]>(initialQuestions);
  const [activeTab, setActiveTab] = useState<'active' | 'resolved'>('active');
  const [selectedReasons, setSelectedReasons] = useState<ReviewQuestion['tags']>([]);
  const [reasonsOpen, setReasonsOpen] = useState(false);
  const reasonsRef = useRef<HTMLDivElement>(null);
  const reasonsButtonRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (!reasonsOpen) return;
    const dismissOutside = (event: PointerEvent) => {
      if (!reasonsRef.current?.contains(event.target as Node)) setReasonsOpen(false);
    };
    const dismissOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setReasonsOpen(false);
        reasonsButtonRef.current?.focus();
      }
    };
    document.addEventListener('pointerdown', dismissOutside);
    document.addEventListener('keydown', dismissOnEscape);
    return () => {
      document.removeEventListener('pointerdown', dismissOutside);
      document.removeEventListener('keydown', dismissOnEscape);
    };
  }, [reasonsOpen]);
  const [inspectedQuestion, setInspectedQuestion] = useState<ReviewQuestion | null>(null);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  const activeCount = questions.filter((q) => q.status === 'active').length;
  const resolvedCount = questions.filter((q) => q.status === 'resolved').length;

  const filteredQuestions = questions.filter((q) =>
    q.status === activeTab &&
    (selectedReasons.length === 0 || selectedReasons.some((reason) => q.tags.includes(reason)))
  );

  const handleToggleResolved = (id: string) => {
    setQuestions((prev) =>
      prev.map((q) => {
        if (q.id === id) {
          const nextStatus = q.status === 'active' ? 'resolved' : 'active';
          showToast(nextStatus === 'resolved' ? 'Question marked as Resolved!' : 'Question restored to Active!');
          return { ...q, status: nextStatus };
        }
        return q;
      })
    );
    setInspectedQuestion(null);
  };

  return (
    <div className="max-w-6xl mx-auto">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-[#111424] text-white px-5 py-3 rounded-xl shadow-xl flex items-center gap-3 border border-[#1a1f36] text-xs font-medium animate-in fade-in slide-in-from-bottom-2 duration-150">
          <Sparkles className="w-4 h-4 text-[#2f66f6]" />
          <span>{toastMessage}</span>
        </div>
      )}

      <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-5 mb-6">
        <h2 className="text-2xl font-bold text-[#1d1935] tracking-tight pt-1">
          Questions to revisit
        </h2>
        <div className="flex flex-col items-end gap-3 self-end sm:self-auto">
          <div className="inline-flex rounded-xl border border-[#e8eaee] p-1 gap-1" aria-label="Question status">
            {(['active', 'resolved'] as const).map((status) => (
              <button
                key={status}
                aria-pressed={activeTab === status}
                onClick={() => {
                  setActiveTab(status);
                  setSelectedReasons([]);
                  setReasonsOpen(false);
                }}
                className={`px-4 py-2 rounded-lg text-sm font-semibold transition-colors ${
                  activeTab === status
                    ? 'bg-[#e8f7f4] text-[#168f89]'
                    : 'text-slate-500 hover:bg-white hover:text-slate-800'
                }`}
              >
                {status === 'active' ? `Active ${activeCount}` : `Resolved ${resolvedCount}`}
              </button>
            ))}
          </div>
          <div
            ref={reasonsRef}
            className="relative"
            onBlur={(event) => {
              if (!event.currentTarget.contains(event.relatedTarget as Node | null)) setReasonsOpen(false);
            }}
          >
            <button
              ref={reasonsButtonRef}
              aria-expanded={reasonsOpen}
              aria-controls="review-reasons"
              onClick={() => setReasonsOpen((open) => !open)}
              className="flex items-center gap-2.5 rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-sm font-medium text-[#272043] hover:border-[#2bb9b1] transition-colors"
            >
              <SlidersHorizontal className="w-4 h-4 text-slate-500" />
              <span>Reasons · {selectedReasons.length === 0 ? 'All' : `${selectedReasons.length} selected`}</span>
              <ChevronDown className={`w-4 h-4 text-slate-500 transition-transform ${reasonsOpen ? 'rotate-180' : ''}`} />
            </button>
            {reasonsOpen && (
              <div id="review-reasons" className="absolute right-0 top-full mt-2 z-40 w-60 rounded-xl border border-[#e8eaee] bg-white shadow-lg p-2">
                <fieldset>
                  <legend className="px-3 pt-2 pb-1 text-sm font-semibold text-[#272043]">Reasons</legend>
                  {(['Incorrect', 'Bookmarked', 'Confused', 'Important'] as const).map((reason) => (
                    <label key={reason} className="flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm text-slate-700 hover:bg-slate-50 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={selectedReasons.includes(reason)}
                        onChange={() => setSelectedReasons((current) =>
                          current.includes(reason) ? current.filter((item) => item !== reason) : [...current, reason]
                        )}
                        className="w-4 h-4 accent-[#168f89]"
                      />
                      {reason}
                    </label>
                  ))}
                </fieldset>
                <div className="border-t border-slate-100 mt-2 pt-1">
                  <button onClick={() => setSelectedReasons([])} className="w-full text-left px-3 py-2 text-sm text-slate-500 hover:text-[#168f89] rounded-lg hover:bg-slate-50">
                    Clear filters
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="space-y-4">
        {filteredQuestions.length === 0 ? (
          <div className="p-8 text-center bg-white rounded-2xl border border-slate-100 text-slate-500 text-sm">
            No questions in this filter category.
          </div>
        ) : (
          filteredQuestions.map((q) => (
            <div key={q.id} className="bg-white rounded-2xl px-5 py-6 sm:px-6 border border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div className="min-w-0">
                <h3 className="font-bold text-[#1d1935] text-base leading-snug">{q.topic}</h3>
                <div className="flex items-center gap-x-3 gap-y-2 mt-2 flex-wrap">
                  <span className="text-xs text-slate-500">{q.paperCode} · {q.part}</span>
                  <div className="flex flex-wrap gap-2">
                    {q.tags.map((tag) => (
                      <span key={tag} className={`px-2.5 py-1 rounded-full text-[11px] font-medium ${
                        tag === 'Incorrect' ? 'bg-amber-50 text-amber-700'
                        : tag === 'Confused' ? 'bg-slate-100 text-slate-600'
                        : tag === 'Bookmarked' ? 'bg-[#e8f7f4] text-[#168f89]'
                        : 'bg-violet-50 text-violet-700'
                      }`}>{tag}</span>
                    ))}
                  </div>
                </div>
              </div>
              <button
                onClick={() => setInspectedQuestion(q)}
                aria-label={`Open question: ${q.topic}`}
                className="flex items-center justify-center gap-2 px-4 py-2 rounded-full border border-[#2bb9b1] text-[#168f89] hover:bg-[#e8f7f4] text-sm font-medium transition-colors shrink-0 self-end sm:self-auto"
              >
                <span>Open question</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          ))
        )}
      </div>

      {/* ================================================================ */}
      {/* INTERACTIVE QUESTION INSPECTION MODAL */}
      {/* ================================================================ */}
      {inspectedQuestion && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4">
          <div className="bg-white rounded-2xl max-w-2xl w-full p-6 shadow-2xl border border-slate-100 animate-in fade-in zoom-in-95 duration-150 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between pb-4 border-b border-slate-100 mb-4">
              <div className="flex items-center gap-2">
                <span className="px-2.5 py-0.5 rounded-md bg-[#eff6ff] text-[#2f66f6] font-mono text-xs font-bold">
                  {inspectedQuestion.paperCode}
                </span>
                <span className="text-xs font-bold text-slate-700">
                  {inspectedQuestion.part}
                </span>
                <span className="text-xs text-slate-400">
                  ({inspectedQuestion.marks} Marks)
                </span>
              </div>
              <button
                onClick={() => setInspectedQuestion(null)}
                className="p-1.5 rounded-lg text-slate-400 hover:text-slate-600 hover:bg-slate-100"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-4">
              <div>
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                  OFFICIAL QUESTION PROMPT
                </span>
                <p className="text-sm font-medium text-[#0f172a] leading-relaxed p-3.5 rounded-xl bg-slate-50 border border-slate-100">
                  {inspectedQuestion.questionText}
                </p>
              </div>

              <div>
                <span className="text-[11px] font-bold text-amber-600 uppercase tracking-wider block mb-1">
                  WHY YOU FLAGGED THIS QUESTION
                </span>
                <p className="text-xs text-slate-600 leading-relaxed p-3.5 rounded-xl bg-amber-50/60 border border-amber-100 text-amber-900">
                  {inspectedQuestion.studentErrorSummary}
                </p>
              </div>

              <div>
                <span className="text-[11px] font-bold text-[#059669] uppercase tracking-wider block mb-1">
                  CAMBRIDGE MARK SCHEME CRITERIA
                </span>
                <p className="text-xs font-mono text-slate-700 leading-relaxed p-3.5 rounded-xl bg-[#ecfdf5]/70 border border-emerald-100">
                  {inspectedQuestion.markSchemeNotes}
                </p>
              </div>

              <div className="flex items-center justify-between pt-4 border-t border-slate-100">
                <button
                  onClick={() => setInspectedQuestion(null)}
                  className="px-4 py-2 text-xs font-medium text-slate-600 hover:bg-slate-100 rounded-xl"
                >
                  Close
                </button>
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => {
                      showToast('Re-attempt session initialized...');
                      setInspectedQuestion(null);
                    }}
                    className="flex items-center gap-1.5 px-4 py-2 rounded-xl border border-slate-200 hover:bg-slate-50 text-xs font-semibold text-slate-700"
                  >
                    <RotateCcw className="w-3.5 h-3.5" />
                    <span>Re-attempt</span>
                  </button>
                  <button
                    onClick={() => handleToggleResolved(inspectedQuestion.id)}
                    className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-[#2f66f6] hover:bg-[#2557df] text-white text-xs font-semibold shadow-xs"
                  >
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>
                      {inspectedQuestion.status === 'active'
                        ? 'Mark as Resolved'
                        : 'Restore to Active'}
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
