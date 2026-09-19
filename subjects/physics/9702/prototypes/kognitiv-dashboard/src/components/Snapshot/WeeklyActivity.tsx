import React, { useState } from 'react';
import { BarChart2 } from 'lucide-react';

interface DayData {
  day: string;
  questions: number;
}

const weeklyData: DayData[] = [
  { day: 'Mon', questions: 30 },
  { day: 'Tue', questions: 45 },
  { day: 'Wed', questions: 18 },
  { day: 'Thu', questions: 32 },
  { day: 'Fri', questions: 58 },
  { day: 'Sat', questions: 45 },
  { day: 'Sun', questions: 32 },
];

const MAX_VALUE = 60;

export const WeeklyActivity: React.FC = () => {
  const [hoveredIdx, setHoveredIdx] = useState<number | null>(null);

  return (
    <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-sm flex flex-col justify-between hover:border-slate-200 transition-colors">
      {/* Card Header */}
      <div className="flex items-center gap-3 mb-6">
        <div className="w-11 h-11 rounded-xl bg-[#eff6ff] flex items-center justify-center text-[#2f66f6] border border-blue-100/60">
          <BarChart2 className="w-5 h-5 stroke-[1.85]" />
        </div>
        <div>
          <h3 className="font-bold text-[#0f172a] text-base leading-snug">
            Weekly Activity
          </h3>
          <p className="text-xs text-[#64748b] font-medium leading-snug mt-0.5">
            Questions attempted this week
          </p>
        </div>
      </div>

      {/* Chart Canvas Area */}
      <div className="relative pt-2 pb-1">
        <div className="flex">
          {/* Y-Axis scale labels */}
          <div className="flex flex-col justify-between text-[11px] font-medium text-[#94a3b8] pr-3 h-40 select-none pb-5">
            <span>60</span>
            <span>30</span>
            <span>0</span>
          </div>

          {/* Chart Plot Area */}
          <div className="relative flex-1 h-40 pb-5">
            {/* Horizontal Grid lines */}
            <div className="absolute inset-0 flex flex-col justify-between pointer-events-none pb-5">
              <div className="border-b border-slate-100 w-full" />
              <div className="border-b border-slate-100 w-full" />
              <div className="border-b border-slate-200 w-full" />
            </div>

            {/* Bars container in uniform Kognitiv Royal Blue */}
            <div className="relative h-full flex items-end justify-between px-2 sm:px-4">
              {weeklyData.map((item, idx) => {
                const heightPercent = (item.questions / MAX_VALUE) * 100;
                const isHovered = hoveredIdx === idx;
                return (
                  <div
                    key={item.day}
                    className="flex flex-col items-center flex-1 max-w-[42px] h-full justify-end group cursor-pointer"
                    onMouseEnter={() => setHoveredIdx(idx)}
                    onMouseLeave={() => setHoveredIdx(null)}
                  >
                    {/* Tooltip */}
                    {isHovered && (
                      <div className="absolute -top-7 px-2 py-1 rounded bg-[#111424] text-white text-[11px] font-semibold whitespace-nowrap shadow-md pointer-events-none z-10 animate-fade-in">
                        {item.questions} questions
                      </div>
                    )}

                    {/* Bar */}
                    <div
                      style={{ height: `${heightPercent}%` }}
                      className={`w-full max-w-[34px] bg-[#2f66f6] rounded-t-[5px] transition-all duration-200 ${
                        isHovered ? 'brightness-110 shadow-sm' : 'hover:brightness-105'
                      }`}
                    />
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* X-Axis Day Labels */}
        <div className="flex justify-between pl-8 pr-2 sm:px-6 mt-2 text-xs font-medium text-[#64748b]">
          {weeklyData.map((item) => (
            <span key={item.day} className="flex-1 text-center max-w-[42px]">
              {item.day}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};
