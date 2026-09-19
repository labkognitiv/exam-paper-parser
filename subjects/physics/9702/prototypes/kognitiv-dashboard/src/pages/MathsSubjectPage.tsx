import React, { useState } from 'react';
import { MathsHeroGreeting } from '../components/Maths/MathsHeroGreeting';
import { MathsExamCalendar } from '../components/Maths/MathsExamCalendar';
import { MathsResumeBanner } from '../components/Maths/MathsResumeBanner';
import { TopicMasterySnapshot } from '../components/Maths/Snapshots/TopicMasterySnapshot';
import { PaperScoreTrajectory } from '../components/Maths/Snapshots/PaperScoreTrajectory';
import { ArchetypeAccuracySnapshot } from '../components/Maths/Snapshots/ArchetypeAccuracySnapshot';
import { VelocityPacingSnapshot } from '../components/Maths/Snapshots/VelocityPacingSnapshot';
import { Sparkles } from 'lucide-react';

interface MathsSubjectPageProps {
  onBackToDashboard: () => void;
  onNavigateToStudy?: () => void;
}

export const MathsSubjectPage: React.FC<MathsSubjectPageProps> = ({
  onBackToDashboard,
  onNavigateToStudy,
}) => {
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  const handleResume = () => {
    showToast('Resuming Pure Mathematics 1: Lesson 3...');
    if (onNavigateToStudy) {
      setTimeout(onNavigateToStudy, 500);
    }
  };

  return (
    <div className="max-w-[1400px] mx-auto">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-[#111424] text-white px-4 py-2.5 rounded-xl shadow-xl flex items-center gap-2.5 border border-[#1a1f36] text-xs font-medium animate-in fade-in slide-in-from-bottom-2 duration-150">
          <Sparkles className="w-3.5 h-3.5 text-[#2f66f6]" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Row 1: Top Section - Balanced Horizontal Ratio (Hero 7/12, Exam Calendar 5/12) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-3.5 mb-3.5 items-stretch">
        {/* Left Hero Greeting & Quote */}
        <div className="lg:col-span-7 xl:col-span-7">
          <MathsHeroGreeting
            userName="Abdullah"
            onBackToDashboard={onBackToDashboard}
          />
        </div>

        {/* Right Exam Schedule Calendar (Official Schedule) */}
        <div className="lg:col-span-5 xl:col-span-5">
          <MathsExamCalendar />
        </div>
      </div>

      {/* Row 2: Streamlined Horizontal Resume Strip */}
      <MathsResumeBanner
        module="Pure Mathematics 1"
        topic="Calculus: Integration by Substitution"
        lesson="Lesson 3"
        lastStudied="3h ago"
        onResume={handleResume}
      />

      {/* Row 3: Minimalist Monochromatic Analytics Snapshots (2x2 Grid) */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h2 className="text-base font-bold text-[#0f172a] tracking-tight">
            Diagnostic Analytics Snapshot
          </h2>
          <span className="text-[11px] text-slate-400 font-medium">
            Cambridge 9709 • Monochromatic Royal Blue System
          </span>
        </div>

        {/* 2x2 Compact Horizontal Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-3.5">
          <TopicMasterySnapshot />
          <PaperScoreTrajectory />
          <ArchetypeAccuracySnapshot />
          <VelocityPacingSnapshot />
        </div>
      </div>
    </div>
  );
};
