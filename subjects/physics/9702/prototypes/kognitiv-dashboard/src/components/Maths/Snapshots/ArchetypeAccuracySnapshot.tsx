import React, { useState } from 'react';
import { Layers, ArrowUpRight } from 'lucide-react';

interface Archetype {
  id: string;
  name: string;
  accuracy: number;
  attempts: number;
  badge: string;
}

const archetypes: Archetype[] = [
  {
    id: 'algebra',
    name: 'Algebraic Proof & Series',
    accuracy: 92,
    attempts: 142,
    badge: 'Mastered',
  },
  {
    id: 'calculus',
    name: 'Calculus & Rates of Change',
    accuracy: 84,
    attempts: 168,
    badge: 'Strong',
  },
  {
    id: 'geometry',
    name: 'Vector Geometry & 3D Lines',
    accuracy: 72,
    attempts: 94,
    badge: 'Needs Review',
  },
  {
    id: 'trig',
    name: 'Trigonometric Identities',
    accuracy: 65,
    attempts: 110,
    badge: 'Priority Focus',
  },
];

export const ArchetypeAccuracySnapshot: React.FC = () => {
  const [hoveredId, setHoveredId] = useState<string | null>(null);

  return (
    <div className="bg-white rounded-2xl p-5 border border-slate-100 shadow-2xs flex flex-col justify-between hover:border-slate-200 transition-colors">
      <div>
        {/* Header */}
        <div className="flex items-center justify-between mb-3.5">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <Layers className="w-4 h-4 stroke-[2]" />
            </div>
            <div>
              <h3 className="font-bold text-[#0f172a] text-sm leading-tight">
                Question Archetype Accuracy
              </h3>
              <p className="text-[11px] text-slate-400 font-normal">
                Accuracy across problem-solving styles
              </p>
            </div>
          </div>

          <span className="text-xs font-semibold text-slate-500 bg-slate-50 px-2.5 py-0.5 rounded-full border border-slate-100">
            514 questions completed
          </span>
        </div>

        {/* Minimal Royal Blue Bars with Hover Disclosure */}
        <div className="space-y-3">
          {archetypes.map((arch) => {
            const isHovered = hoveredId === arch.id;
            return (
              <div
                key={arch.id}
                onMouseEnter={() => setHoveredId(arch.id)}
                onMouseLeave={() => setHoveredId(null)}
                className="group cursor-pointer p-1.5 -mx-1.5 rounded-lg hover:bg-slate-50 transition-colors relative"
              >
                <div className="flex items-center justify-between text-xs mb-1">
                  <span className="font-medium text-slate-700 text-xs">
                    {arch.name}
                  </span>

                  <div className="flex items-center gap-2">
                    <span
                      className={`text-[10px] font-semibold px-2 py-0.5 rounded-md bg-slate-100 text-slate-600 transition-opacity duration-150 ${
                        isHovered ? 'opacity-100' : 'opacity-0'
                      }`}
                    >
                      {arch.badge} ({arch.attempts} Qs)
                    </span>

                    <span className="font-bold text-slate-800 text-xs w-9 text-right">
                      {arch.accuracy}%
                    </span>
                  </div>
                </div>

                {/* Royal Blue Bar */}
                <div className="h-2 bg-slate-100 rounded-full overflow-hidden">
                  <div
                    style={{ width: `${arch.accuracy}%` }}
                    className={`h-full bg-[#2f66f6] rounded-full transition-all duration-300 ${
                      isHovered ? 'brightness-110 shadow-xs' : ''
                    }`}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="flex items-center justify-between mt-3 pt-2.5 border-t border-slate-100 text-[11px] text-slate-400">
        <span className="text-slate-600 font-medium">
          Priority focus: Trigonometric Identities
        </span>
        <button className="font-semibold text-[#2f66f6] hover:text-[#2557df] flex items-center gap-0.5">
          <span>Start drill</span>
          <ArrowUpRight className="w-3 h-3" />
        </button>
      </div>
    </div>
  );
};
