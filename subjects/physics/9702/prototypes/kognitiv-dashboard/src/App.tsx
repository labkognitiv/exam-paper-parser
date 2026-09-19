import { useEffect, useRef, useState, type ReactNode } from 'react';
import curriculumData from './data/curriculumFixtures.json';
import type { CurriculumLesson, CurriculumTopic } from './data/curriculumFixtures';
import {
  Activity, ArrowLeft, ArrowRight, Atom, BarChart3, BookOpen, Bookmark,
  CalendarDays, Check, CheckCircle2, ChevronDown, ChevronRight, CircleHelp,
  Clock3, Ellipsis, FlaskConical, Gamepad2, GraduationCap, Grid2X2, Home, Layers3,
  Lightbulb, ListChecks, LockKeyhole, Play, Plus,
  RotateCcw, Search, Settings, Sparkles, Target, Timer, TrendingUp, Trophy,
  UserRound, X,
} from 'lucide-react';

type Subject = 'Physics' | 'Mathematics' | 'Chemistry' | 'Biology' | 'Accounting' | 'Business' | 'Economics';
type Level = 'AS' | 'A2';
type Section = 'dashboard' | 'study' | 'revision' | 'review' | 'exercises' | 'analytics' | 'settings';
type Scenario = 'Populated Dashboard' | 'New learner' | 'Lesson in progress' | 'Lesson complete' | 'Review queue' | 'Exam running' | 'Exam ended' | 'Empty content' | 'Error example';
type Screen = 'global' | 'subject' | 'modules' | 'lessons' | 'lesson' | 'revision' | 'topical' | 'yearly' | 'paper' | 'games' | 'review' | 'exercises' | 'exercise' | 'analytics' | 'metric' | 'tracker' | 'settings' | 'signin' | 'profile';
type PlayerMode = 'practice' | 'exam' | 'revise' | 'review' | 'game' | 'readonly' | 'exercise';
type PlayerOrigin = 'study' | 'review' | 'paper' | 'game' | 'exercise' | 'analytics';

const curriculum = curriculumData as Record<'Physics' | 'Biology' | 'Chemistry', Record<Level, CurriculumTopic[]>>;
function scopeTopics(scope: {subject:Subject;level:Level}) { return scope.subject in curriculum ? curriculum[scope.subject as keyof typeof curriculum][scope.level] : []; }
function previewCompleted(total:number) { return Math.ceil(total*.46); }

const SUBJECTS: Subject[] = ['Physics', 'Mathematics', 'Chemistry', 'Biology', 'Accounting', 'Business', 'Economics'];
const scenarios: Scenario[] = ['Populated Dashboard', 'New learner', 'Lesson in progress', 'Lesson complete', 'Review queue', 'Exam running', 'Exam ended', 'Empty content', 'Error example'];
const nav: { id: Section; label: string; icon: typeof Home }[] = [
  { id: 'dashboard', label: 'Dashboard', icon: Home }, { id: 'study', label: 'Study', icon: BookOpen },
  { id: 'revision', label: 'Revision', icon: Target }, { id: 'review', label: 'Review', icon: Bookmark },
  { id: 'exercises', label: 'Exercises', icon: ListChecks }, { id: 'analytics', label: 'Analytics', icon: BarChart3 },
];
const subjectMeta: Record<Subject, { color: string; tint: string; progress: number; icon: typeof Atom; image?: string; overlay?: string }> = {
  Physics: { color: '#168f89', tint: '#e6f7f4', progress: 42, icon: Atom, image: '/assets/subjects/physics-card.png', overlay: 'rgba(4, 28, 48, .68)' },
  Mathematics: { color: '#6958c9', tint: '#eeecff', progress: 68, icon: Sparkles, image: '/assets/subjects/mathematics-card.png', overlay: 'rgba(25, 24, 77, .68)' },
  Chemistry: { color: '#d96a3d', tint: '#fff0e8', progress: 55, icon: FlaskConical, image: '/assets/subjects/chemistry-card.png', overlay: 'rgba(72, 15, 18, .64)' }, Biology: { color: '#398c51', tint: '#eaf7e7', progress: 31, icon: Activity },
  Accounting: { color: '#477cac', tint: '#eaf3fb', progress: 0, icon: BarChart3 }, Business: { color: '#9a6734', tint: '#f8efe4', progress: 0, icon: Layers3 },
  Economics: { color: '#a2486a', tint: '#f9eaf1', progress: 0, icon: TrendingUp },
};

function Button({ children, onClick, tone = 'primary', className = '', disabled = false }: { children: ReactNode; onClick?: () => void; tone?: 'primary' | 'secondary' | 'quiet'; className?: string; disabled?: boolean }) { return <button type="button" className={`btn ${tone} ${className}`} onClick={onClick} disabled={disabled}>{children}</button>; }
function Badge({ children, tone = 'neutral' }: { children: ReactNode; tone?: 'neutral' | 'teal' | 'warm' | 'rose' | 'violet' }) { return <span className={`badge ${tone}`}>{children}</span>; }
function Progress({ value }: { value: number }) { return <div className="progress" role="progressbar" aria-label="Course completion" aria-valuemin={0} aria-valuemax={100} aria-valuenow={value}>
<span style={{ width: `${value}%` }} />
</div>; }
function SectionTitle({ eyebrow, title, copy, action }: { eyebrow?: string; title: string; copy?: string; action?: ReactNode }) { return <div className="section-title">
<div>{eyebrow && <p className="eyebrow">{eyebrow}</p>}<h1>{title}</h1>{copy && <p>{copy}</p>}</div>{action}</div>; }

function MiniChart({ type = 'bars', progressLabel = '14 of 30 lessons' }: { type?: 'bars' | 'line' | 'heat' | 'progress'; progressLabel?:string }) {
  if (type === 'heat') return <div className="heatmap">{Array.from({ length: 35 }, (_, i) => <i key={i} className={`h${(i * 7 + i % 4) % 5}`} />)}</div>;
  if (type === 'line') return <svg className="line-chart" viewBox="0 0 300 90" role="img" aria-label="Performance rises from 58 to 76 percent">
<defs>
<linearGradient id="fill" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stopColor="#a698ee" stopOpacity=".35"/>
<stop offset="1" stopColor="#a698ee" stopOpacity="0"/>
</linearGradient>
</defs>
<path d="M0 78 C35 63,55 69,83 50 S135 61,165 37 S220 40,245 22 S280 26,300 10 L300 90 L0 90Z" fill="url(#fill)"/>
<path d="M0 78 C35 63,55 69,83 50 S135 61,165 37 S220 40,245 22 S280 26,300 10" fill="none" stroke="#6958c9" strokeWidth="4" strokeLinecap="round"/>
<g fill="#fff" stroke="#6958c9" strokeWidth="3">{[[0,78],[83,50],[165,37],[245,22],[300,10]].map(([x,y])=>
<circle key={x} cx={x} cy={y} r="5"/>)}</g>
</svg>;
  if (type === 'progress') return <div className="rings">
<div>
<strong>46%</strong>
<span>{progressLabel}</span>
</div>
</div>;
  return <div className="bar-chart">{[35,61,46,82,69,94,54].map((h,i)=>
<span key={i} style={{height:`${h}%`}} title={`${['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][i]} · ${Math.round(h/4)} questions`} />)}</div>;
}
function DashboardCharts({ onMetric, empty = false, scopeLabel = 'Across enrolled courses', lessonTotal }: { onMetric: (title:string) => void; empty?: boolean; scopeLabel?: string; lessonTotal?:number }) {
  const completed=lessonTotal?previewCompleted(lessonTotal):14; const cards = [{ title: 'Study consistency', meta: '12 day streak', type: 'heat' as const, stat: '18 active days' },{ title: 'Practice activity', meta: 'Last 7 days', type: 'bars' as const, stat: '94 questions' },{ title: 'Scored performance', meta: '18 scored questions', type: 'line' as const, stat: '76% latest' },{ title: 'Study progress', meta: scopeLabel, type: 'progress' as const, stat: `${completed} lessons complete` }];
  return <div className="chart-grid">{cards.map(c => <article className="chart-card" key={c.title}>
<div className="card-head">
<div>
<h3>{c.title}</h3>
<p>{empty ? 'No activity yet' : c.meta}</p>
</div>
</div>{empty ? <div className="chart-empty">
<strong>No activity yet</strong>
<span>Your learning will appear here.</span>
</div> : <MiniChart type={c.type} progressLabel={c.type==='progress'&&lessonTotal?`${completed} of ${lessonTotal} lessons`:'14 of 30 lessons'}/>}<div className="chart-foot">
<strong>{empty ? 'Ready when you are' : c.stat}</strong>
<button onClick={()=>onMetric(c.title)}>View details</button>
</div>
</article>)}</div>;
}

