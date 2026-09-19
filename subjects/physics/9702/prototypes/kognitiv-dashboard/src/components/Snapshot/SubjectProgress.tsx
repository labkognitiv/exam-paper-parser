import React from 'react';
import { PieChart } from 'lucide-react';

interface SubjectProgressItem {
  name: string;
  code: string;
  progress: number; // 0 - 100
}

const progressList: SubjectProgressItem[] = [
  { name: 'Mathematics', code: '9709', progress: 68 },
  { name: 'Physics', code: '9702', progress: 42 },
  { name: 'Chemistry', code: '9701', progress: 55 },
];

export const SubjectProgress: React.FC = () => {
  return (
    <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-sm flex flex-col justify-between hover:border-slate-200 transition-colors">
      {/* Card Header */}
      <div className="flex items-center gap-3 mb-6">
        <div className="w-11 h-11 rounded-xl bg-[#eff6ff] flex items-center justify-center text-[#2f66f6] border border-blue-100/60">
          <PieChart className="w-5 h-5 stroke-[1.85]" />
        </div>
        <div>
          <h3 className="font-bold text-[#0f172a] text-base leading-snug">
            Subject Progress
          </h3>
          <p className="text-xs text-[#64748b] font-medium leading-snug mt-0.5">
            Syllabus coverage across all active subjects
          </p>
        </div>
      </div>

      {/* Progress Bars List in Kognitiv Royal Blue */}
      <div className="space-y-5 pb-2">
        {progressList.map((item) => (
          <div key={item.name} className="flex items-center gap-4">
            {/* Subject Label */}
            <div className="w-28 shrink-0">
              <span className="text-sm font-medium text-[#334155] block leading-tight">
                {item.name}
              </span>
              <span className="text-[10px] text-slate-400 font-medium">
                {item.code}
              </span>
            </div>

            {/* Track & Royal Blue Fill */}
            <div className="flex-1 h-3 bg-[#f1f5f9] rounded-full overflow-hidden">
              <div
                style={{ width: `${item.progress}%` }}
                className="h-full bg-[#2f66f6] rounded-full transition-all duration-700 ease-out"
              />
            </div>

            {/* Percent Text */}
            <span className="w-12 text-right text-xs font-bold text-[#0f172a] shrink-0">
              {item.progress}%
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
