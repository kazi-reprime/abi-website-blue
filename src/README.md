# ABI Blue — in-repo static site generator

Zero-framework, zero-dependency Python generator. It rebuilds every root `*.html`
page from version-controlled sources. Vercel serves the generated root HTML directly
(no build step on Vercel).

## Build

```bash
python3 src/build.py      # regenerates all root *.html from src/
```

## Where things live

| Path | What |
|---|---|
| `src/chrome/prefix.html` | Shared chrome BEFORE page content — announcement bar, header, grouped nav menu, phone bar. |
| `src/chrome/suffix.html` | Shared chrome AFTER page content — footer, sticky mobile action bar, scripts. |
| `src/pages/<name>.body.html` | The page's body content (what changes per page). |
| `src/pages/<name>.head.html` | The page's `<head>` inner markup (title, meta, OG, canonical). |
| `src/pages/<name>.json` | `{ "standalone": bool, "lang": "en"\|"es" }`. |
| `src/_bootstrap.py` | One-time script that derived this pipeline from the deployed HTML (provenance; not needed for normal builds). |

## How a page is assembled

- **Standard pages** (most): `<head>` + `chrome/prefix` + `body` + `chrome/suffix`.
  Edit the shared chrome once (`src/chrome/*`) and every standard page updates.
- **Standalone pages** (`index`, and any page with intentionally unique chrome):
  the `.body.html` holds the FULL `<body>` inner markup and the shared chrome is
  skipped. Set `"standalone": true`.
- `<html lang>` comes from each page's `"lang"` (Spanish pages use `es`).

## Editing workflow

1. Edit content in `src/pages/<name>.body.html` (and `.head.html` for SEO/meta).
2. Edit site-wide chrome in `src/chrome/prefix.html` / `suffix.html`.
3. Run `python3 src/build.py`.
4. Commit the changed `src/` files **and** the regenerated root `*.html`.

This pipeline was verified to reproduce all 32 deployed pages with zero content loss.
