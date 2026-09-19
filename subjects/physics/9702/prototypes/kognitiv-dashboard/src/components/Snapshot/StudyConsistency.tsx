import React, { useState } from 'react';
import { Calendar } from 'lucide-react';

type ActivityLevel = 0 | 1 | 2 | 3;

// 4 rows x 18 columns mapped directly to match the screenshot layout
const heatmapData: ActivityLevel[][] = [
  [0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 1, 0, 0, 3, 0, 0],
  [0, 0, 0, 2, 0, 2, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0, 2, 0],
  [0, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0],
];

const levelColors: Record<ActivityLevel, string> = {
  0: 'bg-[#f1f5f9]', // No study (subtle neutral slate)
  1: 'bg-[#bfdbfe]', // Light (soft blue tint)
  2: 'bg-[#60a5fa]', // Moderate (medium blue)
  3: 'bg-[#2f66f6]', // High (vibrant royal blue)
};

const levelLabels: Record<ActivityLevel, string> = {
  0: 'No study',
  1: 'Light (< 30 min)',
  2: 'Moderate (30-60 min)',
  3: 'High (> 60 min)',
};

export const StudyConsistency: React.FC = () => {
  const [hoveredCell, setHoveredCell] = useState<{
    row: number;
    col: number;
    level: ActivityLevel;
  } | null>(null);

  return (
    <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-sm flex flex-col justify-between hover:border-slate-200 transition-colors">
      {/* Card Header */}
      <div>
        <div className="flex items-center gap-3 mb-6">
          <div className="w-11 h-11 rounded-xl bg-[#eff6ff] flex items-center justify-center text-[#2f66f6] border border-blue-100/60">
            <Calendar className="w-5 h-5 stroke-[1.85]" />
          </div>
          <div>
            <h3 className="font-bold text-[#0f172a] text-base leading-snug">
              Study Consistency
            </h3>
            <p className="text-xs text-[#64748b] font-medium leading-snug mt-0.5">
              {hoveredCell
                ? `Day ${hoveredCell.col * 4 + hoveredCell.row + 1} • ${levelLabels[hoveredCell.level]}`
                : 'Your study activity over the last 28 days'}
            </p>
          </div>
        </div>

        {/* Heatmap Grid */}
        <div className="overflow-x-auto pb-2">
          <div className="inline-grid grid-rows-4 gap-2 min-w-full">
            {heatmapData.map((row, rIdx) => (
              <div key={rIdx} className="flex gap-2 justify-between">
                {row.map((level, cIdx) => (
                  <div
                    key={`${rIdx}-${cIdx}`}
                    onMouseEnter={() => setHoveredCell({ row: rIdx, col: cIdx, level })}
                    onMouseLeave={() => setHoveredCell(null)}
                    className={`w-4 h-4 sm:w-5 sm:h-5 rounded-[4px] ${levelColors[level]} cursor-pointer transition-all duration-150 hover:ring-2 hover:ring-[#2f66f6]/50 hover:scale-110 relative group`}
                    title={`Day ${cIdx * 4 + rIdx + 1}: ${levelLabels[level]}`}
                  />
                ))}
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Legend */}
      <div className="flex items-center gap-4 sm:gap-6 mt-6 pt-4 border-t border-slate-50 flex-wrap text-xs text-[#64748b]">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-[3px] bg-[#f1f5f9]" />
          <span>No study</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-[3px] bg-[#bfdbfe]" />
          <span>Light</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-[3px] bg-[#60a5fa]" />
          <span>Moderate</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-[3px] bg-[#2f66f6]" />
          <span>High</span>
        </div>
      </div>
    </div>
  );
};