const consistencyDays = [
  { day: 'Monday', short: 'Mon', minutes: 42, questions: 18, level: 3 },
  { day: 'Tuesday', short: 'Tue', minutes: 28, questions: 12, level: 2 },
  { day: 'Wednesday', short: 'Wed', minutes: 0, questions: 0, level: 0 },
  { day: 'Thursday', short: 'Thu', minutes: 67, questions: 31, level: 4 },
  { day: 'Friday', short: 'Fri', minutes: 35, questions: 16, level: 2 },
  { day: 'Saturday', short: 'Sat', minutes: 86, questions: 38, level: 4 },
  { day: 'Sunday', short: 'Sun', minutes: 21, questions: 8, level: 1 },
];
const courseProgress = [
  { subject: 'Physics', study: 68, papers: 42, color: '#137e79' },
  { subject: 'Mathematics', study: 54, papers: 31, color: '#6958c9' },
  { subject: 'Chemistry', study: 73, papers: 58, color: '#c65a42' },
];
const assessmentPerformance = [
  { subject: 'Physics', score: 78, change: '+6%' },
  { subject: 'Mathematics', score: 71, change: '+3%' },
  { subject: 'Chemistry', score: 83, change: '+8%' },
];
function GlobalDashboardAnalytics({ onMetric, empty = false }: { onMetric: (title:string) => void; empty?: boolean }) { return <div className="global-analytics">
<article className="chart-card consistency-card">
<div className="card-head"><div><h3>Study consistency</h3><p>{empty ? 'No activity yet' : 'Monday to Sunday · sample week'}</p></div></div>
{empty ? <div className="chart-empty"><strong>No activity yet</strong><span>Your learning will appear here.</span></div> : <div className="consistency-heatmap" role="list" aria-label="Study activity from Monday to Sunday">{consistencyDays.map(day=><button type="button" role="listitem" key={day.day} className={`consistency-day heat-${day.level}`} aria-label={`${day.day}: ${day.minutes} minutes studied, ${day.questions} questions attempted`}>
<span className="heat-cell" aria-hidden="true"/><strong>{day.short}</strong><span className="day-tooltip" role="tooltip"><b>{day.day}</b><span>{day.minutes} min studied</span><span>{day.questions} questions attempted</span></span>
</button>)}</div>}
<div className="chart-foot"><strong>{empty ? 'Ready when you are' : '5 active days · 4h 39m'}</strong><button onClick={()=>onMetric('Study consistency')}>View details</button></div>
</article>
<article className="chart-card course-progress-card">
<div className="card-head"><div><h3>Study progress</h3><p>{empty ? 'No progress yet' : 'Illustrative study and past-paper completion'}</p></div></div>
{empty ? <div className="chart-empty"><strong>No progress yet</strong><span>Course progress will appear here.</span></div> : <div className="course-progress-list">{courseProgress.map(course=><div className="course-progress-row" key={course.subject} style={{'--course-color':course.color} as React.CSSProperties}>
<strong>{course.subject}</strong><div className="course-measures"><div><span>Study <b>{course.study}%</b></span><div className="course-track" role="progressbar" aria-label={`${course.subject} study progress`} aria-valuemin={0} aria-valuemax={100} aria-valuenow={course.study}><i style={{width:`${course.study}%`}}/></div></div><div><span>Past papers <b>{course.papers}%</b></span><div className="course-track paper" role="progressbar" aria-label={`${course.subject} past paper progress`} aria-valuemin={0} aria-valuemax={100} aria-valuenow={course.papers}><i style={{width:`${course.papers}%`}}/></div></div></div>
</div>)}</div>}
<div className="chart-foot"><strong>{empty ? 'Ready when you are' : '3 enrolled courses'}</strong><button onClick={()=>onMetric('Study progress')}>View details</button></div>
</article>
<article className="chart-card performance-card">
<div className="card-head"><div><h3>Assessment performance</h3><p>{empty ? 'No scores yet' : 'Latest scored work · illustrative results'}</p></div></div>
{empty ? <div className="chart-empty"><strong>No scores yet</strong><span>Results will appear after your first assessment.</span></div> : <div className="performance-list">{assessmentPerformance.map(course=><div className="performance-row" key={course.subject}><strong>{course.subject}</strong><div className="performance-track"><i style={{width:`${course.score}%`}}/></div><b>{course.score}%</b><span>{course.change}</span></div>)}</div>}
<div className="chart-foot"><strong>{empty ? 'Ready when you are' : '77% average · up 6 points'}</strong><button onClick={()=>onMetric('Assessment performance')}>View details</button></div>
</article>
</div>; }

function Sidebar({ scope, active, onNav, onGlobal, onSettings, onScope, open, onClose }: { scope: { subject: Subject; level: Level } | null; active: Section; onNav: (s: Section) => void; onGlobal: () => void; onSettings: () => void; onScope:()=>void; open: boolean; onClose: () => void }) {
  return <>
<button type="button" className={`drawer-shade ${open ? 'show' : ''}`} aria-label="Close navigation" onClick={onClose}/>
<aside className={`sidebar ${open ? 'open' : ''}`} aria-label="Primary navigation">
<button className="brand" onClick={onGlobal}>
<span>K</span>
<strong>Kognitiv</strong>
</button>
{scope && <div className="scope-box"><button className="scope-current" onClick={onScope}>
<span>
<strong>{scope.subject}</strong>
<small>{scope.level} Level</small>
</span>
</button></div>}
<nav>{nav.map(item => { const disabled=!scope && item.id !== 'dashboard'; const Icon=item.icon; return <button key={item.id} disabled={disabled} className={active===item.id ? 'active' : ''} aria-current={active===item.id?'page':undefined} onClick={()=>onNav(item.id)} title={disabled?'Choose a subject to start':''}>
<Icon size={17} aria-hidden="true"/><span>{item.label}</span>{item.id==='review'&&scope&&<em>10</em>}</button>})}</nav>
<div className="sidebar-bottom">
<button className={active==='settings'?'active':''} aria-current={active==='settings'?'page':undefined} onClick={onSettings}>
<Settings size={17} aria-hidden="true"/>Settings</button>
<div className="profile">
<span>AA</span>
<div>
<strong>Abdullah</strong>
<small>Student account</small>
</div>
</div>
</div>
</aside>
</>;
}
function PreviewBar({ scenario, setScenario, reset }: { scenario: Scenario; setScenario: (s: Scenario) => void; reset: () => void }) { const [open,setOpen]=useState(false); return <div className="preview-bar">
<div>
<Sparkles size={15}/>
<strong>Design preview</strong>
<span>Sample data</span>
</div>
<div className="preview-actions">
<button onClick={()=>setOpen(!open)}>Scenario: {scenario}<ChevronDown size={14}/>
</button>
<button aria-label="Reset preview" onClick={reset}>
<RotateCcw size={16}/>
</button>
</div>{open&&<div className="scenario-menu">{scenarios.map(s=>
<button key={s} className={s===scenario?'selected':''} onClick={()=>{setScenario(s);setOpen(false)}}>
<span>{s}</span>{s===scenario&&<Check size={16}/>}</button>)}</div>}</div>; }
function Streak({ empty = false }: { empty?: boolean }) { return <div className="streak">
<strong>{empty ? '0' : '12'}</strong><span>{empty ? 'start streak' : 'day streak'}</span>
<div className="streak-days" aria-hidden="true">{Array.from({length:7},(_,i)=><i key={i} className={!empty&&i<6?'active':''}/>)}</div>
</div>; }
function Topbar({ scope, title, onMenu, compact = false }: { scope: { subject: Subject; level: Level } | null; title: string; onMenu: () => void; compact?: boolean }) { return <header className={`topbar ${compact ? 'compact' : ''}`}>
<button className="mobile-menu" aria-label="Open navigation" onClick={onMenu}>
<Grid2X2 size={18} aria-hidden="true"/><span>Menu</span>
</button>
<div>
{title !== 'Dashboard'&&<>{scope && <small>{scope.subject} · {scope.level}</small>}<strong>{title}</strong></>}
</div>
</header>; }
function SubjectCard({ subject, levels, onOpen, onRemove }: { subject: Subject; levels: Level[]; onOpen: () => void; onRemove: () => void }) { const meta=subjectMeta[subject]; const [menuOpen,setMenuOpen]=useState(false); const menuRef=useRef<HTMLDivElement>(null); useEffect(()=>{if(!menuOpen)return;const close=(event:PointerEvent)=>{if(!menuRef.current?.contains(event.target as Node))setMenuOpen(false)};const closeOnEscape=(event:KeyboardEvent)=>{if(event.key==='Escape')setMenuOpen(false)};document.addEventListener('pointerdown',close);document.addEventListener('keydown',closeOnEscape);return()=>{document.removeEventListener('pointerdown',close);document.removeEventListener('keydown',closeOnEscape)}},[menuOpen]); return <article className="subject-card" style={{'--subject':meta.color,'--subject-image':`url(${meta.image ?? ''})`,'--subject-overlay':meta.overlay ?? 'rgba(25, 31, 49, .72)'} as React.CSSProperties}>
<div className="subject-card-top">
<div className="level-pills">{levels.map(l=><span key={l}>{l}</span>)}</div>
<div className="subject-actions" ref={menuRef}>
<button className="card-menu-trigger" aria-label={`More options for ${subject}`} aria-haspopup="menu" aria-expanded={menuOpen} onClick={()=>setMenuOpen(value=>!value)}><Ellipsis size={20} aria-hidden="true"/></button>
{menuOpen&&<div className="subject-menu" role="menu"><button role="menuitem" onClick={()=>{setMenuOpen(false);onRemove()}}>Remove subject</button></div>}
</div>
</div>
<button className="subject-main" aria-label={`Open ${subject}`} onClick={onOpen}>
<h3>{subject}</h3>
<span>Open course <ArrowRight size={16} aria-hidden="true"/></span>
</button>
</article>; }

function RemoveSubjectDialog({ subject, onCancel, onConfirm }: { subject:Subject; onCancel:()=>void; onConfirm:()=>void }) { return <div className="remove-dialog-backdrop" role="presentation" onMouseDown={onCancel}><div className="remove-dialog" role="dialog" aria-modal="true" aria-labelledby="remove-subject-title" onMouseDown={e=>e.stopPropagation()}><p>REMOVE SUBJECT</p><h2 id="remove-subject-title">Remove {subject}?</h2><span>This removes it from your dashboard. You can add it again later.</span><div><button onClick={onCancel}>Cancel</button><button className="confirm-remove" onClick={onConfirm}>Remove subject</button></div></div></div>; }

