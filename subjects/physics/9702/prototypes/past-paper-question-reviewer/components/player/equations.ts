/** Presentation-only line breaks. Retains every character of the source equation. */
export function equationLines(source: string): string[] {
  if (/\\begin\{(?:aligned|gathered|array)\}/.test(source)) return [source];
  if (source.length < 85) return [source];
  const lines: string[] = [];
  let delimiters = 0;
  let depth = 0,
    start = 0;
  for (let i = 0; i < source.length; i++) {
    if (source.startsWith('\\left', i)) delimiters++;
    if (source.startsWith('\\right', i)) delimiters--;
    if (source[i] === '{' && source[i - 1] !== '\\') depth++;
    if (source[i] === '}' && source[i - 1] !== '\\') depth--;
    if (depth !== 0 || delimiters !== 0 || i - start < 18) continue;
    const relation =
      source[i] === '=' ||
      source.startsWith('\\implies', i) ||
      source.startsWith('\\quad', i);
    if (relation) {
      lines.push(source.slice(start, i));
      start = i;
    }
  }
  lines.push(source.slice(start));
  return lines;
}
