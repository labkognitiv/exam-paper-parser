import React from 'react';
import { Award, Target, Clock } from 'lucide-react';
import { TopicMasterySnapshot } from '../components/Maths/Snapshots/TopicMasterySnapshot';
import { PaperScoreTrajectory } from '../components/Maths/Snapshots/PaperScoreTrajectory';
import { ArchetypeAccuracySnapshot } from '../components/Maths/Snapshots/ArchetypeAccuracySnapshot';
import { VelocityPacingSnapshot } from '../components/Maths/Snapshots/VelocityPacingSnapshot';

export const AnalyticsPage: React.FC = () => {
  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Page Header */}
      <div>
        <h1 className="text-2xl font-bold text-[#0f172a] tracking-tight">
          Performance Analytics
        </h1>
        <p className="text-sm text-slate-500 mt-1">
          Detailed diagnostic metrics on Cambridge syllabus mastery, pacing, and past paper scoring.
        </p>
      </div>

      {/* 3 Metric Cards in Standard Royal Blue Design */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="p-5 bg-white rounded-2xl border border-slate-100 shadow-2xs">
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
              Predicted Grade
            </span>
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <Award className="w-4 h-4" />
            </div>
          </div>
          <div className="text-3xl font-extrabold text-[#0f172a]">Grade A*</div>
          <span className="text-xs text-[#2f66f6] font-semibold mt-1 inline-block">
            Top 5% Cambridge cohort standing
          </span>
        </div>

        <div className="p-5 bg-white rounded-2xl border border-slate-100 shadow-2xs">
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
              Historical Accuracy
            </span>
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <Target className="w-4 h-4" />
            </div>
          </div>
          <div className="text-3xl font-extrabold text-[#0f172a]">84.2%</div>
          <span className="text-xs text-[#059669] font-semibold mt-1 inline-block">
            +4.1% over last 30 days
          </span>
        </div>

        <div className="p-5 bg-white rounded-2xl border border-slate-100 shadow-2xs">
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
              Total Focus Time
            </span>
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center">
              <Clock className="w-4 h-4" />
            </div>
          </div>
          <div className="text-3xl font-extrabold text-[#0f172a]">142.5 hrs</div>
          <span className="text-xs text-slate-400 font-medium mt-1 inline-block">
            Across 9709 Mathematics components
          </span>
        </div>
      </div>

      {/* 2x2 Monochromatic Diagnostic Snapshots Grid */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h2 className="text-base font-bold text-[#0f172a] tracking-tight">
            Diagnostic Breakdown
          </h2>
          <span className="text-[11px] text-slate-400 font-medium">
            Monochromatic Royal Blue Analytics
          </span>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <TopicMasterySnapshot />
          <PaperScoreTrajectory />
          <ArchetypeAccuracySnapshot />
          <VelocityPacingSnapshot />
        </div>
      </div>
    </div>
  );
};