function GlobalDashboard({ enrolled, choices, onOpen, onAdd, onRemove, onMetric, empty }: { enrolled: Subject[]; choices: Partial<Record<Subject,Level>>; onOpen:(s:Subject)=>void; onAdd:()=>void; onRemove:(s:Subject)=>void; onMetric:(title:string)=>void; empty:boolean }) { const [period,setPeriod]=useState('month'); const [removeTarget,setRemoveTarget]=useState<Subject|null>(null); const subjectGridRef=useRef<HTMLDivElement>(null); const periods=[['7days','Last 7 days'],['month','Last month'],['3months','Last 3 months']] as const; useEffect(()=>{subjectGridRef.current?.scrollTo({left:0,behavior:'instant'})},[enrolled.length]);
  return <div className="page">
<SectionTitle title="Good morning Abdullah" copy="Choose a course or continue your latest lesson." action={<div className="period-tabs" role="group" aria-label="Dashboard period">{periods.map(([value,label])=><button key={value} aria-pressed={period===value} className={period===value?'active':''} onClick={()=>setPeriod(value)}>{label}</button>)}</div>}/>
<section>
<div className="row-title">
<div>
<h2>Your subjects</h2>
<p>{empty ? 'Choose your first course.' : `${enrolled.length} enrolled ${enrolled.length===1?'course':'courses'}`}</p>
</div>
<div className="subject-tools"><Streak empty={empty}/><Button tone="secondary" onClick={onAdd}><Plus size={16} aria-hidden="true"/>Add subject</Button></div>
</div>{empty ? <div className="empty-hero">
<h2>Add your first subject</h2>
<p>Choose a subject and level to shape your learning space.</p>
<Button onClick={onAdd}><Plus size={16} aria-hidden="true"/>Add subject</Button>
</div> : <div className="subject-grid" ref={subjectGridRef} aria-label="Enrolled subjects">{enrolled.map(s=>
<SubjectCard key={s} subject={s} levels={[choices[s]??'AS']} onOpen={()=>onOpen(s)} onRemove={()=>setRemoveTarget(s)}/>)}</div>}</section>{!empty&&<button className="continue-strip" onClick={()=>onOpen('Physics')}>
<span>
<small>START WHERE YOU LEFT OFF · PHYSICS AS</small>
<strong>Waves · Progressive waves</strong>
<em>Notes · section 3 of 6</em>
</span>
<span className="continue-action">Continue <ArrowRight size={16} aria-hidden="true"/></span>
</button>}<div className="row-title analytics-title">
<div>
<h2>Your snapshot</h2>
<p>One clear view across your subjects.</p>
</div>
</div>
<GlobalDashboardAnalytics onMetric={onMetric} empty={empty}/>
{removeTarget&&<RemoveSubjectDialog subject={removeTarget} onCancel={()=>setRemoveTarget(null)} onConfirm={()=>{onRemove(removeTarget);setRemoveTarget(null)}}/>}
</div>;
}
function SubjectDashboard({ scope, onStudy, onMetric, onCalendar }: { scope:{subject:Subject;level:Level}; onStudy:()=>void; onMetric:(title:string)=>void; onCalendar:()=>void }) { const meta=subjectMeta[scope.subject]; const topic=scopeTopics(scope)[0]; const firstLesson=topic?.modules[0]?.lessons[0]; const next=topic&&firstLesson?`${topic.title} · ${firstLesson.title}`:scope.subject==='Mathematics'?'Pure mathematics · Quadratics':'Curriculum preview'; return <div className="page">
<div className="subject-hero" style={{'--subject':meta.color,'--subject-tint':meta.tint} as React.CSSProperties}>
<div>
<p className="eyebrow">{scope.subject.toUpperCase()} · {scope.level} LEVEL</p>
<h1>Welcome back, Abdullah.</h1>
<p>Build momentum with one clear next step.</p>
<button className="hero-continue" onClick={onStudy}>
<span>
<BookOpen/>
</span>
<span>
<small>CONTINUE LEARNING</small>
<strong>{next}</strong>
<em>Notes · section 3 of 6</em>
</span>
<ArrowRight/>
</button>
</div>
<div className="calendar-card">
<div className="card-head">
<div>
<h3>September 2026</h3>
<p>Subject activity</p>
</div>
<CalendarDays size={20}/>
</div>
<div className="week">
<b>M</b>
<b>T</b>
<b>W</b>
<b>T</b>
<b>F</b>
<b>S</b>
<b>S</b>{[7,8,9,10,11,12,13].map(n=>
<button key={n} className={n===12?'today':n===9?'active-day':''} onClick={onCalendar}>{n}{n===9&&<i/>}</button>)}</div>
<button className="exam-row" onClick={onCalendar}>
<span>
<CalendarDays/>
</span>
<span>
<small>SAMPLE EXAM DATE</small>
<strong>Paper 2 · 18 May 2027</strong>
</span>
<ChevronRight/>
</button>
</div>
</div>
<div className="row-title analytics-title">
<div>
<h2>{scope.subject} snapshot</h2>
<p>{scope.level} level · last 28 days</p>
</div>
<button className="text-link" onClick={()=>onMetric('Scored performance')}>Open Analytics <ArrowRight size={15}/>
</button>
</div>
<DashboardCharts onMetric={onMetric} scopeLabel={`${scope.subject} · ${scope.level}`} lessonTotal={scopeTopics(scope).reduce((n,t)=>n+t.modules.reduce((x,m)=>x+m.lessons.length,0),0)}/>
</div>; }

function Modules({ scope, onOpen }: { scope:{subject:Subject;level:Level}; onOpen:(topic:CurriculumTopic)=>void }) { const topics=scopeTopics(scope); return <div className="page narrow">
<SectionTitle eyebrow={`STUDY · ${scope.subject.toUpperCase()} ${scope.level}`} title="Choose a topic" copy={topics.length ? `${topics.length} authored topics · ${topics.reduce((n,t)=>n+t.modules.reduce((x,m)=>x+m.lessons.length,0),0)} lesson titles available` : 'A curriculum title preview is not available for this subject yet.'} action={<button className="search-button">
<Search size={17}/>Browse curriculum</button>}/>
<div className="module-list">{topics.map((topic,i)=>{const count=topic.modules.reduce((n,m)=>n+m.lessons.length,0); const progress=(i*17+23)%88; return <button key={topic.id} onClick={()=>onOpen(topic)}>
<span className="module-number">{String(i+1).padStart(2,'0')}</span>
<span className="module-info">
<small>TOPIC {i+1} · {topic.modules.length} COURSE {topic.modules.length===1?'MODULE':'MODULES'}</small>
<strong>{topic.title}</strong>
<em>{Math.round(count*progress/100)} of {count} {count===1?'lesson':'lessons'} previewed</em>
<Progress value={progress}/>
</span>
<span className="module-action">View curriculum<ChevronRight/>
</span>
</button>})}</div>
</div>; }
function Lessons({ scope, topic, onBack, onOpen }: { scope:{subject:Subject;level:Level}; topic:CurriculumTopic; onBack:()=>void; onOpen:(lesson:CurriculumLesson)=>void }) { let sequence=0; return <div className="page narrow">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to topics</Button>
<SectionTitle eyebrow={`TOPIC · ${scope.subject.toUpperCase()} ${scope.level}`} title={topic.title} copy={`${topic.modules.length} course ${topic.modules.length===1?'module':'modules'} · ${topic.modules.reduce((n,m)=>n+m.lessons.length,0)} authored lesson titles`}/>
<div className="preview-example-note"><Sparkles size={16}/><span><strong>Sample content preview</strong>Each title opens the same short example note and question set to demonstrate the lesson workspace.</span></div>
<div className="curriculum-modules">{topic.modules.map((module,moduleIndex)=><section className="curriculum-module" key={module.id}>
<div className="curriculum-module-head"><div><small>MODULE {moduleIndex+1}</small><h2>{module.title}</h2></div><Badge tone="neutral">{module.lessons.length} {module.lessons.length===1?'lesson':'lessons'}</Badge></div>
<div className="lesson-list">{module.lessons.map(lesson=>{const i=sequence++; const state=i%7===0?'Complete':i%5===0?'In progress':'Preview'; return <button key={lesson.id} onClick={()=>onOpen(lesson)} className={state==='In progress'?'current':''}>
<span className={`lesson-state ${state==='Complete'?'done':state==='In progress'?'doing':''}`}>{state==='Complete'?<Check/>:i+1}</span>
<span><strong>{lesson.title}</strong><small>Notes preview · 20 sample questions</small></span>
<span>{state==='In progress'?'Continue':'Open'}<ChevronRight/></span>
</button>})}</div></section>)}</div>
</div>; }
function Lesson({ scope, topic, lesson, scenario, notesDone, setNotesDone, tab, setTab, onBack, onPlayer }: { scope:{subject:Subject;level:Level}; topic:CurriculumTopic; lesson:CurriculumLesson; scenario:Scenario; notesDone:boolean; setNotesDone:(v:boolean)=>void; tab:'notes'|'questions'; setTab:(v:'notes'|'questions')=>void; onBack:()=>void; onPlayer:()=>void }) { const attempted=scenario==='Lesson complete'?20:scenario==='Lesson in progress'?17:7; const bio=scope.subject==='Biology'; const chemistry=scope.subject==='Chemistry'; return <div className="page lesson-page">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to lessons</Button>
<div className="lesson-heading">
<div>
<p className="eyebrow">{topic.title.toUpperCase()} · LESSON PREVIEW</p>
<h1>{lesson.title}</h1>
</div>
<Badge tone={scenario==='Lesson complete'?'teal':'warm'}>{scenario==='Lesson complete'?<>
<Check size={14}/>Lesson complete</>:<>In progress</>}</Badge>
</div>
<div className="tabs">
<button className={tab==='notes'?'active':''} onClick={()=>setTab('notes')}>Notes {notesDone&&<Check size={14}/>}</button>
<button className={tab==='questions'?'active':''} onClick={()=>setTab('questions')}>Questions · 20</button>
</div>{scenario==='Error example' ? <div className="error-card">
<CircleHelp/>
<h2>These notes could not load</h2>
<p>Your lesson location is safe in this preview.</p>
<Button onClick={()=>setTab('questions')}>Try again</Button>
</div> : tab==='notes' ? <article className="notes-reader">
<div className="notes-toolbar">
<Badge tone="violet">Reusable HTML preview</Badge>
<button>Contents <ChevronDown size={14}/>
</button>
</div>
<p className="kicker">CORE IDEA</p>
<div className="preview-example-note"><Sparkles size={16}/><span><strong>Preview example</strong>This same short note and question set is reused across lesson titles to demonstrate the workspace.</span></div>
<h2>{bio?'Cells contain specialised structures that work together.':chemistry?'Particles and their arrangement explain observable properties.':'Acceleration tells us how quickly velocity changes.'}</h2>
<p className="lead">{bio?'Animal and plant cells share core structures, while plant cells also have a cellulose wall, chloroplasts and a permanent vacuole.':chemistry?'A particle model connects structure, bonding and energy changes to the behaviour we can measure.':"When an object's velocity changes, it is accelerating. The change may be in speed, direction, or both."}</p>
<div className="formula-card">
<span>acceleration</span>
<strong>{bio?'magnification = image size ÷ actual size':chemistry?'n = m ÷ M':<>a = <span>Δv</span> / <span>Δt</span></>}
</strong>
<small>{bio?'Use the same units before dividing':chemistry?'amount = mass ÷ molar mass':'metres per second squared · m s⁻²'}</small>
</div>
<h3>{bio?'Comparing cell structures':'Reading a velocity–time graph'}</h3>
<p>{bio?'A cell diagram should show which structures are shared and which are distinctive. Label only structures that the evidence supports.':'The gradient of a velocity–time graph gives acceleration. A steeper gradient means a larger change in velocity each second.'}</p>
<div className="lesson-visual">
<svg viewBox="0 0 420 180">
<path d="M44 18V150H390" stroke="#aaa" strokeWidth="2" fill="none"/>
<path d="M45 145L355 34" stroke="#2bb9b1" strokeWidth="5" strokeLinecap="round"/>
<path d="M90 129H290V58" fill="#e6f7f4" stroke="#8bd7d1" strokeDasharray="5 5"/>
<text x="172" y="164">time / s</text>
<text x="9" y="92" transform="rotate(-90 9 92)">velocity / m s⁻¹</text>
</svg>
<div>
<Badge tone="teal">Notice</Badge>
<strong>Constant positive gradient</strong>
<p>The object has constant positive acceleration.</p>
</div>
</div>
<div className="check-card">
<div>
<CheckCircle2/>
<span>
<strong>{notesDone?'Notes complete':'Ready to continue?'}</strong>
<small>{notesDone?'Marked complete for this preview visit.':'Mark these notes when you have finished reading.'}</small>
</span>
</div>{notesDone?<>
<Button onClick={()=>setTab('questions')}>Start questions <ArrowRight size={16}/>
</Button>
<Button tone="quiet" onClick={()=>setNotesDone(false)}>Undo</Button>
</>:<Button onClick={()=>setNotesDone(true)}>Mark notes complete</Button>}</div>
</article> : <div className="questions-intro">
<div className="question-progress">
<span>
<strong>{attempted}</strong>
<em>/ 20 attempted</em>
</span>
<Progress value={attempted*5}/>
</div>
<h2>{attempted===20?'Questions complete':'Continue your lesson questions'}</h2>
<p>{attempted===20?'You attempted every required question. Correctness stays separate from completion.':`${20-attempted} questions remain in this sample set.`}</p>
<div className="question-actions">
<Button onClick={onPlayer}>{attempted===20?'Review answers':'Continue questions'}<ArrowRight size={17}/>
</Button>{attempted===20&&<Button tone="secondary" onClick={onPlayer}>Practise again</Button>}</div>
<div className="question-preview-grid">{Array.from({length:20},(_,i)=>
<span key={i} className={i<attempted?'done':i===attempted?'current':''}>{i+1}</span>)}</div>
</div>}</div>; }

