import React from 'react';
import { ArrowRight, BookOpen } from 'lucide-react';

interface MathsResumeBannerProps {
  module?: string;
  topic?: string;
  lesson?: string;
  lastStudied?: string;
  onResume?: () => void;
}

export const MathsResumeBanner: React.FC<MathsResumeBannerProps> = ({
  module = 'Pure Mathematics 1',
  topic = 'Calculus: Integration by Substitution',
  lesson = 'Lesson 3',
  lastStudied = '3 hours ago',
  onResume,
}) => {
  return (
    <div className="mb-4 p-4 sm:p-5 bg-white rounded-2xl border border-slate-100 shadow-2xs flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:border-slate-200 transition-colors">
      <div className="flex items-center gap-4">
        {/* Themed Icon in Standard Brand Tint */}
        <div className="w-12 h-12 rounded-xl bg-[#eff6ff] border border-blue-100/60 text-[#2f66f6] flex items-center justify-center shrink-0">
          <BookOpen className="w-5 h-5 stroke-[1.8]" />
        </div>

        {/* Content Hierarchy matching standard Kognitiv dashboard */}
        <div>
          <span className="text-xs text-[#64748b] font-medium block">
            Continue where you left off
          </span>
          <div className="text-base font-bold text-[#0f172a] mt-0.5 flex items-center gap-2 flex-wrap">
            <span>Maths</span>
            <span className="text-slate-300">•</span>
            <span>{module}</span>
            <span className="text-slate-300">•</span>
            <span>{topic}</span>
          </div>
          <div className="flex items-center gap-3 text-xs text-[#94a3b8] mt-1">
            <span>Last studied {lastStudied}</span>
            <span className="text-slate-200">•</span>
            <span className="text-[#2f66f6] font-semibold">{lesson}</span>
            <span className="text-slate-200">•</span>
            <span>35 mins remaining</span>
          </div>
        </div>
      </div>

      {/* Standard Royal Blue Resume Button */}
      <button
        onClick={onResume}
        className="flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl bg-[#2f66f6] hover:bg-[#2557df] text-white text-sm font-medium transition-all shadow-sm active:scale-[0.98] group shrink-0 self-start sm:self-auto"
      >
        <span>Resume study</span>
        <ArrowRight className="w-4 h-4 text-white/90 group-hover:text-white transition-transform group-hover:translate-x-0.5" />
      </button>
    </div>
  );
};
