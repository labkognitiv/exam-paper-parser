'use client';

import React from 'react';
import katex from 'katex';
import { equationLines } from './equations';

function renderMathChunks(text: string, keyPrefix: string = 'm') {
  const cleanText = (text || '').replace(/\{\{figure:[^}]+\}\}\s*/g, '');
  const chunks = cleanText.split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+\$)/g);

  return chunks.map((chunk, i) => {
    if (!chunk.startsWith('$')) {
      const parts = chunk.split(/(\*\*[^*]+\*\*)/g);
      return (
        <span key={`${keyPrefix}-${i}`}>
          {parts.map((part, j) => {
            if (part.startsWith('**') && part.endsWith('**') && part.length >= 4) {
              return <strong key={`${keyPrefix}-${i}-${j}`}>{part.slice(2, -2)}</strong>;
            }
            return part;
          })}
        </span>
      );
    }
    const display = chunk.startsWith('$$');
    const source = chunk.slice(display ? 2 : 1, display ? -2 : -1);
    const lines = display ? equationLines(source) : [source];
    return (
      <span key={`${keyPrefix}-${i}`} className={display ? 'display-math' : undefined}>
        {lines.map((line, n) => (
          <span
            key={n}
            className={display ? 'equation-line' : undefined}
            dangerouslySetInnerHTML={{
              __html: katex.renderToString(line, {
                displayMode: display,
                throwOnError: false,
                trust: false,
                strict: 'ignore',
                output: 'htmlAndMathml',
              }),
            }}
          />
        ))}
      </span>
    );
  });
}

function splitTableRow(line: string): string[] {
  const trimmed = line.trim();
  const inner = trimmed.startsWith('|') && trimmed.endsWith('|')
    ? trimmed.slice(1, -1)
    : trimmed;

  const cells: string[] = [];
  let current = '';
  let inInlineMath = false;
  let inDisplayMath = false;

  for (let i = 0; i < inner.length; i++) {
    const char = inner[i];
    const prevChar = i > 0 ? inner[i - 1] : '';

    if (char === '$' && prevChar !== '\\') {
      if (inner[i + 1] === '$') {
        inDisplayMath = !inDisplayMath;
        current += '$$';
        i++;
        continue;
      } else if (!inDisplayMath) {
        inInlineMath = !inInlineMath;
      }
    }

    if (char === '|' && !inInlineMath && !inDisplayMath && prevChar !== '\\') {
      cells.push(current.trim());
      current = '';
    } else {
      current += char;
    }
  }
  cells.push(current.trim());
  return cells;
}