function RevisionHub({ open }: { open:(s:'topical'|'yearly'|'games')=>void }) { const cards=[['topical','Topical','Build a focused session from topics and lessons.',Target,'2 topics selected'],['yearly','Yearly','Browse complete papers by year, session and mode.',CalendarDays,'2016–2025'],['games','Games','Follow a visual path with quick, varied interactions.',Gamepad2,'Continue Kinematics']] as const; return <div className="page">
<SectionTitle eyebrow="PHYSICS · AS LEVEL" title="Revision" copy="Choose how you want to practise today."/>
<div className="revision-grid">{cards.map(([id,title,copy,Icon,meta])=>
<button key={id} onClick={()=>open(id)}>
<span className={`revision-icon ${id}`}>
<Icon/>
</span>
<h2>{title}</h2>
<p>{copy}</p>
<div>
<Badge tone={id==='games'?'violet':'teal'}>{meta}</Badge>
<span>Open <ArrowRight/>
</span>
</div>
</button>)}</div>
</div>; }
function Topical({ onBack, onPlayer }: { onBack:()=>void; onPlayer:()=>void }) { const [setup,setSetup]=useState(false); const [more,setMore]=useState(false); return <div className="page narrow">
<Button tone="quiet" onClick={()=>setup?setSetup(false):onBack()}>
<ArrowLeft size={17}/>{setup?'Back to topics':'Back to Revision'}</Button>{!setup?<>
<SectionTitle eyebrow="TOPICAL" title="What would you like to practise?" copy="Select a topic, or open it to choose individual lessons."/>
<div className="topic-select">{['Physical quantities & units','Kinematics','Dynamics','Forces, density & pressure','Work, energy & power'].map((t,i)=>
<div className={i===1?'selected':''} key={t}>
<button className="check">{i===1?<Check/>:''}</button>
<span>
<strong>{t}</strong>
<small>{i===1?'3 lessons selected':'6 lessons'}</small>
</span>
<button>
<ChevronDown/>
</button>
</div>)}</div>
<div className="sticky-summary">
<span>
<strong>1 topic · 3 lessons</strong>
<small>42 example questions available</small>
</span>
<Button onClick={()=>setSetup(true)}>Continue <ArrowRight size={16}/>
</Button>
</div>
</>:<>
<SectionTitle eyebrow="TOPICAL · 1 TOPIC" title="Set up your session" copy="Kinematics · 3 lessons"/>
<div className="setup-card">
<label>Question type<select>
<option>MCQs · Paper 1</option>
<option>Structured · Paper 2</option>
</select>
</label>
<div>
<span className="field-label">Mode</span>
<div className="segmented">
<button className="active">Practice<small>Feedback as you go</small>
</button>
<button>Exam<small>Support hidden</small>
</button>
<button>Revise<small>Read through</small>
</button>
</div>
</div>
<div>
<span className="field-label">Length</span>
<div className="lengths">
<button className="active">10</button>
<button>20</button>
<button>All 42</button>
</div>
</div>
<button className="more" onClick={()=>setMore(!more)}>More options <Badge tone="violet">2 customised</Badge>
<ChevronDown/>
</button>{more&&<div className="advanced">
<label>Difficulty<select>
<option>Mixed</option>
</select>
</label>
<label>Order<select>
<option>By topic</option>
</select>
</label>
</div>}</div>
<div className="session-summary">
<div>
<small>YOUR SESSION</small>
<strong>10 Physics MCQs · Practice</strong>
<span>Kinematics · Mixed difficulty</span>
</div>
<Button onClick={onPlayer}>Start session <Play size={16}/>
</Button>
</div>
</>}</div>; }
function Yearly({ onBack, onPaper }: { onBack:()=>void; onPaper:()=>void }) { return <div className="page narrow">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to Revision</Button>
<SectionTitle eyebrow="YEARLY PAPERS" title="Choose a paper" copy="Physics · AS Level" action={<div className="period">Paper 2 <ChevronDown size={15}/>
</div>}/>
<div className="year-strip">{[2025,2024,2023,2022,2021].map((y,i)=>
<button className={i===0?'active':''} key={y}>{y}</button>)}</div>
<h2 className="subheading">May / June 2025</h2>
<div className="paper-list">{[['Physics AS Theory','Paper 21','New'],['Physics AS Theory','Paper 22','In progress'],['Physics AS Theory','Paper 23','Attempted']].map((p,i)=>
<button key={p[1]} onClick={onPaper}>
<span className="paper-icon">
<BookOpen/>
</span>
<span>
<strong>{p[0]}</strong>
<small>9702/2{i+1} · 60 marks · 1 hour 15 min</small>
</span>
<Badge tone={i===1?'warm':i===2?'teal':'neutral'}>{p[2]}</Badge>
<ChevronRight/>
</button>)}</div>
</div>; }
function Paper({ onBack, onPlayer, onExam }: { onBack:()=>void; onPlayer:(mode:PlayerMode)=>void; onExam:()=>void }) { return <div className="page narrow">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to papers</Button>
<div className="paper-hero">
<Badge tone="violet">MAY / JUNE 2025</Badge>
<h1>Physics AS Theory · Paper 22</h1>
<p>9702/22 · 7 complete questions</p>
<div>
<span>
<Clock3/>1 hour 15 min</span>
<span>
<Trophy/>60 marks</span>
<span>
<CheckCircle2/>Previous: 41 / 60</span>
</div>
</div>
<h2 className="subheading">Choose a mode</h2>
<div className="mode-grid">
<button onClick={()=>onPlayer('practice')}>
<Target/>
<strong>Practice</strong>
<span>Answer with support available when you need it.</span>
<em>Start practice <ArrowRight/>
</em>
</button>
<button onClick={onExam}>
<Timer/>
<strong>Exam</strong>
<span>Timed conditions. Support appears after finishing.</span>
<em>Start exam <ArrowRight/>
</em>
</button>
<button onClick={()=>onPlayer('revise')}>
<BookOpen/>
<strong>Revise</strong>
<span>Read questions, schemes and walkthroughs together.</span>
<em>Open paper <ArrowRight/>
</em>
</button>
</div>
<button className="previous-attempt">
<span>
<strong>Previous attempts</strong>
<small>1 example attempt · 68%</small>
</span>
<ChevronDown/>
</button>
</div>; }
function Games({ onBack, onNode }: { onBack:()=>void; onNode:()=>void }) { const nodes=[{name:'Distance & displacement',state:'complete',icon:Check},{name:'Speed & velocity',state:'complete',icon:Check},{name:'Acceleration',state:'current',icon:Play},{name:'Motion graphs',state:'available',icon:Sparkles},{name:'Equations of motion',state:'locked',icon:LockKeyhole}]; return <div className="page game-page">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to Revision</Button>
<div className="game-banner">
<div>
<Badge tone="violet">TOPIC 02</Badge>
<h1>Kinematics</h1>
<p>Follow the path. Each stop turns a core idea into a short game.</p>
</div>
<div className="game-stats">
<span>
<Trophy/>2 complete</span>
<span>
<Target/>5 nodes</span>
</div>
</div>
<div className="path-wrap">
<div className="path-line"/>{nodes.map((n,i)=>{const Icon=n.icon;return <div className={`path-node ${n.state} side-${i%2}`} key={n.name}>
<button onClick={n.state==='locked'?undefined:onNode}>
<Icon/>
</button>
<div>
<small>{n.state==='current'?'CURRENT LESSON':n.state.toUpperCase()}</small>
<strong>{n.name}</strong>
<span>{n.state==='locked'?'Games coming soon':n.state==='current'?'Medium · 12 quick questions':'Choice · matching · order'}</span>
</div>
</div>})}</div>
</div>; }

