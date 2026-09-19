import React from 'react';
import {
  Home,
  BookOpen,
  ClipboardList,
  Bookmark,
  BarChart3,
  Settings,
  ChevronLeft,
  LogOut,
} from 'lucide-react';

export type NavTab = 'dashboard' | 'study' | 'revision' | 'review' | 'analytics' | 'settings';

interface SidebarProps {
  activeTab: NavTab;
  onSelectTab: (tab: NavTab) => void;
}

const navItems = [
  { id: 'dashboard' as NavTab, label: 'Dashboard', icon: Home },
  { id: 'study' as NavTab, label: 'Study', icon: BookOpen },
  { id: 'revision' as NavTab, label: 'Revision', icon: ClipboardList },
  { id: 'review' as NavTab, label: 'Review', icon: Bookmark },
  { id: 'analytics' as NavTab, label: 'Analytics', icon: BarChart3 },
  { id: 'settings' as NavTab, label: 'Settings', icon: Settings },
];

export const Sidebar: React.FC<SidebarProps> = ({ activeTab, onSelectTab }) => {
  return (
    <aside className="w-64 bg-[#f6f8fa] text-[#1d1935] flex flex-col justify-between h-screen sticky top-0 shrink-0 select-none border-r border-[#e8eaee] shadow-[22px_0_55px_#26283818]">
      {/* Top section: Brand & Navigation */}
      <div className="p-5">
        {/* Kognitiv Brand Logo matching live production */}
        <div className="flex items-center justify-between mb-8 px-1">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-xl bg-[#2bb9b1] flex items-center justify-center shadow-sm">
              <span className="text-white font-bold text-lg tracking-tight">K</span>
            </div>
            <span className="text-lg font-bold text-[#272043] tracking-tight font-sans">
              Kognitiv
            </span>
          </div>
          <button
            title="Collapse sidebar"
            className="p-1.5 rounded-lg text-[#888995] hover:text-[#272043] hover:bg-[#e8f7f4] transition-colors"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>
        </div>

        {/* Navigation Menu */}
        <nav className="space-y-1.5">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => onSelectTab(item.id)}
                className={`w-full flex items-center gap-3.5 px-4 py-2.5 rounded-xl font-medium text-[14px] transition-all duration-150 text-left ${
                  isActive
                    ? 'bg-[#e1e1fb] text-[#272043] shadow-sm'
                    : 'text-[#555563] hover:text-[#272043] hover:bg-white'
                }`}
              >
                <Icon
                  className={`w-4 h-4 ${
                    isActive ? 'text-[#6d66c7]' : 'text-[#888995]'
                  }`}
                  strokeWidth={isActive ? 2.2 : 1.9}
                />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>
      </div>

      {/* Bottom section: User Profile matching live production */}
      <div className="p-4 border-t border-[#e8eaee] m-2">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3 min-w-0">
            <div className="w-9 h-9 rounded-full bg-[#dbf2ef] text-[#147e79] flex items-center justify-center font-bold text-sm shrink-0 shadow-sm">
              A
            </div>
            <div className="truncate">
              <p className="text-sm font-semibold text-[#272043] leading-tight truncate">
                AbdullahJeevan
              </p>
              <p className="text-xs text-[#888995] font-medium leading-tight mt-0.5">
                Account
              </p>
            </div>
          </div>
          <button
            title="Logout"
            className="p-1.5 text-[#888995] hover:text-[#272043] rounded-lg hover:bg-[#e8f7f4] transition-colors shrink-0 ml-1"
          >
            <LogOut className="w-4 h-4 stroke-[1.75]" />
          </button>
        </div>
      </div>
    </aside>
  );
};
