# Changelog — American Barber Institute (Blue)

All notable changes to this site are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/). Versions stay in
the **0.x** range throughout the upgrade cycle; the move to **1.0.0** happens only
when the client approves the official production release.

## [Unreleased]
_Work in progress toward 0.2.0._

## [0.1.0] — 2026-06-18
Baseline for the production upgrade cycle — the full current site, handover-ready.

- **Architecture:** zero-dependency static HTML rebuilt from version-controlled
  sources by an in-repo Python generator (`src/build.py`, sources under `src/`);
  Vercel serves the built files directly.
- **Content:** 32 pages (English + Spanish) — home, courses
  (500-hour Master, Bronx, 200-hour fundamentals, SMP, 50-hour refresher,
  3-hour contagious-disease), how-to-get-started, schedule, tuition, instructors,
  jobs / job-opportunities, gallery, FAQs, contact, veterans, ACCESS-VR, partners,
  resources, virtual tour, and account stubs (login/register/shop-registration).
- **Mobile:** mobile-first phone-frame layout with `viewport-fit=cover`,
  iOS safe-area insets, and full `prefers-reduced-motion` support.
- **Cleanup at baseline:** removed superseded `src/legacy/` generators (active
  generator documented in `src/README.md`).
