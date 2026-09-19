import React, { useState } from 'react';
import { Target, ArrowUpRight } from 'lucide-react';

interface TopicItem {
  id: string;
  name: string;
  subtitle: string;
  progress: number;
  completed: number;
  total: number;
  weight: string;
}

const topics: TopicItem[] = [
  {
    id: 'pure1',
    name: 'Pure Mathematics 1',
    subtitle: 'Quadratics, Functions & Calculus',
    progress: 78,
    completed: 28,
    total: 36,
    weight: '30% of total grade',
  },
  {
    id: 'pure3',
    name: 'Pure Mathematics 3',
    subtitle: 'Complex Numbers, Vectors & Diff Eq',
    progress: 58,
    completed: 22,
    total: 38,
    weight: '30% of total grade',
  },
  {
    id: 'mechanics',
    name: 'Mechanics',
    subtitle: 'Newtonian Laws, Equilibrium & Energy',
    progress: 72,
    completed: 18,
    total: 25,
    weight: '20% of total grade',
  },
  {
    id: 'stats',
    name: 'Probability & Statistics',
    subtitle: 'Distributions & Data Modeling',
    progress: 64,
    completed: 16,
    total: 25,
    weight: '20% of total grade',
  },
];

export const TopicMasterySnapshot: React.FC = () => {
  const [hoveredTopic, setHoveredTopic] = useState<string | null>(null);

  return (
    <div className="bg-white rounded-2xl p-5 border border-slate-100 shadow-2xs flex flex-col justify-between hover:border-slate-200 transition-colors">
      <div>
        {/* Header */}
        <div className="flex items-center justify-between mb-3.5">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <Target className="w-4 h-4 stroke-[2]" />
            </div>
            <div>
              <h3 className="font-bold text-[#0f172a] text-sm leading-tight">
                Topic Mastery
              </h3>
              <p className="text-[11px] text-slate-400 font-normal">
                Syllabus progress across all four areas
              </p>
            </div>
          </div>

          <span className="text-xs font-bold text-[#2f66f6] bg-[#eff6ff] px-2.5 py-0.5 rounded-full border border-blue-100/60">
            68% Complete
          </span>
        </div>

        {/* Topic rows with unified Kognitiv Royal Blue bars */}
        <div className="space-y-3">
          {topics.map((t) => {
            const isHovered = hoveredTopic === t.id;
            return (
              <div
                key={t.id}
                onMouseEnter={() => setHoveredTopic(t.id)}
                onMouseLeave={() => setHoveredTopic(null)}
                className="group cursor-pointer p-1.5 -mx-1.5 rounded-lg hover:bg-slate-50 transition-colors relative"
              >
                <div className="flex items-center justify-between text-xs mb-1">
                  <div>
                    <span className="font-semibold text-slate-800 text-xs block">
                      {t.name}
                    </span>
                    <span className="text-[10px] text-slate-400 font-normal">
                      {t.subtitle}
                    </span>
                  </div>

                  <div className="flex items-center gap-2">
                    <span
                      className={`text-[11px] text-slate-400 font-medium transition-opacity duration-150 ${
                        isHovered ? 'opacity-100' : 'opacity-0'
                      }`}
                    >
                      {t.completed} of {t.total} lessons
                    </span>
                    <span className="font-bold text-slate-800 text-xs w-9 text-right">
                      {t.progress}%
                    </span>
                  </div>
                </div>

                {/* Unified Royal Blue Progress Bar */}
                <div className="h-2 bg-slate-100 rounded-full overflow-hidden">
                  <div
                    style={{ width: `${t.progress}%` }}
                    className={`h-full bg-[#2f66f6] rounded-full transition-all duration-300 ${
                      isHovered ? 'brightness-110 shadow-xs' : ''
                    }`}
                  />
                </div>

                {/* Hover Reveal Floating Badge */}
                {isHovered && (
                  <div className="absolute right-0 top-[-24px] z-20 flex items-center gap-2 px-2.5 py-1 rounded-md bg-[#111424] text-white text-[10px] font-medium shadow-lg animate-in fade-in duration-150 pointer-events-none">
                    <span>{t.weight}</span>
                    <span className="text-blue-300">•</span>
                    <span>Ready for practice</span>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <div className="flex items-center justify-between mt-3 pt-2.5 border-t border-slate-100 text-[11px] text-slate-400">
        <span>84 of 124 syllabus objectives checked</span>
        <button className="font-semibold text-[#2f66f6] hover:text-[#2557df] flex items-center gap-0.5">
          <span>Drill topics</span>
          <ArrowUpRight className="w-3 h-3" />
        </button>
      </div>
    </div>
  );
};
