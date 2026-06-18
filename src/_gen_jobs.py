#!/usr/bin/env python3
"""Generate ABI 'blue' job-opportunities listings from committed sample data.

Reads src/data/jobs_sample.json (a curated, varied sample of REAL partner-shop
openings — multiple shops across NY-area locations) and rebuilds
src/pages/job-opportunities.body.html with the hero + real listing cards +
placement-office CTA. No salary shown (source has none).
Run:  python3 src/_gen_jobs.py   (then python3 src/build.py)
"""
import json, html, pathlib

REPO  = pathlib.Path(__file__).resolve().parent.parent
PAGES = REPO / "src" / "pages"
DATA  = REPO / "src" / "data" / "jobs_sample.json"

def esc(s):
    return html.escape(s or "", quote=True)

jobs = json.load(open(DATA, encoding="utf-8"))

def card(j):
    apply_url = j.get("apply_url") or ""
    if apply_url:
        cta = (f'<a href="{esc(apply_url)}" target="_blank" rel="noopener" '
               f'class="cta-out" style="margin-top:10px">Apply &rarr;</a>')
    else:
        cta = ('<a href="contact.html" class="cta-out" style="margin-top:10px">'
               'Apply Through ABI &rarr;</a>')
    return (
        '<div class="info">'
        f'<h3>{esc(j.get("title") or "Barber")}</h3>'
        f'<p style="color:#1252A3;font-weight:800;margin:2px 0">{esc(j.get("company"))} &middot; {esc(j.get("location"))}</p>'
        f'<p>{esc(j.get("desc"))}</p>'
        f'{cta}</div>'
    )

cards = "".join(card(j) for j in jobs)

body = (
    "<section class=\"page-hero\" style=\"background:linear-gradient(rgba(7,25,46,.72),"
    "rgba(9,28,55,.9)),url('assets/img/pics/abi-students-011.jpg') center/cover\">"
    "<div class=\"crumb\"><a href=\"jobs.html\">Job Placement</a> &rsaquo; Opportunities</div>"
    "<h1>Barber Job Opportunities</h1>"
    "<p>Openings at partner barbershops across the New York area actively hiring ABI graduates. "
    "Apply through our placement office — it's free for graduates.</p>"
    "<div class=\"pbtns\"><a href=\"contact.html\" class=\"cta\" style=\"margin-top:0;flex:1\">Apply Now &rarr;</a>"
    "<a href=\"shop-registration.html\" class=\"cta-bd\" style=\"flex:1\">Own a shop? Post a job</a></div></section>"
    "<section class=\"sec sw\"><div class=\"slbl\">Now Hiring</div><div class=\"stit\">Open Positions</div>"
    f"<div class=\"sdesc\">A sample of {len(jobs)} barbershops across the NY area currently hiring licensed barbers. "
    "New graduates are encouraged to apply — our placement team helps with resume, portfolio and interview prep.</div>"
    f"{cards}"
    "<a href=\"contact.html\" class=\"cta\">Talk to the Placement Office &rarr;</a></section>"
)
(PAGES / "job-opportunities.body.html").write_text(body, encoding="utf-8")
print(f"blue job-opportunities: {len(jobs)} real listings")
