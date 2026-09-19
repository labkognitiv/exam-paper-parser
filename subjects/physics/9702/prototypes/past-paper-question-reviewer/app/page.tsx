'use client';

/* Cambridge Physics 9702 Past Paper Question Reviewer */
/* Aligned with Mathematics 9709, Physics 9702 and Physics 9702 prototypes */
/* eslint-disable next/no-img-element */
import { type ClipboardEvent, useCallback, useEffect, useMemo, useRef, useState } from 'react';
import {
  ArrowLeft,
  ArrowRight,
  Check,
  ChevronLeft,
  ChevronRight,
  CircleAlert,
  CheckCircle2,
  XCircle,
  Eye,
  Flag,
  Info,
  ImagePlus,
  ListFilter,
  Maximize2,
  Minimize2,
  PanelRightOpen,
  Save,
  Search,
  X,
} from 'lucide-react';
import { MathText } from '@/components/player/MathText';
import { AnswerEditor, type SelfMark } from '@/components/player/AnswerEditor';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogTitle,
} from '@/components/ui/dialog';
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from '@/components/ui/resizable';
import { usePanelRef } from 'react-resizable-panels';
import 'katex/dist/katex.min.css';

type QuestionRef = { id: string; number: number; issues: number };
type Paper = {
  id: string;
  paper_code: string;
  year: number;
  session: string;
  variant: string | number;
  questions: QuestionRef[];
};
type ComponentGroup = { id: string; name: string; papers: Paper[] };
type Index = { components: ComponentGroup[]; questionCount: number; issueCount: number };

type Part = {
  id: string;
  label: string;
  part_stem?: string | null;
  text: string;
  marks: number | null;
  answer_prompt?: string | null;
  unit?: string | null;
  dependencies?: unknown[];
  figureIds?: string[];
  figures?: Figure[];
  enrichment?: Record<string, unknown> | null;
  markscheme?: Record<string, unknown> | null;
  markscheme_points?: Array<{ tag?: string | null; text: string; guidance?: string | null }>;
  hints?: string[];
  proper_answer?: string | null;
  walkthrough?: string[];
};

type Figure = {
  id: string;
  label?: string;
  url: string;
};

type MCQOptionInfo = {
  status: string;
  explanation: string;
};

type MCQEnrichment = {
  question_num?: number;
  correct_answer?: string;
  hints?: string[];
  teacher_walkthrough?: string[];
  options_breakdown?: Record<string, MCQOptionInfo>;
};

type Question = {
  id: string;
  component: string;
  paperCode: string;
  number: number;
  year: number;
  session: string;
  variant: string | number;
  title: string;
  stem: string;
  marks: number | null;
  parts: Part[];
  figures: Figure[];
  stemFigures?: Figure[];
  questionImage?: string | null;
  questionPrintableImage?: string | null;
  questionCompactImage?: string | null;
  markschemeImage?: string | null;
  isMcq: boolean;
  options?: string[];
  correctAnswer?: string;
  enrichment: MCQEnrichment | Record<string, unknown> | null;
  markscheme: Record<string, unknown> | null;
  issues: string[];
  sourcePath: string;
};

type ReviewAttachment = {
  name: string;
  path: string;
  url: string;
  mimeType: string;
  createdAt: string;
};
type Review = {
  decision: 'pass' | 'flag' | 'draft';
  note: string;
  updatedAt: string;
  attachments?: ReviewAttachment[];
};
type PaperReviewStatus = 'passed' | 'not-started' | 'needs-attention';
type SupportTab = 'scheme' | 'hints' | 'walkthrough' | 'scan';
type GroundTruthMode = 'printable' | 'compact' | 'markscheme';

type DigitizedMarkSchemePoint = {
  tag?: string | null;
  text: string;
  guidance?: string | null;
};

type DigitizedMarkSchemePart = {
  id?: string;
  label?: string;
  marks?: number;
  marking_points?: DigitizedMarkSchemePoint[];
};

type DigitizedMarkScheme = {
  total_marks?: number;
  parts?: DigitizedMarkSchemePart[];
};

const REVIEW_KEY = 'physics-past-paper-question-reviews-v1';

