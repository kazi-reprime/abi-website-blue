#!/usr/bin/env python3
"""Generate ABI 'blue' blog post pages from committed blog data.

Reads src/data/blog_posts.json (faithful copy of the site's real blog content)
and emits, for each published post:
  - src/pages/<slug>.body.html   (hero + article, blue chrome conventions)
  - src/pages/<slug>.head.html   (title/meta/OG/canonical + BlogPosting schema)
  - src/pages/<slug>.json        ({"standalone": false, "lang": "en"})
Then rebuilds src/pages/blog.body.html with real cards linking to each post,
and injects a small .post typography block into assets/css/abi-add.css (idempotent).

Content is ported verbatim from the source — nothing is fabricated or summarised.
Run:  python3 src/_gen_blog.py   (then python3 src/build.py)
"""
import json, html, os, pathlib
from datetime import datetime

REPO  = pathlib.Path(__file__).resolve().parent.parent
PAGES = REPO / "src" / "pages"
PICS  = REPO / "assets" / "img" / "pics"
CSS   = REPO / "assets" / "css" / "abi-add.css"
DATA  = REPO / "src" / "data" / "blog_posts.json"
SITE  = "https://www.abi.edu"
FALLBACK_COVER = "barbershop-full-shop.jpeg"

def esc(s):
    return html.escape(s or "", quote=True)

def pick_cover(r):
    base = os.path.basename((r.get("cover_image") or "").split("?")[0])
    return base if base and (PICS / base).exists() else FALLBACK_COVER

def fmt_date(s):
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).strftime("%B %-d, %Y")
    except Exception:
        return ""

posts = json.load(open(DATA, encoding="utf-8"))
posts = [r for r in posts if r.get("is_published")]
posts.sort(key=lambda r: r.get("published_at", ""), reverse=True)

cards = []
for r in posts:
    slug   = r["slug"]
    title  = r["title"]
    excerpt = r.get("excerpt") or ""
    content = (r.get("content") or "").replace("\r", "").strip()
    cover  = pick_cover(r)
    date   = fmt_date(r.get("published_at", ""))
    desc   = excerpt or title

    body = (
        f"<section class=\"page-hero\" style=\"background:linear-gradient(rgba(7,25,46,.72),"
        f"rgba(9,28,55,.9)),url('assets/img/pics/{cover}') center/cover\">"
        f"<div class=\"crumb\"><a href='index.html'>Home</a> &rsaquo; <a href='blog.html'>Blog</a></div>"
        f"<h1>{esc(title)}</h1><p>{esc(excerpt)}</p><p class=\"post-meta\">{date}</p></section>\n"
        f"<section class=\"sec sw\"><article class=\"post\">\n{content}\n</article>"
        f"<a href=\"contact.html\" class=\"cta\">Start Your Barber Career &rarr;</a>"
        f"<p class=\"post-back\"><a href=\"blog.html\">&larr; Back to all articles</a></p></section>"
    )
    (PAGES / f"{slug}.body.html").write_text(body, encoding="utf-8")

    schema = json.dumps({
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": title, "description": desc, "datePublished": r.get("published_at"),
        "image": f"{SITE}/assets/img/pics/{cover}",
        "publisher": {"@type": "Organization", "name": "American Barber Institute"},
    })
    head = (
        "<meta charset=\"UTF-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        f"<meta name=\"description\" content=\"{esc(desc)}\">\n"
        f"<title>{esc(title)} | American Barber Institute</title>\n"
        "<link rel=\"stylesheet\" href=\"assets/css/abi.css?v=15\">\n"
        "<link rel=\"stylesheet\" href=\"assets/css/abi-add.css?v=15\">\n"
        "<script>try{document.documentElement.dataset.theme=localStorage.getItem('abi-theme')||'classic'}catch(e){}</script>\n"
        f"<link rel=\"canonical\" href=\"{SITE}/{slug}\"><meta name=\"robots\" content=\"index,follow\">\n"
        "<meta property=\"og:type\" content=\"article\"><meta property=\"og:site_name\" content=\"American Barber Institute\">\n"
        f"<meta property=\"og:title\" content=\"{esc(title)}\"><meta property=\"og:description\" content=\"{esc(desc)}\">\n"
        f"<meta property=\"og:url\" content=\"{SITE}/{slug}\"><meta property=\"og:image\" content=\"{SITE}/assets/img/pics/{cover}\">\n"
        "<meta name=\"twitter:card\" content=\"summary_large_image\">\n"
        "<script defer src=\"assets/js/analytics.js?v=15\"></script>\n"
        f"<script type=\"application/ld+json\">{schema}</script>"
    )
    (PAGES / f"{slug}.head.html").write_text(head, encoding="utf-8")
    (PAGES / f"{slug}.json").write_text(json.dumps({"standalone": False, "lang": "en"}), encoding="utf-8")

    cards.append(
        f"<a class=\"lkcard\" href=\"{slug}.html\"><div class=\"lkt\">{esc(title)}</div>"
        f"<div class=\"lkd\">{esc(excerpt)}</div></a>"
    )

blog = (
    "<section class=\"page-hero\" style=\"background:linear-gradient(rgba(7,25,46,.72),"
    "rgba(9,28,55,.9)),url('assets/img/pics/abi-students-007.jpg') center/cover\">"
    "<div class=\"crumb\"><a href='index.html'>Home</a> &rsaquo; Blog</div><h1>The ABI Blog</h1>"
    "<p>Careers, licensing, financial aid, and stories from NYC's only dedicated barber school.</p></section>"
    "<section class=\"sec sw\"><div class=\"slbl\">Latest</div><div class=\"stit\">News &amp; Tips</div>"
    + "".join(cards) +
    "<a href=\"contact.html\" class=\"cta\">Apply Now &rarr;</a></section>"
)
(PAGES / "blog.body.html").write_text(blog, encoding="utf-8")

# idempotent CSS injection for article typography
css = CSS.read_text(encoding="utf-8")
if ".post{" not in css:
    css += (
        "\n/* v17 — blog post article typography */\n"
        ".post{max-width:680px;margin:0 auto;line-height:1.7}\n"
        ".post p{margin:0 0 1.1em}\n"
        ".post h2,.post h3{margin:1.5em 0 .5em;line-height:1.25}\n"
        ".post ul,.post ol{margin:0 0 1.1em 1.2em}\n"
        ".post li{margin:.3em 0}\n"
        ".post-meta{opacity:.7;font-size:.92rem;margin-top:.4rem}\n"
        ".post-back{margin-top:1.4rem;font-weight:600}\n"
    )
    CSS.write_text(css, encoding="utf-8")
    print("injected .post CSS into abi-add.css")
else:
    print(".post CSS already present")

print(f"generated {len(posts)} blog posts + rebuilt blog index")
