# Pre-Change Git State — ABI Blue site

Recorded: 2026-06-18 (UTC), before any upgrade implementation.

| Field | Value |
|---|---|
| Repo path | `/Users/mkazi/Documents/Claude/Projects/ABI 2/site` |
| GitHub | `kazi-reprime/abi-barber-institute` |
| Default branch | `main` |
| Upgrade branch | `upgrade/abi-blue-mobile-content` |
| Baseline commit | `fe7f5d5 (baseline incl. 68 preserved edits)` |
| Vercel project | `site` |
| Git author | kazi-reprime <kazi@reprime.com> |
| Working tree at start | preserved (see notes) |

## Notes
Local `master` had diverged from `origin/main` (v15). Per user decision, local work committed to the upgrade branch; `main` left intact. PAT scrubbed from remote URL — recommend rotating the token.

## Safety rules honored
- Branched off baseline; `main` is not modified.
- No force-push, no reset, no discarded work.
- Secrets are not committed; `.git/config` token scrubbed where present.
- No merge to `main` will occur without explicit user approval.

## Scraped source collection
- Public scrape (85 pages, EN+ES): `/Users/mkazi/website-source-collection/abi-app-123.vercel.app/`
- Authenticated backend data (agent token): `/Users/mkazi/website-source-collection/abi-app-123.vercel.app/authenticated/`
  (courses, jobs(373), gallery_items(75), blog_posts(8), profiles, shop_registrations)
