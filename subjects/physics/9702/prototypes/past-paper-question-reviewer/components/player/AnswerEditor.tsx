'use client';

import { useRef, useState } from 'react';
import {
  Check,
  Minus,
  X,
  HelpCircle,
  Lightbulb,
  BookOpen,
  ChevronDown,
  Sparkles,
  FlaskConical,
} from 'lucide-react';
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
} from '@/components/ui/dropdown-menu';
import { MathText } from './MathText';

export type SelfMark = 'Correct' | 'Partial' | 'Incorrect' | 'Confused';

export const markOptions: SelfMark[] = [
  'Correct',
  'Partial',
  'Incorrect',
  'Confused',
];

export const markIcons = {
  Correct: Check,
  Partial: Minus,
  Incorrect: X,
  Confused: HelpCircle,
};

export function MarkMenu({
  value,
  onChange,
}: {
  value?: SelfMark;
  onChange: (v?: SelfMark) => void;
}) {
  const Icon = value ? markIcons[value] : Check;
  return (
    <DropdownMenu>
      <DropdownMenuTrigger
        className={`selfmark ${value ? value.toLowerCase() : ''}`}
        type="button"
      >
        <Icon size={14} />
        <span>{value || 'Mark yourself'}</span>
        <ChevronDown size={12} />
      </DropdownMenuTrigger>
      <DropdownMenuContent className="mark-menu">
        {markOptions.map((v) => {
          const I = markIcons[v];
          return (
            <DropdownMenuItem key={v} onClick={() => onChange(v)}>
              <span className={`status-dot ${v.toLowerCase()}`}>
                <I size={13} />
              </span>
              <span>{v}</span>
              {value === v && <Check className="ml-auto text-emerald-600" size={14} />}
            </DropdownMenuItem>
          );
        })}
        <DropdownMenuItem onClick={() => onChange(undefined)}>
          <span className="text-slate-500">Clear self-mark</span>
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}

const chemShortcuts = [
  { label: '→', code: ' \\rightarrow ' },
  { label: '⇌', code: ' \\rightleftharpoons ' },
  { label: 'ΔH', code: ' \\Delta H ' },
  { label: 'kJ mol⁻¹', code: '\\text{ kJ mol}^{-1}' },
  { label: 'mol dm⁻³', code: '\\text{ mol dm}^{-3}' },
  { label: '°C', code: '^{\\circ}\\text{C}' },
  { label: 'X₂', code: '_2' },
  { label: 'X₃', code: '_3' },
  { label: 'X₄', code: '_4' },
  { label: 'M⁺', code: '^{+}' },
  { label: 'M²⁺', code: '^{2+}' },
  { label: 'A⁻', code: '^{-}' },
  { label: 'A²⁻', code: '^{2-}' },
  { label: '(s)', code: '\\text{(s)}' },
  { label: '(l)', code: '\\text{(l)}' },
  { label: '(g)', code: '\\text{(g)}' },
  { label: '(aq)', code: '\\text{(aq)}' },
  { label: '×10ⁿ', code: ' \\times 10^{} ' },
  { label: 'a/b', code: '\\frac{}{}' },
];

interface AnswerEditorProps {
  id: string;
  value: string;
  onChange: (value: string) => void;
  onFocus?: () => void;
  onScheme?: () => void;
  onHints?: () => void;
  onWalkthrough?: () => void;
  marks?: number | null;
  answerPrompt?: string;
  unit?: string;
  selfMark?: SelfMark;
  onSelfMarkChange?: (mark?: SelfMark) => void;
}

export function AnswerEditor({
  id,
  value,
  onChange,
  onFocus,
  onScheme,
  onHints,
  onWalkthrough,
  marks,
  answerPrompt,
  unit,
  selfMark,
  onSelfMarkChange,
}: AnswerEditorProps) {
  const [expanded, setExpanded] = useState(false);
  const [showTools, setShowTools] = useState(false);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  function insertSymbol(symbol: string) {
    const el = inputRef.current;
    const start = el?.selectionStart ?? value.length;
    const end = el?.selectionEnd ?? start;
    const next = value.slice(0, start) + symbol + value.slice(end);
    onChange(next);
    requestAnimationFrame(() => {
      el?.focus();
      const pos = start + symbol.length;
      el?.setSelectionRange(pos, pos);
    });
  }

  const hasMath = value.includes('$') || value.includes('\\') || value.includes('^') || value.includes('_');

  return (
    <div className="editor-wrap mt-3">
      <div
        className={`editor ${expanded ? 'expanded' : ''} border border-slate-200 dark:border-slate-800 rounded-lg bg-white dark:bg-slate-900 transition-all focus-within:border-emerald-500 focus-within:ring-2 focus-within:ring-emerald-500/10`}
        onFocusCapture={() => {
          setExpanded(true);
          onFocus?.();
        }}
      >
        <textarea
          ref={inputRef}
          id={`answer-${id}`}
          aria-label="Answer and working"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder={
            answerPrompt
              ? `Write your working or final value for ${answerPrompt.replace(/\$|\\text\{|\}/g, '').trim()}...`
              : 'Write your answer or add your working...'
          }
          rows={expanded ? 4 : 2}
          className="w-full p-3.5 text-sm bg-transparent outline-none resize-vertical text-slate-800 dark:text-slate-100 placeholder:text-slate-400 leading-relaxed min-h-[58px]"
        />

        {/* Cambridge answer line if specified in OCR */}
        {(answerPrompt || unit) && (
          <div className="px-3.5 pb-2 text-xs text-slate-600 dark:text-slate-400 flex items-center justify-between border-t border-slate-100 dark:border-slate-800/60 pt-2 bg-slate-50/50 dark:bg-slate-850/40">
            <div className="font-medium italic text-slate-700 dark:text-slate-300">
              <MathText text={`${answerPrompt || 'Answer'}:`} />
            </div>
            {unit && (
              <div className="font-semibold text-slate-900 dark:text-slate-100">
                <MathText text={unit} />
              </div>
            )}
          </div>
        )}

        {/* Chemical symbol keypad */}
        {showTools && (
          <div className="math-keyboard border-t border-slate-100 dark:border-slate-800 p-2.5 bg-slate-50 dark:bg-slate-850 flex flex-wrap items-center gap-1.5 text-xs">
            <span className="text-slate-500 dark:text-slate-400 font-medium mr-1 flex items-center gap-1">
              <FlaskConical size={13} />
              Symbols:
            </span>
            {chemShortcuts.map((item) => (
              <button
                key={item.label}
                type="button"
                onClick={() => insertSymbol(item.code)}
                className="px-2 py-1 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:bg-emerald-50 hover:border-emerald-300 hover:text-emerald-700 text-slate-700 dark:text-slate-300 font-mono transition-colors cursor-pointer text-xs"
              >
                {item.label}
              </button>
            ))}
            <button
              type="button"
              onClick={() => setShowTools(false)}
              className="ml-auto text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 p-1 cursor-pointer"
              title="Close symbols"
            >
              <X size={14} />
            </button>
          </div>
        )}

        {/* Formula preview when math or chemical notation is typed */}
        {(showTools || hasMath) && value.trim() && (
          <div className="math-preview border-t border-slate-100 dark:border-slate-800 p-3 bg-slate-50/70 dark:bg-slate-850/60 text-xs">
            <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1">
              Formula Preview
            </span>
            <div className="text-slate-900 dark:text-slate-100 text-sm">
              <MathText text={value} />
            </div>
          </div>
        )}

        {/* Expandable toolbar */}
        {expanded && (
          <div className="editor-toolbar flex items-center justify-between px-3 py-2 border-t border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-850/30">
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => setShowTools(!showTools)}
                className={`text-xs px-2.5 py-1 rounded-md border transition-colors flex items-center gap-1.5 cursor-pointer ${
                  showTools
                    ? 'bg-emerald-100 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 border-emerald-300 dark:border-emerald-800 font-semibold'
                    : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:bg-slate-100'
                }`}
              >
                <FlaskConical size={13} />
                <span>Chemistry Symbols</span>
              </button>
            </div>

            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => {
                  setExpanded(false);
                  setShowTools(false);
                }}
                className="text-xs text-slate-500 hover:text-slate-800 dark:hover:text-slate-200 px-2 py-1 cursor-pointer"
              >
                Collapse
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Action shortcuts & Self-marking matching Mathematics 9709 */}
      <div className="part-footer flex items-center justify-between mt-2.5 pt-1 text-xs">
        <div className="flex items-center gap-3">
          {onScheme && marks !== null && marks !== undefined && marks > 0 && (
            <button
              type="button"
              onClick={onScheme}
              className="text-slate-500 hover:text-emerald-700 dark:hover:text-emerald-400 font-medium flex items-center gap-1 cursor-pointer transition-colors"
            >
              <BookOpen size={13} />
              <span>Mark scheme ({marks}m)</span>
            </button>
          )}
          {onHints && (
            <button
              type="button"
              onClick={onHints}
              className="text-slate-500 hover:text-emerald-700 dark:hover:text-emerald-400 font-medium flex items-center gap-1 cursor-pointer transition-colors"
            >
              <Lightbulb size={13} />
              <span>Hints</span>
            </button>
          )}
          {onWalkthrough && (
            <button
              type="button"
              onClick={onWalkthrough}
              className="text-slate-500 hover:text-emerald-700 dark:hover:text-emerald-400 font-medium flex items-center gap-1 cursor-pointer transition-colors"
            >
              <Sparkles size={13} />
              <span>Walkthrough</span>
            </button>
          )}
        </div>

        {onSelfMarkChange && (
          <MarkMenu value={selfMark} onChange={onSelfMarkChange} />
        )}
      </div>
    </div>
  );
}
