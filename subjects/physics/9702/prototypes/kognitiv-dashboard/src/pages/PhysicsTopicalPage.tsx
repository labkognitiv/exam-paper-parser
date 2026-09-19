import React, { useState } from 'react';
import './PhysicsTopicalPage.css';
import catalog from '../data/physicsRevisionTopics.json';

const papers = [{ id: 'P1', label: 'MCQs' }, { id: 'P2', label: 'Theory' }, { id: 'P3', label: 'Laboratory' }];
const allLessonIds = catalog.topics.flatMap((topic) => topic.lessons.map((lesson) => lesson.id));
// Stable mock buckets only: no canonical question data or availability mappings.
const mockCounts = Object.fromEntries(allLessonIds.map((id, index) => [id,
  Object.fromEntries(papers.map((paper, paperIndex) => [paper.id,
    ['Easy', 'Medium', 'Hard'].map((difficulty, difficultyIndex) => {
      const total = 4 + ((index * 7 + paperIndex * 11 + difficultyIndex * 5) % 19);
      return { difficulty, total, unattempted: Math.floor(total * (0.4 + ((index + paperIndex) % 4) * 0.1)) };
    }),
  ])),
]));
const fieldClass = 'w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 text-sm text-[#272043] focus:outline-none focus:ring-2 focus:ring-[#2bb9b1]';
const labelClass = 'block text-xs font-semibold text-slate-600 mb-2';

