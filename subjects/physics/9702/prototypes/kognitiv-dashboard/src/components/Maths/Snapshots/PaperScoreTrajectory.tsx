import React, { useState } from 'react';
import { Award, ArrowUpRight } from 'lucide-react';

interface PaperScore {
  session: string;
  score: number;
  maxScore: number;
  grade: string;
  percentile: string;
}

const scoresData: PaperScore[] = [
  { session: 'May 2022', score: 58, maxScore: 75, grade: 'Grade A', percentile: 'Top 12%' },
  { session: 'Nov 2022', score: 62, maxScore: 75, grade: 'Grade A*', percentile: 'Top 7%' },
  { session: 'May 2023', score: 65, maxScore: 75, grade: 'Grade A*', percentile: 'Top 5%' },
  { session: 'Nov 2023', score: 63, maxScore: 75, grade: 'Grade A*', percentile: 'Top 6%' },
  { session: 'May 2024', score: 71, maxScore: 75, grade: 'Grade A*', percentile: 'Top 2%' },
];

export const PaperScoreTrajectory: React.FC = () => {
  const [activeIdx, setActiveIdx] = useState<number | null>(null);

  const width = 450;
  const height = 120;
  const paddingX = 30;
  const paddingTop = 15;
  const paddingBottom = 20;
  const maxScore = 75;
  const minScore = 48;

  const points = scoresData.map((d, i) => {
    const x = paddingX + (i / (scoresData.length - 1)) * (width - paddingX * 2);
    const y = paddingTop + (1 - (d.score - minScore) / (maxScore - minScore)) * (height - paddingTop - paddingBottom);
    return { ...d, x, y };
  });

  const aStarY = paddingTop + (1 - (62 - minScore) / (maxScore - minScore)) * (height - paddingTop - paddingBottom);

  const generateSmoothPath = (pts: typeof points) => {
    if (pts.length === 0) return '';
    let path = `M ${pts[0].x} ${pts[0].y}`;
    for (let i = 0; i < pts.length - 1; i++) {
      const p0 = pts[i === 0 ? 0 : i - 1];
      const p1 = pts[i];
      const p2 = pts[i + 1];
      const p3 = pts[i + 2 < pts.length ? i + 2 : i + 1];

      const cp1x = p1.x + (p2.x - p0.x) / 6;
      const cp1y = p1.y + (p2.y - p0.y) / 6;
      const cp2x = p2.x - (p3.x - p1.x) / 6;
      const cp2y = p2.y - (p3.y - p1.y) / 6;

      path += ` C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${p2.x} ${p2.y}`;
    }
    return path;
  };

  const linePath = generateSmoothPath(points);
  const baselineY = height - paddingBottom;
  const areaPath = `${linePath} L ${points[points.length - 1].x} ${baselineY} L ${points[0].x} ${baselineY} Z`;

  const hoveredData = activeIdx !== null ? scoresData[activeIdx] : scoresData[scoresData.length - 1];

  return (
    <div className="bg-white rounded-2xl p-5 border border-slate-100 shadow-2xs flex flex-col justify-between hover:border-slate-200 transition-colors">
      <div>
        {/* Header */}
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <Award className="w-4 h-4 stroke-[2]" />
            </div>
            <div>
              <h3 className="font-bold text-[#0f172a] text-sm leading-tight">
                Past Paper Score Trajectory
              </h3>
              <p className="text-[11px] text-slate-400 font-normal">
                Timed mock performance vs. Cambridge A* boundary
              </p>
            </div>
          </div>

          <div className="text-right">
            <span className="text-xs font-bold text-[#2f66f6]">
              {hoveredData.score} of 75 Marks
            </span>
            <span className="text-[10px] text-slate-500 font-semibold block">
              {hoveredData.grade} • {hoveredData.percentile}
            </span>
          </div>
        </div>

        {/* SVG Curve in Royal Blue */}
        <div className="relative pt-1">
          <div className="h-28 w-full relative">
            {/* Dashed A* boundary guideline */}
            <div
              className="absolute w-full border-b border-dashed border-blue-200 pointer-events-none z-0"
              style={{ top: `${(aStarY / height) * 100}%` }}
            >
              <span className="absolute right-0 -top-3 text-[9px] font-semibold text-[#2f66f6] bg-[#eff6ff] px-1.5 py-0.5 rounded border border-blue-100">
                A* Boundary (62 Marks)
              </span>
            </div>

            <svg
              viewBox={`0 0 ${width} ${height}`}
              className="w-full h-full overflow-visible"
              preserveAspectRatio="none"
            >
              <defs>
                <linearGradient id="scoreCurveGradBlue" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor="#2f66f6" stopOpacity="0.20" />
                  <stop offset="100%" stopColor="#2f66f6" stopOpacity="0.0" />
                </linearGradient>
              </defs>

              {/* Gradient Area */}
              <path d={areaPath} fill="url(#scoreCurveGradBlue)" />

              {/* Line */}
              <path
                d={linePath}
                fill="none"
                stroke="#2f66f6"
                strokeWidth="2.4"
                strokeLinecap="round"
                strokeLinejoin="round"
              />

              {/* Points */}
              {points.map((pt, i) => {
                const isHovered = activeIdx === i;
                return (
                  <g key={pt.session} className="cursor-pointer">
                    <circle
                      cx={pt.x}
                      cy={pt.y}
                      r={14}
                      fill="transparent"
                      onMouseEnter={() => setActiveIdx(i)}
                      onMouseLeave={() => setActiveIdx(null)}
                    />
                    {isHovered && (
                      <circle cx={pt.x} cy={pt.y} r={7} fill="#bfdbfe" opacity={0.8} />
                    )}
                    <circle
                      cx={pt.x}
                      cy={pt.y}
                      r={4}
                      fill="#2f66f6"
                      stroke="#ffffff"
                      strokeWidth={2}
                    />
                  </g>
                );
              })}
            </svg>

            {/* Hover Tooltip */}
            {activeIdx !== null && (
              <div
                className="absolute -top-7 px-2.5 py-1 rounded-md bg-[#111424] text-white text-[11px] font-semibold shadow-md pointer-events-none z-10 transform -translate-x-1/2"
                style={{
                  left: `${((points[activeIdx].x - paddingX) / (width - paddingX * 2)) * 100}%`,
                }}
              >
                {points[activeIdx].score} / 75 ({points[activeIdx].grade})
              </div>
            )}
          </div>

          {/* X-Axis labels */}
          <div className="flex justify-between px-2 text-[10px] font-medium text-slate-400 mt-1">
            {scoresData.map((d) => (
              <span key={d.session}>{d.session}</span>
            ))}
          </div>
        </div>
      </div>

      <div className="flex items-center justify-between mt-3 pt-2.5 border-t border-slate-100 text-[11px] text-slate-400">
        <span>Average score +14% above boundary threshold</span>
        <button className="font-semibold text-[#2f66f6] hover:text-[#2557df] flex items-center gap-0.5">
          <span>View all papers</span>
          <ArrowUpRight className="w-3 h-3" />
        </button>
      </div>
    </div>
  );
};
