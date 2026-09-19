import React, { useState, useEffect } from 'react';
import { Flame, Clock, Play, Pause, Bell } from 'lucide-react';

interface HeaderProps {
  title?: string;
  subtitle?: string;
  breadcrumb?: { label: string; onClick?: () => void }[];
  streakDays?: number;
}

export const Header: React.FC<HeaderProps> = ({
  title,
  subtitle,
  breadcrumb,
  streakDays = 0,
}) => {
  const [seconds, setSeconds] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    let timer: NodeJS.Timeout;
    if (isRunning) {
      timer = setInterval(() => setSeconds((prev) => prev + 1), 1000);
    }
    return () => clearInterval(timer);
  }, [isRunning]);

  const formatTime = (totalSec: number) => {
    const mins = Math.floor(totalSec / 60);
    const secs = totalSec % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  };

  return (
    <header className="bg-white border-b border-slate-100/90 px-6 py-3.5 flex items-center justify-between sticky top-0 z-30 select-none shadow-2xs">
      {/* Left: Breadcrumbs or Title */}
      <div className="flex items-center gap-2 text-sm font-medium text-slate-800">
        {breadcrumb && breadcrumb.length > 0 ? (
          <nav className="flex items-center gap-2">
            {breadcrumb.map((crumb, idx) => {
              const isLast = idx === breadcrumb.length - 1;
              return (
                <React.Fragment key={crumb.label}>
                  {idx > 0 && <span className="text-slate-300">/</span>}
                  {crumb.onClick && !isLast ? (
                    <button
                      onClick={crumb.onClick}
                      className="text-slate-500 hover:text-[#2f66f6] transition-colors"
                    >
                      {crumb.label}
                    </button>
                  ) : (
                    <span className={isLast ? 'font-bold text-slate-900 text-base' : 'text-slate-500'}>
                      {crumb.label}
                    </span>
                  )}
                </React.Fragment>
              );
            })}
          </nav>
        ) : (
          <div>
            <h1 className="text-base font-bold text-slate-900 leading-tight">
              {title || 'Dashboard'}
            </h1>
            {subtitle && (
              <p className="text-xs text-slate-400 font-normal">{subtitle}</p>
            )}
          </div>
        )}
      </div>

      {/* Right: Live Production Focus Timer, Streak & Bell */}
      <div className="flex items-center gap-3">
        {/* Focus Timer Pill matching live production screenshot */}
        <div className="flex items-center gap-2.5 px-3 py-1 rounded-full border border-slate-200 bg-white shadow-xs text-xs font-semibold text-slate-700">
          <Clock className="w-3.5 h-3.5 text-slate-400" />
          <span className="font-mono text-[12px]">{formatTime(seconds)}</span>
          <button
            onClick={() => setIsRunning(!isRunning)}
            title={isRunning ? 'Pause focus timer' : 'Start focus timer'}
            className="w-6 h-6 rounded-full bg-[#2f66f6] hover:bg-[#2557df] text-white flex items-center justify-center shadow-xs transition-transform active:scale-95"
          >
            {isRunning ? (
              <Pause className="w-3 h-3 fill-current" />
            ) : (
              <Play className="w-3 h-3 fill-current ml-0.5" />
            )}
          </button>
        </div>

        {/* Streak Pill matching live production screenshot */}
        <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#eff6ff] text-[#2f66f6] text-xs font-semibold">
          <Flame className="w-3.5 h-3.5 text-[#2f66f6] fill-current" />
          <span>{streakDays} days</span>
        </div>

        {/* Notification Bell */}
        <button
          title="Notifications"
          className="p-1.5 text-slate-400 hover:text-slate-600 rounded-full hover:bg-slate-100 transition-colors"
        >
          <Bell className="w-4 h-4 stroke-[1.8]" />
        </button>
      </div>
    </header>
  );
};
