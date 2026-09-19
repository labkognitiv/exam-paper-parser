import { YearlyPage } from './YearlyPage';
import { PhysicsTopicalPage } from './PhysicsTopicalPage';
import React, { useState } from 'react';
import {
  Sparkles,
} from 'lucide-react';

export const RevisionPage: React.FC = () => {
  const [viewMode, setViewMode] = useState<'hub' | 'topical' | 'yearly'>('hub');
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  if (viewMode === 'topical') return <PhysicsTopicalPage onBack={() => setViewMode('hub')} />;
  if (viewMode === 'yearly') return <YearlyPage onBack={() => setViewMode('hub')} />;

  return (
    <div className="max-w-5xl mx-auto">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-[#111424] text-white px-5 py-3 rounded-xl shadow-xl flex items-center gap-3 border border-[#1a1f36] text-xs font-medium animate-in fade-in slide-in-from-bottom-2 duration-150">
          <Sparkles className="w-4 h-4 text-[#2f66f6]" />
          <span>{toastMessage}</span>
        </div>
      )}

      {viewMode === 'hub' && (
        <section aria-labelledby="revision-options-heading">
          <h2 id="revision-options-heading" className="text-2xl font-bold text-[#1d1935] tracking-tight mb-6">
            Choose how you want to revise
          </h2>
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 lg:gap-5">
            {[
              { id: 'topical', title: 'Topical', description: 'Focused questions, one topic at a time.' },
              { id: 'yearly', title: 'Yearly', description: 'Complete past papers, organised by year.' },
              { id: 'games', title: 'Games', description: 'Short challenges, one step at a time.' },
            ].map((option) => (
              <button
                key={option.id}
                onClick={() => {
                  if (option.id === 'games') {
                    showToast('Games preview is not available yet.');
                  } else {
                    setViewMode(option.id as 'topical' | 'yearly');
                  }
                }}
                className="group flex flex-col items-start text-left bg-white rounded-2xl border border-[#e8eaee] p-6 sm:p-7 transition-colors hover:bg-[#f2faf8] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#2bb9b1] focus-visible:ring-offset-4"
              >
                <h3 className="text-xl font-bold text-[#1d1935]">{option.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-slate-500 max-w-[24ch]">{option.description}</p>
                <span className="mt-7 pt-4 border-t border-[#e8eaee] w-full text-sm font-semibold text-[#168f89] group-hover:text-[#116e69]">
                  Open {option.title.toLowerCase()}
                </span>
              </button>
            ))}
          </div>
        </section>
      )}

    </div>
  );
};