function ReviewList({ onOpen }: { onOpen:(i:number,readOnly:boolean)=>void }) { const items=['Vectors and scalars','Acceleration from graphs','Newton’s second law','Moments and equilibrium','Conservation of momentum','Electric current','Potential difference','Wave superposition','Stationary waves','Particle interactions']; return <div className="page narrow">
<SectionTitle eyebrow="PHYSICS · AS LEVEL" title="Review" copy="A stable queue of questions you saved to revisit." action={<Button onClick={()=>onOpen(0,false)}>Review all 10 <ArrowRight size={16}/>
</Button>}/>
<div className="review-toolbar">
<div className="tabs compact">
<button className="active">Active · 10</button>
<button>Resolved · 4</button>
</div>
<button className="filter">Reasons <ChevronDown/>
</button>
</div>
<p className="match-count">10 matching questions</p>
<div className="review-list">{items.map((x,i)=>
<button key={x} onClick={()=>onOpen(i,i===3)}>
<span className="review-number">{i+1}</span>
<span>
<strong>{x}</strong>
<small>{i%2?'Yearly · Paper 22':'Study · Kinematics'} · Question {i+1}</small>
</span>
<Badge tone={i===3?'violet':i%3===0?'warm':'neutral'}>{i===3?'Previous answer':i%3===0?'Difficult':'Revisit'}</Badge>
<ChevronRight/>
</button>)}</div>
</div>; }
function Exercises({ onOpen, empty }: { onOpen:()=>void; empty:boolean }) { if(empty)return <div className="page narrow">
<SectionTitle eyebrow="PHYSICS · AS" title="Exercises"/>
<div className="empty-hero">
<div>
<ListChecks/>
</div>
<h2>No exercises published yet</h2>
<p>Your teacher's practice sets will appear here.</p>
</div>
</div>; return <div className="page narrow">
<SectionTitle eyebrow="PHYSICS · AS LEVEL" title="Exercises" copy="Published practice sets and due dates."/>
<div className="tabs compact">
<button className="active">Current · 3</button>
<button>Completed · 5</button>
</div>
<div className="exercise-list">{[['Waves checkpoint','12 questions','Due 18 Sep','In progress'],['Kinematics mixed practice','20 questions','Due 24 Sep','Not started'],['Forces consolidation','8 questions','Due 02 Oct','Not started']].map((e,i)=>
<button key={e[0]} onClick={onOpen}>
<span className="exercise-icon">
<ListChecks/>
</span>
<span>
<strong>{e[0]}</strong>
<small>{e[1]} · {e[2]}</small>
</span>
<Badge tone={i===0?'warm':'neutral'}>{e[3]}</Badge>
<ChevronRight/>
</button>)}</div>
</div>; }
function ExerciseDetail({ onBack, onPlayer, submitted }: { onBack:()=>void; onPlayer:()=>void; submitted:boolean }) { return <div className="page narrow">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to exercises</Button>
<div className="exercise-detail">
<div className="exercise-title">
<span>
<ListChecks/>
</span>
<div>
<p className="eyebrow">PHYSICS · AS LEVEL</p>
<h1>Waves checkpoint</h1>
<p>Set by your teacher · sample exercise</p>
</div>
<Badge tone={submitted?'teal':'warm'}>{submitted?'Submitted':'In progress'}</Badge>
</div>
<div className="exercise-facts">
<span>
<ListChecks/>
<strong>12</strong>
<small>questions</small>
</span>
<span>
<Timer/>
<strong>25 min</strong>
<small>attempt timer</small>
</span>
<span>
<CalendarDays/>
<strong>18 Sep</strong>
<small>due · 16:00</small>
</span>
</div>
<div className="instructions">
<h3>Before you start</h3>
<p>Answer every question. You can leave and continue before the due date. Mark schemes are available after submission.</p>
</div>
<Button onClick={onPlayer}>{submitted?'Review submission':'Continue exercise'}<ArrowRight size={17}/>
</Button>
</div>
</div>; }

function Analytics({ scope, onMetric, onTracker, onTopical }: { scope:{subject:Subject;level:Level}; onMetric:(title:string)=>void; onTracker:()=>void; onTopical:()=>void }) { const [tab,setTab]=useState<'overview'|'study'|'performance'>('overview'); const topics=scopeTopics(scope); const lessonCount=topics.reduce((n,t)=>n+t.modules.reduce((x,m)=>x+m.lessons.length,0),0); const completed=previewCompleted(lessonCount); return <div className="page">
<SectionTitle eyebrow={`${scope.subject.toUpperCase()} · ${scope.level} LEVEL`} title="Analytics" copy="Fixed fictional values show how activity, progress and scored work could look." action={<div className="period">Last 28 days <ChevronDown size={15}/>
</div>}/>
<div className="tabs analytics-tabs">
<button className={tab==='overview'?'active':''} onClick={()=>setTab('overview')}>Overview</button>
<button className={tab==='study'?'active':''} onClick={()=>setTab('study')}>Study</button>
<button className={tab==='performance'?'active':''} onClick={()=>setTab('performance')}>Performance</button>
</div>
{tab==='overview'&&<><DashboardCharts onMetric={onMetric} scopeLabel={`${scope.subject} · ${scope.level}`} lessonTotal={lessonCount}/>
<div className="insight-row">
<div>
<span>
<Lightbulb/>
</span>
<div>
<small>SAMPLE INSIGHT</small>
<strong>{topics[0]?.title ?? 'Your first topic'} is ready for another practice set</strong>
<p>3 of 8 recent scored preview questions were correct.</p>
</div>
<Button tone="secondary" onClick={onTopical}>Set up topical practice</Button>
</div>
</div></>}
{tab==='study'&&<div className="analytics-panel"><div className="analytics-summary"><article><small>AUTHORED TOPICS</small><strong>{topics.length || 12}</strong><span>in this title preview</span></article><article><small>LESSON TITLES</small><strong>{lessonCount || 74}</strong><span>available to browse</span></article><article><small>FICTIONAL COMPLETION</small><strong>46%</strong><span>{completed} lessons sampled</span></article><article><small>STUDY TIME</small><strong>8h 24m</strong><span>+1h 18m this period</span></article></div><DashboardCharts onMetric={onMetric} scopeLabel={`${scope.subject} · ${scope.level}`} lessonTotal={lessonCount}/><Button onClick={onTracker}>Open full progress tracker <ArrowRight size={16}/></Button></div>}
{tab==='performance'&&<div className="analytics-panel"><div className="analytics-summary"><article><small>LATEST SCORE</small><strong>76%</strong><span>41 of 54 marks</span></article><article><small>AVERAGE</small><strong>71%</strong><span>+8 points in 28 days</span></article><article><small>ATTEMPTED</small><strong>184</strong><span>preview questions</span></article><article><small>ACCURACY</small><strong>73%</strong><span>134 correct</span></article></div><DashboardCharts onMetric={onMetric} scopeLabel={`${scope.subject} · ${scope.level}`} lessonTotal={lessonCount}/><div className="attempt-table"><div><strong>Recent sample attempts</strong><small>Fixed fictional data</small></div>{[['Mixed topic practice','76%','41 / 54'],['Topical checkpoint','72%','18 / 25'],['Quick recall','84%','21 / 25']].map(r=><button key={r[0]} onClick={()=>onMetric('Scored performance')}><span><strong>{r[0]}</strong><small>9 Sep 2026 · Practice</small></span><b>{r[1]}</b><span>{r[2]}<ChevronRight size={15}/></span></button>)}</div></div>}
</div>; }
function Metric({ scope, onBack, onPlayer, global, onSubject, metricTitle }: { scope:{subject:Subject;level:Level}|null; onBack:()=>void; onPlayer:()=>void; global:boolean; onSubject:()=>void; metricTitle:string }) { const chartType=metricTitle.includes('consistency')?'heat':metricTitle.includes('activity')?'bars':metricTitle.includes('progress')?'progress':'line'; const performance=chartType==='line'; return <div className="page">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>{global?'Back to Dashboard':'Back to Analytics'}</Button>
<SectionTitle eyebrow={global?'ALL SUBJECTS · LAST 28 DAYS':`${scope?.subject.toUpperCase()} · ${scope?.level} · LAST 28 DAYS`} title={metricTitle} copy="Fixed sample detail · same 28-day period" action={global?<Button tone="secondary" onClick={onSubject}>View Physics · AS</Button>:undefined}/>
<div className="metric-layout">
<article className="metric-chart">
<div className="metric-stat">
<span>
<small>{performance?'LATEST':'PERIOD TOTAL'}</small>
<strong>{performance?'76%':chartType==='progress'?'46%':'18 days'}</strong>
</span>
<span>
<small>{performance?'CHANGE':'CURRENT STREAK'}</small>
<strong className="up">{performance?'+8%':'12 days'}</strong>
</span>
<span>
<small>{performance?'COVERAGE':'SCOPE'}</small>
<strong>{performance?'18 questions':global?'3 subjects':`${scope?.subject} · ${scope?.level}`}</strong>
</span>
</div>
<MiniChart type={chartType}/>
<div className="x-axis">
<span>19 Aug</span>
<span>26 Aug</span>
<span>2 Sep</span>
<span>9 Sep</span>
</div>
</article>
<aside className="metric-detail">
<Badge tone="violet">SELECTED POINT</Badge>
<h2>{performance?'Paper 22 practice':'9 September 2026'}</h2>
<strong className="big-score">{performance?'41 / 60':chartType==='progress'?'14 / 30':'42 min'}</strong>
<p>{performance?'68% · self-marked theory':'Fixed example detail for this metric'}</p>
<dl>
<div>
<dt>Date</dt>
<dd>9 Sep 2026</dd>
</div>
<div>
<dt>Support</dt>
<dd>2 hints used</dd>
</div>
<div>
<dt>Mode</dt>
<dd>Practice</dd>
</div>
</dl>
{performance&&<Button onClick={onPlayer}>Open sample attempt <ArrowRight size={16}/>
</Button>
}
</aside>
</div>
</div>; }
function Tracker({ scope, onBack, onLesson }: { scope:{subject:Subject;level:Level}; onBack:()=>void; onLesson:(topic:CurriculumTopic,lesson:CurriculumLesson)=>void }) { const topics=scopeTopics(scope); const [expanded,setExpanded]=useState(topics[0]?.id ?? ''); const total=topics.reduce((n,t)=>n+t.modules.reduce((x,m)=>x+m.lessons.length,0),0); return <div className="page narrow">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to Analytics</Button>
<SectionTitle eyebrow={`STUDY · ${scope.subject.toUpperCase()} ${scope.level}`} title="Progress tracker" copy={`${previewCompleted(total)} of ${total} lesson titles shown as complete · fictional preview values`} action={<div className="period">All topics <ChevronDown size={15}/>
</div>}/>
<Progress value={46}/>
<div className="tracker-list">{topics.map((topic,i)=>{const lessons=topic.modules.flatMap(m=>m.lessons); const progress=(31+i*13)%91; const done=Math.round(lessons.length*progress/100); const open=expanded===topic.id; return <div className={open?'expanded':''} key={topic.id}>
<button onClick={()=>setExpanded(open?'':topic.id)}>
<span>
<strong>{topic.title}</strong>
<small>{done} of {lessons.length} {lessons.length===1?'lesson':'lessons'}</small>
</span>
<span className="tracker-progress">
<Progress value={progress}/>{progress}%</span>
<ChevronDown/>
</button>{open&&<div className="tracker-lessons">{lessons.slice(0,4).map((lesson,j)=><div key={lesson.id}>
{j<2?<CheckCircle2/>:<span className="mini-index">{j+1}</span>}
<span><strong>{lesson.title}</strong><small>{j<2?'Notes complete · Questions 20/20':'Notes ready · Questions 7/20'}</small></span>
{j<2?<Badge tone="teal">Complete</Badge>:<Button tone="secondary" onClick={()=>onLesson(topic,lesson)}>Continue</Button>}
</div>)}</div>}</div>})}</div>
</div>; }
function SettingsPage({ onBack, onAdd, onSignout }: { onBack:()=>void; onAdd:()=>void; onSignout:()=>void }) { return <div className="page narrow">
<Button tone="quiet" onClick={onBack}>
<ArrowLeft size={17}/>Back to previous screen</Button>
<SectionTitle eyebrow="ACCOUNT & PREFERENCES" title="Settings" copy="Sample controls change only for this preview visit."/>
<div className="settings-layout">
<nav>
<button className="active">
<UserRound/>Account</button>
<button>
<GraduationCap/>Subjects</button>
<button>
<CalendarDays/>Exams & dates</button>
<button>
<Settings/>Preferences</button>
<button>
<CircleHelp/>Help</button>
</nav>
<div className="settings-card">
<h2>Account</h2>
<p>Manage the details shown in your learning space.</p>
<label>Name<input defaultValue="Abdullah Aftab"/>
</label>
<label>Phone number<div className="phone">
<select defaultValue="+44">
<option>+44</option>
<option>+92</option>
</select>
<input defaultValue="7700 900123"/>
</div>
</label>
<label>Google account<input disabled value="abdullah@example.com"/>
</label>
<div className="settings-actions">
<Button>Save changes</Button>
<Button tone="quiet" onClick={onSignout}>Sign out</Button>
</div>
<hr/>
<div className="subjects-setting">
<div>
<h3>Subjects</h3>
<p>Add or remove visible subject and level pairs.</p>
</div>
<Button tone="secondary" onClick={onAdd}>
<Plus size={16}/>Add subject</Button>
</div>
</div>
</div>
</div>; }

