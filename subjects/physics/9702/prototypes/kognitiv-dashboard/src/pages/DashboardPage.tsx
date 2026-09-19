import React, { useState } from 'react';
import { SubjectCards } from '../components/SubjectCards';
import { ResumeStudyCard } from '../components/ResumeStudyCard';
import { StudyConsistency } from '../components/Snapshot/StudyConsistency';
import { WeeklyActivity } from '../components/Snapshot/WeeklyActivity';
import { StudyTimeTrend } from '../components/Snapshot/StudyTimeTrend';
import { SubjectProgress } from '../components/Snapshot/SubjectProgress';
import { X, Plus, Sparkles } from 'lucide-react';

interface DashboardPageProps {
  onNavigateToStudy?: () => void;
  onSelectSubject?: (subjectId: string) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({
  onNavigateToStudy,
  onSelectSubject,
}) => {
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  const handleResume = () => {
    showToast('Resuming Pure Mathematics 1: Lesson 3...');
    if (onNavigateToStudy) {
      setTimeout(onNavigateToStudy, 600);
    }
  };

  const handleSelectSubject = (id: string) => {
    if (onSelectSubject) {
      onSelectSubject(id);
    } else {
      showToast(`Opening ${id.toUpperCase()} curriculum...`);
    }
  };

  return (
    <div className="max-w-7xl mx-auto">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-[#111424] text-white px-5 py-3 rounded-xl shadow-xl flex items-center gap-3 border border-[#1a1f36] animate-in fade-in slide-in-from-bottom-2 duration-150">
          <Sparkles className="w-4 h-4 text-[#2f66f6]" />
          <span className="text-sm font-medium">{toastMessage}</span>
        </div>
      )}

      {/* Top Greeting */}
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-[#0f172a] tracking-tight">
          Good evening, Abdullah
        </h1>
        <p className="text-[15px] text-[#64748b] mt-1 font-normal">
          Here's your learning overview and Cambridge exam preparation for today.
        </p>
      </div>

      {/* Subject Selector Cards */}
      <SubjectCards
        onSelectSubject={handleSelectSubject}
        onAddSubject={() => setIsAddModalOpen(true)}
      />

      {/* Resume Study Banner */}
      <ResumeStudyCard
        subject="Mathematics"
        topic="Pure Mathematics 1 · Integration by Substitution"
        lesson="Lesson 3"
        lastStudied="3 hours ago"
        onResume={handleResume}
      />

      {/* Snapshot Section */}
      <div className="mt-8">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-[#0f172a] tracking-tight">
            Snapshot
          </h2>
          <span className="text-xs text-slate-400 font-medium">
            Active syllabus activity • Last 28 days
          </span>
        </div>

        {/* 2x2 Snapshot Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
          <StudyConsistency />
          <WeeklyActivity />
          <StudyTimeTrend />
          <SubjectProgress />
        </div>
      </div>

      {/* Add Subject Modal */}
      {isAddModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/40 backdrop-blur-sm p-4">
          <div className="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl border border-slate-100 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center justify-between pb-4 border-b border-slate-100">
              <h3 className="font-bold text-[#0f172a] text-lg">Add New Subject</h3>
              <button
                onClick={() => setIsAddModalOpen(false)}
                className="p-1 rounded-lg text-slate-400 hover:text-slate-600 hover:bg-slate-100"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="py-5 space-y-3">
              <p className="text-sm text-slate-500">
                Choose a Cambridge syllabus to add to your active plan:
              </p>
              {[
                { name: 'Biology (9700)' },
                { name: 'Economics (9708)' },
                { name: 'Computer Science (9618)' },
              ].map((sub) => (
                <button
                  key={sub.name}
                  onClick={() => {
                    showToast(`Added ${sub.name}!`);
                    setIsAddModalOpen(false);
                  }}
                  className="w-full text-left p-3.5 rounded-xl border border-slate-200 hover:border-[#2f66f6] hover:bg-[#eff6ff]/40 font-medium text-slate-800 transition-colors flex items-center justify-between group"
                >
                  <span>{sub.name}</span>
                  <Plus className="w-4 h-4 text-slate-400 group-hover:text-[#2f66f6]" />
                </button>
              ))}
            </div>
            <div className="flex justify-end pt-2">
              <button
                onClick={() => setIsAddModalOpen(false)}
                className="px-4 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 rounded-xl"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
