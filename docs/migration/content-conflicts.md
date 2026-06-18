# Content Conflicts Log — ABI Blue

Records content discrepancies found during the dual-site upgrade, and how each
was resolved. Per project rule: **enhance but never distort or fabricate content;
record conflicts here rather than silently "fixing" them.**

---

## CONFLICT-001 — 500-Hour Master Barber Program price ($4,600 vs $5,600)

**Status:** ✅ RESOLVED — not an actual conflict (confirmed valid plan variants)
**Date investigated:** 2026-06-18
**Severity:** was flagged HIGH (pricing), downgraded to NONE after context review

### What looked wrong
A raw text sweep counted both `$4,600` (19 mentions) and `$5,600` (8 mentions) for
the 500-hour program on the same site, which initially read as a self-contradiction.

### What is actually true
The two figures are **two legitimate schedule plans of the same program**, not two
prices for one thing:

| Plan | Schedule | Price | Terms |
|---|---|---|---|
| Plan A — Morning | Mon–Fri 8:00 AM–2:00 PM | **$5,600** | $500 down (incl. $100 reg.) + 17×$300 |
| Plan B — Afternoon (MOST POPULAR) | Mon–Fri 2:00 PM–8:00 PM | **$4,600** | $500 down + 16×$250 + final $100 |
| Plan C — Weekend | Sat & Sun 9:00 AM–7:00 PM | (weekend plan) | weekly plan |

This is stated explicitly and consistently across the site:
- `src/pages/index.body.html` — "Flexible Payment Plans" section, one labeled card per plan.
- `src/pages/faqs.body.html` — "The 500 Hour program starts at $4,600 (afternoon/weekend) or $5,600 (morning)."

The backend `courses` table (scrape source-of-truth) lists **$5,600** — i.e. the
morning-plan price. It is not in conflict; it simply records one of the two plans.

### Resolution
**No content change required.** Both prices are accurate and already presented as
plan-dependent everywhere they appear. Confirmed correct with the site owner
(2026-06-18): keep both, present clearly. Already satisfied by existing structure.

### Other figures verified consistent (no conflict)
- 50-Hour Refresher: **$1,500**
- Contagious-Disease (3-hour): **$100**
- Registration / down payment: **$500** (includes $100 registration)