function AddSubject({ caller, enrolled, onClose, onAdd }: { caller:string; enrolled:Subject[]; onClose:()=>void; onAdd:(s:Subject,l:Level)=>void }) { const [step,setStep]=useState<1|2>(1); const [subject,setSubject]=useState<Subject>('Biology'); const [level,setLevel]=useState<Level|''>(''); return <div className="modal-wrap" role="dialog" aria-modal="true">
<div className="modal">
<div className="modal-head">
<div>
<small>ADD SUBJECT · STEP {step} OF 2</small>
<h2>{step===1?'Choose a subject':'Choose your level'}</h2>
</div>
<button onClick={onClose}>
<X/>
</button>
</div>{step===1?<div className="subject-options">{SUBJECTS.map(s=>{const Icon=subjectMeta[s].icon;return <button key={s} className={subject===s?'active':''} onClick={()=>setSubject(s)}>
<span style={{background:subjectMeta[s].tint,color:subjectMeta[s].color}}>
<Icon/>
</span>
<strong>{s}</strong>{enrolled.includes(s)&&<Badge tone="teal">Added</Badge>}{subject===s&&<Check/>}</button>})}</div>:<>
<button className="selected-subject" onClick={()=>setStep(1)}>
<span style={{background:subjectMeta[subject].tint,color:subjectMeta[subject].color}}>{subject.slice(0,1)}</span>
<span>
<small>SELECTED SUBJECT</small>
<strong>{subject}</strong>
</span>
<em>Change</em>
</button>
<div className="level-options">
<button className={level==='AS'?'active':''} onClick={()=>setLevel('AS')}>
<span>AS</span>
<div>
<strong>AS Level</strong>
<small>First half of the Cambridge course</small>
</div>{level==='AS'&&<Check/>}</button>
<button className={level==='A2'?'active':''} onClick={()=>setLevel('A2')}>
<span>A2</span>
<div>
<strong>A2 Level</strong>
<small>Second half of the Cambridge course</small>
</div>{level==='A2'&&<Check/>}</button>
</div>
</>}<div className="modal-foot">
<Button tone="quiet" onClick={step===2?()=>setStep(1):onClose}>{step===2?<>
<ArrowLeft size={16}/>Back</>:'Cancel'}</Button>
<span>Returns to {caller}</span>
<Button disabled={step===2&&!level} onClick={()=>step===1?setStep(2):onAdd(subject,level as Level)}>{step===1?'Choose level':`Add ${subject} · ${level}`}<ArrowRight size={16}/>
</Button>
</div>
</div>
</div>; }
function ScopeSwitcher({ enrolled, choices, onClose, onSelect, onAdd }: { enrolled:Subject[]; choices:Partial<Record<Subject,Level>>; onClose:()=>void; onSelect:(s:Subject,l:Level)=>void; onAdd:()=>void }) { return <div className="modal-wrap" role="dialog" aria-modal="true"><div className="modal"><div className="modal-head"><div><small>SUBJECT & LEVEL</small><h2>Switch learning space</h2></div><button aria-label="Close subject switcher" onClick={onClose}><X/></button></div><div className="subject-options">{enrolled.flatMap(s=>(s==='Physics'||s==='Biology'||s==='Chemistry'?(['AS','A2'] as Level[]):(['AS'] as Level[])).map(level=>{const Icon=subjectMeta[s].icon;return <button key={`${s}-${level}`} className={choices[s]===level?'active':''} onClick={()=>onSelect(s,level)}><span style={{background:subjectMeta[s].tint,color:subjectMeta[s].color}}><Icon/></span><strong>{s} · {level}</strong><ChevronRight/></button>}))}</div><div className="modal-foot"><Button tone="quiet" onClick={onClose}>Cancel</Button><span>Selecting opens that subject dashboard</span><Button tone="secondary" onClick={onAdd}><Plus size={16}/>Add subject</Button></div></div></div>; }
function CalendarModal({ onClose, onSettings }: { onClose:()=>void; onSettings:()=>void }) { return <div className="modal-wrap">
<div className="calendar-modal">
<div className="modal-head">
<div>
<small>SAMPLE DATE · 18 MAY 2027</small>
<h2>Physics AS Theory · Paper 2</h2>
</div>
<button onClick={onClose}>
<X/>
</button>
</div>
<div className="calendar-event">
<span>
<CalendarDays/>
</span>
<div>
<strong>09:00 · 1 hour 15 minutes</strong>
<p>Personal target date · not an official timetable connection</p>
</div>
</div>
<div className="modal-foot">
<Button tone="quiet" onClick={onClose}>Close</Button>
<Button tone="secondary" onClick={onSettings}>Edit date in Settings</Button>
</div>
</div>
</div>; }
function NodeModal({ onClose, onStart }: { onClose:()=>void; onStart:()=>void }) { return <div className="modal-wrap">
<div className="node-modal">
<button className="modal-x" onClick={onClose}>
<X/>
</button>
<div className="node-orbit">
<Atom/>
<i/>
<i/>
<i/>
</div>
<Badge tone="violet">CURRENT NODE · MEDIUM</Badge>
<h2>Acceleration</h2>
<p>Use graphs and quick choices to connect velocity change with acceleration.</p>
<div className="node-facts">
<span>
<Gamepad2/>
<strong>12</strong>
<small>quick questions</small>
</span>
<span>
<Clock3/>
<strong>8 min</strong>
<small>approximate</small>
</span>
</div>
<Button onClick={onStart}>Start game <Play size={16}/>
</Button>
<Button tone="quiet" onClick={onClose}>Back to path</Button>
</div>
</div>; }
function Countdown({ onCancel, onStart }: { onCancel:()=>void; onStart:()=>void }) { return <div className="player-overlay">
<div className="countdown">
<Badge tone="warm">EXAM CONDITIONS · SAMPLE</Badge>
<div className="countdown-ring">5</div>
<h1>Physics AS Theory · Paper 22</h1>
<p>Your timer begins when you enter the paper. Support stays hidden until the example result.</p>
<div>
<Button tone="quiet" onClick={onCancel}>Cancel</Button>
<Button onClick={onStart}>Start now</Button>
</div>
</div>
</div>; }
function Results({ mode, onBack, onReview }: { mode:PlayerMode; onBack:()=>void; onReview:()=>void }) { const game=mode==='game'; return <div className="player-overlay">
<div className="results-card">
<div className="result-icon">{game?<Trophy/>:<CheckCircle2/>}</div>
<Badge tone="teal">SAMPLE RESULT</Badge>
<h1>{game?'Node complete':'Session complete'}</h1>
<p>{game?'You covered 12 unique game questions.':'You attempted 17 of 20 questions in this example.'}</p>
<div className="result-stats">
<span>
<strong>{game?'10 / 12':'68%'}</strong>
<small>{game?'first try':'scored work'}</small>
</span>
<span>
<strong>{game?'2':'17 / 20'}</strong>
<small>{game?'retries':'attempted'}</small>
</span>
<span>
<strong>18:42</strong>
<small>sample time</small>
</span>
</div>
<Button onClick={game?onBack:onReview}>{game?'Continue path':'Review answers'}<ArrowRight size={16}/>
</Button>
<Button tone="quiet" onClick={onBack}>{game?'Back to node':'Back to source'}</Button>
</div>
</div>; }