export const PhysicsTopicalPage: React.FC<{ onBack: () => void }> = ({ onBack }) => {
  const [selectedPapers, setSelectedPapers] = useState(['P1']);
  const [selectedLessons, setSelectedLessons] = useState<string[]>([]);
  const [unattempted, setUnattempted] = useState(false);
  const [difficulty, setDifficulty] = useState('Mixed');
  const [mode, setMode] = useState('Practice');
  const [sizeType, setSizeType] = useState('Questions');
  const [size, setSize] = useState('10');
  const [order, setOrder] = useState('By topic');
  const [search, setSearch] = useState('');
  const [inPlayer, setInPlayer] = useState(false);
  const [sampleIndex, setSampleIndex] = useState(0);
  const lessonQuestionCount = (id: string) => selectedPapers.reduce((sum, paper) => sum + mockCounts[id][paper]
    .filter((bucket) => difficulty === 'Mixed' || bucket.difficulty === difficulty)
    .reduce((subtotal, bucket) => subtotal + (unattempted ? bucket.unattempted : bucket.total), 0), 0);
  const selectedQuestionCount = selectedLessons.reduce((sum, id) => sum + lessonQuestionCount(id), 0);
  const countLabel = (count: number) => `${count.toLocaleString()} ${count === 1 ? 'question' : 'questions'}`;
  const selectedTopics = catalog.topics.filter((topic) => topic.lessons.some((lesson) => selectedLessons.includes(lesson.id)));
  const sizeValid = sizeType === 'All matching' || (/^\d+$/.test(size) && Number(size) >= 1 && Number(size) <= 999);
  const canStart = selectedLessons.length > 0 && selectedPapers.length > 0 && sizeValid;
  const toggleLessons = (ids: string[]) => setSelectedLessons((current) =>
    ids.every((id) => current.includes(id)) ? current.filter((id) => !ids.includes(id)) : [...new Set([...current, ...ids])]
  );
  const selectionSummary = `${selectedTopics.length} ${selectedTopics.length === 1 ? 'topic' : 'topics'} · ${selectedLessons.length} ${selectedLessons.length === 1 ? 'lesson' : 'lessons'}`;
  const paperSummary = papers.filter((paper) => selectedPapers.includes(paper.id)).map((paper) => `${paper.id} ${paper.label}`).join(' + ');
  const sessionSummary = `${mode} · ${difficulty} difficulty · ${sizeType === 'All matching' ? 'All matching questions' : `${size} ${sizeType === 'Questions' ? 'questions' : 'minutes'}`} · ${order}${unattempted ? ' · Unattempted only' : ''}`;

  if (inPlayer) return (
    <div className="max-w-5xl mx-auto space-y-6">
      <button onClick={() => setInPlayer(false)} className="text-sm font-medium text-[#168f89]">Back to session setup</button>
      <div>
        <h2 className="text-2xl font-bold text-[#1d1935]">Question preview</h2>
        <p className="mt-2 text-sm text-slate-500">{selectionSummary} · {paperSummary}</p>
        <p className="mt-1 text-xs text-slate-500">{sessionSummary}</p>
      </div>
      <div className="bg-white rounded-2xl border border-slate-100 p-6 sm:p-8">
        <p className="text-xs font-semibold text-[#168f89] mb-4">Layout sample {sampleIndex + 1} of 2</p>
        <h3 className="text-lg font-semibold text-[#1d1935]">{sampleIndex === 0 ? 'A cyclist travels 120 m in 20 s. Calculate the average speed.' : 'Describe how you could measure the average speed of a moving object in the laboratory.'}</h3>
        <p className="text-sm text-slate-500 mt-6">These two sample prompts show the player layout only. They are not drawn from your selection; question matching and player behaviour will be added later.</p>
        <div className="flex justify-between mt-8">
          <button disabled={sampleIndex === 0} onClick={() => setSampleIndex(0)} className="text-sm font-medium text-[#168f89] disabled:opacity-30">Previous</button>
          <button disabled={sampleIndex === 1} onClick={() => setSampleIndex(1)} className="text-sm font-medium text-[#168f89] disabled:opacity-30">Next sample</button>
        </div>
      </div>
    </div>
  );

  return (
    <div className="topical-setup max-w-6xl mx-auto">
      <button onClick={onBack} className="text-sm font-medium text-[#168f89] mb-5">Back to revision options</button>
      <div className="mb-6">
        <p className="text-xs font-semibold tracking-widest uppercase text-[#168f89] mb-2">Physics · AS Level</p>
        <h2 className="text-2xl font-bold text-[#1d1935]">Topical practice</h2>
        <p className="text-sm text-slate-500 mt-1">Choose whole topics or individual lessons, then build your session.</p>
      </div>
      <div className="topical-papers flex flex-wrap gap-2 mb-6" aria-label="Paper types">
        <button aria-pressed={selectedPapers.length === papers.length} onClick={() => setSelectedPapers(papers.map((paper) => paper.id))} className={`px-4 py-2 rounded-full text-sm font-medium border ${selectedPapers.length === papers.length ? 'border-[#168f89] bg-[#e8f7f4] text-[#168f89]' : 'border-slate-200 bg-white text-slate-600'}`}>All papers</button>
        {papers.map((paper) => (
          <button key={paper.id} aria-pressed={selectedPapers.includes(paper.id)} onClick={() => setSelectedPapers((current) => current.includes(paper.id) ? current.filter((id) => id !== paper.id) : [...current, paper.id])} className={`px-4 py-2 rounded-full text-sm font-medium border ${selectedPapers.includes(paper.id) ? 'border-[#168f89] bg-[#e8f7f4] text-[#168f89]' : 'border-slate-200 bg-white text-slate-600'}`}>{paper.id} · {paper.label}</button>
        ))}
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-[minmax(0,1fr)_300px] gap-6 items-start">
        <section className="min-w-0" aria-labelledby="topics-heading">
          <div className="topical-list-toolbar">
          <div className="flex flex-wrap justify-between items-center gap-3 mb-4">
            <h3 id="topics-heading" className="text-base font-bold text-[#1d1935]">Topics & lessons</h3>
            <div className="flex gap-4 text-xs font-semibold">
              <button onClick={() => setSelectedLessons(allLessonIds)} className="text-[#168f89]">Select entire course</button>
              <button onClick={() => setSelectedLessons([])} className="text-slate-500">Clear</button>
            </div>
          </div>
          <input aria-label="Find a topic or lesson" placeholder="Find a topic or lesson" value={search} onChange={(event) => setSearch(event.target.value)} className={`${fieldClass} mb-4`} />
          <p className="text-xs text-slate-500 mb-4">11 topics · Select whole topics or choose lessons.</p>
          <p className="text-xs text-slate-500 mb-4">Sample counts · {selectedPapers.length ? papers.filter((paper) => selectedPapers.includes(paper.id)).map((paper) => paper.id).join(' + ') : 'No papers selected'} · {difficulty}{unattempted ? ' · Unattempted' : ''}</p>
          </div>
          <div className="space-y-3">
            {catalog.topics.filter((topic) => `${topic.title} ${topic.lessons.map((lesson) => lesson.title).join(' ')}`.toLowerCase().includes(search.toLowerCase())).map((topic) => {
              const ids = topic.lessons.map((lesson) => lesson.id);
              const count = ids.filter((id) => selectedLessons.includes(id)).length;
              return (
                <div key={topic.id} className={`topical-topic ${count ? 'has-selection' : ''}`}>
                  <div className="flex items-center gap-3">
                    <input type="checkbox" aria-label={`Select all ${topic.title} lessons`} checked={count === ids.length} ref={(node) => { if (node) node.indeterminate = count > 0 && count < ids.length; }} onChange={() => toggleLessons(ids)} className="w-4 h-4 accent-[#168f89] shrink-0" />
                    <span className="text-sm font-semibold text-[#272043] flex-1">{topic.title}</span>
                    <div className="topical-topic-count text-right shrink-0 text-xs">
                      <span className="block font-medium text-[#168f89] tabular-nums">{countLabel(ids.reduce((sum, id) => sum + lessonQuestionCount(id), 0))}</span>
                      <span className="block mt-1 text-slate-400">{count ? `${count} / ${ids.length} lessons` : `${ids.length} lessons`}</span>
                    </div>
                  </div>
                  <details className="topical-lessons mt-3" open={search.trim() ? true : undefined}>
                    <summary className="text-xs text-[#168f89] cursor-pointer w-fit py-1 ml-7">Choose lessons</summary>
                    <div className="topical-lesson-list mt-3">
                      {topic.lessons.map((lesson) => (
                        <label key={lesson.id} className={`topical-lesson flex items-start gap-3 cursor-pointer text-sm text-slate-600 ${selectedLessons.includes(lesson.id) ? 'is-selected' : ''}`}>
                          <input type="checkbox" checked={selectedLessons.includes(lesson.id)} onChange={() => toggleLessons([lesson.id])} className="w-4 h-4 accent-[#168f89] mt-0.5 shrink-0" />
                          <span className="min-w-0 flex-1">{lesson.title}</span>
                          <span className="shrink-0 text-xs text-slate-500 tabular-nums pt-0.5" title="Sample questions matching your filters">{countLabel(lessonQuestionCount(lesson.id))}</span>
                        </label>
                      ))}
                    </div>
                  </details>
                </div>
              );
            })}
            {!catalog.topics.some((topic) => `${topic.title} ${topic.lessons.map((lesson) => lesson.title).join(' ')}`.toLowerCase().includes(search.toLowerCase())) && <p className="text-sm text-slate-500 py-6">No topics or lessons found.</p>}
          </div>
        </section>
        <aside className="topical-session bg-white rounded-2xl border border-slate-100 p-5 lg:sticky lg:top-4" aria-labelledby="session-heading">
          <h3 id="session-heading" className="text-base font-bold text-[#1d1935]">Your session</h3>
          <div className="topical-session-summary mt-4">
          <p className="text-xs text-slate-500" aria-live="polite">{selectionSummary}</p>
          <p className="text-xs text-[#168f89] mt-1">{paperSummary || 'Choose at least one paper type'}</p>
          <p className="mt-3 text-lg font-semibold text-[#272043]" aria-live="polite">{countLabel(selectedQuestionCount)} available</p>
          <p className="text-xs text-slate-500 mt-1">Sample availability</p>
          </div>
          <div className="space-y-4 mt-5">
            <label className="block"><span className={labelClass}>Mode</span><select value={mode} onChange={(event) => setMode(event.target.value)} className={fieldClass}>{['Practice', 'Timed practice', 'Exam simulation', 'Games'].map((item) => <option key={item}>{item}</option>)}</select></label>
            <label className="block"><span className={labelClass}>Difficulty</span><select value={difficulty} onChange={(event) => setDifficulty(event.target.value)} className={fieldClass}>{['Mixed', 'Easy', 'Medium', 'Hard'].map((item) => <option key={item}>{item}</option>)}</select></label>
            <label className="flex items-center gap-3 text-sm text-slate-600"><input type="checkbox" checked={unattempted} onChange={(event) => setUnattempted(event.target.checked)} className="w-4 h-4 accent-[#168f89]" />Unattempted only</label>
            <div>
              <label className="block"><span className={labelClass}>Session size</span><select value={sizeType} onChange={(event) => setSizeType(event.target.value)} className={fieldClass}>{['Questions', 'Minutes', 'All matching'].map((item) => <option key={item}>{item}</option>)}</select></label>
              {sizeType !== 'All matching' && <label className="block mt-2"><span className="sr-only">{sizeType === 'Questions' ? 'Number of questions' : 'Time limit in minutes'}</span><input type="number" min="1" max="999" step="1" value={size} onChange={(event) => setSize(event.target.value)} className={fieldClass} /></label>}
              {!sizeValid && <p className="text-xs text-red-600 mt-1">Enter a whole number from 1 to 999.</p>}
            </div>
            <label className="block"><span className={labelClass}>Order</span><select value={order} onChange={(event) => setOrder(event.target.value)} className={fieldClass}>{['By topic', 'By lesson', 'Easy to hard', 'Shuffled'].map((item) => <option key={item}>{item}</option>)}</select></label>
          </div>
          <button disabled={!canStart} onClick={() => { setSampleIndex(0); setInPlayer(true); }} className="w-full mt-6 rounded-xl bg-[#2bb9b1] hover:bg-[#168f89] px-4 py-3 text-white font-semibold text-sm disabled:opacity-40 disabled:cursor-not-allowed">Preview session</button>
          <p className="text-xs text-slate-500 mt-3">{selectedLessons.length === 0 ? 'Select a topic or lesson to continue.' : 'Preview uses two sample prompts only.'}</p>
        </aside>
      </div>
    </div>
  );
};
