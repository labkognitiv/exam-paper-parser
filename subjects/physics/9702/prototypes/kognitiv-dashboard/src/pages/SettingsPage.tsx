import React, { useState } from 'react';
import { User, Calendar, CreditCard, HelpCircle, ArrowRight, Clock, Sparkles } from 'lucide-react';

export const SettingsPage: React.FC = () => {
  const [activeSubTab, setActiveSubTab] = useState<'account' | 'exams' | 'subscription' | 'help'>('exams');
  const [userName, setUserName] = useState('AbdullahJeevan');
  const [userEmail, setUserEmail] = useState('a.aftabwork@gmail.com');
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  const subNavItems = [
    {
      id: 'account' as const,
      label: 'Account',
      subtitle: 'Personal details and security',
      icon: User,
    },
    {
      id: 'exams' as const,
      label: 'Exams & dates',
      subtitle: 'Your exam series and timetable',
      icon: Calendar,
    },
    {
      id: 'subscription' as const,
      label: 'Subscription',
      subtitle: 'Plan, billing, and credits',
      icon: CreditCard,
    },
    {
      id: 'help' as const,
      label: 'Help & legal',
      subtitle: 'Support, privacy, and policies',
      icon: HelpCircle,
    },
  ];

  return (
    <div className="max-w-6xl mx-auto">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-[#111424] text-white px-5 py-3 rounded-xl shadow-xl flex items-center gap-3 border border-[#1a1f36] text-xs font-medium animate-in fade-in slide-in-from-bottom-2 duration-150">
          <Sparkles className="w-4 h-4 text-[#2f66f6]" />
          <span>{toastMessage}</span>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Settings Left Sub-Navigation (Matching Screenshots 1, 2, 3) */}
        <div className="lg:col-span-4 bg-white rounded-2xl p-3 border border-slate-100 shadow-2xs space-y-1 select-none">
          {subNavItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeSubTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveSubTab(item.id)}
                className={`w-full text-left p-3.5 rounded-xl transition-all flex items-start gap-3.5 ${
                  isActive
                    ? 'border border-[#2f66f6] bg-[#eff6ff]/70 text-[#2f66f6]'
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 border border-transparent'
                }`}
              >
                <Icon
                  className={`w-5 h-5 shrink-0 mt-0.5 ${
                    isActive ? 'text-[#2f66f6]' : 'text-slate-400'
                  }`}
                />
                <div>
                  <span className={`text-sm font-bold block ${isActive ? 'text-[#2f66f6]' : 'text-slate-900'}`}>
                    {item.label}
                  </span>
                  <span className="text-xs text-slate-500 font-normal leading-tight block mt-0.5">
                    {item.subtitle}
                  </span>
                </div>
              </button>
            );
          })}
        </div>

        {/* Settings Right Content Area */}
        <div className="lg:col-span-8 space-y-6">
          {/* ================================================================ */}
          {/* TAB 1: ACCOUNT (Matching Screenshot 1) */}
          {/* ================================================================ */}
          {activeSubTab === 'account' && (
            <>
              {/* Card 1: Account personal details */}
              <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                  SETTINGS
                </span>
                <h2 className="text-2xl font-bold text-[#0f172a] mb-1">Account</h2>
                <p className="text-sm text-slate-500 mb-6">Manage your personal details.</p>

                <div className="space-y-4">
                  <div>
                    <label className="text-xs font-bold text-slate-700 block mb-1.5">
                      Name
                    </label>
                    <input
                      type="text"
                      value={userName}
                      onChange={(e) => setUserName(e.target.value)}
                      className="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-slate-50/50 text-sm font-medium text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#2f66f6]/40 focus:border-[#2f66f6]"
                    />
                  </div>

                  <div>
                    <label className="text-xs font-bold text-slate-700 block mb-1.5">
                      Email
                    </label>
                    <input
                      type="email"
                      value={userEmail}
                      onChange={(e) => setUserEmail(e.target.value)}
                      className="w-full px-4 py-2.5 rounded-xl border border-slate-200 bg-slate-50/50 text-sm font-medium text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#2f66f6]/40 focus:border-[#2f66f6]"
                    />
                  </div>

                  <div className="flex justify-end pt-2">
                    <button
                      onClick={() => showToast('Changes saved successfully')}
                      className="px-5 py-2.5 rounded-xl bg-[#2f66f6] hover:bg-[#2557df] text-white text-sm font-medium transition-all shadow-xs active:scale-[0.98]"
                    >
                      Save changes
                    </button>
                  </div>
                </div>
              </div>

              {/* Card 2: Password & security */}
              <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                  SECURITY
                </span>
                <h3 className="text-lg font-bold text-[#0f172a] mb-4">Password & security</h3>
                <div className="flex items-center justify-between p-4 rounded-xl border border-slate-100 bg-slate-50/50">
                  <span className="text-xs text-slate-600">
                    Managed securely through email verification
                  </span>
                  <button
                    onClick={() => showToast('Password reset link sent to your email')}
                    className="px-4 py-2 rounded-xl border border-slate-200 bg-white text-xs font-semibold text-slate-800 hover:bg-slate-50 transition-colors shadow-xs"
                  >
                    Change password
                  </button>
                </div>
              </div>

              {/* Card 3: Daily focus timer / Time & region (Matching bottom of Screenshot 1) */}
              <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                  DAILY FOCUS TIMER
                </span>
                <h3 className="text-lg font-bold text-[#0f172a] mb-1">Time & region</h3>
                <p className="text-xs text-slate-500 mb-4 leading-relaxed">
                  Focus days reset at midnight in this timezone. Historical days retain the timezone snapshot they were created in.
                </p>

                <div className="flex items-center justify-between p-4 rounded-xl border border-slate-100 bg-slate-50/50">
                  <div className="flex items-center gap-3">
                    <Clock className="w-4 h-4 text-slate-400" />
                    <div>
                      <span className="text-xs font-bold text-slate-900 block">
                        (UTC+05:00) Islamabad, Karachi
                      </span>
                      <span className="text-[11px] text-slate-400">
                        Pakistan Standard Time (PKT)
                      </span>
                    </div>
                  </div>
                  <span className="text-xs text-[#2f66f6] font-semibold bg-[#eff6ff] px-2.5 py-1 rounded-md">
                    Auto-detected
                  </span>
                </div>
              </div>
            </>
          )}

          {/* ================================================================ */}
          {/* TAB 2: EXAMS & DATES (Matching Screenshot 2) */}
          {/* ================================================================ */}
          {activeSubTab === 'exams' && (
            <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
              <div className="flex items-start justify-between mb-4">
                <div>
                  <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                    OFFICIAL COMPONENT SCHEDULE
                  </span>
                  <h2 className="text-2xl font-bold text-[#0f172a]">
                    October/November 2026
                  </h2>
                  <p className="text-xs text-slate-500 mt-0.5">
                    Cambridge Mathematics 9709 · Administrative Zone 4
                  </p>
                </div>
                <span className="px-3 py-1 rounded-full text-xs font-semibold bg-[#ecfdf5] text-[#059669] border border-emerald-100/60">
                  Final timetable
                </span>
              </div>

              {/* 4 Exam Component Cards matching Screenshot 2 */}
              <div className="space-y-3 mt-6">
                {[
                  {
                    code: 'P1',
                    name: 'Pure Mathematics 1',
                    paper: 'Cambridge paper 9709/12',
                    date: 'Wednesday, 30 September 2026',
                    session: 'PM',
                    duration: '110 minutes',
                  },
                  {
                    code: 'S1',
                    name: 'Probability & Statistics 1',
                    paper: 'Cambridge paper 9709/52',
                    date: 'Wednesday, 7 October 2026',
                    session: 'PM',
                    duration: '75 minutes',
                  },
                  {
                    code: 'M1',
                    name: 'Mechanics',
                    paper: 'Cambridge paper 9709/42',
                    date: 'Tuesday, 13 October 2026',
                    session: 'PM',
                    duration: '75 minutes',
                  },
                  {
                    code: 'P3',
                    name: 'Pure Mathematics 3',
                    paper: 'Cambridge paper 9709/32',
                    date: 'Thursday, 15 October 2026',
                    session: 'PM',
                    duration: '110 minutes',
                  },
                ].map((item) => (
                  <div
                    key={item.code}
                    className="p-4 rounded-xl border border-slate-100 bg-white hover:border-slate-200 transition-all flex flex-col md:flex-row md:items-center justify-between gap-4"
                  >
                    <div className="flex items-center gap-3.5 min-w-0">
                      <div className="w-10 h-10 rounded-lg bg-[#eff6ff] text-[#2f66f6] font-bold text-sm flex items-center justify-center shrink-0">
                        {item.code}
                      </div>
                      <div className="min-w-0">
                        <span className="font-bold text-sm text-[#0f172a] block leading-tight">
                          {item.name}
                        </span>
                        <span className="text-xs text-slate-400 block mt-0.5">
                          {item.paper}
                        </span>
                      </div>
                    </div>

                    <div className="flex items-center gap-6 text-xs shrink-0 self-end md:self-auto">
                      <div>
                        <span className="text-[10px] font-bold text-slate-400 block uppercase">
                          DATE
                        </span>
                        <span className="font-semibold text-slate-800">{item.date}</span>
                      </div>
                      <div>
                        <span className="text-[10px] font-bold text-slate-400 block uppercase">
                          SESSION
                        </span>
                        <span className="font-bold text-slate-900">{item.session}</span>
                      </div>
                      <div>
                        <span className="text-[10px] font-bold text-slate-400 block uppercase">
                          DURATION
                        </span>
                        <span className="font-bold text-slate-900">{item.duration}</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* ================================================================ */}
          {/* TAB 3: SUBSCRIPTION (Matching Screenshot 3) */}
          {/* ================================================================ */}
          {activeSubTab === 'subscription' && (
            <>
              {/* Card 1: Current Plan */}
              <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block">
                    CURRENT PLAN
                  </span>
                  <span className="px-3 py-1 rounded-full text-xs font-semibold bg-[#ecfdf5] text-[#059669] border border-emerald-100/60">
                    Active
                  </span>
                </div>
                <h2 className="text-2xl font-bold text-[#0f172a]">EduPlus</h2>
                <p className="text-xs text-slate-500 mt-1 mb-6">Your subscription is active.</p>

                <div className="grid grid-cols-2 gap-4 p-4 rounded-xl bg-slate-50/70 border border-slate-100 mb-6">
                  <div>
                    <span className="text-[11px] font-bold text-slate-400 uppercase block mb-1">
                      BILLING INTERVAL
                    </span>
                    <span className="text-sm font-bold text-slate-900">Monthly</span>
                  </div>
                  <div>
                    <span className="text-[11px] font-bold text-slate-400 uppercase block mb-1">
                      RENEWS
                    </span>
                    <span className="text-sm font-bold text-slate-900">7 October 2026</span>
                  </div>
                </div>

                <div className="flex items-center gap-3 flex-wrap">
                  <button
                    onClick={() => showToast('Opening payment gateway modal...')}
                    className="px-4 py-2 rounded-xl border border-slate-200 bg-white text-xs font-semibold text-slate-800 hover:bg-slate-50 transition-colors shadow-xs flex items-center gap-2"
                  >
                    <CreditCard className="w-3.5 h-3.5 text-slate-500" />
                    <span>Manage payment method</span>
                  </button>
                  <button
                    onClick={() => showToast('Subscription cancellation window opened')}
                    className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:text-red-600 transition-colors"
                  >
                    Cancel subscription
                  </button>
                </div>
              </div>

              {/* Card 2: Billing history */}
              <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                  PAYMENTS
                </span>
                <h3 className="text-lg font-bold text-[#0f172a] mb-1">Billing history</h3>
                <p className="text-xs text-slate-500 mb-4">
                  Completed subscription payments recorded for this account.
                </p>

                <div className="p-4 rounded-xl border border-slate-100 bg-white flex items-center justify-between">
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="text-sm font-bold text-slate-900">EUR 1.00</span>
                      <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-[#ecfdf5] text-[#059669]">
                        Completed
                      </span>
                    </div>
                    <div className="flex items-center gap-4 text-xs text-slate-400 mt-1">
                      <span>PAID ON: 7 August 2026</span>
                      <span>•</span>
                      <span>INVOICE: 43127-10001</span>
                    </div>
                  </div>

                  <button
                    onClick={() => showToast('Downloading invoice PDF #43127-10001...')}
                    className="px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition-colors"
                  >
                    View invoice
                  </button>
                </div>
              </div>

              {/* Card 3: Credits (Matching bottom of Screenshot 3) */}
              <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
                <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                  CREDITS
                </span>
                <div className="flex items-center justify-between mb-2">
                  <h3 className="text-lg font-bold text-[#0f172a]">Monthly explanation grant</h3>
                  <span className="text-xs font-bold text-[#2f66f6] bg-[#eff6ff] px-2.5 py-0.5 rounded-full">
                    100 / 100 Available
                  </span>
                </div>
                <p className="text-xs text-slate-500 leading-relaxed">
                  Your monthly grant of step-by-step AI question walkthroughs resets on 7 October 2026.
                </p>
              </div>
            </>
          )}

          {/* ================================================================ */}
          {/* TAB 4: HELP & LEGAL */}
          {/* ================================================================ */}
          {activeSubTab === 'help' && (
            <div className="bg-white rounded-2xl p-6 border border-slate-100 shadow-2xs">
              <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                SUPPORT & POLICIES
              </span>
              <h2 className="text-2xl font-bold text-[#0f172a] mb-2">Help & Legal</h2>
              <p className="text-sm text-slate-500 mb-6">Need assistance with your Cambridge revision or past papers?</p>
              <div className="space-y-3">
                <div className="p-4 rounded-xl border border-slate-100 flex items-center justify-between hover:bg-slate-50 transition-colors cursor-pointer">
                  <span className="text-sm font-medium text-slate-800">Frequently Asked Questions</span>
                  <ArrowRight className="w-4 h-4 text-slate-400" />
                </div>
                <div className="p-4 rounded-xl border border-slate-100 flex items-center justify-between hover:bg-slate-50 transition-colors cursor-pointer">
                  <span className="text-sm font-medium text-slate-800">Cambridge Syllabus Mappings & Verification</span>
                  <ArrowRight className="w-4 h-4 text-slate-400" />
                </div>
                <div className="p-4 rounded-xl border border-slate-100 flex items-center justify-between hover:bg-slate-50 transition-colors cursor-pointer">
                  <span className="text-sm font-medium text-slate-800">Privacy Policy & Terms of Service</span>
                  <ArrowRight className="w-4 h-4 text-slate-400" />
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
