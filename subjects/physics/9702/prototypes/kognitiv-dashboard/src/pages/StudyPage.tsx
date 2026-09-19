import React, { useState } from 'react';
import { Play, CheckCircle2, ChevronRight, Clock, Sparkles } from 'lucide-react';

interface StudyUnit {
  id: string;
  component: string;
  title: string;
  subtitle: string;
  lessonsCompleted: number;
  totalLessons: number;
  activeLessonTitle: string;
  estimatedMinutes: number;
}

const studyUnits: StudyUnit[] = [
  {
    id: 'p1',
    component: 'P1',
    title: 'Pure Mathematics 1',
    subtitle: 'Quadratics, Functions, Coordinate Geometry, Trigonometry, Vectors & Calculus',
    lessonsCompleted: 28,
    totalLessons: 36,
    activeLessonTitle: 'Lesson 3: Integration by Substitution & Definite Integrals',
    estimatedMinutes: 35,
  },
  {
    id: 's1',
    component: 'S1',
    title: 'Probability & Statistics 1',
    subtitle: 'Data Representation, Permutations & Combinations, Probability & Normal Distribution',
    lessonsCompleted: 16,
    totalLessons: 25,
    activeLessonTitle: 'Lesson 2: Standard Normal Distribution & Standardisation Formula',
    estimatedMinutes: 40,
  },
  {
    id: 'm1',
    component: 'M1',
    title: 'Mechanics',
    subtitle: 'Kinematics, Force & Motion, Friction, Work, Energy & Power, Momentum',
    lessonsCompleted: 18,
    totalLessons: 25,
    activeLessonTitle: 'Lesson 4: Work-Energy Principle & Conservation on Rough Inclines',
    estimatedMinutes: 30,
  },
  {
    id: 'p3',
    component: 'P3',
    title: 'Pure Mathematics 3',
    subtitle: 'Advanced Calculus, Differential Equations, Vectors in 3D & Complex Numbers',
    lessonsCompleted: 22,
    totalLessons: 38,
    activeLessonTitle: 'Lesson 5: Separation of Variables & Partial Fraction Integration',
    estimatedMinutes: 45,
  },
];

export const StudyPage: React.FC = () => {
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-[#111424] text-white px-5 py-3 rounded-xl shadow-xl flex items-center gap-3 border border-[#1a1f36] text-xs font-medium animate-in fade-in slide-in-from-bottom-2 duration-150">
          <Sparkles className="w-4 h-4 text-[#2f66f6]" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Page Header */}
      <div>
        <h1 className="text-2xl font-bold text-[#0f172a] tracking-tight">
          Study Portal
        </h1>
        <p className="text-sm text-slate-500 mt-1">
          Pick up your structured Cambridge Mathematics lessons, formula sheets, and concept notes.
        </p>
      </div>

      {/* Featured Active Lesson Card matching Kognitiv Blue */}
      <div className="p-6 bg-white rounded-2xl border border-slate-100 shadow-2xs">
        <div className="flex items-center gap-2 text-xs font-semibold text-[#2f66f6] uppercase tracking-wider mb-2">
          <span>Currently in progress</span>
        </div>

        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <span className="w-7 h-7 rounded-lg bg-[#eff6ff] text-[#2f66f6] font-bold text-xs flex items-center justify-center">
                P1
              </span>
              <h2 className="text-xl font-bold text-[#0f172a]">
                Pure Mathematics 1 · Calculus: Integration by Substitution
              </h2>
            </div>
            <p className="text-slate-500 text-xs mt-1 max-w-2xl leading-relaxed">
              Master the change of variable technique, boundary conversion for definite integrals, and algebraic substitutions in Cambridge 9709 past papers.
            </p>

            <div className="flex items-center gap-5 mt-4 text-xs font-medium text-slate-500">
              <span className="flex items-center gap-1.5">
                <Clock className="w-4 h-4 text-slate-400" />
                35 mins remaining
              </span>
              <span className="flex items-center gap-1.5">
                <CheckCircle2 className="w-4 h-4 text-[#2f66f6]" />
                28 of 36 objectives mastered
              </span>
            </div>
          </div>

          <button
            onClick={() => showToast('Launching lesson player for Pure Mathematics 1: Lesson 3...')}
            className="flex items-center gap-2 px-6 py-3 rounded-xl bg-[#2f66f6] hover:bg-[#2557df] text-white text-sm font-semibold transition-all shadow-xs shrink-0 self-start md:self-auto active:scale-[0.98]"
          >
            <Play className="w-4 h-4 fill-white" />
            <span>Continue Lesson 3</span>
          </button>
        </div>
      </div>

      {/* Cambridge 9709 Syllabus Units */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-bold text-[#0f172a]">
            Cambridge Mathematics (9709) Units
          </h3>
          <span className="text-xs text-slate-400 font-medium">
            October/November 2026 Series
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {studyUnits.map((unit) => {
            const progressPct = Math.round((unit.lessonsCompleted / unit.totalLessons) * 100);
            return (
              <div
                key={unit.id}
                className="p-5 bg-white rounded-2xl border border-slate-100 shadow-2xs hover:border-[#2f66f6]/40 transition-all flex flex-col justify-between group"
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center gap-2.5">
                      <span className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] font-bold text-xs flex items-center justify-center">
                        {unit.component}
                      </span>
                      <h4 className="font-bold text-sm text-[#0f172a] group-hover:text-[#2f66f6] transition-colors">
                        {unit.title}
                      </h4>
                    </div>
                    <span className="text-xs font-bold text-slate-900">
                      {progressPct}%
                    </span>
                  </div>

                  <p className="text-xs text-slate-500 mb-3 line-clamp-2">
                    {unit.subtitle}
                  </p>

                  <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden mb-3">
                    <div
                      className="h-full bg-[#2f66f6] rounded-full"
                      style={{ width: `${progressPct}%` }}
                    />
                  </div>

                  <div className="text-[11px] text-slate-600 bg-slate-50 p-2 rounded-lg border border-slate-100/80 mb-3 truncate">
                    <strong className="text-[#2f66f6]">Active:</strong> {unit.activeLessonTitle}
                  </div>
                </div>

                <div className="flex items-center justify-between pt-2 border-t border-slate-100 text-xs">
                  <span className="text-slate-400">
                    {unit.lessonsCompleted} of {unit.totalLessons} lessons
                  </span>
                  <button
                    onClick={() => showToast(`Opening ${unit.title} unit curriculum...`)}
                    className="font-semibold text-[#2f66f6] hover:text-[#2557df] flex items-center gap-1"
                  >
                    <span>View lessons</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
