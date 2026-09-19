import React, { useState } from 'react';
import { Gauge, ArrowUpRight, CheckCircle2 } from 'lucide-react';

export const VelocityPacingSnapshot: React.FC = () => {
  const [hoveredMeter, setHoveredMeter] = useState<string | null>(null);

  return (
    <div className="bg-white rounded-2xl p-5 border border-slate-100 shadow-2xs flex flex-col justify-between hover:border-slate-200 transition-colors">
      <div>
        {/* Header */}
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <Gauge className="w-4 h-4 stroke-[2]" />
            </div>
            <div>
              <h3 className="font-bold text-[#0f172a] text-sm leading-tight">
                Exam Readiness & Pacing
              </h3>
              <p className="text-[11px] text-slate-400 font-normal">
                Preparation score & time management index
              </p>
            </div>
          </div>

          <span className="text-xs font-bold text-[#2f66f6] bg-[#eff6ff] px-2.5 py-0.5 rounded-full border border-blue-100/60">
            A* Pacing
          </span>
        </div>

        {/* Readiness Ring & Key Stat Showcase */}
        <div className="p-3 rounded-xl bg-slate-50/80 border border-slate-100 mb-3.5 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            {/* SVG Mini Radial Progress Ring (88%) in Royal Blue */}
            <div className="relative w-12 h-12 shrink-0 flex items-center justify-center">
              <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <path
                  className="text-slate-200"
                  strokeWidth="3.5"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  className="text-[#2f66f6]"
                  strokeDasharray="88, 100"
                  strokeWidth="3.5"
                  strokeLinecap="round"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
              </svg>
              <span className="absolute text-xs font-extrabold text-slate-900">
                88%
              </span>
            </div>

            <div>
              <span className="text-xs font-bold text-slate-900 block leading-tight">
                Exam Readiness Index
              </span>
              <p className="text-[11px] text-slate-500 mt-0.5">
                Pacing <strong className="text-[#2f66f6] font-semibold">18 minutes ahead</strong> of the 1h 50m limit.
              </p>
            </div>
          </div>

          <div className="text-right shrink-0 border-l border-slate-200/80 pl-3">
            <span className="text-[10px] text-slate-400 block font-medium">Time Buffer</span>
            <span className="text-sm font-bold text-[#2f66f6]">+18 mins</span>
          </div>
        </div>

        {/* 3 Balanced Metric Breakdown Meters in Royal Blue */}
        <div className="space-y-2.5">
          {/* Meter 1: Syllabus Coverage */}
          <div
            onMouseEnter={() => setHoveredMeter('coverage')}
            onMouseLeave={() => setHoveredMeter(null)}
            className="cursor-pointer"
          >
            <div className="flex items-center justify-between text-xs mb-1">
              <span className="font-medium text-slate-700 text-xs">
                Syllabus Mastery
              </span>
              <span className="text-[11px] font-bold text-slate-800">
                78%
              </span>
            </div>
            <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
              <div className="h-full bg-[#2f66f6] rounded-full" style={{ width: '78%' }} />
            </div>
          </div>

          {/* Meter 2: Question Accuracy */}
          <div
            onMouseEnter={() => setHoveredMeter('accuracy')}
            onMouseLeave={() => setHoveredMeter(null)}
            className="cursor-pointer"
          >
            <div className="flex items-center justify-between text-xs mb-1">
              <span className="font-medium text-slate-700 text-xs">
                Historical Accuracy
              </span>
              <span className="text-[11px] font-bold text-slate-800">
                84%
              </span>
            </div>
            <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
              <div className="h-full bg-[#2f66f6] rounded-full" style={{ width: '84%' }} />
            </div>
          </div>

          {/* Meter 3: Speed Efficiency */}
          <div
            onMouseEnter={() => setHoveredMeter('speed')}
            onMouseLeave={() => setHoveredMeter(null)}
            className="cursor-pointer"
          >
            <div className="flex items-center justify-between text-xs mb-1">
              <span className="font-medium text-slate-700 text-xs">
                Solving Speed Efficiency
              </span>
              <span className="text-[11px] font-bold text-slate-800">
                91% (1.08 mins/mark)
              </span>
            </div>
            <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
              <div className="h-full bg-[#2f66f6] rounded-full" style={{ width: '91%' }} />
            </div>
          </div>
        </div>

        {/* Hover Micro-Disclosure */}
        {hoveredMeter && (
          <div className="mt-2 text-[11px] text-[#2f66f6] font-medium bg-[#eff6ff] px-2.5 py-1 rounded-lg border border-blue-100/60 animate-in fade-in duration-150">
            {hoveredMeter === 'coverage' && '84 of 124 syllabus objectives checked across Pure Maths, Mechanics & Stats.'}
            {hoveredMeter === 'accuracy' && '82% fully correct marks, 11% arithmetic slips, 7% method gaps.'}
            {hoveredMeter === 'speed' && 'Current speed: 1.08 min/mark. Recommended exam target: 1.20 min/mark.'}
          </div>
        )}
      </div>

      <div className="flex items-center justify-between mt-3 pt-2.5 border-t border-slate-100 text-[11px] text-slate-400">
        <span className="flex items-center gap-1 text-slate-500">
          <CheckCircle2 className="w-3.5 h-3.5 text-[#2f66f6]" />
          18 min buffer for checking answers
        </span>
        <button className="font-semibold text-[#2f66f6] hover:text-[#2557df] flex items-center gap-0.5">
          <span>Readiness report</span>
          <ArrowUpRight className="w-3 h-3" />
        </button>
      </div>
    </div>
  );
};
