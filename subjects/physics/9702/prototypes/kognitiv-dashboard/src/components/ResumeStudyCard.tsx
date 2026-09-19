import React from 'react';
import { BookOpen, ArrowRight } from 'lucide-react';

interface ResumeStudyProps {
  subject?: string;
  topic?: string;
  lesson?: string;
  lastStudied?: string;
  onResume?: () => void;
}

export const ResumeStudyCard: React.FC<ResumeStudyProps> = ({
  subject = 'Mathematics',
  topic = 'Pure Mathematics 1 · Integration by Substitution',
  lesson = 'Lesson 3',
  lastStudied = '3 hours ago',
  onResume,
}) => {
  return (
    <div className="mb-8 p-5 bg-white rounded-2xl border border-slate-100 shadow-2xs flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:border-slate-200 transition-colors">
      <div className="flex items-center gap-4">
        {/* Book Icon Container in Standard Kognitiv Blue */}
        <div className="w-12 h-12 rounded-xl bg-[#eff6ff] flex items-center justify-center text-[#2f66f6] shrink-0 border border-blue-100/60">
          <BookOpen className="w-6 h-6 stroke-[1.85]" />
        </div>

        {/* Text details */}
        <div>
          <span className="text-xs text-[#64748b] font-medium block mb-0.5">
            Continue where you left off
          </span>
          <div className="text-base font-bold text-[#0f172a] flex items-center gap-1.5 flex-wrap">
            <span>{subject}</span>
            <span className="text-slate-300 font-bold">•</span>
            <span>{topic}</span>
            <span className="text-slate-300 font-bold">•</span>
            <span className="text-[#2f66f6]">{lesson}</span>
          </div>
          <span className="text-xs text-[#94a3b8] font-normal block mt-0.5">
            Last studied {lastStudied}
          </span>
        </div>
      </div>

      {/* Resume Button in Solid Kognitiv Royal Blue */}
      <button
        onClick={onResume}
        className="flex items-center justify-center gap-2 px-6 py-2.5 rounded-xl bg-[#2f66f6] text-white text-[14px] font-medium hover:bg-[#2557df] active:scale-[0.98] transition-all duration-150 shadow-sm self-stretch sm:self-auto shrink-0 group"
      >
        <span>Resume study</span>
        <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-0.5" />
      </button>
    </div>
  );
};
