# Particle Physics Lesson 1 Reviewer Prototype
## The Nuclear Atom and Alpha-Particle Scattering (`9702_t11_cm01_l01`)

This prototype pairs each verified visual page with a short, page-specific teacher explanation for Cambridge AS Physics (9702) Topic 11.

### Architecture
- **Right Panel:** Displays the 8 verified visual lesson pages (1024 × 1536 standalone PNGs) released on 2026-09-01.
- **Left Panel:** Gives only the extra explanation needed for the current page: simple teacher language, a definition or formula when useful, compact tables, small visual cues, and one check.
- The left panel stays inside the Cambridge lesson boundary and does not duplicate the visual page or introduce extension physics.

### Quick Start
Run the local server:
```bash
python3 server.py --port 8766
```
Then open:
[http://localhost:8766](http://localhost:8766)

### Navigation & Shortcuts
- Click tabs **P01** through **P08** or use numeric keys `1`–`8` to jump directly to any page.
- Use `←` / `→` arrow keys or `P` / `N` to step forward/backward.
- Press `Z` or click the image to open the full-resolution inspector modal.
