import React, { useState } from 'react';
import { Calendar as CalendarIcon } from 'lucide-react';

interface ExamComponent {
  code: string;
  paperNumber: string;
  name: string;
  paperCode: string;
  dayOfMonth: number;
  monthName: string;
  fullDate: string;
  session: string;
  duration: string;
}

const officialSchedule: Record<number, ExamComponent> = {
  30: {
    code: 'P1',
    paperNumber: 'Paper 1',
    name: 'Pure Mathematics 1',
    paperCode: 'Cambridge paper 9709/12',
    dayOfMonth: 30,
    monthName: 'Sep',
    fullDate: 'Wednesday, 30 September 2026',
    session: 'PM',
    duration: '110 minutes',
  },
  7: {
    code: 'S1',
    paperNumber: 'Paper 5',
    name: 'Probability & Statistics 1',
    paperCode: 'Cambridge paper 9709/52',
    dayOfMonth: 7,
    monthName: 'Oct',
    fullDate: 'Wednesday, 7 October 2026',
    session: 'PM',
    duration: '75 minutes',
  },
  13: {
    code: 'M1',
    paperNumber: 'Paper 4',
    name: 'Mechanics',
    paperCode: 'Cambridge paper 9709/42',
    dayOfMonth: 13,
    monthName: 'Oct',
    fullDate: 'Tuesday, 13 October 2026',
    session: 'PM',
    duration: '75 minutes',
  },
  15: {
    code: 'P3',
    paperNumber: 'Paper 3',
    name: 'Pure Mathematics 3',
    paperCode: 'Cambridge paper 9709/32',
    dayOfMonth: 15,
    monthName: 'Oct',
    fullDate: 'Thursday, 15 October 2026',
    session: 'PM',
    duration: '110 minutes',
  },
};

export const MathsExamCalendar: React.FC = () => {
  const [selectedDay, setSelectedDay] = useState<number>(30);
  const [hoveredDay, setHoveredDay] = useState<number | null>(null);

  // October 2026 starts on Thursday (index 3 in Mon=0, Tue=1, Wed=2, Thu=3)
  const offsetDays = 3;
  const totalDays = 31;
  const daysArray = Array.from({ length: totalDays }, (_, i) => i + 1);
  const blanks = Array.from({ length: offsetDays }, (_, i) => i);

  const activeDay = hoveredDay && officialSchedule[hoveredDay] ? hoveredDay : selectedDay;
  const activeExam = officialSchedule[activeDay] || officialSchedule[30];

  return (
    <div className="bg-white rounded-2xl p-5 sm:p-6 border border-slate-100 shadow-2xs hover:border-slate-200 transition-colors select-none flex flex-col justify-between h-full">
      <div>
        {/* Calendar Header matching live Kognitiv schedule */}
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <CalendarIcon className="w-4 h-4" />
            </div>
            <div>
              <span className="font-bold text-sm text-[#0f172a] block leading-tight">
                Exam Calendar
              </span>
              <span className="text-[11px] text-slate-400 font-normal">
                October/November 2026 Series
              </span>
            </div>
          </div>

          <span className="px-2.5 py-1 rounded-full text-xs font-semibold bg-[#ecfdf5] text-[#059669] border border-emerald-100/60">
            Final timetable
          </span>
        </div>

        {/* Days of Week */}
        <div className="grid grid-cols-7 text-center text-[10px] font-bold text-slate-400 mb-1.5">
          <span>Mon</span>
          <span>Tue</span>
          <span>Wed</span>
          <span>Thu</span>
          <span>Fri</span>
          <span>Sat</span>
          <span>Sun</span>
        </div>

        {/* Calendar Matrix with Royal Blue brand styling */}
        <div className="grid grid-cols-7 gap-1 text-center text-xs">
          {blanks.map((b) => (
            <div key={`blank-${b}`} className="h-6 w-6" />
          ))}

          {daysArray.map((day) => {
            const examInfo = officialSchedule[day];
            const isSelected = activeDay === day;

            return (
              <button
                key={`day-${day}`}
                onClick={() => examInfo && setSelectedDay(day)}
                onMouseEnter={() => examInfo && setHoveredDay(day)}
                onMouseLeave={() => setHoveredDay(null)}
                className={`h-6 w-6 mx-auto rounded-md flex items-center justify-center text-[11px] transition-all relative ${
                  examInfo
                    ? isSelected
                      ? 'bg-[#2f66f6] text-white font-bold shadow-xs scale-105'
                      : 'bg-[#eff6ff] text-[#2f66f6] font-bold hover:bg-[#dbeafe] hover:scale-105'
                    : 'text-slate-600 hover:bg-slate-50'
                }`}
              >
                <span>{day}</span>
                {examInfo && !isSelected && (
                  <span className="absolute -bottom-0.5 w-1 h-1 rounded-full bg-[#2f66f6]" />
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Selected Exam Information Dock matching the official component schedule card */}
      <div className="mt-3.5 pt-3 border-t border-slate-100">
        <div className="p-3 rounded-xl bg-slate-50/90 border border-slate-100/90 hover:border-slate-200 transition-all">
          <div className="flex items-center justify-between mb-1.5">
            <div className="flex items-center gap-2">
              <span className="w-7 h-7 rounded-lg bg-[#eff6ff] text-[#2f66f6] font-bold text-xs flex items-center justify-center">
                {activeExam.code}
              </span>
              <div>
                <span className="text-xs font-bold text-slate-900 block leading-tight">
                  {activeExam.name}
                </span>
                <span className="text-[10px] text-slate-400 font-normal">
                  {activeExam.paperCode}
                </span>
              </div>
            </div>
            <span className="text-[10px] font-semibold text-slate-600 bg-white px-2 py-0.5 rounded border border-slate-200/80">
              {activeExam.duration}
            </span>
          </div>

          <div className="grid grid-cols-2 gap-2 mt-2 pt-2 border-t border-slate-200/60 text-[10px]">
            <div>
              <span className="text-slate-400 font-medium block">DATE</span>
              <span className="font-semibold text-slate-800">{activeExam.fullDate}</span>
            </div>
            <div className="text-right">
              <span className="text-slate-400 font-medium block">SESSION</span>
              <span className="font-bold text-slate-800">{activeExam.session}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