function renderMarkdownTable(tableLines: string[], tableIndex: number) {
  const rawRows = tableLines
    .map((line) => line.trim())
    .filter((line) => line.startsWith('|') && line.endsWith('|'))
    .map((line) => splitTableRow(line));

  if (rawRows.length === 0) return null;

  // Detect separator row like |---|:---|
  const hasSeparator = rawRows.length > 1 && rawRows[1].every((c) => /^[:\s-]+$/.test(c));
  const headerRow = rawRows[0];
  const bodyRows = hasSeparator ? rawRows.slice(2) : rawRows.slice(1);

  return (
    <div key={`tbl-${tableIndex}`} className="overflow-x-auto my-3.5 max-w-full">
      <table className="min-w-[300px] border-collapse border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 rounded-lg text-sm shadow-xs">
        <thead>
          <tr className="bg-slate-100/90 dark:bg-slate-800/90 border-b border-slate-300 dark:border-slate-700">
            {headerRow.map((headerCell, cIdx) => (
              <th
                key={cIdx}
                className="px-4 py-2.5 text-left font-semibold text-slate-800 dark:text-slate-100 border-r border-slate-300 dark:border-slate-700 last:border-r-0"
              >
                {renderMathChunks(headerCell, `th-${tableIndex}-${cIdx}`)}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
          {bodyRows.map((row, rIdx) => (
            <tr key={rIdx} className="hover:bg-slate-50/70 dark:hover:bg-slate-850/40 transition-colors">
              {row.map((cell, cIdx) => (
                <td
                  key={cIdx}
                  className="px-4 py-2 text-slate-700 dark:text-slate-300 border-r border-slate-200 dark:border-slate-800 last:border-r-0 min-w-[75px]"
                >
                  {cell.length > 0 ? (
                    renderMathChunks(cell, `td-${tableIndex}-${rIdx}-${cIdx}`)
                  ) : (
                    <span className="inline-block w-12 h-5 border-b border-dashed border-slate-400/80 dark:border-slate-600" />
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function normalizeInlineTables(rawText: string): string {
  if (!rawText || !rawText.includes('|') || !/Table\s+\d/i.test(rawText)) {
    return rawText;
  }
  if (/\n\s*\|.*\|\s*\n?/.test(rawText)) {
    return rawText;
  }

  const tableMatch = rawText.match(/(Table\s+\d+(?:\.\d+)?)\s*\|\s*([\s\S]+)/);
  if (!tableMatch) return rawText;

  const intro = rawText.slice(0, tableMatch.index).trim();
  const title = tableMatch[1].trim();
  const tableContent = tableMatch[2].trim();

  const normalized = tableContent.replace(/\s*\|\s*/g, '|');
  const rowSplit = normalized.replace(/\|{3,}/g, '\n| |').replace(/\|{2}/g, '\n|');
  const rawRows = rowSplit.split('\n').map((r) => r.trim()).filter(Boolean);

  const cleanRows: string[][] = [];
  let maxCols = 0;
  for (const raw of rawRows) {
    const line = raw.startsWith('|') ? raw : `|${raw}`;
    const fullLine = line.endsWith('|') ? line : `${line}|`;
    const cells = fullLine.split('|').slice(1, -1).map((c) => c.trim());
    if (cells.length > 0) {
      maxCols = Math.max(maxCols, cells.length);
      cleanRows.push(cells);
    }
  }

  if (cleanRows.length === 0) return rawText;

  const header = cleanRows[0];
  while (header.length < maxCols) header.push('');
  const headerStr = `| ${header.map((c) => c || ' ').join(' | ')} |`;
  const sepStr = `| ${Array(maxCols).fill('---').join(' | ')} |`;

  const bodyStrs: string[] = [];
  for (const row of cleanRows.slice(1)) {
    while (row.length < maxCols) row.push('');
    bodyStrs.push(`| ${row.join(' | ')} |`);
  }

  const mdTable = `\n\n**${title}**\n\n${headerStr}\n${sepStr}\n${bodyStrs.join('\n')}\n\n`;
  return `${intro}\n${mdTable}`.trim();
}

export function MathText({
  text,
  className = '',
}: {
  text: string;
  className?: string;
}) {
  if (!text) return null;

  const processedText = normalizeInlineTables(text);

  // Check if text contains markdown table syntax
  if (processedText.includes('|') && /\n\s*\|.*\|\s*\n?/.test(processedText)) {
    const lines = processedText.split('\n');
    const blocks: Array<{ type: 'table' | 'text'; lines: string[] }> = [];
    let currentBlock: { type: 'table' | 'text'; lines: string[] } | null = null;

    for (const line of lines) {
      const isTableLine = /^\s*\|.*\|\s*$/.test(line);
      const targetType = isTableLine ? 'table' : 'text';

      if (!currentBlock || currentBlock.type !== targetType) {
        currentBlock = { type: targetType, lines: [line] };
        blocks.push(currentBlock);
      } else {
        currentBlock.lines.push(line);
      }
    }

    return (
      <div className={`math-copy ${className} space-y-2`}>
        {blocks.map((block, bIdx) => {
          if (block.type === 'table') {
            return renderMarkdownTable(block.lines, bIdx);
          }
          const blockText = block.lines.join('\n').trim();
          if (!blockText) return null;
          return (
            <p key={`p-${bIdx}`} className="leading-relaxed">
              {renderMathChunks(blockText, `blk-${bIdx}`)}
            </p>
          );
        })}
      </div>
    );
  }

  // Collapse 3 or more consecutive newlines down to 2
  const cleanedText = processedText.replace(/\n{3,}/g, '\n\n').trim();
  const paragraphs = cleanedText.split(/\n\n+/);

  if (paragraphs.length > 1) {
    return (
      <div className={`math-copy ${className} space-y-1.5`}>
        {paragraphs.map((para, pIdx) => {
          const trimmed = para.trim();
          if (!trimmed) return null;
          return (
            <p key={`p-${pIdx}`} className="leading-relaxed">
              {renderMathChunks(trimmed, `p-${pIdx}`)}
            </p>
          );
        })}
      </div>
    );
  }

  // Standard single-paragraph rendering
  return (
    <span className={`math-copy ${className}`}>
      {renderMathChunks(cleanedText)}
    </span>
  );
}
