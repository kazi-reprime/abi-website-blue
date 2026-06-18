# Content Audit — ABI Blue (toward v0.2.0)

Verified comparison of the live site's content against the authoritative scrape
(`~/website-source-collection/abi-app-123.vercel.app/`, incl. `authenticated/`
backend dumps). All claims below were checked against actual files — not assumed.

_Date: 2026-06-18 · Baseline: v0.1.0_

## What's already solid (no action needed)
- **Instructors:** strong — 10 detailed bios + photos (`src/pages/instructors.body.html`),
  exceeds the scrape's profile data.
- **Programs/pricing:** 500hr ($5,600 morning / $4,600 afternoon-weekend / weekend),
  50hr refresher ($1,500), 3hr contagious ($100) present and consistent; FAQ explicit.

## Gaps to close for 0.2.0 (verified, prioritized — bigger than black's)
1. **Blog has no post content.** `src/pages/blog.body.html` is a landing page with
   card links but **0 individual post bodies**; the scrape has **8** posts. Action:
   add the 8 post pages (port content from scrape) so links don't dead-end. _Highest
   client-handover risk._
2. **Spanish is a single stub.** Only `src/pages/es.body.html` exists. Scrape has
   `title_es`/`description_es` populated. Action: build real ES course/key pages.
3. **Gallery depth.** ~10 images vs **75** `gallery_items` available. Action: expand
   to ~30–40 curated images with lazy-loading + lightbox.
4. **Job listings not shown.** Scrape has **373** jobs; site shows overview only.
   Action: curated sample (15–25) + "placement office" framing.
5. **Account stubs** (`login`/`register`/`shop-registration`): UI shells, no backend
   (expected for static demo). Action: ensure they read as "coming soon"/route to a
   working contact path so a client demo doesn't hit dead ends.
6. **Bronx campus detail** thin in `contact` — add address (121 Westchester Square, Bronx).

## Accuracy items to CONFIRM WITH OWNER (do not change unilaterally)
- **200-hour Fundamentals** ($3,600) and **SMP 50hr** ($3,500) appear on the site but
  are **not** in the backend `courses` table (only 500hr / 50hr / 3hr are). Confirm
  these are live offerings before relying on them.
- **Contagious-disease price:** site shows **$100** = backend course `price` field
  (correct). Backend also has a $50 schedule-plan `total` — confirm it's not current.
- (See `docs/migration/content-conflicts.md` for the resolved 500hr price item.)

## Notes
- This is a **static** site (in-repo Python generator, `src/`), so large backend
  tables (jobs/gallery) are curated/baked at build time, not live-queried.