export default function Home() {
  const [index, setIndex] = useState<Index | null>(null);
  const [componentId, setComponentId] = useState('p1');
  const [paperId, setPaperId] = useState('');
  const [questionIndex, setQuestionIndex] = useState(0);
  const [question, setQuestion] = useState<Question | null>(null);
  const [tab, setTab] = useState<SupportTab>('scheme');
  const [dock, setDock] = useState(true);
  const [libraryOpen, setLibraryOpen] = useState(false);
  const [search, setSearch] = useState('');
  const [statusFilter, setStatusFilter] = useState<
    'all' | 'not-started' | 'passed' | 'needs-attention'
  >('all');
  const [zoom, setZoom] = useState<string | null>(null);
  const [reviews, setReviews] = useState<Record<string, Review>>({});
  const reviewsRef = useRef<Record<string, Review>>({});
  const [reviewsLoaded, setReviewsLoaded] = useState(false);
  const [note, setNote] = useState('');
  const [saved, setSaved] = useState(false);
  const [uploadingImage, setUploadingImage] = useState(false);

  // View state for theory questions: clean digital, printable scan or compact scan.
  const [theoryViewMode, setTheoryViewMode] = useState<'digital' | 'printable' | 'compact' | 'split'>('digital');
  const [partId, setPartId] = useState<string>('');
  // Scan mode for full paper PDF iframe
  const [groundTruthMode, setGroundTruthMode] = useState<GroundTruthMode>('printable');
  // Interactive MCQ student selection
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [showAnswer, setShowAnswer] = useState(false);
  const [showExtractedText, setShowExtractedText] = useState(false);

  // Student answer inputs & self-marking (parity with Mathematics 9709)
  const ANSWERS_STORAGE_KEY = 'physics-student-answers-v1';
  const SELFMARKS_STORAGE_KEY = 'physics-student-selfmarks-v1';
  const [answers, setAnswers] = useState<Record<string, string>>(() => {
    if (typeof window === 'undefined') return {};
    try {
      return JSON.parse(localStorage.getItem(ANSWERS_STORAGE_KEY) || '{}');
    } catch {
      return {};
    }
  });
  const [selfMarks, setSelfMarks] = useState<Record<string, SelfMark>>(() => {
    if (typeof window === 'undefined') return {};
    try {
      return JSON.parse(localStorage.getItem(SELFMARKS_STORAGE_KEY) || '{}');
    } catch {
      return {};
    }
  });

  function updateAnswer(pid: string, val: string) {
    setAnswers((prev) => {
      const next = { ...prev, [pid]: val };
      try {
        localStorage.setItem(ANSWERS_STORAGE_KEY, JSON.stringify(next));
      } catch {}
      return next;
    });
  }

  function updateSelfMark(pid: string, mark?: SelfMark) {
    setSelfMarks((prev) => {
      const next = { ...prev };
      if (mark) {
        next[pid] = mark;
      } else {
        delete next[pid];
      }
      try {
        localStorage.setItem(SELFMARKS_STORAGE_KEY, JSON.stringify(next));
      } catch {}
      return next;
    });
  }

  const pane = useRef<HTMLElement>(null);
  const supportPanel = usePanelRef();

  // Load index data
  useEffect(() => {
    void fetch('/data/index.json')
      .then((response) => response.json() as Promise<Index>)
      .then((data) => {
        setIndex(data);
        const params = new URLSearchParams(window.location.search);
        const pParam = params.get('paper');
        const cParam = params.get('component');
        const qParam = params.get('q');

        let targetComponent = data.components[0]?.id || 'p1';
        let targetPaper = data.components[0]?.papers[0]?.id || '';

        if (pParam) {
          for (const comp of data.components) {
            if (comp.papers.some((p) => p.id === pParam)) {
              targetComponent = comp.id;
              targetPaper = pParam;
              break;
            }
          }
        } else if (cParam && data.components.some((c) => c.id === cParam)) {
          targetComponent = cParam;
          const comp = data.components.find((c) => c.id === cParam);
          targetPaper = comp?.papers[0]?.id || '';
        }

        setComponentId(targetComponent);
        setPaperId(targetPaper);

        if (qParam) {
          const parsedQ = parseInt(qParam, 10);
          if (!isNaN(parsedQ) && parsedQ >= 1) {
            setQuestionIndex(parsedQ - 1);
          }
        }
      })
      .catch(() => setIndex({ components: [], questionCount: 0, issueCount: 1 }));
  }, []);

  // Load reviews from review_server / local storage
  useEffect(() => {
    void fetch('/api/reviews', { cache: 'no-store' })
      .then((response) => {
        if (!response.ok) throw new Error('Review state unavailable');
        return response.json() as Promise<{ reviews: Record<string, Review> }>;
      })
      .then((payload) => {
        reviewsRef.current = payload.reviews || {};
        setReviews(payload.reviews || {});
        localStorage.setItem(REVIEW_KEY, JSON.stringify(payload.reviews || {}));
        setReviewsLoaded(true);
      })
      .catch(() => {
        try {
          const fallback = JSON.parse(localStorage.getItem(REVIEW_KEY) || '{}') as Record<string, Review>;
          reviewsRef.current = fallback;
          setReviews(fallback);
        } catch {
          setReviews({});
        }
        setReviewsLoaded(true);
      });
  }, []);

  const component = index?.components.find((item) => item.id === componentId);
  const paper = component?.papers.find((item) => item.id === paperId) || component?.papers[0];
  const questionRef = paper?.questions[questionIndex];

  // Load question data
  useEffect(() => {
    if (!questionRef || !reviewsLoaded) return;
    void fetch(`/data/questions/${questionRef.id}.json`)
      .then((response) => response.json() as Promise<Question>)
      .then((data) => {
        setQuestion(data);
        setNote(reviewsRef.current[data.id]?.note || '');
        setSelectedOption(null);
        setShowAnswer(false);
        const firstMarked = data.parts?.find((p) => p.marks !== null && p.marks > 0) || data.parts?.[0];
        setPartId(firstMarked?.id || '');
        pane.current?.scrollTo({ top: 0 });
      })
      .catch(() => setQuestion(null));
  }, [questionRef, reviewsLoaded]);

  // Support panel collapse / expand
  useEffect(() => {
    if (dock) supportPanel.current?.expand();
    else supportPanel.current?.collapse();
  }, [dock, supportPanel]);

  const filteredPapers = useMemo(() => {
    const query = search.trim().toLowerCase();
    return (component?.papers || []).filter((candidate) => {
      if (query && !`${candidate.id} ${candidate.year} ${candidate.session}`.toLowerCase().includes(query)) {
        return false;
      }
      if (statusFilter === 'all') return true;
      const paperStatus: PaperReviewStatus = candidate.questions.every(
        (item) => reviews[item.id]?.decision === 'pass',
      )
        ? 'passed'
        : candidate.questions.every((item) => !reviews[item.id])
          ? 'not-started'
          : 'needs-attention';
      return paperStatus === statusFilter;
    });
  }, [component, search, statusFilter, reviews]);

  function chooseComponent(id: string) {
    const next = index?.components.find((item) => item.id === id);
    setComponentId(id);
    setPaperId(next?.papers[0]?.id || '');
    setQuestionIndex(0);
  }

  function choosePaper(id: string) {
    setPaperId(id);
    setQuestionIndex(0);
    setLibraryOpen(false);
  }

  const persist = useCallback((questionId: string, reviewData: Review) => {
    void fetch('/api/reviews', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question_id: questionId, review: reviewData }),
    })
      .then((response) => {
        if (!response.ok) throw new Error('Could not save review file');
        return response.json() as Promise<{ reviews: Record<string, Review> }>;
      })
      .then((payload) => {
        const canonical = payload.reviews || {};
        reviewsRef.current = canonical;
        setReviews(canonical);
        localStorage.setItem(REVIEW_KEY, JSON.stringify(canonical));
        setSaved(true);
        window.setTimeout(() => setSaved(false), 1800);
      })
      .catch(() => setSaved(false));
  }, []);

  async function pasteReviewImages(event: ClipboardEvent<HTMLTextAreaElement>) {
      if (!question) return;
      const images = Array.from(event.clipboardData.items)
        .filter((item) => item.kind === 'file' && item.type.startsWith('image/'))
        .map((item) => item.getAsFile())
        .filter((file): file is File => Boolean(file));
      if (!images.length) return;
      event.preventDefault();
      setUploadingImage(true);
      try {
        const uploaded: ReviewAttachment[] = [];
        for (const file of images) {
          const response = await fetch(`/api/review-images?question_id=${encodeURIComponent(question.id)}`, {
            method: 'POST',
            headers: { 'Content-Type': file.type },
            body: file,
          });
          if (!response.ok) throw new Error('Could not save pasted image');
          const payload = (await response.json()) as { attachment: ReviewAttachment };
          uploaded.push(payload.attachment);
        }
        const current = reviewsRef.current[question.id];
        const reviewData: Review = {
          decision: current?.decision || 'draft',
          note: note.trim(),
          updatedAt: new Date().toISOString(),
          attachments: [...(current?.attachments || []), ...uploaded],
        };
        const next = { ...reviewsRef.current, [question.id]: reviewData };
        reviewsRef.current = next;
        setReviews(next);
        persist(question.id, reviewData);
      } finally {
        setUploadingImage(false);
      }
  }

  const saveDraft = useCallback(() => {
    if (!question || !note.trim() || reviews[question.id]?.note === note.trim()) return;
    const decision = reviews[question.id]?.decision || 'draft';
    const next = {
      ...reviews,
      [question.id]: {
        decision,
        note: note.trim(),
        updatedAt: new Date().toISOString(),
        attachments: reviews[question.id]?.attachments || [],
      },
    };
    reviewsRef.current = next;
    setReviews(next);
    persist(question.id, next[question.id]);
  }, [note, persist, question, reviews]);

  const navigate = useCallback(
    (delta: number) => {
      if (!paper) return;
      saveDraft();
      const next = Math.max(0, Math.min(paper.questions.length - 1, questionIndex + delta));
      setQuestionIndex(next);
    },
    [paper, questionIndex, saveDraft],
  );

  // Keyboard navigation
  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes((e.target as HTMLElement)?.tagName)) {
        return;
      }
      if (e.key === 'ArrowLeft') {
        navigate(-1);
      } else if (e.key === 'ArrowRight') {
        navigate(1);
      }
    }
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [navigate]);

  function saveReview(decision: 'pass' | 'flag') {
    if (!question) return;
    const next = {
      ...reviews,
      [question.id]: {
        decision,
        note: note.trim(),
        updatedAt: new Date().toISOString(),
        attachments: reviews[question.id]?.attachments || [],
      },
    };
    reviewsRef.current = next;
    setReviews(next);
    persist(question.id, next[question.id]);
  }

  const review = question ? reviews[question.id] : undefined;
  const part = question?.parts.find((item) => item.id === partId) || question?.parts?.[0];

  // Active question image logic
  const activeTheoryImage =
    theoryViewMode === 'printable'
      ? question?.questionPrintableImage || question?.questionImage
      : question?.questionCompactImage || question?.questionPrintableImage || question?.questionImage;

  return (
    <div className={`studio review-studio ${dock ? '' : 'focus-mode'}`}>
      <header className="topbar">
        <div className="brand">
          <span className="brandmark">K</span>Kognitiv
          <span className="brand-divider" />
          <span className="workspace-label">Physics Review studio</span>
        </div>
        <div className="flex items-center gap-3">
          <button
            className="quiet flex items-center gap-1.5 px-2.5 py-1 text-xs font-medium rounded-md border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900"
            onClick={() => setLibraryOpen(true)}
          >
            <ListFilter size={14} />
            <span>{paper?.paper_code || paper?.id || 'Select Paper'}</span>
          </button>
          <span className="prototype-label hidden sm:inline-block">Cambridge 9702</span>
        </div>
        <button
          className="icon-button focus-button"
          aria-label={dock ? 'Enter focus mode' : 'Show support'}
          onClick={() => setDock(!dock)}
        >
          {dock ? <Maximize2 size={17} /> : <Minimize2 size={17} />}
        </button>
        <span className="avatar">C</span>
      </header>

      <div className="workspace">
        <ResizablePanelGroup orientation="horizontal" disabled={!dock} className="player-split">
          <ResizablePanel id="question" defaultSize="62%" minSize="340px" className="question-slot">
            <main className="question-pane" ref={pane}>
              <div className="question-inner">
                <nav className="breadcrumbs" aria-label="Breadcrumb">
                  <button onClick={() => setLibraryOpen(true)}>
                    <ArrowLeft size={15} />Papers
                  </button>
                  <ChevronRight size={13} />
                  <span>{component?.name || 'Physics'}</span>
                  <ChevronRight size={13} />
                  <span>{question?.paperCode || 'Loading'}</span>
                </nav>

                {question ? (
                  <>
                    <div className="question-heading">
                      <div>
                        <h1>
                          Question {question.number}
                          <Info size={17} className="inline-info" />
                        </h1>
                        <p className="source-line">
                          {question.session} {question.year} · Paper {question.variant} · {question.id}
                        </p>
                      </div>
                      <div className="question-actions">
                        {question.issues.length > 0 && (
                          <span className="issue-badge">
                            <CircleAlert size={14} />
                            {question.issues.length} notice{question.issues.length === 1 ? '' : 's'}
                          </span>
                        )}
                        <button className="quiet" onClick={() => setLibraryOpen(true)}>
                          <ListFilter size={15} />Browse papers
                        </button>
                      </div>
                    </div>

                    {question.issues.length > 0 && (
                      <div className="issue-list">
                        {question.issues.map((issue) => (
                          <span key={issue}>{issue}</span>
                        ))}
                      </div>
                    )}

                    <section className={`review-panel review-panel-top ${review?.decision || ''}`}>
                      <div className="review-panel-head">
                        <div>
                          <span className="eyebrow">Your review</span>
                          <h2>
                            {review?.decision === 'pass'
                              ? 'Passed'
                              : review?.decision === 'flag'
                              ? 'Flagged'
                              : review?.decision === 'draft'
                              ? 'Draft saved'
                              : 'Not reviewed'}
                          </h2>
                        </div>
                        {saved && (
                          <span className="saved-state">
                            <Save size={14} />Saved to review file
                          </span>
                        )}
                      </div>
                      <Textarea
                        value={note}
                        onChange={(event) => setNote(event.target.value)}
                        onPaste={pasteReviewImages}
                        onBlur={saveDraft}
                        placeholder="Describe the issue, then paste a screenshot here if useful…"
                        aria-label="Review note"
                      />
                      <div className="review-image-help">
                        <ImagePlus size={15} />
                        {uploadingImage ? 'Saving pasted image…' : 'Paste an image into the note to attach it for the AI fixer.'}
                      </div>
                      {!!review?.attachments?.length && (
                        <div className="review-attachments" aria-label="Attached review images">
                          {review.attachments.map((attachment) => (
                            <a key={attachment.path} href={attachment.url} target="_blank" rel="noreferrer">
                              <img src={attachment.url} alt={attachment.name} />
                              <span>{attachment.name}</span>
                            </a>
                          ))}
                        </div>
                      )}
                      <div className="review-buttons">
                        <Button className="pass-button" onClick={() => saveReview('pass')}>
                          <Check size={16} />Pass question
                        </Button>
                        <Button variant="outline" className="flag-button" onClick={() => saveReview('flag')}>
                          <Flag size={16} />Flag for correction
                        </Button>
                      </div>
                    </section>

                    <article className="question-paper">
                      {/* P1 MCQ Question Layout */}
                      {question.isMcq ? (
                        <div className="mcq-container space-y-4">
                          {question.questionImage && (
                            <figure className="figure-wrap relative">
                              <img
                                src={question.questionImage}
                                alt={`Question ${question.number}`}
                                className="w-full rounded-md border border-slate-200 dark:border-slate-800"
                              />
                              <button
                                className="zoom-figure absolute top-2 right-2 bg-white/90 p-1.5 rounded-md shadow-xs"
                                aria-label="Enlarge question diagram"
                                onClick={() => setZoom(question.questionImage!)}
                              >
                                <Maximize2 size={14} />
                              </button>
                            </figure>
                          )}

                          {/* Extracted text toggle for P1 */}
                          {question.stem && (
                            <div className="mt-3">
                              <button
                                type="button"
                                onClick={() => setShowExtractedText(!showExtractedText)}
                                className="text-xs text-slate-500 hover:text-slate-800 dark:hover:text-slate-200 flex items-center gap-1 mb-2 cursor-pointer"
                              >
                                <Eye size={13} />
                                {showExtractedText ? 'Hide extracted text' : 'Show extracted text'}
                              </button>
                              {showExtractedText && (
                                <div className="p-3 bg-slate-50 dark:bg-slate-900 rounded-md border border-slate-200 dark:border-slate-800 text-sm whitespace-pre-wrap font-mono">
                                  <MathText text={question.stem} />
                                </div>
                              )}
                            </div>
                          )}

                          {/* MCQ Option selector buttons */}
                          <div className="mcq-options-panel p-4 bg-slate-50 dark:bg-slate-900/60 rounded-xl border border-slate-200 dark:border-slate-800 space-y-3 mt-4">
                            <div className="flex items-center justify-between">
                              <span className="text-xs font-semibold uppercase tracking-wider text-slate-500">
                                Select Answer (1 Mark)
                              </span>
                              <button
                                type="button"
                                onClick={() => setShowAnswer(!showAnswer)}
                                className="text-xs text-emerald-700 dark:text-emerald-400 hover:underline font-medium cursor-pointer"
                              >
                                {showAnswer ? 'Hide answer' : 'Reveal official answer'}
                              </button>
                            </div>

                            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
                              {(question.options || ['A', 'B', 'C', 'D']).map((opt) => {
                                const isSelected = selectedOption === opt;
                                const isCorrect = question.correctAnswer?.toUpperCase() === opt.toUpperCase();
                                let btnClasses =
                                  'h-12 text-base font-bold rounded-lg border transition-all flex items-center justify-center gap-2 cursor-pointer ';

                                if (showAnswer) {
                                  if (isCorrect) {
                                    btnClasses +=
                                      'border-emerald-500 bg-emerald-50 text-emerald-800 dark:bg-emerald-950/50 dark:text-emerald-300';
                                  } else if (isSelected) {
                                    btnClasses +=
                                      'border-rose-400 bg-rose-50 text-rose-800 dark:bg-rose-950/50 dark:text-rose-300';
                                  } else {
                                    btnClasses +=
                                      'border-slate-200 bg-white text-slate-700 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-300 opacity-60';
                                  }
                                } else if (isSelected) {
                                  if (isCorrect) {
                                    btnClasses +=
                                      'border-emerald-500 bg-emerald-50 text-emerald-800 dark:bg-emerald-950/50 dark:text-emerald-300 ring-2 ring-emerald-400/20';
                                  } else {
                                    btnClasses +=
                                      'border-rose-400 bg-rose-50 text-rose-800 dark:bg-rose-950/50 dark:text-rose-300 ring-2 ring-rose-400/20';
                                  }
                                } else {
                                  btnClasses +=
                                    'border-slate-200 bg-white text-slate-800 hover:border-slate-400 dark:border-slate-700 dark:bg-slate-950 dark:text-slate-200';
                                }

                                return (
                                  <button
                                    key={opt}
                                    type="button"
                                    className={btnClasses}
                                    onClick={() => {
                                      setSelectedOption(opt);
                                      setShowAnswer(true);
                                    }}
                                  >
                                    <span>Option {opt}</span>
                                    {showAnswer && isCorrect && <CheckCircle2 size={16} className="text-emerald-600" />}
                                    {showAnswer && isSelected && !isCorrect && (
                                      <XCircle size={16} className="text-rose-600" />
                                    )}
                                  </button>
                                );
                              })}
                            </div>

                            {showAnswer && (
                              <div className="pt-2 text-xs text-slate-600 dark:text-slate-400 flex items-center justify-between border-t border-slate-200 dark:border-slate-800">
                                <span>Official key: <strong className="text-emerald-700 dark:text-emerald-400">{question.correctAnswer}</strong></span>
                                {selectedOption && (
                                  <span>
                                    {selectedOption.toUpperCase() === question.correctAnswer?.toUpperCase()
                                      ? '✅ Correct selection'
                                      : '❌ Incorrect selection'}
                                  </span>
                                )}
                              </div>
                            )}
                          </div>
                        </div>
                      ) : (
                        /* P2 & P4 Structured Theory Question Layout */
                        <div className="theory-container space-y-4">
                          {/* View Mode Toolbar */}
                          <div className="flex flex-wrap items-center justify-between bg-slate-100 dark:bg-slate-900 p-1.5 rounded-lg border border-slate-200 dark:border-slate-800 gap-2">
                            <div className="flex items-center gap-1.5">
                              <span className="text-xs font-semibold px-2 text-slate-600 dark:text-slate-400">
                                Display View:
                              </span>
                              <div className="flex items-center gap-1 bg-white/80 dark:bg-slate-800/80 p-0.5 rounded-md border border-slate-200 dark:border-slate-700/60">
                                <button
                                  type="button"
                                  onClick={() => setTheoryViewMode('digital')}
                                  className={`text-xs px-3 py-1 font-medium rounded-md transition-colors cursor-pointer flex items-center gap-1.5 ${
                                    theoryViewMode === 'digital'
                                      ? 'bg-emerald-600 text-white shadow-xs'
                                      : 'text-slate-600 hover:text-slate-900 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-700/50'
                                  }`}
                                >
                                  <span>Digital Question</span>
                                  <span className="text-[10px] uppercase font-bold opacity-90 bg-emerald-700 px-1 rounded">Clean</span>
                                </button>
                                <button
                                  type="button"
                                  onClick={() => setTheoryViewMode('printable')}
                                  className={`text-xs px-3 py-1 font-medium rounded-md transition-colors cursor-pointer ${
                                    theoryViewMode === 'printable'
                                      ? 'bg-white dark:bg-slate-800 text-emerald-800 dark:text-emerald-300 shadow-xs'
                                      : 'text-slate-600 hover:text-slate-900 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-700/50'
                                  }`}
                                >
                                  Printable Scan
                                </button>
                                <button
                                  type="button"
                                  onClick={() => setTheoryViewMode('compact')}
                                  className={`text-xs px-3 py-1 font-medium rounded-md transition-colors cursor-pointer ${
                                    theoryViewMode === 'compact'
                                      ? 'bg-white dark:bg-slate-800 text-emerald-800 dark:text-emerald-300 shadow-xs'
                                      : 'text-slate-600 hover:text-slate-900 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-700/50'
                                  }`}
                                >
                                  Compact Scan
                                </button>
                              </div>
                            </div>

                            <div className="flex items-center gap-2">
                              {question.marks !== null && (
                                <span className="text-xs font-semibold px-2.5 py-1 bg-slate-200/80 dark:bg-slate-800 rounded-md text-slate-700 dark:text-slate-300">
                                  Total: {question.marks} marks
                                </span>
                              )}
                            </div>
                          </div>

                          {/* Digital Clean Question View */}
                          {theoryViewMode === 'digital' && (
                            <div className="digital-question-container space-y-5">
                              {question.stem && (
                                <div className="question-stem text-slate-900 dark:text-slate-100 font-normal mb-4 leading-relaxed text-base">
                                  <MathText text={question.stem} />
                                  {question.stemFigures && question.stemFigures.length > 0 && (
                                    <div className="stem-figures space-y-3 my-3">
                                      {question.stemFigures.map((fig) => (
                                        <figure
                                          key={fig.id}
                                          className="figure-wrap p-3 bg-slate-50 dark:bg-slate-850 rounded-xl border border-slate-200/80 dark:border-slate-800 relative flex flex-col items-center shadow-xs"
                                        >
                                          <div className="w-full text-xs font-semibold text-slate-600 dark:text-slate-400 mb-2 flex items-center justify-between">
                                            <span className="font-mono text-emerald-700 dark:text-emerald-400 font-bold">
                                              {fig.label || fig.id}
                                            </span>
                                          </div>
                                          <img
                                            src={fig.url}
                                            alt={fig.label || fig.id}
                                            className="max-h-72 sm:max-h-84 w-auto object-contain rounded-md"
                                          />
                                          <button
                                            type="button"
                                            className="zoom-figure absolute top-2 right-2 bg-white/90 dark:bg-slate-800/90 p-1.5 rounded-md shadow-xs border border-slate-200 dark:border-slate-700 hover:bg-white cursor-pointer"
                                            aria-label="Enlarge diagram"
                                            onClick={() => setZoom(fig.url)}
                                          >
                                            <Maximize2 size={14} />
                                          </button>
                                        </figure>
                                      ))}
                                    </div>
                                  )}
                                </div>
                              )}

                              {/* Question parts */}
                              <div className="question-parts space-y-5">
                                {question.parts.map((item) => {
                                  const cleanLabel = item.label ? item.label.replace(/[()]/g, '').trim() : '';
                                  const showBadge = Boolean(cleanLabel);
                                  const isSelected = item.id === part?.id;
                                  const isIntroSection = (!item.marks || item.marks === 0) && !item.text && item.part_stem;

                                  if (isIntroSection) {
                                    return (
                                      <div
                                        key={item.id}
                                        className="intro-section p-3.5 bg-slate-50 dark:bg-slate-850/70 rounded-xl border border-slate-200/80 dark:border-slate-800 text-slate-800 dark:text-slate-200 text-sm sm:text-base leading-relaxed"
                                      >
                                        <div className="flex items-start gap-2.5">
                                          <span className="font-bold text-slate-900 dark:text-slate-100 shrink-0">
                                            ({cleanLabel})
                                          </span>
                                          <div className="flex-1">
                                            <MathText text={item.part_stem!} />
                                          </div>
                                        </div>
                                        {item.figures && item.figures.length > 0 && (
                                          <div className="part-figures space-y-3 my-3">
                                            {item.figures.map((fig) => (
                                              <figure
                                                key={fig.id}
                                                className="figure-wrap p-3 bg-white dark:bg-slate-900 rounded-xl border border-slate-200/80 dark:border-slate-800 relative flex flex-col items-center shadow-xs"
                                              >
                                                <div className="w-full text-xs font-semibold text-slate-600 dark:text-slate-400 mb-2 flex items-center justify-between">
                                                  <span className="font-mono text-emerald-700 dark:text-emerald-400 font-bold">
                                                    {fig.label || fig.id}
                                                  </span>
                                                </div>
                                                <img
                                                  src={fig.url}
                                                  alt={fig.label || fig.id}
                                                  className="max-h-72 w-auto object-contain rounded-md"
                                                />
                                                <button
                                                  type="button"
                                                  className="zoom-figure absolute top-2 right-2 bg-white/90 p-1.5 rounded-md shadow-xs"
                                                  onClick={() => setZoom(fig.url)}
                                                >
                                                  <Maximize2 size={14} />
                                                </button>
                                              </figure>
                                            ))}
                                          </div>
                                        )}
                                      </div>
                                    );
                                  }

                                  return (
                                    <section
                                      key={item.id}
                                      id={`part-${item.id}`}
                                      className={`question-part rounded-xl p-4 sm:p-5 transition-all bg-white dark:bg-slate-900 border ${
                                        isSelected
                                          ? 'border-emerald-500/60 ring-2 ring-emerald-500/10 shadow-xs'
                                          : 'border-slate-200/80 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
                                      }`}
                                    >
                                      <div className="part-head flex items-start gap-3.5">
                                        {showBadge && (
                                          <button
                                            type="button"
                                            onClick={() => setPartId(item.id)}
                                            className={`part-badge shrink-0 font-bold text-xs px-2.5 py-1 rounded-md transition-colors cursor-pointer ${
                                              isSelected
                                                ? 'bg-slate-900 text-white dark:bg-slate-100 dark:text-slate-900 shadow-xs'
                                                : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                                            }`}
                                          >
                                            ({cleanLabel})
                                          </button>
                                        )}

                                        <div className="part-body flex-1 text-slate-800 dark:text-slate-200 leading-relaxed text-sm sm:text-base">
                                          {item.part_stem && (
                                            <div className="part-stem font-medium text-slate-900 dark:text-slate-100 mb-2">
                                              <MathText text={item.part_stem} />
                                            </div>
                                          )}

                                          {/* Inline Part Figures right inside the subpart where they belong */}
                                          {item.figures && item.figures.length > 0 && (
                                            <div className="part-figures space-y-3 my-3">
                                              {item.figures.map((fig) => (
                                                <figure
                                                  key={fig.id}
                                                  className="figure-wrap p-3 bg-slate-50 dark:bg-slate-850 rounded-xl border border-slate-200/80 dark:border-slate-800 relative flex flex-col items-center shadow-xs"
                                                >
                                                  <div className="w-full text-xs font-semibold text-slate-600 dark:text-slate-400 mb-2 flex items-center justify-between">
                                                    <span className="font-mono text-emerald-700 dark:text-emerald-400 font-bold">
                                                      {fig.label || fig.id}
                                                    </span>
                                                    <span className="text-[11px] text-slate-400">Click to enlarge</span>
                                                  </div>
                                                  <img
                                                    src={fig.url}
                                                    alt={fig.label || fig.id}
                                                    className="max-h-72 sm:max-h-84 w-auto object-contain rounded-md"
                                                  />
                                                  <button
                                                    type="button"
                                                    className="zoom-figure absolute top-2 right-2 bg-white/90 dark:bg-slate-800/90 p-1.5 rounded-md shadow-xs border border-slate-200 dark:border-slate-700 hover:bg-white cursor-pointer"
                                                    aria-label="Enlarge diagram"
                                                    onClick={() => setZoom(fig.url)}
                                                  >
                                                    <Maximize2 size={14} />
                                                  </button>
                                                </figure>
                                              ))}
                                            </div>
                                          )}

                                          {item.text && (
                                            <div className="part-text">
                                              <MathText text={item.text} />
                                            </div>
                                          )}
                                        </div>

                                        {item.marks !== null && item.marks > 0 && (
                                          <span className="part-marks shrink-0 text-xs font-semibold text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded-sm">
                                            [{item.marks}]
                                          </span>
                                        )}
                                      </div>

                                      {/* Student Answer Block with formula preview, symbols and self-marking */}
                                      {item.marks !== null && item.marks > 0 && (
                                        <AnswerEditor
                                          id={item.id}
                                          value={answers[item.id] || ''}
                                          onChange={(val) => updateAnswer(item.id, val)}
                                          onFocus={() => setPartId(item.id)}
                                          onScheme={() => {
                                            setPartId(item.id);
                                            setTab('scheme');
                                            setDock(true);
                                          }}
                                          onHints={() => {
                                            setPartId(item.id);
                                            setTab('hints');
                                            setDock(true);
                                          }}
                                          onWalkthrough={() => {
                                            setPartId(item.id);
                                            setTab('walkthrough');
                                            setDock(true);
                                          }}
                                          marks={item.marks}
                                          answerPrompt={item.answer_prompt || undefined}
                                          unit={item.unit || undefined}
                                          selfMark={selfMarks[item.id]}
                                          onSelfMarkChange={(mark) => updateSelfMark(item.id, mark)}
                                        />
                                      )}
                                    </section>
                                  );
                                })}
                              </div>
                            </div>
                          )}

                          {/* Printable or Compact Single Scan View */}
                          {(theoryViewMode === 'printable' || theoryViewMode === 'compact') && (
                            <div className="scan-view space-y-4">
                              {activeTheoryImage && (
                                <figure className="figure-wrap relative">
                                  <img
                                    src={activeTheoryImage}
                                    alt={`Question ${question.number} (${theoryViewMode})`}
                                    className="w-full rounded-md border border-slate-200 dark:border-slate-800"
                                  />
                                  <button
                                    className="zoom-figure absolute top-2 right-2 bg-white/90 p-1.5 rounded-md shadow-xs cursor-pointer"
                                    aria-label="Enlarge question scan"
                                    onClick={() => setZoom(activeTheoryImage)}
                                  >
                                    <Maximize2 size={14} />
                                  </button>
                                </figure>
                              )}
                            </div>
                          )}

                          {/* Split View (Digital Question + Official Scan Side-by-Side) */}
                          {theoryViewMode === 'split' && (
                            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                              <div className="bg-white dark:bg-slate-900 rounded-xl p-5 border border-slate-200 dark:border-slate-800 text-sm leading-relaxed overflow-y-auto max-h-[85vh] space-y-4">
                                <div className="text-xs font-semibold uppercase text-emerald-700 dark:text-emerald-400 pb-1.5 border-b border-slate-200 dark:border-slate-800">
                                  Clean Digital OCR Version
                                </div>
                                {question.stem && (
                                  <div className="question-stem mb-3">
                                    <MathText text={question.stem} />
                                  </div>
                                )}
                                <div className="space-y-3.5">
                                  {question.parts.map((item) => {
                                    const cleanLabel = item.label ? item.label.replace(/[()]/g, '').trim() : '';
                                    const isIntroSection = (!item.marks || item.marks === 0) && !item.text && item.part_stem;

                                    if (isIntroSection) {
                                      return (
                                        <div
                                          key={item.id}
                                          className="p-2.5 bg-slate-100/80 dark:bg-slate-800/80 rounded-lg text-xs leading-relaxed text-slate-800 dark:text-slate-200"
                                        >
                                          <span className="font-bold mr-1.5">({cleanLabel})</span>
                                          <MathText text={item.part_stem!} />
                                        </div>
                                      );
                                    }

                                    return (
                                      <div
                                        key={item.id}
                                        className="p-3 bg-slate-50 dark:bg-slate-850 rounded-lg border border-slate-200 dark:border-slate-700/60"
                                      >
                                        <div className="flex items-start gap-2.5 mb-1.5">
                                          {cleanLabel && (
                                            <span className="part-badge shrink-0 font-bold text-xs px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                                              ({cleanLabel})
                                            </span>
                                          )}
                                          <div className="flex-1">
                                            {item.part_stem && (
                                              <div className="font-medium mb-1 text-slate-900 dark:text-slate-100">
                                                <MathText text={item.part_stem} />
                                              </div>
                                            )}
                                            {item.text && (
                                              <div>
                                                <MathText text={item.text} />
                                              </div>
                                            )}
                                          </div>
                                          {item.marks !== null && item.marks > 0 && (
                                            <span className="text-xs font-semibold bg-slate-200 dark:bg-slate-800 px-1.5 py-0.5 rounded text-slate-700 dark:text-slate-300">
                                              [{item.marks}]
                                            </span>
                                          )}
                                        </div>
                                      </div>
                                    );
                                  })}
                                </div>
                              </div>

                              <div className="bg-white dark:bg-slate-900 rounded-xl p-4 border border-slate-200 dark:border-slate-800 overflow-y-auto max-h-[85vh]">
                                <div className="flex items-center justify-between text-xs font-semibold uppercase text-slate-500 mb-3 pb-1 border-b border-slate-200 dark:border-slate-800">
                                  <span>Official Cambridge Scan</span>
                                  <div className="flex gap-2 text-[11px]">
                                    <button
                                      type="button"
                                      onClick={() => setTheoryViewMode('printable')}
                                      className="text-emerald-600 hover:underline cursor-pointer"
                                    >
                                      Full Printable
                                    </button>
                                    <span className="text-slate-300 dark:text-slate-700">•</span>
                                    <button
                                      type="button"
                                      onClick={() => setTheoryViewMode('compact')}
                                      className="text-emerald-600 hover:underline cursor-pointer"
                                    >
                                      Full Compact
                                    </button>
                                  </div>
                                </div>
                                {activeTheoryImage && (
                                  <figure className="figure-wrap relative">
                                    <img
                                      src={activeTheoryImage}
                                      alt={`Question ${question.number} scan`}
                                      className="w-full rounded border border-slate-200 dark:border-slate-800"
                                    />
                                    <button
                                      className="zoom-figure absolute top-2 right-2 bg-white/90 p-1.5 rounded shadow-xs cursor-pointer"
                                      onClick={() => setZoom(activeTheoryImage)}
                                    >
                                      <Maximize2 size={14} />
                                    </button>
                                  </figure>
                                )}
                              </div>
                            </div>
                          )}

                          {/* Only show unassigned figures at the bottom if any */}
                          {(() => {
                            const assignedFigureIds = new Set(
                              question.parts
                                .flatMap((p) => p.figures?.map((f) => f.id) || [])
                                .concat(question.stemFigures?.map((f) => f.id) || [])
                            );
                            const unassignedFigures = question.figures.filter((f) => !assignedFigureIds.has(f.id));
                            if (unassignedFigures.length === 0) return null;
                            return (
                              <div className="standalone-figures mt-6 pt-4 border-t border-slate-200 dark:border-slate-800">
                                <h3 className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-3">
                                  Additional Diagrams & Figures ({unassignedFigures.length})
                                </h3>
                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                  {unassignedFigures.map((fig) => (
                                    <figure
                                      key={fig.id}
                                      className="figure-wrap p-2 bg-slate-50 dark:bg-slate-900 rounded-lg border border-slate-200 dark:border-slate-800 relative"
                                    >
                                      <div className="text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">
                                        {fig.label || fig.id}
                                      </div>
                                      <img
                                        src={fig.url}
                                        alt={fig.label || fig.id}
                                        className="w-full rounded-sm object-contain max-h-60"
                                      />
                                      <button
                                        className="zoom-figure absolute top-2 right-2 bg-white/90 p-1 rounded-md shadow-xs"
                                        aria-label="Enlarge diagram"
                                        onClick={() => setZoom(fig.url)}
                                      >
                                        <Maximize2 size={12} />
                                      </button>
                                    </figure>
                                  ))}
                                </div>
                              </div>
                            );
                          })()}
                        </div>
                      )}
                    </article>

                    <div className="paper-note">
                      <span>{question.marks ? `${question.marks} marks in total` : 'Structured Theory Question'}</span>
                      {question.parts.some((p) => p.marks && p.marks > 0) && (
                        <span>
                          {question.parts.filter((p) => selfMarks[p.id]).length} /{' '}
                          {question.parts.filter((p) => p.marks && p.marks > 0).length} parts self-marked
                        </span>
                      )}
                      <span>{question.sourcePath}</span>
                    </div>

                  </>
                ) : (
                  <div className="loading-card">Loading question…</div>
                )}
              </div>

              <footer className="question-navigation">
                <button
                  className="secondary previous-question"
                  disabled={!paper || questionIndex === 0}
                  onClick={() => navigate(-1)}
                >
                  <ChevronLeft size={16} />Previous
                </button>
                <span className="question-position">
                  {paper ? `${questionIndex + 1} / ${paper.questions.length}` : '-'}
                </span>
                <button
                  className="primary next-question"
                  disabled={!paper || questionIndex === paper.questions.length - 1}
                  onClick={() => navigate(1)}
                >
                  Next question<ArrowRight size={16} />
                </button>
              </footer>
            </main>
          </ResizablePanel>

          <ResizableHandle className={`player-divider ${dock ? '' : 'divider-hidden'}`} withHandle />
          <ResizablePanel
            id="support"
            defaultSize="38%"
            minSize="340px"
            maxSize="65%"
            collapsible
            collapsedSize="0%"
            panelRef={supportPanel}
            className={`support-slot ${dock ? '' : 'slot-closed'}`}
          >
            <aside className="support-dock review-support" inert={!dock}>
              <div className="dock-heading">
                <span>Support Dock</span>
                <button className="icon-button" onClick={() => setDock(false)} aria-label="Close support">
                  <X size={17} />
                </button>
              </div>

              <Tabs className="support-tabs" value={tab} onValueChange={(value) => setTab(value as SupportTab)}>
                <TabsList className="dock-tabs">
                  <TabsTrigger value="scheme">Mark Scheme</TabsTrigger>
                  <TabsTrigger value="hints">Hints</TabsTrigger>
                  <TabsTrigger value="walkthrough">Walkthrough</TabsTrigger>
                  <TabsTrigger value="scan">Official Scan</TabsTrigger>
                </TabsList>

                <div className="dock-context">
                  <span>Question {question?.number || ''}</span>
                  <span className="text-xs text-slate-500 font-mono">
                    {question?.paperCode || paper?.paper_code}
                  </span>
                </div>

                {/* Mark Scheme Tab */}
                <TabsContent value="scheme" keepMounted className="support-panel">
                  <div className="dock-content">
                    <div className="section-heading">
                      <h2>Official Mark Scheme</h2>
                    </div>

                    {question?.isMcq ? (
                      <div className="p-4 bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800 rounded-lg">
                        <span className="text-xs font-semibold uppercase text-emerald-800 dark:text-emerald-300 block mb-1">
                          Official Answer Key
                        </span>
                        <div className="text-3xl font-bold text-emerald-700 dark:text-emerald-400">
                          {question.correctAnswer || 'Not recorded'}
                        </div>
                        <p className="text-xs text-slate-600 dark:text-slate-400 mt-2">
                          Extracted directly from official Cambridge mark scheme: {question.paperCode}_ms.
                        </p>
                      </div>
                    ) : (
                      <div className="space-y-4">
                        {(() => {
                          const ms = question?.markscheme as unknown as DigitizedMarkScheme | undefined;
                          if (ms?.parts && Array.isArray(ms.parts) && ms.parts.length > 0) {
                            return (
                              <div className="mark-scheme-summary">
                                <div className="mark-scheme-summary-header">
                                  <span className="text-xs font-semibold uppercase text-slate-500">
                                    Digitized Criteria ({ms.total_marks || question?.marks} Marks)
                                  </span>
                                  <span className="mark-scheme-source">
                                    Official criteria
                                  </span>
                                </div>

                                {ms.parts.map((p, pIdx) => (
                                  <div key={pIdx} className="mark-scheme-part">
                                    <div className="mark-scheme-part-header">
                                      <span className="font-bold text-slate-800 dark:text-slate-200">
                                        Part {p.label || `(${pIdx + 1})`}
                                      </span>
                                      <span className="mark-scheme-total">
                                        {p.marks} {p.marks === 1 ? 'mark' : 'marks'}
                                      </span>
                                    </div>

                                    <div className="mark-scheme-points">
                                      {(p.marking_points || []).map((mp, mpIdx) => (
                                        <div key={mpIdx} className="mark-scheme-point">
                                          <div className="flex items-start gap-2">
                                            {mp.tag && (
                                              <span className="mark-scheme-code">
                                                [{mp.tag}]
                                              </span>
                                            )}
                                            <div className="mark-scheme-text">
                                              <MathText text={mp.text} />
                                            </div>
                                          </div>
                                          {mp.guidance && (
                                            <div className="mark-scheme-guidance">
                                              <span className="font-semibold mr-1">Guidance:</span>
                                              <MathText text={mp.guidance} />
                                            </div>
                                          )}
                                        </div>
                                      ))}
                                    </div>
                                  </div>
                                ))}
                              </div>
                            );
                          }
                          return (
                            <p className="text-sm text-slate-500 italic">
                              No structured digitized mark scheme is available for this question.
                            </p>
                          );
                        })()}

                        {question?.markschemeImage ? (
                          <div className="space-y-2 pt-2 border-t border-slate-200 dark:border-slate-800">
                            <span className="text-xs font-semibold uppercase text-slate-500 block">
                              Visual Mark Scheme Slice
                            </span>
                            <figure className="figure-wrap relative">
                              <img
                                src={question.markschemeImage}
                                alt={`Mark Scheme for Question ${question.number}`}
                                className="w-full rounded-md border border-slate-200 dark:border-slate-800"
                              />
                              <button
                                className="zoom-figure absolute top-2 right-2 bg-white/90 p-1.5 rounded-md shadow-xs"
                                aria-label="Enlarge mark scheme"
                                onClick={() => setZoom(question.markschemeImage!)}
                              >
                                <Maximize2 size={14} />
                              </button>
                            </figure>
                          </div>
                        ) : (
                          <div className="p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg text-slate-600 dark:text-slate-400 text-sm">
                            <p className="font-medium text-slate-800 dark:text-slate-200 mb-1">
                              No mark scheme recorded
                            </p>
                            <p className="text-xs leading-relaxed">
                              Mark scheme OCR and structured marking JSON are deferred to the multimodal AI pipeline.
                            </p>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                </TabsContent>

                {/* Hints Tab */}
                <TabsContent value="hints" keepMounted className="support-panel">
                  <div className="dock-content">
                    <div className="section-heading">
                      <h2>Guided Hints</h2>
                    </div>
                    {question?.isMcq ? (
                      question.enrichment && Array.isArray((question.enrichment as Record<string, unknown>).hints) && ((question.enrichment as Record<string, unknown>).hints as string[]).length > 0 ? (
                        <div className="space-y-3">
                          {((question.enrichment as Record<string, unknown>).hints as string[]).map((hint, hIdx) => (
                            <div
                              key={hIdx}
                              className="p-3.5 bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-900/40 rounded-lg text-sm text-amber-950 dark:text-amber-200"
                            >
                              <div className="font-semibold text-xs text-amber-700 dark:text-amber-400 uppercase tracking-wide mb-1">
                                Hint {hIdx + 1}
                              </div>
                              <div className="leading-relaxed">
                                <MathText text={hint.replace(/^Hint\s*\d+\s*:\s*/i, '')} />
                              </div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <div className="p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg text-slate-600 dark:text-slate-400 text-sm">
                          <p className="font-medium text-slate-800 dark:text-slate-200 mb-1">
                            No hints recorded yet
                          </p>
                          <p className="text-xs leading-relaxed">
                            Enrichment will be populated during the AI enrichment phase.
                          </p>
                        </div>
                      )
                    ) : (
                      /* Theory Paper Parts (P2 / P4) */
                      question?.parts && question.parts.some((p) => p.hints && p.hints.length > 0) ? (
                        <div className="space-y-4">
                          {question.parts.map((p, pIdx) => (
                            <div
                              key={pIdx}
                              className="bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-3.5 space-y-2.5"
                            >
                              <div className="flex items-center justify-between pb-1 border-b border-slate-200/80 dark:border-slate-800/80">
                                <span className="font-bold text-slate-800 dark:text-slate-200 text-sm">
                                  Part {p.label || `(${pIdx + 1})`}
                                </span>
                                <span className="text-xs font-semibold bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300 px-2 py-0.5 rounded">
                                  {p.hints?.length || 0} {p.hints?.length === 1 ? 'hint' : 'hints'}
                                </span>
                              </div>
                              <div className="space-y-2">
                                {(p.hints || []).map((hint, hIdx) => (
                                  <div
                                    key={hIdx}
                                    className="p-2.5 bg-white dark:bg-slate-950 border border-amber-200/60 dark:border-amber-900/40 rounded text-xs text-amber-950 dark:text-amber-200 leading-relaxed"
                                  >
                                    <span className="font-semibold text-amber-700 dark:text-amber-400 uppercase tracking-wide mr-1.5">
                                      Hint {hIdx + 1}:
                                    </span>
                                    <MathText text={hint.replace(/^Hint\s*\d+\s*:\s*/i, '')} />
                                  </div>
                                ))}
                              </div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <div className="p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg text-slate-600 dark:text-slate-400 text-sm">
                          <p className="font-medium text-slate-800 dark:text-slate-200 mb-1">
                            No hints recorded yet
                          </p>
                          <p className="text-xs leading-relaxed">
                            Theory enrichment will be populated during the AI enrichment phase.
                          </p>
                        </div>
                      )
                    )}
                  </div>
                </TabsContent>

                {/* Walkthrough Tab */}
                <TabsContent value="walkthrough" keepMounted className="support-panel">
                  <div className="dock-content">
                    <div className="section-heading walk-title">
                      <h2>Teacher Walkthrough</h2>
                    </div>
                    {question?.isMcq ? (
                      (() => {
                        const enr = question.enrichment as MCQEnrichment | null;
                        const walkthrough = enr?.teacher_walkthrough || [];
                        const optionsBreakdown = enr?.options_breakdown;

                        if (walkthrough.length === 0 && !optionsBreakdown) {
                          return null;
                        }

                        return (
                          <div className="space-y-4">
                            {/* Stepped Walkthrough */}
                            {walkthrough.map((step, sIdx) => {
                              const stepMatch = step.match(/^Step\s*\d+\s*:\s*\*\*(.*?)\*\*\s*([\s\S]*)$/i);
                              const stepHeading = stepMatch ? stepMatch[1] : `Step ${sIdx + 1}`;
                              const stepBody = stepMatch ? stepMatch[2] : step.replace(/^Step\s*\d+\s*:\s*/i, '');
                              return (
                                <div
                                  key={sIdx}
                                  className="walk-card p-3.5 bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 rounded-lg text-sm"
                                >
                                  <div className="flex items-center gap-2 mb-1.5">
                                    <span className="px-2 py-0.5 text-xs font-semibold rounded bg-sky-100 dark:bg-sky-950 text-sky-700 dark:text-sky-300">
                                      Step {sIdx + 1}
                                    </span>
                                    <span className="font-semibold text-slate-800 dark:text-slate-200">
                                      {stepHeading}
                                    </span>
                                  </div>
                                  <div className="text-slate-700 dark:text-slate-300 leading-relaxed">
                                    <MathText text={stepBody} />
                                  </div>
                                </div>
                              );
                            })}

                            {/* Options Breakdown if present */}
                            {optionsBreakdown && (
                              <div className="mt-4 pt-4 border-t border-slate-200 dark:border-slate-800">
                                <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2.5">
                                  Options Analysis
                                </h3>
                                <div className="space-y-2">
                                  {Object.entries(optionsBreakdown).map(([opt, info]) => {
                                    const isCorrect = info.status === 'correct';
                                    return (
                                      <div
                                        key={opt}
                                        className={`p-3 rounded-lg border text-xs leading-relaxed ${
                                          isCorrect
                                            ? 'bg-emerald-50/80 dark:bg-emerald-950/20 border-emerald-300 dark:border-emerald-800/60 text-emerald-950 dark:text-emerald-200'
                                            : 'bg-rose-50/50 dark:bg-rose-950/20 border-rose-200 dark:border-rose-900/40 text-rose-950 dark:text-rose-200'
                                        }`}
                                      >
                                        <div className="flex items-center gap-2 mb-1">
                                          <span
                                            className={`font-mono font-bold px-1.5 py-0.5 rounded text-[11px] ${
                                              isCorrect
                                                ? 'bg-emerald-200 dark:bg-emerald-800 text-emerald-900 dark:text-emerald-100'
                                                : 'bg-rose-200 dark:bg-rose-800 text-rose-900 dark:text-rose-100'
                                            }`}
                                          >
                                            Option {opt}
                                          </span>
                                          <span className="font-semibold text-[11px] uppercase tracking-wide">
                                            {isCorrect ? '✓ Correct' : '✗ False'}
                                          </span>
                                        </div>
                                        <div>
                                          <MathText text={info.explanation} />
                                        </div>
                                      </div>
                                    );
                                  })}
                                </div>
                              </div>
                            )}
                          </div>
                        );
                      })() || (
                        <div className="p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg text-slate-600 dark:text-slate-400 text-sm">
                          <p className="font-medium text-slate-800 dark:text-slate-200 mb-1">
                            No walkthrough recorded yet
                          </p>
                          <p className="text-xs leading-relaxed">
                            Step-by-step teacher walkthrough will be generated during the AI enrichment phase.
                          </p>
                        </div>
                      )
                    ) : (
                      /* Theory Paper Parts (P2 / P4) */
                      question?.parts && question.parts.some((p) => p.walkthrough && p.walkthrough.length > 0) ? (
                        <div className="space-y-4">
                          {question.parts.map((p, pIdx) => (
                            <div
                              key={pIdx}
                              className="bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-3.5 space-y-3"
                            >
                              <div className="flex items-center justify-between pb-1 border-b border-slate-200/80 dark:border-slate-800/80">
                                <span className="font-bold text-slate-800 dark:text-slate-200 text-sm">
                                  Part {p.label || `(${pIdx + 1})`}
                                </span>
                                <span className="text-xs font-semibold bg-sky-100 dark:bg-sky-950/60 text-sky-800 dark:text-sky-300 px-2 py-0.5 rounded">
                                  {p.marks} {p.marks === 1 ? 'mark' : 'marks'}
                                </span>
                              </div>
                              {p.proper_answer && (
                                <div className="p-3 bg-emerald-50/60 dark:bg-emerald-950/30 border border-emerald-200/80 dark:border-emerald-800/60 rounded-md text-xs leading-relaxed">
                                  <div className="flex items-center gap-2 mb-1.5">
                                    <span className="px-1.5 py-0.5 text-[10px] font-semibold rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300">
                                      Model Answer
                                    </span>
                                  </div>
                                  <div className="text-slate-800 dark:text-slate-200 font-medium">
                                    <MathText text={p.proper_answer} />
                                  </div>
                                </div>
                              )}
                              <div className="space-y-2">
                                {(p.walkthrough || []).map((step, sIdx) => {
                                  const stepMatch = step.match(/^Step\s*\d+\s*:\s*\*\*(.*?)\*\*\s*([\s\S]*)$/i);
                                  const stepHeading = stepMatch ? stepMatch[1] : `Step ${sIdx + 1}`;
                                  const stepBody = stepMatch ? stepMatch[2] : step.replace(/^Step\s*\d+\s*:\s*/i, '');
                                  return (
                                    <div
                                      key={sIdx}
                                      className="p-3 bg-white dark:bg-slate-950 border border-slate-200/80 dark:border-slate-800/80 rounded-md text-xs leading-relaxed"
                                    >
                                      <div className="flex items-center gap-2 mb-1.5">
                                        <span className="px-1.5 py-0.5 text-[10px] font-semibold rounded bg-sky-100 dark:bg-sky-950 text-sky-700 dark:text-sky-300">
                                          Step {sIdx + 1}
                                        </span>
                                        <span className="font-semibold text-slate-800 dark:text-slate-200">
                                          {stepHeading}
                                        </span>
                                      </div>
                                      <div className="text-slate-700 dark:text-slate-300">
                                        <MathText text={stepBody} />
                                      </div>
                                    </div>
                                  );
                                })}
                              </div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <div className="p-4 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg text-slate-600 dark:text-slate-400 text-sm">
                          <p className="font-medium text-slate-800 dark:text-slate-200 mb-1">
                            No walkthrough recorded yet
                          </p>
                          <p className="text-xs leading-relaxed">
                            Step-by-step teacher walkthrough will be generated during the AI enrichment phase.
                          </p>
                        </div>
                      )
                    )}
                  </div>
                </TabsContent>

                {/* Official Paper Scan Tab */}
                <TabsContent value="scan" keepMounted className="support-panel">
                  <div className="dock-content" style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
                    <div className="section-heading">
                      <h2>Official Paper & Mark Scheme PDFs</h2>
                    </div>
                    <div style={{ display: 'flex', gap: '8px', marginBottom: '12px' }}>
                      <button
                        type="button"
                        className={`quiet ${groundTruthMode === 'printable' ? 'active' : ''}`}
                        style={{
                          fontWeight: groundTruthMode === 'printable' ? 700 : 400,
                          padding: '5px 10px',
                          borderRadius: '6px',
                          border: '1px solid #ccd9d5',
                          background: groundTruthMode === 'printable' ? '#eef7f4' : 'white',
                          color: groundTruthMode === 'printable' ? '#176b57' : '#4a6058',
                          fontSize: '13px',
                          cursor: 'pointer',
                        }}
                        onClick={() => setGroundTruthMode('printable')}
                      >
                        Printable paper
                      </button>
                      <button
                        type="button"
                        className={`quiet ${groundTruthMode === 'compact' ? 'active' : ''}`}
                        style={{
                          fontWeight: groundTruthMode === 'compact' ? 700 : 400,
                          padding: '5px 10px',
                          borderRadius: '6px',
                          border: '1px solid #ccd9d5',
                          background: groundTruthMode === 'compact' ? '#eef7f4' : 'white',
                          color: groundTruthMode === 'compact' ? '#176b57' : '#4a6058',
                          fontSize: '13px',
                          cursor: 'pointer',
                        }}
                        onClick={() => setGroundTruthMode('compact')}
                      >
                        Compact paper
                      </button>
                      <button
                        type="button"
                        className={`quiet ${groundTruthMode === 'markscheme' ? 'active' : ''}`}
                        style={{
                          fontWeight: groundTruthMode === 'markscheme' ? 700 : 400,
                          padding: '5px 10px',
                          borderRadius: '6px',
                          border: '1px solid #ccd9d5',
                          background: groundTruthMode === 'markscheme' ? '#eef7f4' : 'white',
                          color: groundTruthMode === 'markscheme' ? '#176b57' : '#4a6058',
                          fontSize: '13px',
                          cursor: 'pointer',
                        }}
                        onClick={() => setGroundTruthMode('markscheme')}
                      >
                        Mark scheme
                      </button>
                    </div>
                    <iframe
                      src={
                        groundTruthMode === 'markscheme'
                          ? `/data/assets/${paper?.paper_code || paper?.id}/paper_markscheme.pdf`
                          : groundTruthMode === 'compact'
                          ? `/data/assets/${paper?.paper_code || paper?.id}/paper_compact.pdf`
                          : `/data/assets/${paper?.paper_code || paper?.id}/paper_printable.pdf`
                      }
                      style={{
                        width: '100%',
                        height: 'calc(100vh - 270px)',
                        border: '1px solid #ccd9d5',
                        borderRadius: '8px',
                      }}
                      title="Ground Truth PDF Scan"
                    />
                  </div>
                </TabsContent>
              </Tabs>
            </aside>
          </ResizablePanel>
        </ResizablePanelGroup>
        {!dock && (
          <button className="open-support" onClick={() => setDock(true)}>
            <PanelRightOpen size={17} />
            <span>Open support</span>
          </button>
        )}
      </div>

      {/* Browse Papers Modal Dialog */}
      <Dialog open={libraryOpen} onOpenChange={setLibraryOpen}>
        <DialogContent className="library-dialog">
          <DialogTitle>Physics 9702 Past-Paper Library</DialogTitle>
          <DialogDescription>
            Choose a component and paper to review. Review decisions are autosaved to review-state.json.
          </DialogDescription>
          <div className="component-switch">
            {index?.components.map((item) => (
              <button
                key={item.id}
                className={componentId === item.id ? 'active' : ''}
                onClick={() => chooseComponent(item.id)}
              >
                {item.name}
              </button>
            ))}
          </div>
          <div className="library-tools">
            <div className="search-control">
              <Search size={15} />
              <Input
                aria-label="Search paper or year"
                value={search}
                onChange={(event) => setSearch(event.target.value)}
                placeholder="Search paper (e.g. s24, w24, m24)…"
              />
            </div>
            <select
              aria-label="Review status"
              value={statusFilter}
              onChange={(event) => setStatusFilter(event.target.value as typeof statusFilter)}
            >
              <option value="all">All statuses</option>
              <option value="not-started">Not started</option>
              <option value="passed">Fully passed</option>
              <option value="needs-attention">Not passed</option>
            </select>
          </div>
          <div className="paper-library">
            {filteredPapers.map((item) => {
              const passed = item.questions.filter((q) => reviews[q.id]?.decision === 'pass').length;
              const flagged = item.questions.filter((q) => reviews[q.id]?.decision === 'flag').length;
              const paperStatus: PaperReviewStatus =
                passed === item.questions.length
                  ? 'passed'
                  : item.questions.every((q) => !reviews[q.id])
                    ? 'not-started'
                    : 'needs-attention';
              return (
                <button
                  key={item.id}
                  className={`${paper?.id === item.id ? 'active' : ''} paper-status-${paperStatus}`}
                  onClick={() => choosePaper(item.id)}
                >
                  <span>
                    <strong>{item.paper_code || item.id}</strong>
                    <small>
                      {item.session} {item.year} · Variant {item.variant}
                    </small>
                  </span>
                  <span>
                    <strong className="paper-status-label">
                      {paperStatus === 'passed'
                        ? 'Passed'
                        : paperStatus === 'not-started'
                          ? 'Not started'
                          : 'Not passed'}
                    </strong>
                    <small>{passed}/{item.questions.length} passed</small>
                    {flagged ? ` · ${flagged} flagged` : ''}
                  </span>
                </button>
              );
            })}
          </div>
        </DialogContent>
      </Dialog>

      {/* Enlarged Zoom Figure Modal */}
      <Dialog open={!!zoom} onOpenChange={() => setZoom(null)}>
        <DialogContent className="figure-modal max-w-4xl">
          <DialogTitle>Question Diagram / Scan</DialogTitle>
          {zoom && (
            <div className="overflow-auto max-h-[85vh] p-2 flex justify-center">
              <img src={zoom} alt="Enlarged view" className="max-w-full h-auto rounded-md object-contain" />
            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
