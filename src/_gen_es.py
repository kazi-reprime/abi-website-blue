#!/usr/bin/env python3
"""Generate ABI 'blue' Spanish (ES) course pages from committed course data.

Reads src/data/courses.json and emits faithful Spanish pages using ONLY the
source's own ES text (title_es / description_es) plus language-neutral facts
(price, duration). UI labels are standard interface localisation, not content.

Emits, for each ES-enabled course:
  - src/pages/es-course-<key>.{body,head,json}
Plus an ES overview:
  - src/pages/es-courses.{body,head,json}
And appends a discoverable "Programas" section to es.body.html (idempotent).

Run:  python3 src/_gen_es.py   (then python3 src/build.py)
"""
import json, html, pathlib

REPO  = pathlib.Path(__file__).resolve().parent.parent
PAGES = REPO / "src" / "pages"
DATA  = REPO / "src" / "data" / "courses.json"
SITE  = "https://www.abi.edu"

# slug -> (page key, cover image in assets/img/pics, hours label)
MAP = {
    "500-hour-master-barber":     ("es-course-500",   "program-500.jpg", "500"),
    "50-hour-barber-refresher":   ("es-course-50",    "program-50.jpg",  "50"),
    "3-hour-contagious-diseases": ("es-course-3hr",   "program-3hr.jpg", "3"),
    "540-hour-master-barber-bronx": ("es-course-bronx", "banner-slide1.jpg", "500"),
}

def esc(s):
    return html.escape(s or "", quote=True)

def money(p):
    try:
        return "$" + format(int(round(float(p))), ",")
    except Exception:
        return ""

def head(title, desc, slug):
    return (
        "<meta charset=\"UTF-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        f"<meta name=\"description\" content=\"{esc(desc)}\">\n"
        f"<title>{esc(title)} | American Barber Institute</title>\n"
        "<link rel=\"stylesheet\" href=\"assets/css/abi.css?v=15\">\n"
        "<link rel=\"stylesheet\" href=\"assets/css/abi-add.css?v=15\">\n"
        "<script>try{document.documentElement.dataset.theme=localStorage.getItem('abi-theme')||'classic'}catch(e){}</script>\n"
        f"<link rel=\"canonical\" href=\"{SITE}/{slug}\"><meta name=\"robots\" content=\"index,follow\">\n"
        f"<link rel=\"alternate\" hreflang=\"es\" href=\"{SITE}/{slug}\">\n"
        "<meta property=\"og:type\" content=\"website\"><meta property=\"og:site_name\" content=\"American Barber Institute\">\n"
        f"<meta property=\"og:title\" content=\"{esc(title)}\"><meta property=\"og:description\" content=\"{esc(desc)}\">\n"
        f"<meta property=\"og:url\" content=\"{SITE}/{slug}\">\n"
        "<meta name=\"twitter:card\" content=\"summary_large_image\">\n"
        "<script defer src=\"assets/js/analytics.js?v=15\"></script>"
    )

def write_page(key, body, head_html, lang="es"):
    (PAGES / f"{key}.body.html").write_text(body, encoding="utf-8")
    (PAGES / f"{key}.head.html").write_text(head_html, encoding="utf-8")
    (PAGES / f"{key}.json").write_text(json.dumps({"standalone": False, "lang": lang}), encoding="utf-8")

courses = json.load(open(DATA, encoding="utf-8"))
courses = [r for r in courses if r.get("title_es") and r.get("slug") in MAP]

cards = []
for r in courses:
    slug = r["slug"]
    key, cover, hours = MAP[slug]
    title = r["title_es"]
    desc  = r["description_es"]
    price = money(r.get("price"))
    dur   = r.get("duration") or ""

    body = (
        f"<section class=\"page-hero\" style=\"background:linear-gradient(rgba(7,25,46,.72),"
        f"rgba(9,28,55,.9)),url('assets/img/pics/{cover}') center/cover\">"
        f"<div class=\"crumb\"><a href='es.html'>Inicio</a> &rsaquo; <a href='es-courses.html'>Programas</a> &rsaquo; {esc(title)}</div>"
        f"<h1>{esc(title)}</h1><p>{esc(desc)}</p>"
        f"<div class=\"pbtns\"><a href=\"contact.html\" class=\"cta\" style=\"margin-top:0;flex:1\">Inscr&iacute;bete &rarr;</a>"
        f"<a href=\"tel:+12122900278\" class=\"cta-bd\" style=\"flex:1\">Llama (212) 290-0278</a></div></section>\n"
        f"<section class=\"sec sw\"><div class=\"kgrid\">"
        f"<div class=\"kbox\"><div class=\"kn\">{esc(dur)}</div><div class=\"kl\">Duraci&oacute;n</div></div>"
        f"<div class=\"kbox\"><div class=\"kn\">{hours}</div><div class=\"kl\">Horas</div></div>"
        f"<div class=\"kbox\"><div class=\"kn\">{price}</div><div class=\"kl\">Matr&iacute;cula</div></div></div>"
        f"<div class=\"slbl\">Descripci&oacute;n</div><div class=\"stit\">Sobre el Programa</div>"
        f"<div class=\"sdesc\">{esc(desc)}</div>"
        f"<a href=\"contact.html\" class=\"cta\">Solicitar Informaci&oacute;n &rarr;</a>"
        f"<p class=\"post-back\"><a href=\"es-courses.html\">&larr; Ver todos los programas</a></p></section>"
    )
    write_page(key, body, head(f"{title}", desc, key))
    cards.append(
        f"<a class=\"lkcard\" href=\"{key}.html\"><div class=\"lkt\">{esc(title)}</div>"
        f"<div class=\"lkd\">{esc(desc[:150])}{'…' if len(desc) > 150 else ''}</div></a>"
    )

# ES courses overview
ov_body = (
    "<section class=\"page-hero\" style=\"background:linear-gradient(rgba(7,25,46,.72),"
    "rgba(9,28,55,.9)),url('assets/img/pics/program-500.jpg') center/cover\">"
    "<div class=\"crumb\"><a href='es.html'>Inicio</a> &rsaquo; Programas</div><h1>Nuestros Programas</h1>"
    "<p>Programas de barber&iacute;a con licencia del Estado de Nueva York — ma&ntilde;ana, tarde y fin de semana.</p></section>"
    "<section class=\"sec sw\"><div class=\"slbl\">Programas</div><div class=\"stit\">Elige tu Camino</div>"
    + "".join(cards) +
    "<a href=\"contact.html\" class=\"cta\">Inscr&iacute;bete Ahora &rarr;</a></section>"
)
write_page("es-courses",
           ov_body,
           head("Nuestros Programas",
                "Programas de barbería con licencia del Estado de NY en American Barber Institute — Maestro Barbero de 500 horas, actualización de 50 horas y más.",
                "es-courses"))

# discoverable link from ES home (idempotent)
es = PAGES / "es.body.html"
src = es.read_text(encoding="utf-8")
if "es-programs-link" not in src:
    src += (
        "\n<!-- es-programs-link -->\n"
        "<section class=\"sec sb\"><div class=\"slbl\">Programas</div>"
        "<div class=\"stit\">Nuestros Programas en Espa&ntilde;ol</div>"
        "<div class=\"sdesc\">Conoce nuestros programas de barber&iacute;a con licencia del Estado de NY.</div>"
        "<a href=\"es-courses.html\" class=\"cta\">Ver Programas &rarr;</a></section>"
    )
    es.write_text(src, encoding="utf-8")
    print("linked es-courses from es home")

print(f"generated {len(courses)} ES course pages + ES overview")
