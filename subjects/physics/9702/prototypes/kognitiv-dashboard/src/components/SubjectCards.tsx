import React from 'react';
import { Plus, Calculator, Atom, FlaskConical, ChevronRight } from 'lucide-react';

interface SubjectItem {
  id: string;
  name: string;
  code: string;
  subtitle: string;
  icon: React.ElementType;
}

const subjects: SubjectItem[] = [
  {
    id: 'maths',
    name: 'Mathematics',
    code: '9709',
    subtitle: 'Continue learning',
    icon: Calculator,
  },
  {
    id: 'physics',
    name: 'Physics',
    code: '9702',
    subtitle: 'Continue learning',
    icon: Atom,
  },
  {
    id: 'chemistry',
    name: 'Chemistry',
    code: '9701',
    subtitle: 'Continue learning',
    icon: FlaskConical,
  },
];

interface SubjectCardsProps {
  onSelectSubject?: (subjectId: string) => void;
  onAddSubject?: () => void;
}

export const SubjectCards: React.FC<SubjectCardsProps> = ({
  onSelectSubject,
  onAddSubject,
}) => {
  return (
    <div className="mb-6">
      {/* Section Header */}
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold text-[#0f172a] tracking-tight">
          Your subjects
        </h2>
        <button
          onClick={onAddSubject}
          className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-[#2f66f6] text-white text-[13px] font-medium hover:bg-[#2557df] active:scale-[0.98] transition-all duration-150 shadow-sm"
        >
          <Plus className="w-4 h-4" />
          <span>Add Subject</span>
        </button>
      </div>

      {/* Cards Grid using standard Kognitiv brand colors */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        {subjects.map((s) => {
          const Icon = s.icon;
          return (
            <div
              key={s.id}
              onClick={() => onSelectSubject?.(s.id)}
              className="p-5 rounded-2xl border border-slate-100 bg-white hover:border-[#2f66f6]/40 flex items-center justify-between cursor-pointer transition-all duration-200 hover:shadow-md hover:translate-y-[-1px] group"
            >
              <div className="flex items-center gap-4">
                {/* Standard Royal Blue Icon Container */}
                <div className="w-12 h-12 rounded-xl bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center shadow-xs border border-blue-100/60 transition-transform group-hover:scale-105">
                  <Icon className="w-6 h-6 stroke-[1.85]" />
                </div>
                {/* Labels */}
                <div>
                  <div className="flex items-center gap-1.5">
                    <h3 className="font-bold text-[#0f172a] text-base leading-snug group-hover:text-[#2f66f6] transition-colors">
                      {s.name}
                    </h3>
                    <span className="text-[11px] font-semibold text-slate-400">
                      ({s.code})
                    </span>
                  </div>
                  <p className="text-xs text-[#64748b] font-medium mt-0.5">
                    {s.subtitle}
                  </p>
                </div>
              </div>

              {/* Arrow Indicator in Royal Blue tone */}
              <div className="w-8 h-8 rounded-full bg-slate-50 group-hover:bg-[#eff6ff] flex items-center justify-center transition-colors">
                <ChevronRight className="w-4 h-4 text-slate-400 group-hover:text-[#2f66f6] group-hover:translate-x-0.5 transition-all" />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
