# Kognitiv Student Learning Prototype

A pixel-perfect UI/UX prototype matching the Kognitiv learning overview dashboard, built with React, TypeScript, and Tailwind CSS.

## Architecture

- **React + TypeScript + Vite**: Ultra-fast hot module reloading, modern component modularity.
- **Tailwind CSS**: Exact design tokens for colors, shadows, typography, and responsive layouts.
- **Lucide Icons**: Crisp SVG icons for navigation, subjects, streak, and metrics.
- **Custom Visualizations**:
  - `StudyConsistency.tsx`: 4-row activity matrix with exact 4-level color coding and legend.
  - `WeeklyActivity.tsx`: Pixel-precise bar chart with question volume and tooltips.
  - `StudyTimeTrend.tsx`: Smooth cubic bezier spline area chart with gradient fills and data nodes.
  - `SubjectProgress.tsx`: 3-tier progress bars for Maths, Physics, and Chemistry.
- **Multi-page Expandability**:
  - Full tab switching between `Dashboard`, `Study`, `Revision`, `Review`, and `Analytics`.
  - Ready for rapid development of secondary screens, question drill interfaces, and lesson modules.

## Getting Started

To run locally in development mode:
```bash
cd subjects/physics/9702/prototypes/kognitiv-dashboard
npm run dev
```

To build for production:
```bash
npm run build
npm run preview
```
