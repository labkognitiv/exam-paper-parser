import React, { useState } from 'react';
import { Clock, TrendingUp } from 'lucide-react';

interface WeekPoint {
  label: string;
  hours: number;
}

const trendData: WeekPoint[] = [
  { label: 'Week 1', hours: 2.2 },
  { label: 'Week 2', hours: 3.6 },
  { label: 'Week 3', hours: 3.1 },
  { label: 'Week 4', hours: 5.2 },
];

export const StudyTimeTrend: React.FC = () => {
  const [activePoint, setActivePoint] = useState<number | null>(null);

  // SVG dimensions
  const width = 500;
  const height = 150;
  const paddingX = 35;
  const paddingTop = 20;
  const paddingBottom = 25;
  const maxHours = 6;

  // Coordinate mapping
  const points = trendData.map((d, i) => {
    const x = paddingX + (i / (trendData.length - 1)) * (width - paddingX * 2);
    const y = paddingTop + (1 - d.hours / maxHours) * (height - paddingTop - paddingBottom);
    return { ...d, x, y };
  });

  // Generate smooth cubic bezier SVG path
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

  return (
    <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-sm flex flex-col justify-between hover:border-slate-200 transition-colors">
      {/* Card Header with Stat */}
      <div className="flex items-start justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="w-11 h-11 rounded-xl bg-[#eff6ff] flex items-center justify-center text-[#2f66f6] border border-blue-100/60">
            <Clock className="w-5 h-5 stroke-[1.85]" />
          </div>
          <div>
            <h3 className="font-bold text-[#0f172a] text-base leading-snug">
              Study Time Trend
            </h3>
            <p className="text-xs text-[#64748b] font-medium leading-snug mt-0.5">
              Total study time over the last 4 weeks
            </p>
          </div>
        </div>

        {/* Growth badge */}
        <div className="text-right">
          <div className="flex items-center justify-end gap-1 text-[#059669] font-bold text-sm">
            <span>+28%</span>
            <TrendingUp className="w-3.5 h-3.5 stroke-[2.5]" />
          </div>
          <span className="text-[11px] text-[#94a3b8] font-normal block">
            vs. previous 4 weeks
          </span>
        </div>
      </div>

      {/* SVG Smooth Curve Area Chart in Royal Blue */}
      <div className="relative pt-1">
        <div className="flex">
          {/* Y-Axis scale */}
          <div className="flex flex-col justify-between text-[11px] font-medium text-[#94a3b8] pr-2 select-none h-36 pb-6">
            <span>6h</span>
            <span>3h</span>
            <span>0h</span>
          </div>

          {/* SVG Plot */}
          <div className="relative flex-1 h-36">
            {/* Horizontal Grid lines */}
            <div className="absolute inset-0 flex flex-col justify-between pointer-events-none pb-6">
              <div className="border-b border-slate-100 w-full" />
              <div className="border-b border-slate-100 w-full" />
              <div className="border-b border-slate-200 w-full" />
            </div>

            <svg
              viewBox={`0 0 ${width} ${height}`}
              className="w-full h-full overflow-visible"
              preserveAspectRatio="none"
            >
              <defs>
                <linearGradient id="trendGradientBlue" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor="#2f66f6" stopOpacity="0.22" />
                  <stop offset="100%" stopColor="#2f66f6" stopOpacity="0.0" />
                </linearGradient>
              </defs>

              {/* Gradient Area Fill */}
              <path d={areaPath} fill="url(#trendGradientBlue)" />

              {/* Line Stroke */}
              <path
                d={linePath}
                fill="none"
                stroke="#2f66f6"
                strokeWidth="2.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />

              {/* Data points */}
              {points.map((pt, i) => {
                const isActive = activePoint === i;
                return (
                  <g key={pt.label} className="cursor-pointer">
                    {/* Hover hit area */}
                    <circle
                      cx={pt.x}
                      cy={pt.y}
                      r={14}
                      fill="transparent"
                      onMouseEnter={() => setActivePoint(i)}
                      onMouseLeave={() => setActivePoint(null)}
                    />
                    {/* Outer glow on hover */}
                    {isActive && (
                      <circle
                        cx={pt.x}
                        cy={pt.y}
                        r={8}
                        fill="#bfdbfe"
                        opacity={0.6}
                      />
                    )}
                    {/* Inner point */}
                    <circle
                      cx={pt.x}
                      cy={pt.y}
                      r={4.5}
                      fill="#2f66f6"
                      stroke="#ffffff"
                      strokeWidth={2.5}
                    />
                  </g>
                );
              })}
            </svg>

            {/* Hover Tooltip */}
            {activePoint !== null && (
              <div
                className="absolute -top-7 px-2.5 py-1 rounded-md bg-[#111424] text-white text-[11px] font-semibold shadow-md pointer-events-none z-10 transform -translate-x-1/2"
                style={{
                  left: `${((points[activePoint].x - paddingX) / (width - paddingX * 2)) * 100}%`,
                }}
              >
                {points[activePoint].hours} hrs
              </div>
            )}
          </div>
        </div>

        {/* X-Axis labels */}
        <div className="flex justify-between pl-8 pr-4 mt-2 text-xs font-medium text-[#64748b]">
          {trendData.map((d) => (
            <span key={d.label}>{d.label}</span>
          ))}
        </div>
      </div>
    </div>
  );
};
