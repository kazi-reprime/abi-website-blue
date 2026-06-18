#!/usr/bin/env python3
"""ABI 'blue' static-site generator (in-repo, reproducible).

Reassembles every root *.html page from:
  - shared chrome:  src/chrome/prefix.html (announce+header+menu+phones)
                    src/chrome/suffix.html (footer+sticky+scripts)
  - per page:       src/pages/<name>.head.html   (<head> inner)
                    src/pages/<name>.body.html   (page content)
                    src/pages/<name>.json        ({"standalone": bool})

Standalone pages store their full <body> inner and skip the shared chrome.
Run:  python3 src/build.py
"""
import json, pathlib

REPO   = pathlib.Path(__file__).resolve().parent.parent
SRC    = SRC = pathlib.Path(__file__).resolve().parent
CHROME = SRC / "chrome"
PAGES  = SRC / "pages"

PREFIX = (CHROME / "prefix.html").read_text(encoding="utf-8")
SUFFIX = (CHROME / "suffix.html").read_text(encoding="utf-8")

def render(name):
    head = (PAGES / f"{name}.head.html").read_text(encoding="utf-8")
    body = (PAGES / f"{name}.body.html").read_text(encoding="utf-8")
    meta = json.loads((PAGES / f"{name}.json").read_text(encoding="utf-8"))
    inner = body if meta.get("standalone") else f"{PREFIX}\n{body}\n{SUFFIX}"
    lang = meta.get("lang", "en")
    return (
        f'<!DOCTYPE html>\n<html lang="{lang}">\n<head>\n'
        f"{head}\n</head>\n<body>\n{inner}\n</body>\n</html>\n"
    )

def main():
    names = sorted(p.name[:-len(".body.html")] for p in PAGES.glob("*.body.html"))
    for name in names:
        (REPO / f"{name}.html").write_text(render(name), encoding="utf-8")
    print(f"built {len(names)} pages -> repo root")

if __name__ == "__main__":
    main()