function Player({ mode, origin, contextTitle, index, onIndex, onClose, onFinish }: { mode:PlayerMode; origin:PlayerOrigin; contextTitle:string; index:number; onIndex:(n:number)=>void; onClose:()=>void; onFinish:()=>void }) {
  const [support,setSupport]=useState<'scheme'|'hints'|'walkthrough'>('scheme'); const [answer,setAnswer]=useState(''); const [choice,setChoice]=useState(''); const [grid,setGrid]=useState(false); const [resolved,setResolved]=useState(false); const [mobileTab,setMobileTab]=useState<'question'|'support'>('question'); const total=origin==='review'?10:origin==='paper'||origin==='analytics'?7:origin==='game'?12:20; const pos=Math.min(index,total-1); const readonly=mode==='readonly'||(origin==='review'&&pos===3); const exam=mode==='exam'; const game=origin==='game'; const title=game?'Kinematics game · Acceleration':origin==='review'?'Saved Review queue':origin==='exercise'?'Exercise · Waves checkpoint':origin==='analytics'?'Example previous answers':`${contextTitle} · preview questions`;
  return <div className="player-overlay">
<div className="player">
<header className="player-head">
<button className="player-close" aria-label="Close question player" onClick={onClose}>
<X/>
<span>Close</span>
</button>
<div>
<small>{game?'GAMES':origin==='review'?'REVIEW':origin==='exercise'?'EXERCISE':origin==='analytics'?'ANALYTICS · SAMPLE ATTEMPT':'STUDY · PHYSICS AS'}</small>
<strong>{title}</strong>
</div>
<div className="player-meta">
<Badge tone={readonly?'violet':exam?'warm':'teal'}>{readonly?'READ ONLY':exam?'EXAM · 42:16':'SAMPLE SESSION'}</Badge>
<strong>{pos+1} of {total}</strong>{origin==='review'&&<button className={resolved?'resolved':''} onClick={()=>setResolved(!resolved)}>{resolved?<>
<RotateCcw/>Undo resolve</>:<>
<Check/>Resolve</>}</button>}</div>
</header>
<div className="mobile-player-tabs">
<button className={mobileTab==='question'?'active':''} onClick={()=>setMobileTab('question')}>Question</button>
<button className={mobileTab==='support'?'active':''} onClick={()=>setMobileTab('support')} disabled={exam}>Support</button>
</div>
<div className="player-body">
<main className={`question-panel ${mobileTab==='question'?'mobile-active':''}`}>
<div className="question-label">
<span>Question {pos+1}</span>
<Badge tone="neutral">4 marks</Badge>
</div>{game?<>
<p className="question-type">TAP TILES IN ORDER</p>
<h1>Arrange the steps for calculating acceleration from a velocity–time graph.</h1>
<div className="graph-mini">
<svg viewBox="0 0 360 150">
<path d="M30 10V128H340" stroke="#aaa" strokeWidth="2"/>
<path d="M32 124L285 25" stroke="#6958c9" strokeWidth="5" strokeLinecap="round"/>
<path d="M90 100H245V42" fill="#eeecff" stroke="#a698ee" strokeDasharray="5 5"/>
</svg>
</div>
<div className="tile-answer">{['Find Δv','Find Δt','Calculate Δv ÷ Δt','Add units'].map((x,i)=>
<button key={x} onClick={()=>setChoice(String(i))} className={choice===String(i)?'selected':''}>
<span>{i+1}</span>{x}</button>)}</div>
</>:pos%2===0?<>
<p className="question-type">MULTIPLE CHOICE</p>
<h1>A car increases its velocity uniformly from 8.0 m s⁻¹ to 20 m s⁻¹ in 6.0 s. What is its acceleration?</h1>
<div className="choices">{['0.50 m s⁻²','2.0 m s⁻²','4.7 m s⁻²','12 m s⁻²'].map((x,i)=>
<button key={x} disabled={readonly} onClick={()=>setChoice(String(i))} className={choice===String(i)||readonly&&i===1?'selected':''}>
<span>{'ABCD'[i]}</span>{x}{readonly&&i===1&&<Check/>}</button>)}</div>
</>:<>
<p className="question-type">STRUCTURED · PART (B)</p>
<h1>The graph shows how the velocity of an object varies with time.</h1>
<div className="theory-wrap">
<div className="graph-mini">
<svg viewBox="0 0 360 150">
<path d="M30 10V128H340" stroke="#aaa" strokeWidth="2"/>
<path d="M32 124L125 85L245 85L315 28" stroke="#2bb9b1" strokeWidth="5" fill="none" strokeLinecap="round"/>
</svg>
</div>
<p>
<strong>(b)</strong> Determine the acceleration between 12 s and 18 s. Show your working.</p>
<textarea value={readonly?'a = Δv / Δt = (18 − 10) / 6 = 1.33 m s⁻²':answer} onChange={e=>setAnswer(e.target.value)} disabled={readonly} placeholder="Write your answer and working…"/>
</div>
</>} </main>
<aside className={`support-panel ${mobileTab==='support'?'mobile-active':''}`}>{exam?<div className="exam-support">
<LockKeyhole/>
<h2>Support is hidden</h2>
<p>Mark schemes, hints and walkthroughs become available after this sample exam ends.</p>
</div>:<>
<div className="support-head">
<div>
<small>ANSWER SUPPORT</small>
<strong>{readonly?`Previous answer · ${pos%2===0?'MCQ':'part (b)'}`:'Question '+(pos+1)}</strong>
</div>
<button aria-label="Close support panel" onClick={()=>setMobileTab('question')}>
<X/>
</button>
</div>
<div className="support-tabs">
<button className={support==='scheme'?'active':''} onClick={()=>setSupport('scheme')}>Mark scheme</button>
<button className={support==='hints'?'active':''} onClick={()=>setSupport('hints')}>Hints</button>
<button className={support==='walkthrough'?'active':''} onClick={()=>setSupport('walkthrough')}>Walkthrough</button>
</div>
<div className="support-content">{support==='scheme'?<>
<Badge tone="teal">{pos%2===0?'ANSWER · 1 MARK':'PART (B) · 4 MARKS'}</Badge>
<h2>Example mark scheme</h2>
{pos%2===0?<div className="mark-point"><span>B</span><p>2.0 m s⁻²</p></div>:<>
<div className="mark-point">
<span>M1</span>
<p>Uses gradient of the velocity–time graph.</p>
</div>
<div className="mark-point">
<span>C1</span>
<p>Correctly identifies the change in velocity and time interval.</p>
</div>
<div className="mark-point">
<span>A1</span>
<p>Calculates acceleration with an appropriate unit.</p>
</div>
</>}
</>:support==='hints'?<>
<Badge tone="warm">2 HINTS</Badge>
<h2>Start with the graph</h2>
<div className="hint">
<Lightbulb/>
<p>Acceleration is the gradient. Read two clear points from the straight section.</p>
</div>
<button className="reveal">Reveal next hint</button>
</>:<>
<Badge tone="violet">3 STEPS</Badge>
<h2>Walkthrough</h2>
<ol className="walkthrough">
<li>
<span>1</span>
<p>
<strong>Read the values</strong>Find the initial and final velocity.</p>
</li>
<li>
<span>2</span>
<p>
<strong>Find the changes</strong>Subtract velocities and times.</p>
</li>
<li>
<span>3</span>
<p>
<strong>Calculate the gradient</strong>Divide Δv by Δt and add units.</p>
</li>
</ol>
</>}</div>
</>}</aside>
</div>
<footer className="player-foot">
<Button tone="quiet" disabled={pos===0} onClick={()=>onIndex(Math.max(0,pos-1))}>
<ArrowLeft size={17}/>Previous</Button>
<button className="grid-button" onClick={()=>setGrid(!grid)}>
<Grid2X2 size={17}/>
<span>Question grid</span>
</button>{readonly?<Button onClick={()=>pos+1<total?onIndex(pos+1):onClose()}>{pos+1<total?'Next':'Back to results'}<ArrowRight size={17}/>
</Button>:<div className="player-next">
<Button tone="quiet" onClick={()=>onIndex(Math.min(total-1,pos+1))}>Skip</Button>
<Button onClick={()=>pos+1===total?onFinish():onIndex(pos+1)}>{pos+1===total?'Finish':'Check & next'}<ArrowRight size={17}/>
</Button>
</div>}</footer>{grid&&<div className="question-grid-sheet">
<div>
<strong>Question grid</strong>
<button onClick={()=>setGrid(false)}>
<X/>
</button>
</div>
<section>{Array.from({length:total},(_,i)=>
<button className={i===pos?'current':i<pos?'done':''} key={i} onClick={()=>{onIndex(i);setGrid(false)}}>{i+1}</button>)}</section>
<p>
<span className="dot done"/>Submitted <span className="dot current"/>Current <span className="dot"/>Unseen</p>
</div>}</div>
</div>;
}

function SignIn({ onContinue }: { onContinue:()=>void }) { return <div className="onboarding">
<div className="onboard-brand">
<span>K</span>Kognitiv</div>
<div className="onboard-card">
<div className="onboard-art">
<span>
<BookOpen/>
</span>
<i/>
<i/>
<i/>
</div>
<Badge tone="violet">CAMBRIDGE LEARNING</Badge>
<h1>One place to learn, practise and make progress.</h1>
<p>Move from clear lessons to focused questions, then revisit what matters.</p>
<Button onClick={onContinue}>
<span className="google-g">G</span>Continue with Google</Button>
<small>Design preview · no Google connection is made</small>
</div>
</div>; }
function Profile({ onContinue }: { onContinue:()=>void }) { const [phone,setPhone]=useState(''); const [error,setError]=useState(false); return <div className="onboarding">
<div className="onboard-brand">
<span>K</span>Kognitiv</div>
<div className="profile-card">
<Badge tone="teal">ONE LAST STEP</Badge>
<h1>Complete your profile</h1>
<p>Check your name and add a phone number.</p>
<label>Name<input defaultValue="Abdullah Aftab"/>
</label>
<label>Phone number<div className={`phone ${error?'error':''}`}>
<select defaultValue="+44">
<option>+44</option>
<option>+92</option>
</select>
<input value={phone} onChange={e=>setPhone(e.target.value)} placeholder="7700 900123"/>
</div>{error&&<small className="field-error">Enter a phone number to continue</small>}</label>
<Button onClick={()=>phone.trim()?onContinue():setError(true)}>Continue <ArrowRight size={17}/>
</Button>
<small>Your details are sample-only and are not stored.</small>
</div>
</div>; }

