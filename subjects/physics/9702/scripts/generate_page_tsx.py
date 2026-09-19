import sys
from pathlib import Path

content = """'use client';

/* Cambridge Physics 9702 Paper 2 - Multi-Paper Dual Reviewer & Pedagogical Inspector */
/* eslint-disable next/no-img-element */
import { useEffect, useMemo, useRef, useState } from 'react';
import {
  AlertTriangle,
  ArrowRight,
  BookOpen,
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  Clock,
  ExternalLink,
  FileText,
  GraduationCap,
  Info,
  Lightbulb,
  Maximize2,
  Minimize2,
  PanelRightOpen,
  X,
} from 'lucide-react';
import { MathText } from '@/components/player/MathText';
import {
  Dialog,
  DialogContent,
  DialogTitle,
} from '@/components/ui/dialog';
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from '@/components/ui/resizable';
import { usePanelRef } from 'react-resizable-panels';
import 'katex/dist/katex.min.css';

type PaperManifestItem = {
  paper_code: string;
  title: string;
  full_title: string;
  year: number;
  session: string;
  variant: string;
  total_questions: number;
  total_marks: number;
  json_url: string;
  paper_compact_pdf: string;
  paper_printable_pdf: string;
  paper_markscheme_pdf: string;
};

type QuestionPart = {
  label: string;
  part_stem?: string | null;
  text: string;
  marks: number | null;
  answer_prompt?: string | null;
  unit?: string | null;
  hints?: string[];
  teacher_walkthrough?: string[];
  walkthrough?: string[];
  common_pitfalls?: string[];
  formulas_used?: string[];
  target_time_minutes?: number | null;
};

type MarkSchemePoint = {
  tag?: string;
  text: string;
};

type MarkSchemePart = {
  label: string;
  marks: number;
  marking_points: MarkSchemePoint[];
};

type QuestionData = {
  question_num: number;
  total_marks: number;
  title: string;
  main_stem?: string | null;
  parts: QuestionPart[];
  markscheme?: MarkSchemePart[];
  difficulty?: number;
  question_patterns?: string[];
  meta?: {
    model: string;
    compact_image_url: string;
    printable_image_url: string;
    printable_pdf_url: string;
    markscheme_image_url?: string;
  };
};

type PaperData = {
  paper_code: string;
  metadata: {
    title: string;
    full_title: string;
    session: string;
    year: number;
    variant: string;
    paper_code: string;
  };
  total_questions: number;
  total_marks: number;
  questions: Record<string, QuestionData>;
};

function formatUnit(unitStr: string | null | undefined): string {
  if (!unitStr) return '';
  const trimmed = unitStr.trim();
  if (trimmed.startsWith('$') && trimmed.endsWith('$')) return trimmed;
  if (/[\\^\\\\_{}]/.test(trimmed)) {
    return `$${trimmed}$`;
  }
  return trimmed;
}

export default function Home() {
  const [manifest, setManifest] = useState<PaperManifestItem[]>([]);
  const [selectedPaperCode, setSelectedPaperCode] = useState<string>(() => {
    if (typeof window !== 'undefined') {
      const p = new URLSearchParams(window.location.search).get('paper');
      if (p) return p;
    }
    return '9702_m23_22';
  });
  const [paperData, setPaperData] = useState<PaperData | null>(null);
  const [questionIndex, setQuestionIndex] = useState<number>(() => {
    if (typeof window !== 'undefined') {
      const q = new URLSearchParams(window.location.search).get('q');
      const parsed = q ? parseInt(q, 10) : NaN;
      if (!isNaN(parsed) && parsed >= 1) return parsed - 1;
    }
    return 0;
  });
  const [dock, setDock] = useState<boolean>(true);
  const [zoom, setZoom] = useState<string | null>(null);
  const [groundTruthMode, setGroundTruthMode] = useState<'printable' | 'compact' | 'markscheme'>(() => {
    if (typeof window !== 'undefined') {
      const mode = new URLSearchParams(window.location.search).get('mode');
      if (mode === 'compact' || mode === 'printable' || mode === 'markscheme') return mode;
    }
    return 'printable';
  });
  const [activeTabByPart, setActiveTabByPart] = useState<Record<string, 'hints' | 'walkthrough' | 'markscheme' | 'pitfalls' | 'none'>>({});
  
  const pane = useRef<HTMLElement>(null);
  const supportPanel = usePanelRef();

  // Load manifest on mount
  useEffect(() => {
    fetch('/data/papers_manifest.json')
      .then((res) => (res.ok ? (res.json() as Promise<{ papers: PaperManifestItem[] }>) : null))
      .then((data) => {
        if (data && data.papers && data.papers.length > 0) {
          setManifest(data.papers);
          const params = new URLSearchParams(window.location.search);
          const pParam = params.get('paper');
          if (pParam && data.papers.some((p: PaperManifestItem) => p.paper_code === pParam)) {
            setSelectedPaperCode(pParam);
          } else if (!pParam) {
            setSelectedPaperCode(data.papers[0].paper_code);
          }
        }
      })
      .catch((err) => console.error('Failed to load papers manifest:', err));
  }, []);

  // Load selected paper data
  useEffect(() => {
    if (!selectedPaperCode) return;
    fetch(`/data/papers/${selectedPaperCode}.json`)
      .then((res) => (res.ok ? (res.json() as Promise<PaperData>) : null))
      .then((data) => {
        if (!data) return;
        setPaperData(data);
        const qCount = Object.keys(data.questions || {}).length;
        setQuestionIndex((prev) => (prev >= qCount ? 0 : prev));
      })
      .catch((err) => console.error('Failed to load paper data:', err));
  }, [selectedPaperCode]);

  // Expand/collapse panel
  useEffect(() => {
    if (dock) supportPanel.current?.expand();
    else supportPanel.current?.collapse();
  }, [dock, supportPanel]);

  const questionsList: QuestionData[] = useMemo(() => {
    if (!paperData || !paperData.questions) return [];
    return Object.values(paperData.questions).sort((a, b) => a.question_num - b.question_num);
  }, [paperData]);

  const totalQuestions = questionsList.length;
  const currentQuestion: QuestionData | null = questionsList[questionIndex] || null;

  const currentQNum = currentQuestion?.question_num || (questionIndex + 1);
  const currentQNumStr = String(currentQNum).padStart(2, '0');

  // Ground truth image resolution
  const groundTruthImageUrl = useMemo(() => {
    if (!currentQuestion) return null;
    if (groundTruthMode === 'printable') {
      return `/data/assets/${selectedPaperCode}_q${currentQNumStr}/question_printable.png`;
    } else if (groundTruthMode === 'compact') {
      return `/data/assets/${selectedPaperCode}_q${currentQNumStr}/question_compact.png`;
    } else {
      return `/data/assets/${selectedPaperCode}_q${currentQNumStr}/markscheme.png`;
    }
  }, [selectedPaperCode, currentQNumStr, groundTruthMode, currentQuestion]);

  const printablePdfUrl = `/data/assets/${selectedPaperCode}_q${currentQNumStr}/question_printable.pdf`;
  const paperPrintablePdfUrl = `/data/assets/${selectedPaperCode}/paper_printable.pdf`;
  const paperMarkschemePdfUrl = `/data/assets/${selectedPaperCode}/paper_markscheme.pdf`;

  function navigate(delta: number) {
    const next = Math.max(0, Math.min(totalQuestions - 1, questionIndex + delta));
    setQuestionIndex(next);
  }

  function handlePaperChange(paperCode: string) {
    setSelectedPaperCode(paperCode);
    setQuestionIndex(0);
    const url = new URL(window.location.href);
    url.searchParams.set('paper', paperCode);
    url.searchParams.set('q', '1');
    window.history.replaceState({}, '', url.toString());
  }

  const activePaperMeta = manifest.find((p) => p.paper_code === selectedPaperCode) || paperData?.metadata;

  return (
    <div className={`studio review-studio ${dock ? '' : 'focus-mode'}`}>
      {/* Top Header */}
      <header className="topbar">
        <div className="brand">
          <span className="brandmark">K</span>Kognitiv
          <span className="brand-divider" />
          <span className="workspace-label">Physics Review</span>
        </div>

        {/* Paper Selector Dropdown */}
        <div className="flex items-center gap-2">
          <div className="relative inline-flex items-center">
            <select
              value={selectedPaperCode}
              onChange={(e) => handlePaperChange(e.target.value)}
              className="appearance-none bg-white dark:bg-slate-900 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-slate-100 text-xs font-semibold py-1.5 pl-3 pr-8 rounded-lg shadow-xs hover:border-emerald-500 focus:outline-hidden cursor-pointer"
            >
              {manifest.map((p) => (
                <option key={p.paper_code} value={p.paper_code}>
                  📄 {p.title} — {p.total_questions} Qs ({p.paper_code})
                </option>
              ))}
            </select>
            <ChevronDown size={14} className="absolute right-2.5 pointer-events-none text-muted-foreground" />
          </div>
          <span className="prototype-label hidden sm:inline-block">Cambridge 9702 P2</span>
        </div>

        <div className="flex items-center gap-2">
          <button
            className="icon-button focus-button"
            aria-label={dock ? 'Enter focus mode' : 'Show support'}
            onClick={() => setDock(!dock)}
          >
            {dock ? <Maximize2 size={17} /> : <Minimize2 size={17} />}
          </button>
          <span className="avatar">P</span>
        </div>
      </header>

      <div className="workspace">
        <ResizablePanelGroup orientation="horizontal" disabled={!dock} className="player-split">
          {/* Main Left Question Pane */}
          <ResizablePanel id="question" defaultSize="58%" minSize="340px" className="question-slot">
            <main className="question-pane" ref={pane}>
              <div className="question-inner">
                {/* Breadcrumbs */}
                <nav className="breadcrumbs" aria-label="Breadcrumb">
                  <span>Physics 9702</span>
                  <ChevronRight size={13} />
                  <span>Paper 2 (AS Structured)</span>
                  <ChevronRight size={13} />
                  <span className="font-semibold text-foreground">{activePaperMeta?.title || selectedPaperCode}</span>
                </nav>

                {currentQuestion ? (
                  <>
                    <div className="question-heading">
                      <div>
                        <h1>
                          Question {currentQuestion.question_num}
                          <Info size={17} className="inline-info" />
                        </h1>
                        <p className="source-line">
                          {activePaperMeta?.full_title || activePaperMeta?.title} · Theory Question {currentQuestion.question_num} · {currentQuestion.total_marks} Marks
                        </p>
                      </div>
                    </div>

                    {/* Meta Banner */}
                    <div className="ai-model-bar my-4 p-3.5 rounded-xl bg-emerald-50/80 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800/60 shadow-xs">
                      <div className="flex flex-wrap items-center justify-between gap-3">
                        <div className="flex items-center gap-2.5">
                          <span className="px-2.5 py-1 text-xs font-bold rounded-md bg-white dark:bg-slate-900 text-emerald-800 dark:text-emerald-200 border border-emerald-300 dark:border-emerald-700 shadow-2xs flex items-center gap-1.5">
                            📄 {activePaperMeta?.title || selectedPaperCode}
                          </span>
                          <span className="px-2.5 py-1 text-xs font-bold rounded-md bg-white dark:bg-slate-900 text-emerald-800 dark:text-emerald-200 border border-emerald-300 dark:border-emerald-700 shadow-2xs flex items-center gap-1.5">
                            ⚡ Meta Muse Spark 1.3
                          </span>
                          <span className="text-xs text-muted-foreground font-medium">
                            Question {questionIndex + 1} of {totalQuestions}
                          </span>
                        </div>
                        <div className="flex items-center gap-3 text-xs">
                          {currentQuestion.difficulty && (
                            <span className="text-muted-foreground">
                              Tier: <strong>Level {currentQuestion.difficulty}/3</strong>
                            </span>
                          )}
                          <span className="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-100 dark:bg-emerald-900/60 text-emerald-800 dark:text-emerald-200 border border-emerald-300 dark:border-emerald-700">
                            Total: {currentQuestion.total_marks} marks
                          </span>
                        </div>
                      </div>
                    </div>

                    {/* Question Content */}
                    <article className="question-paper">
                      {/* Main Stem if present */}
                      {currentQuestion.main_stem && (
                        <div className="question-stem-block mb-5 p-4 rounded-xl bg-slate-50/90 dark:bg-slate-900/50 border border-slate-200 dark:border-slate-800">
                          <span className="stem-indicator font-semibold text-xs text-indigo-700 dark:text-indigo-300 mb-2 block uppercase tracking-wider">
                            Question Background
                          </span>
                          <div className="text-sm leading-relaxed text-slate-800 dark:text-slate-200">
                            <MathText text={currentQuestion.main_stem} />
                          </div>
                        </div>
                      )}

                      {/* Question Parts */}
                      {currentQuestion.parts.map((p, idx) => {
                        const partKey = `${currentQNum}_part_${idx}`;
                        const activeTab = activeTabByPart[partKey] || 'none';

                        return (
                          <div key={idx} className="question-part-wrapper mb-6 p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950/40 shadow-xs">
                            {/* Part Heading & Text */}
                            <div className="flex items-start gap-3">
                              <span className="px-2.5 py-1 text-xs font-bold rounded-lg bg-indigo-50 dark:bg-indigo-950/70 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800">
                                {p.label || `Part ${idx + 1}`}
                              </span>
                              <div className="flex-1 text-sm leading-relaxed text-slate-900 dark:text-slate-100">
                                {p.part_stem && (
                                  <div className="mb-2 text-slate-700 dark:text-slate-300 font-medium">
                                    <MathText text={p.part_stem} />
                                  </div>
                                )}
                                <MathText text={p.text} />

                                {/* Answer Prompt & Unit Boxes */}
                                {(p.answer_prompt || p.unit) && (
                                  <div className="answer-field-box my-3 p-3 rounded-xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-dashed border-emerald-300 dark:border-emerald-800/80 flex flex-wrap items-center justify-between gap-2 text-xs">
                                    <div className="flex items-center gap-2">
                                      <span className="font-bold text-emerald-800 dark:text-emerald-300 uppercase tracking-wider text-[11px]">
                                        Answer:
                                      </span>
                                      <span className="font-semibold text-slate-900 dark:text-slate-100">
                                        <MathText text={p.answer_prompt || ''} />
                                      </span>
                                      <span className="inline-block w-28 border-b-2 border-emerald-400 dark:border-emerald-600 mx-2" />
                                    </div>
                                    {p.unit && (
                                      <div className="flex items-center gap-1.5">
                                        <span className="text-muted-foreground text-[11px]">Unit:</span>
                                        <span className="px-2.5 py-0.5 rounded-md bg-emerald-100 dark:bg-emerald-900/60 text-emerald-800 dark:text-emerald-200 font-mono font-bold text-xs shadow-2xs">
                                          <MathText text={formatUnit(p.unit)} />
                                        </span>
                                      </div>
                                    )}
                                  </div>
                                )}
                              </div>
                              {p.marks !== null && (
                                <span className="text-xs font-bold text-slate-600 dark:text-slate-400">
                                  [{p.marks}]
                                </span>
                              )}
                            </div>

                            {/* Pedagogical Inspection Tabs */}
                            <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800/60">
                              <div className="flex flex-wrap items-center gap-1.5 text-xs">
                                <button
                                  onClick={() => setActiveTabByPart((prev) => ({ ...prev, [partKey]: prev[partKey] === 'hints' ? 'none' : 'hints' }))}
                                  className={`px-2.5 py-1 rounded-md font-medium transition flex items-center gap-1 ${
                                    activeTab === 'hints'
                                      ? 'bg-amber-100 text-amber-900 dark:bg-amber-950 dark:text-amber-200 font-semibold'
                                      : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200'
                                  }`}
                                >
                                  <Lightbulb size={13} />
                                  <span>Hints ({p.hints?.length || 0})</span>
                                </button>

                                <button
                                  onClick={() => setActiveTabByPart((prev) => ({ ...prev, [partKey]: prev[partKey] === 'walkthrough' ? 'none' : 'walkthrough' }))}
                                  className={`px-2.5 py-1 rounded-md font-medium transition flex items-center gap-1 ${
                                    activeTab === 'walkthrough'
                                      ? 'bg-indigo-100 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200 font-semibold'
                                      : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200'
                                  }`}
                                >
                                  <GraduationCap size={13} />
                                  <span>Teacher Walkthrough</span>
                                </button>

                                <button
                                  onClick={() => setActiveTabByPart((prev) => ({ ...prev, [partKey]: prev[partKey] === 'markscheme' ? 'none' : 'markscheme' }))}
                                  className={`px-2.5 py-1 rounded-md font-medium transition flex items-center gap-1 ${
                                    activeTab === 'markscheme'
                                      ? 'bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200 font-semibold'
                                      : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200'
                                  }`}
                                >
                                  <BookOpen size={13} />
                                  <span>Mark Scheme</span>
                                </button>

                                {p.common_pitfalls && p.common_pitfalls.length > 0 && (
                                  <button
                                    onClick={() => setActiveTabByPart((prev) => ({ ...prev, [partKey]: prev[partKey] === 'pitfalls' ? 'none' : 'pitfalls' }))}
                                    className={`px-2.5 py-1 rounded-md font-medium transition flex items-center gap-1 ${
                                      activeTab === 'pitfalls'
                                        ? 'bg-rose-100 text-rose-900 dark:bg-rose-950 dark:text-rose-200 font-semibold'
                                        : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200'
                                    }`}
                                  >
                                    <AlertTriangle size={13} />
                                    <span>Traps ({p.common_pitfalls.length})</span>
                                  </button>
                                )}

                                {p.target_time_minutes && (
                                  <span className="ml-auto text-[11px] text-muted-foreground flex items-center gap-1">
                                    <Clock size={12} /> {p.target_time_minutes} min pacing
                                  </span>
                                )}
                              </div>

                              {/* Active Tab Drawer Content */}
                              {activeTab === 'hints' && p.hints && (
                                <div className="mt-3 p-3.5 rounded-lg bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800 text-xs text-amber-900 dark:text-amber-100 flex flex-col gap-2">
                                  <div className="font-bold flex items-center gap-1.5 text-amber-800 dark:text-amber-200 uppercase tracking-wider text-[11px]">
                                    <Lightbulb size={13} /> Mark-Proportional Hints (1 per mark)
                                  </div>
                                  <ol className="list-decimal list-inside space-y-1.5 pl-1 leading-relaxed">
                                    {p.hints.map((hint, hIdx) => (
                                      <li key={hIdx}>
                                        <MathText text={hint} />
                                      </li>
                                    ))}
                                  </ol>
                                </div>
                              )}

                              {activeTab === 'walkthrough' && p.teacher_walkthrough && (
                                <div className="mt-3 p-3.5 rounded-lg bg-indigo-50/70 dark:bg-indigo-950/30 border border-indigo-200 dark:border-indigo-800 text-xs text-indigo-950 dark:text-indigo-100 flex flex-col gap-2">
                                  <div className="font-bold flex items-center gap-1.5 text-indigo-800 dark:text-indigo-200 uppercase tracking-wider text-[11px]">
                                    <GraduationCap size={13} /> Humane Step-by-Step Teacher Walkthrough
                                  </div>
                                  <div className="space-y-2 leading-relaxed">
                                    {p.teacher_walkthrough.map((step, sIdx) => (
                                      <div key={sIdx} className="p-2 rounded bg-white/70 dark:bg-slate-900/60 border border-indigo-100 dark:border-indigo-900/50">
                                        <MathText text={step} />
                                      </div>
                                    ))}
                                  </div>
                                </div>
                              )}

                              {activeTab === 'markscheme' && (
                                <div className="mt-3 p-3.5 rounded-lg bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800 text-xs text-emerald-950 dark:text-emerald-100 flex flex-col gap-2">
                                  <div className="font-bold flex items-center gap-1.5 text-emerald-800 dark:text-emerald-200 uppercase tracking-wider text-[11px]">
                                    <BookOpen size={13} /> Official Mark Scheme Points
                                  </div>
                                  {p.walkthrough && p.walkthrough.length > 0 ? (
                                    <ul className="space-y-1.5 pl-1 leading-relaxed">
                                      {p.walkthrough.map((mp, mIdx) => (
                                        <li key={mIdx} className="flex items-start gap-1.5">
                                          <span className="font-bold text-emerald-700 dark:text-emerald-300">•</span>
                                          <MathText text={mp} />
                                        </li>
                                      ))}
                                    </ul>
                                  ) : (
                                    <p className="text-muted-foreground italic">Check the right panel for the authentic mark scheme image slice.</p>
                                  )}
                                </div>
                              )}

                              {activeTab === 'pitfalls' && p.common_pitfalls && (
                                <div className="mt-3 p-3.5 rounded-lg bg-rose-50/70 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800 text-xs text-rose-950 dark:text-rose-100 flex flex-col gap-2">
                                  <div className="font-bold flex items-center gap-1.5 text-rose-800 dark:text-rose-200 uppercase tracking-wider text-[11px]">
                                    <AlertTriangle size={13} /> Common Examiner Pitfalls
                                  </div>
                                  <ul className="list-disc list-inside space-y-1.5 pl-1 leading-relaxed">
                                    {p.common_pitfalls.map((trap, tIdx) => (
                                      <li key={tIdx}>
                                        <MathText text={trap} />
                                      </li>
                                    ))}
                                  </ul>
                                </div>
                              )}
                            </div>
                          </div>
                        );
                      })}
                    </article>

                    <div className="paper-note flex items-center justify-between text-xs text-muted-foreground mt-4 pt-3 border-t border-slate-200 dark:border-slate-800">
                      <span>{currentQuestion.total_marks} marks total</span>
                      <span>Model: Meta Muse Spark 1.3 Contributor</span>
                    </div>
                  </>
                ) : (
                  <div className="loading-card p-12 text-center text-muted-foreground text-sm">
                    Loading question data...
                  </div>
                )}
              </div>

              {/* Bottom Navigation */}
              <footer className="question-navigation flex items-center justify-between gap-2 p-3 bg-white dark:bg-slate-950 border-t border-slate-200 dark:border-slate-800">
                <button
                  className="secondary previous-question text-xs px-3 py-1.5 rounded-md border border-slate-200 dark:border-slate-800 flex items-center gap-1"
                  disabled={questionIndex === 0}
                  onClick={() => navigate(-1)}
                >
                  <ChevronLeft size={16} />
                  <span>Previous</span>
                </button>

                <div className="flex items-center gap-1">
                  {Array.from({ length: totalQuestions }).map((_, i) => (
                    <button
                      key={i}
                      className={`w-7 h-7 text-xs rounded-md font-semibold transition ${
                        questionIndex === i
                          ? 'bg-emerald-600 text-white shadow-xs'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700'
                      }`}
                      onClick={() => setQuestionIndex(i)}
                    >
                      {i + 1}
                    </button>
                  ))}
                </div>

                <button
                  className="primary next-question text-xs px-3 py-1.5 rounded-md bg-emerald-600 text-white flex items-center gap-1"
                  disabled={questionIndex === totalQuestions - 1}
                  onClick={() => navigate(1)}
                >
                  <span>Next</span>
                  <ArrowRight size={16} />
                </button>
              </footer>
            </main>
          </ResizablePanel>

          <ResizableHandle className={`player-divider ${dock ? '' : 'divider-hidden'}`} withHandle />

          {/* Right Ground Truth Dock */}
          <ResizablePanel
            id="support"
            defaultSize="42%"
            minSize="320px"
            maxSize="65%"
            collapsible
            collapsedSize="0%"
            panelRef={supportPanel}
            className={`support-slot ${dock ? '' : 'slot-closed'}`}
          >
            <aside className="support-dock review-support flex flex-col h-full bg-slate-100/70 dark:bg-slate-900/60" inert={!dock}>
              {/* Dock Header */}
              <div className="dock-heading flex items-center justify-between p-3 border-b border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950">
                <div className="flex items-center gap-2">
                  <span className="font-semibold text-xs text-slate-800 dark:text-slate-100">Original Source</span>
                  
                  {/* Mode Selector */}
                  <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-800 p-0.5 rounded-lg border border-slate-200 dark:border-slate-700 text-xs">
                    <button
                      className={`px-2 py-0.5 rounded-md transition ${
                        groundTruthMode === 'printable'
                          ? 'bg-white dark:bg-slate-900 text-foreground font-semibold shadow-2xs'
                          : 'text-muted-foreground hover:text-foreground'
                      }`}
                      onClick={() => setGroundTruthMode('printable')}
                      title="Authentic printable question with answer spaces"
                    >
                      🖨️ Printable
                    </button>
                    <button
                      className={`px-2 py-0.5 rounded-md transition ${
                        groundTruthMode === 'compact'
                          ? 'bg-white dark:bg-slate-900 text-foreground font-semibold shadow-2xs'
                          : 'text-muted-foreground hover:text-foreground'
                      }`}
                      onClick={() => setGroundTruthMode('compact')}
                      title="Compact question with whitespace stripped"
                    >
                      📦 Compact
                    </button>
                    <button
                      className={`px-2 py-0.5 rounded-md transition ${
                        groundTruthMode === 'markscheme'
                          ? 'bg-white dark:bg-slate-900 text-foreground font-semibold shadow-2xs'
                          : 'text-muted-foreground hover:text-foreground'
                      }`}
                      onClick={() => setGroundTruthMode('markscheme')}
                      title="Official mark scheme table slice"
                    >
                      📋 Mark Scheme
                    </button>
                  </div>
                </div>

                <div className="flex items-center gap-1.5 text-xs">
                  {/* PDF Links */}
                  <div className="flex items-center gap-1">
                    <a
                      href={printablePdfUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="px-2 py-1 rounded-md bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition flex items-center gap-1"
                      title="Open continuous PDF for this question"
                    >
                      <FileText size={12} />
                      <span>Q-PDF</span>
                    </a>

                    <a
                      href={groundTruthMode === 'markscheme' ? paperMarkschemePdfUrl : paperPrintablePdfUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="px-2 py-1 rounded-md bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition flex items-center gap-1"
                      title="Open full compiled document PDF"
                    >
                      <ExternalLink size={12} />
                      <span>{groundTruthMode === 'markscheme' ? 'MS PDF' : 'Paper PDF'}</span>
                    </a>
                  </div>

                  {groundTruthImageUrl && (
                    <button
                      className="px-2 py-1 rounded-md bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition flex items-center gap-1"
                      onClick={() => setZoom(groundTruthImageUrl)}
                      aria-label="Enlarge image"
                    >
                      <Maximize2 size={12} />
                      <span>Zoom</span>
                    </button>
                  )}
                  <button className="icon-button" onClick={() => setDock(false)} aria-label="Close original view">
                    <X size={16} />
                  </button>
                </div>
              </div>

              {/* Dock Image Body */}
              <div className="flex-1 overflow-auto p-4 flex flex-col items-center justify-start">
                {groundTruthImageUrl ? (
                  <div className="max-w-full flex flex-col items-center">
                    <button
                      type="button"
                      className="cursor-zoom-in border-0 bg-transparent p-0 transition hover:opacity-95 text-left"
                      onClick={() => setZoom(groundTruthImageUrl)}
                      aria-label="Enlarge image"
                    >
                      <img
                        key={groundTruthImageUrl}
                        src={groundTruthImageUrl}
                        alt={`Ground truth view for Question ${currentQNum}`}
                        className="max-w-full h-auto rounded-lg shadow-md border border-slate-200 dark:border-slate-800"
                      />
                    </button>
                    <p className="mt-2 text-center text-[11px] text-muted-foreground flex items-center gap-1">
                      <Maximize2 size={12} /> Click image to zoom / inspect details
                    </p>
                  </div>
                ) : (
                  <div className="p-8 text-center text-muted-foreground text-xs">
                    No image slice found for this selection.
                  </div>
                )}
              </div>
            </aside>
          </ResizablePanel>
        </ResizablePanelGroup>

        {!dock && (
          <button className="open-support" onClick={() => setDock(true)}>
            <PanelRightOpen size={17} />
            <span>Open original paper</span>
          </button>
        )}
      </div>

      {/* Lightbox Zoom Dialog */}
      <Dialog open={!!zoom} onOpenChange={() => setZoom(null)}>
        <DialogContent className="figure-modal max-w-5xl max-h-[92vh] overflow-auto">
          <DialogTitle>Ground Truth Slice Inspection</DialogTitle>
          {zoom && <img src={zoom} alt="Enlarged diagram" className="max-w-full h-auto mx-auto" />}
        </DialogContent>
      </Dialog>
    </div>
  );
}
"""

target = Path("/Users/abdullahaftab/Kognitiv/exam-paper-parser/subjects/physics/9702/prototypes/past-paper-question-reviewer/app/page.tsx")
target.write_text(content, encoding="utf-8")
print(f"✓ Updated {target} successfully!")
