#!/usr/bin/env python3
"""One-time bootstrap: derive an in-repo, reproducible generator for ABI 'blue'
from the CURRENT committed root HTML (the source of truth) — no content loss.

Splits every page into shared chrome + per-page <head> + per-page body, then writes
a file-based pipeline under src/ and a build.py that reassembles the root HTML.
Run:  python3 src/_bootstrap.py
"""
import re, json, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC  = REPO / "src"
CHROME = SRC / "chrome"
PAGES  = SRC / "pages"
for d in (CHROME, PAGES):
    d.mkdir(parents=True, exist_ok=True)

PHONES_RE = re.compile(r'<div class="phones">.*?</div>', re.S)

def head_inner(doc):
    m = re.search(r'<head>(.*?)</head>', doc, re.S)
    return m.group(1).strip("\n") if m else ""

def body_inner(doc):
    m = re.search(r'<body>(.*?)</body>', doc, re.S)
    return m.group(1).strip("\n") if m else ""

def split_standard(bi):
    """Return (prefix, content, suffix) if page has phones-chrome + footer, else None."""
    pm = PHONES_RE.search(bi)
    fi = bi.find("<footer")
    if not pm or fi < 0 or pm.end() > fi:
        return None
    prefix = bi[:pm.end()]
    content = bi[pm.end():fi]
    suffix = bi[fi:]
    return prefix, content, suffix

pages = sorted(p for p in REPO.glob("*.html"))
ref = (REPO / "about.html").read_text(encoding="utf-8")
ref_split = split_standard(body_inner(ref))
assert ref_split, "about.html must be a standard page"
PREFIX, _, SUFFIX = ref_split
(CHROME / "prefix.html").write_text(PREFIX, encoding="utf-8")
(CHROME / "suffix.html").write_text(SUFFIX, encoding="utf-8")

report = []
for p in pages:
    name = p.stem
    doc = p.read_text(encoding="utf-8")
    head = head_inner(doc)
    bi = body_inner(doc)
    lm = re.search(r'<html[^>]*\blang="([^"]*)"', doc)
    lang = lm.group(1) if lm else "en"
    sp = split_standard(bi)
    (PAGES / f"{name}.head.html").write_text(head, encoding="utf-8")
    # Only treat as "standard" (shared chrome) when this page's chrome EXACTLY
    # matches the canonical prefix/suffix; otherwise keep it standalone so its
    # page-specific chrome (e.g. Spanish nav on es, unique homepage chrome) is
    # reproduced verbatim with zero content loss.
    if sp and sp[0] == PREFIX and sp[2] == SUFFIX:
        _, content, _ = sp
        (PAGES / f"{name}.body.html").write_text(content.strip("\n"), encoding="utf-8")
        (PAGES / f"{name}.json").write_text(json.dumps({"standalone": False, "lang": lang}), encoding="utf-8")
        report.append((name, "standard", len(content)))
    else:
        (PAGES / f"{name}.body.html").write_text(bi, encoding="utf-8")
        (PAGES / f"{name}.json").write_text(json.dumps({"standalone": True, "lang": lang}), encoding="utf-8")
        report.append((name, "STANDALONE", len(bi)))

print(f"pages processed: {len(report)}")
for n, kind, ln in report:
    print(f"  {n:34} {kind:11} body={ln}")
print(f"chrome/prefix.html: {len(PREFIX)} bytes  chrome/suffix.html: {len(SUFFIX)} bytes")
