import React, { useState, useEffect } from 'react';
import { ArrowLeft, Quote, RotateCcw } from 'lucide-react';

interface MathsHeroGreetingProps {
  userName?: string;
  onBackToDashboard: () => void;
}

const motivationalQuotes = [
  {
    quote: "Pure mathematics is, in its way, the poetry of logical ideas.",
    author: "Albert Einstein",
    context: "Theoretical Physicist",
  },
  {
    quote: "The beauty of mathematics only shows itself to more patient followers.",
    author: "Maryam Mirzakhani",
    context: "Fields Medalist & Mathematician",
  },
  {
    quote: "Mathematics is the art of giving the same name to different things.",
    author: "Henri Poincaré",
    context: "Mathematician & Philosopher",
  },
  {
    quote: "An equation has no meaning unless it expresses a profound truth.",
    author: "Srinivasa Ramanujan",
    context: "Mathematical Prodigy",
  },
  {
    quote: "In mathematics, the art of proposing a question must be held higher than solving it.",
    author: "Georg Cantor",
    context: "Founder of Set Theory",
  },
];

export const MathsHeroGreeting: React.FC<MathsHeroGreetingProps> = ({
  userName = 'Abdullah',
  onBackToDashboard,
}) => {
  const [greeting, setGreeting] = useState('Good evening');
  const [quoteIndex, setQuoteIndex] = useState(0);
  const [isRotating, setIsRotating] = useState(false);

  useEffect(() => {
    const hour = new Date().getHours();
    if (hour >= 5 && hour < 12) {
      setGreeting('Good morning');
    } else if (hour >= 12 && hour < 17) {
      setGreeting('Good afternoon');
    } else {
      setGreeting('Good evening');
    }
  }, []);

  const handleNextQuote = () => {
    setIsRotating(true);
    setTimeout(() => {
      setQuoteIndex((prev) => (prev + 1) % motivationalQuotes.length);
      setIsRotating(false);
    }, 180);
  };

  const currentQuote = motivationalQuotes[quoteIndex];

  return (
    <div className="bg-white rounded-2xl p-5 sm:p-6 border border-slate-100 shadow-2xs hover:border-slate-200 transition-colors flex flex-col justify-between h-full">
      <div>
        {/* Navigation Breadcrumb & Standard Badges */}
        <div className="flex items-center justify-between mb-3 text-xs">
          <button
            onClick={onBackToDashboard}
            className="flex items-center gap-1.5 text-slate-500 hover:text-[#2f66f6] transition-colors py-0.5 px-2 rounded-lg hover:bg-slate-50 -ml-2 font-medium"
          >
            <ArrowLeft className="w-3.5 h-3.5 transition-transform group-hover:-translate-x-0.5 text-[#2f66f6]" />
            <span>Dashboard</span>
            <span className="text-slate-300">/</span>
            <span className="text-slate-900 font-semibold">Mathematics</span>
            <span className="text-slate-400 font-normal">(9709)</span>
          </button>

          <div className="flex items-center gap-2">
            <span className="px-2.5 py-1 rounded-xl text-xs font-semibold bg-[#eff6ff] text-[#2f66f6] border border-blue-100/60">
              Zone 4
            </span>
            <span className="px-3 py-1 rounded-xl text-xs font-semibold bg-[#ecfdf5] text-[#059669] border border-emerald-100/60">
              Final timetable
            </span>
          </div>
        </div>

        {/* Big, Commanding Greeting */}
        <div>
          <h1 className="text-3xl sm:text-4xl font-bold text-[#0f172a] tracking-tight leading-tight">
            {greeting}, {userName}
          </h1>
          <p className="text-sm text-slate-500 mt-1 font-normal">
            Here is your learning overview and exam preparation for Cambridge Mathematics.
          </p>
        </div>

        {/* Motivational Quote - Positioned directly beneath greeting with zero white space gap */}
        <div
          onClick={handleNextQuote}
          className="mt-3.5 p-3.5 rounded-xl bg-slate-50/80 hover:bg-[#eff6ff]/60 border border-slate-100/90 transition-all group relative cursor-pointer"
        >
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-[#eff6ff] text-[#2f66f6] flex items-center justify-center shrink-0">
              <Quote className="w-4 h-4" />
            </div>
            <div className="flex-1 min-w-0 pr-6">
              <p
                className={`text-xs sm:text-[13px] text-slate-800 italic font-medium leading-snug transition-opacity ${
                  isRotating ? 'opacity-20' : 'opacity-100'
                }`}
              >
                "{currentQuote.quote}"
              </p>
              <div className="text-[11px] text-slate-400 flex items-center gap-1.5 mt-0.5">
                <span className="font-semibold text-slate-700">{currentQuote.author}</span>
                <span className="text-slate-300">•</span>
                <span className="text-[#2f66f6] font-medium">{currentQuote.context}</span>
              </div>
            </div>
          </div>

          <button
            onClick={(e) => {
              e.stopPropagation();
              handleNextQuote();
            }}
            title="Inspire with another quote"
            className="absolute right-2.5 top-1/2 -translate-y-1/2 p-1.5 rounded-lg text-slate-400 hover:text-[#2f66f6] hover:bg-white transition-all opacity-60 group-hover:opacity-100 shadow-2xs"
          >
            <RotateCcw className={`w-3.5 h-3.5 ${isRotating ? 'animate-spin' : ''}`} />
          </button>
        </div>
      </div>

      {/* Clean Bottom Study Summary in Standard Brand Colors */}
      <div className="grid grid-cols-3 gap-2.5 mt-3.5 pt-3 border-t border-slate-100">
        <div className="p-2.5 rounded-xl bg-slate-50/80 border border-slate-100/80">
          <span className="text-[10px] text-slate-400 font-medium block">Current Standing</span>
          <span className="text-xs font-bold text-[#2f66f6] block mt-0.5">Grade A*</span>
        </div>
        <div className="p-2.5 rounded-xl bg-slate-50/80 border border-slate-100/80">
          <span className="text-[10px] text-slate-400 font-medium block">Syllabus Progress</span>
          <span className="text-xs font-bold text-slate-800 block mt-0.5">68% Complete</span>
        </div>
        <div className="p-2.5 rounded-xl bg-slate-50/80 border border-slate-100/80">
          <span className="text-[10px] text-slate-400 font-medium block">Active Components</span>
          <span className="text-xs font-bold text-slate-800 block mt-0.5">4 Papers (P1, S1, M1, P3)</span>
        </div>
      </div>
    </div>
  );
};