export default function App() {
  const [scenario,setScenarioState]=useState<Scenario>('Populated Dashboard'); const [screen,setScreen]=useState<Screen>('global'); const [active,setActive]=useState<Section>('dashboard'); const [scope,setScope]=useState<{subject:Subject;level:Level}|null>(null); const [drawer,setDrawer]=useState(false); const [addOpen,setAddOpen]=useState(false); const [scopeOpen,setScopeOpen]=useState(false); const [calendar,setCalendar]=useState(false); const [node,setNode]=useState(false); const [countdown,setCountdown]=useState(false); const [player,setPlayer]=useState<PlayerMode|null>(null); const [playerIndex,setPlayerIndex]=useState(0); const [results,setResults]=useState(false); const [lessonTab,setLessonTab]=useState<'notes'|'questions'>('notes'); const [notesDone,setNotesDone]=useState(false); const [enrolled,setEnrolled]=useState<Subject[]>(['Physics','Mathematics','Chemistry']); const [levelChoices,setLevelChoices]=useState<Partial<Record<Subject,Level>>>({Physics:'AS',Mathematics:'AS',Chemistry:'AS'}); const [returnScreen,setReturnScreen]=useState<Screen>('global'); const empty=scenario==='Empty content';
  const [playerOrigin,setPlayerOrigin]=useState<PlayerOrigin>('study');
  const [metricTitle,setMetricTitle]=useState('Scored performance');
  const [metricReturnGlobal,setMetricReturnGlobal]=useState(false);
  const [readonlyFromResults,setReadonlyFromResults]=useState(false);
  const [lessonFromTracker,setLessonFromTracker]=useState(false);
  const [selectedTopic,setSelectedTopic]=useState<CurriculumTopic>(curriculum.Physics.AS[0]);
  const [selectedLesson,setSelectedLesson]=useState<CurriculumLesson>(curriculum.Physics.AS[0].modules[0].lessons[0]);
  const title:Record<Screen,string>={global:'Dashboard',subject:'Subject dashboard',modules:'Study',lessons:selectedTopic.title,lesson:selectedLesson.title,revision:'Revision',topical:'Topical',yearly:'Yearly papers',paper:'Paper 22',games:'Games',review:'Review',exercises:'Exercises',exercise:'Waves checkpoint',analytics:'Analytics',metric:'Detail',tracker:'Progress tracker',settings:'Settings',signin:'Sign in',profile:'Complete profile'};
  const selectFirstLesson=(nextScope:{subject:Subject;level:Level})=>{const topic=scopeTopics(nextScope)[0]; if(topic){setSelectedTopic(topic);setSelectedLesson(topic.modules[0].lessons[0])}};
  const goto=(s:Screen,section:Section=active)=>{setScreen(s);setActive(section);window.scrollTo(0,0)}; const openSubject=(subject:Subject,levelOverride?:Level)=>{const level=levelOverride??levelChoices[subject]??'AS';const nextScope={subject,level};setLevelChoices(p=>({...p,[subject]:level}));setScope(nextScope);selectFirstLesson(nextScope);goto('subject','dashboard')}; const openPlayer=(m:PlayerMode,i=0,origin:PlayerOrigin='study')=>{setPlayerIndex(i);setPlayerOrigin(origin);setPlayer(m);setResults(false);setReadonlyFromResults(false)};
  const dismissOverlays=()=>{setPlayer(null);setResults(false);setAddOpen(false);setScopeOpen(false);setCalendar(false);setNode(false);setCountdown(false)};
  const reset=()=>{dismissOverlays();setScenarioState('Populated Dashboard');setScreen('global');setActive('dashboard');setScope(null);setEnrolled(['Physics','Mathematics','Chemistry']);setNotesDone(false);setMetricReturnGlobal(false);setLessonFromTracker(false)};
  const setScenario=(s:Scenario)=>{dismissOverlays();setScenarioState(s);if(s==='New learner'){setScreen('signin');setScope(null);setActive('dashboard')}else if(s==='Review queue'){setScope({subject:'Physics',level:'AS'});selectFirstLesson({subject:'Physics',level:'AS'});setScreen('review');setActive('review')}else if(s==='Lesson in progress'||s==='Lesson complete'||s==='Error example'){setScope({subject:'Physics',level:'AS'});selectFirstLesson({subject:'Physics',level:'AS'});setScreen('lesson');setActive('study');setLessonTab('notes');setNotesDone(s==='Lesson complete')}else if(s==='Exam running'){setScope({subject:'Physics',level:'AS'});setScreen('paper');setActive('revision');openPlayer('exam',0,'paper')}else if(s==='Exam ended'){setScope({subject:'Physics',level:'AS'});setScreen('paper');setActive('revision');setPlayerOrigin('paper');setPlayer('exam');setResults(true)}else{setScreen('global');setScope(null);setActive('dashboard')}};
  const onNav=(s:Section)=>{if(s==='dashboard')goto(scope?'subject':'global','dashboard');else if(s==='study')goto('modules','study');else if(s==='revision')goto('revision','revision');else if(s==='review')goto('review','review');else if(s==='exercises')goto('exercises','exercises');else if(s==='analytics')goto('analytics','analytics')};
  
  const openMetric=(name:string)=>{setMetricTitle(name);setMetricReturnGlobal(false);goto('metric','analytics')};
  const content=()=>{switch(screen){case'global':return <GlobalDashboard enrolled={enrolled} choices={levelChoices} onOpen={openSubject} onAdd={()=>setAddOpen(true)} onRemove={subject=>setEnrolled(current=>current.filter(item=>item!==subject))} onMetric={openMetric} empty={empty||enrolled.length===0}/>;
case'subject':return <SubjectDashboard scope={scope!} onStudy={()=>{selectFirstLesson(scope!);setLessonTab('notes');goto('lesson','study')}} onMetric={openMetric} onCalendar={()=>setCalendar(true)}/>;
case'modules':return <Modules scope={scope!} onOpen={topic=>{setSelectedTopic(topic);setSelectedLesson(topic.modules[0].lessons[0]);goto('lessons','study')}}/>;
case'lessons':return <Lessons scope={scope!} topic={selectedTopic} onBack={()=>goto('modules','study')} onOpen={lesson=>{setSelectedLesson(lesson);goto('lesson','study')}}/>;
case'lesson':return <Lesson scope={scope!} topic={selectedTopic} lesson={selectedLesson} scenario={scenario} notesDone={notesDone} setNotesDone={setNotesDone} tab={lessonTab} setTab={setLessonTab} onBack={()=>{if(lessonFromTracker){setLessonFromTracker(false);goto('tracker','analytics')}else goto('lessons','study')}} onPlayer={()=>openPlayer(scenario==='Lesson complete'?'readonly':'practice',scenario==='Lesson in progress'?17:0,'study')}/>;
case'revision':return <RevisionHub open={s=>goto(s,'revision')}/>;
case'topical':return <Topical onBack={()=>goto('revision','revision')} onPlayer={()=>openPlayer('practice',0,'study')}/>;
case'yearly':return <Yearly onBack={()=>goto('revision','revision')} onPaper={()=>goto('paper','revision')}/>;
case'paper':return <Paper onBack={()=>goto('yearly','revision')} onPlayer={m=>openPlayer(m,0,'paper')} onExam={()=>setCountdown(true)}/>;
case'games':return <Games onBack={()=>goto('revision','revision')} onNode={()=>setNode(true)}/>;
case'review':return <ReviewList onOpen={(i,r)=>openPlayer(r?'readonly':'review',i,'review')}/>;
case'exercises':return <Exercises onOpen={()=>goto('exercise','exercises')} empty={empty}/>;
case'exercise':return <ExerciseDetail onBack={()=>goto('exercises','exercises')} onPlayer={()=>openPlayer(scenario==='Exam ended'?'readonly':'exercise',0,'exercise')} submitted={scenario==='Exam ended'}/>;
case'analytics':return <Analytics scope={scope!} onMetric={openMetric} onTracker={()=>goto('tracker','analytics')} onTopical={()=>goto('topical','revision')}/>;
case'metric':return <Metric scope={scope} metricTitle={metricTitle} global={!scope} onBack={()=>{if(metricReturnGlobal){setMetricReturnGlobal(false);setScope(null);goto('metric','analytics')}else goto(scope?'analytics':'global',scope?'analytics':'dashboard')}} onSubject={()=>{setMetricReturnGlobal(true);setScope({subject:'Physics',level:'AS'});goto('metric','analytics')}} onPlayer={()=>openPlayer('readonly',0,'analytics')}/>;
case'tracker':return <Tracker scope={scope!} onBack={()=>goto('analytics','analytics')} onLesson={(topic,lesson)=>{setSelectedTopic(topic);setSelectedLesson(lesson);setLessonFromTracker(true);goto('lesson','study')}}/>;
case'settings':return <SettingsPage onBack={()=>goto(returnScreen,active)} onAdd={()=>setAddOpen(true)} onSignout={()=>goto('signin','dashboard')}/>;
case'signin':return <SignIn onContinue={()=>goto('profile','dashboard')}/>;
case'profile':return <Profile onContinue={()=>{setEnrolled([]);goto('global','dashboard')}}/>}};
  if(screen==='signin'||screen==='profile')return <>
<PreviewBar scenario={scenario} setScenario={setScenario} reset={reset}/>{content()}</>;
  return <div className="app-shell">
<PreviewBar scenario={scenario} setScenario={setScenario} reset={reset}/>
<Sidebar scope={scope} active={active} open={drawer} onClose={()=>setDrawer(false)} onGlobal={()=>{setScope(null);goto('global','dashboard')}} onScope={()=>setScopeOpen(true)} onNav={onNav} onSettings={()=>{setReturnScreen(screen);goto('settings','settings')}}/>
<div className={`app-main ${screen === 'global' ? 'dashboard' : ''}`}>
<Topbar scope={scope} title={title[screen]} onMenu={()=>setDrawer(true)} compact={screen === 'global'}/>
<main className="content">{content()}</main>
</div>{addOpen&&<AddSubject caller={screen==='settings'?'Settings':scope?'Subject selector':'Dashboard'} enrolled={enrolled} onClose={()=>setAddOpen(false)} onAdd={(s,l)=>{setEnrolled(p=>p.includes(s)?p:[...p,s]);setLevelChoices(p=>({...p,[s]:l}));setAddOpen(false)}}/>}{scopeOpen&&<ScopeSwitcher enrolled={enrolled} choices={levelChoices} onClose={()=>setScopeOpen(false)} onSelect={(s,l)=>{setScopeOpen(false);openSubject(s,l)}} onAdd={()=>{setScopeOpen(false);setAddOpen(true)}}/>}{calendar&&<CalendarModal onClose={()=>setCalendar(false)} onSettings={()=>{setCalendar(false);setReturnScreen('subject');goto('settings','settings')}}/>}{node&&<NodeModal onClose={()=>setNode(false)} onStart={()=>{setNode(false);openPlayer('game',0,'game')}}/>}{countdown&&<Countdown onCancel={()=>setCountdown(false)} onStart={()=>{setCountdown(false);openPlayer('exam',0,'paper')}}/>}{player&&results?<Results mode={player} onBack={()=>{setResults(false);setPlayer(null);if(playerOrigin==='game')setNode(true)}} onReview={()=>{setResults(false);setReadonlyFromResults(true);setPlayer('readonly');setPlayerIndex(0)}}/>:player&&<Player mode={player} origin={playerOrigin} contextTitle={selectedLesson.title} index={playerIndex} onIndex={setPlayerIndex} onClose={()=>{if(readonlyFromResults){setResults(true);setReadonlyFromResults(false)}else{setPlayer(null);if(playerOrigin==='game')setNode(true)}}} onFinish={()=>setResults(true)}/>}</div>;
}
