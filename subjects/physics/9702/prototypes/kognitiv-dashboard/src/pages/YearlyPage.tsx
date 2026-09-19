import React, { useEffect, useState } from 'react';
import inventory from '../data/physicsYearlyPapers.json';

type Paper = typeof inventory.papers[number];
const sessions = [
  { id: 'february-march', label: 'February / March' },
  { id: 'may-june', label: 'May / June' },
  { id: 'october-november', label: 'October / November' },
];
const componentNames: Record<string, string> = { P1: 'MCQs', P2: 'Theory', P3: 'Practical', P4: 'A Level theory' };
const attempted = (paper: Paper) => inventory.papers.findIndex((item) => item.id === paper.id) % 4 === 1;
// UI-only duration presets; production will read each paper's own duration.
const paperDurationMinutes: Record<string, number> = { P1: 75, P2: 75, P4: 120 };
const years = Array.from({ length: 10 }, (_, i) => 2016 + i);
const card = 'bg-white rounded-2xl border border-[#e8eaee] p-5 sm:p-6';
const link = 'text-sm font-medium text-[#168f89]';
const formatTime = (seconds: number) => `${Math.floor(seconds / 60).toString().padStart(2, '0')}:${(seconds % 60).toString().padStart(2, '0')}`;

export const YearlyPage: React.FC<{ onBack: () => void }> = ({ onBack }) => {
  const [year, setYear] = useState<number | null>(null);
  const [paper, setPaper] = useState<Paper | null>(null);
  const [component, setComponent] = useState('All papers');
  const [sessionId, setSessionId] = useState(sessions[0].id);
  const [mode, setMode] = useState('Practice');
  const [stage, setStage] = useState<'setup' | 'countdown' | 'player'>('setup');
  const [countdownEnd, setCountdownEnd] = useState(0);
  const [now, setNow] = useState(Date.now());
  const countdown = Math.max(0, Math.ceil((countdownEnd - now) / 1000));
  const timed = mode === 'Exam condition';
  const minutes = paper ? paperDurationMinutes[paper.component] ?? 60 : 60;
  const remaining = Math.max(0, Number(minutes) * 60 - Math.floor((now - countdownEnd) / 1000));

  useEffect(() => {
    if (stage === 'setup' || (stage === 'player' && !timed)) return;
    const interval = window.setInterval(() => {
      const current = Date.now();
      setNow(current);
      if (stage === 'countdown' && current >= countdownEnd) setStage('player');
    }, 200);
    return () => window.clearInterval(interval);
  }, [stage, countdownEnd, timed]);

  const paperLabel = paper ? `${paper.component} · ${componentNames[paper.component]} · ${paper.paperCode} · ${sessions.find((session) => session.id === paper.session)?.label} ${paper.year} · Variant ${paper.variant}` : '';
  const yearPapers = inventory.papers.filter((item) => item.year === year);
  const availableComponents = [...new Set(['P3', ...yearPapers.map((item) => item.component)])].sort();

  if (stage === 'countdown') return (
    <div className="max-w-3xl mx-auto text-center py-16 sm:py-24">
      <p className="text-sm text-slate-500">{paperLabel}</p>
      <h2 className="text-2xl font-bold text-[#1d1935] mt-4">Get ready</h2>
      <p className="text-sm text-slate-500 mt-2">{mode} starts in</p>
      <div className="text-8xl font-bold text-[#168f89] tabular-nums my-10" role="timer" aria-live="polite" aria-label={`${countdown} seconds`}>{countdown}</div>
      <button onClick={() => setStage('setup')} className={link}>Cancel</button>
    </div>
  );

  if (stage === 'player') return (
    <div className="max-w-5xl mx-auto space-y-6">
      <button onClick={() => setStage('setup')} className={link}>Back to session options</button>
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div><h2 className="text-2xl font-bold text-[#1d1935]">{paper?.paperCode}</h2><p className="text-sm text-slate-500 mt-2">{paperLabel} · {mode}</p></div>
        {timed && <div className="rounded-xl bg-[#e8f7f4] px-4 py-3 text-[#168f89]"><p className="text-xs">Time remaining</p><p className="text-xl font-semibold font-mono tabular-nums" role="timer">{formatTime(remaining)}</p></div>}
      </div>
      <div className={`${card} min-h-64 flex flex-col items-center justify-center text-center`}>
        <h3 className="text-lg font-semibold text-[#272043]">{timed && remaining === 0 ? 'Time is up' : mode === 'Revise' ? 'Revise paper' : 'Paper player preview'}</h3>
        <p className="text-sm text-slate-500 mt-2">{mode === 'Revise' ? 'Read through questions one by one, without submitting answers.' : 'Questions will appear here.'} The screen inside is still to be designed.</p>
      </div>
    </div>
  );

  if (paper) return (
    <div className="max-w-4xl mx-auto">
      <button onClick={() => setPaper(null)} className={`${link} mb-5`}>Back to {year} papers</button>
      <h2 className="text-2xl font-bold text-[#1d1935]">Session options</h2>
      <p className="mt-2 text-sm text-slate-500">{paperLabel}</p>
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mt-6" aria-label="Session mode">
        {[
          { title: 'Practice', description: 'Work through the paper at your own pace.' },
          { title: 'Exam condition', description: 'Attempt a timed paper without hints or walkthroughs.' },
          { title: 'Revise', description: 'Read through the questions without attempting them.' },
        ].map((option) => (
          <button key={option.title} aria-pressed={mode === option.title} onClick={() => setMode(option.title)} className={`rounded-2xl border p-5 text-left transition-colors ${mode === option.title ? 'border-[#168f89] bg-[#e8f7f4]' : 'border-[#e8eaee] bg-white hover:bg-slate-50'}`}>
            <span className="block text-base font-semibold text-[#272043]">{option.title}</span>
            <span className="block text-sm text-slate-500 mt-2">{option.description}</span>
          </button>
        ))}
      </div>
      <div className="flex flex-wrap items-center justify-between gap-4 mt-8">
        <p className="text-xs text-slate-500">{mode === 'Revise' ? 'Opens directly, without a countdown.' : 'Starts after a 5-second countdown.'}</p>
        <button onClick={() => { if (mode === 'Revise') { setStage('player'); return; } const start = Date.now(); setNow(start); setCountdownEnd(start + 5000); setStage('countdown'); }} className="rounded-xl px-8 py-3 bg-[#2bb9b1] hover:bg-[#168f89] text-white font-semibold text-sm">{mode === 'Revise' ? 'Open revision' : 'Start'}</button>
      </div>
      <div className="mt-8 border-t border-slate-200 pt-4 text-sm text-slate-500">
        <div className="flex flex-wrap justify-between gap-2"><span className="font-medium text-slate-600">Previous attempts</span><span className="text-xs">Sample history</span></div>
        <p className="mt-2">{attempted(paper) ? '1 attempt · Practice · 8 September 2026' : 'No previous attempts.'}</p>
      </div>
    </div>
  );

  return (
    <div className="max-w-6xl mx-auto">
      <button onClick={() => { if (year) { setYear(null); setComponent('All papers'); } else onBack(); }} className={`${link} mb-5`}>{year ? 'Back to years' : 'Back to revision options'}</button>
      <h2 className="text-2xl font-bold text-[#1d1935]">{year || 'Yearly papers'}</h2>
      <p className="text-sm text-slate-500 mt-2 mb-6">{year ? 'Choose a session and paper variant.' : 'Choose an exam year.'}</p>
      {year === null ? (
        <div className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-4">
          {years.map((item) => <button key={item} onClick={() => { setYear(item); setSessionId(sessions.find((session) => inventory.papers.some((paper) => paper.year === item && paper.session === session.id))?.id || sessions[0].id); }} className={`${card} text-left hover:bg-[#f2faf8] transition-colors`}><span className="block text-2xl font-bold text-[#272043]">{item}</span><span className="block text-xs text-slate-500 mt-3">{inventory.papers.filter((entry) => entry.year === item).length} papers</span></button>)}
        </div>
      ) : (
        <>
          <div className="flex gap-2 flex-wrap mb-6" aria-label="Paper components">{['All papers', ...availableComponents].map((item) => <button key={item} aria-pressed={component === item} onClick={() => setComponent(item)} className={`px-4 py-2 rounded-full text-sm border ${component === item ? 'border-[#168f89] bg-[#e8f7f4] text-[#168f89]' : 'border-slate-200 bg-white text-slate-600'}`}>{item === 'All papers' ? item : `${item} · ${componentNames[item]}`}</button>)}</div>
          <div className="flex flex-wrap gap-2 border-b border-slate-200 mb-5" aria-label="Exam sessions">
            {sessions.map((session) => <button key={session.id} aria-pressed={sessionId === session.id} onClick={() => setSessionId(session.id)} className={`px-3 py-3 text-sm border-b-2 ${sessionId === session.id ? 'border-[#168f89] text-[#168f89] font-semibold' : 'border-transparent text-slate-500'}`}>{session.label}</button>)}
          </div>
          <div className="space-y-7">
            {sessions.filter((session) => session.id === sessionId).map((session) => {
              const entries = yearPapers.filter((item) => item.session === session.id && (component === 'All papers' || item.component === component));
              return <section key={session.id} aria-label={session.label}>
                <h3 className="font-semibold text-[#272043] mb-3">{session.label}</h3>
                {entries.length ? <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-3">{entries.map((item) => <button key={item.id} onClick={() => { setPaper(item); setMode('Practice'); setStage('setup'); }} className={`${card} text-left hover:bg-[#f2faf8] transition-colors`}><span className="flex flex-wrap items-center justify-between gap-2"><span className="font-semibold text-[#272043]">{item.component} · {componentNames[item.component]}</span><span className={`rounded-full px-2 py-1 text-xs font-medium ${attempted(item) ? 'bg-[#e8f7f4] text-[#168f89]' : 'bg-[#eeedff] text-[#6553b5]'}`}>{attempted(item) ? 'Attempted' : 'New'}</span></span><span className="block mt-3 text-sm text-slate-600">Variant {item.variant}</span><span className="block mt-1 text-xs text-slate-500">{item.paperCode}</span></button>)}</div> : <p className="text-sm text-slate-500">{component === 'P3' ? 'P3 · Practical papers are not available in this prototype yet.' : 'No papers in this session in the current collection.'}</p>}
              </section>;
            })}
          </div>
          <p className="mt-5 text-xs text-slate-500">New and Attempted show sample history.</p>
        </>
      )}
    </div>
  );
};
