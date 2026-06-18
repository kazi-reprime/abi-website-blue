#!/usr/bin/env python3
"""Generate ABI 'blue' Spanish (ES) prose pages: about, faqs, contact, schedule.

Content is transcribed FAITHFULLY from the authenticated scrape source — the
real Spanish pages the live backend already serves:
  website-source-collection/abi-app-123.vercel.app/markdown/es__about.md
  .../markdown/es__faqs.md   .../markdown/es__contact.md   .../markdown/es__schedule.md
No machine translation, no invented copy: every string below comes from those
source files (prices, schedules, FAQ answers, addresses are quoted verbatim).

Emits (each as a chrome-wrapped, lang=es page):
  src/pages/es-about.{body,head,json}
  src/pages/es-faqs.{body,head,json}
  src/pages/es-contact.{body,head,json}
  src/pages/es-schedule.{body,head,json}

Run:  python3 src/_gen_es_pages.py   (then python3 src/build.py)
"""
import json, html, pathlib

REPO  = pathlib.Path(__file__).resolve().parent.parent
PAGES = REPO / "src" / "pages"
SITE  = "https://www.abi.edu"


def esc(s):
    return html.escape(s or "", quote=True)


def head(title, desc, slug):
    return (
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<meta name="description" content="{esc(desc)}">\n'
        f"<title>{esc(title)} | American Barber Institute</title>\n"
        '<link rel="stylesheet" href="assets/css/abi.css?v=15">\n'
        '<link rel="stylesheet" href="assets/css/abi-add.css?v=15">\n'
        "<script>try{document.documentElement.dataset.theme=localStorage.getItem('abi-theme')||'classic'}catch(e){}</script>\n"
        f'<link rel="canonical" href="{SITE}/{slug}"><meta name="robots" content="index,follow">\n'
        f'<link rel="alternate" hreflang="es" href="{SITE}/{slug}">\n'
        '<meta property="og:type" content="website"><meta property="og:site_name" content="American Barber Institute">\n'
        f'<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">\n'
        f'<meta property="og:url" content="{SITE}/{slug}">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<script defer src="assets/js/analytics.js?v=15"></script>'
    )


def hero(img, crumb_label, title, sub, with_btns=True):
    btns = (
        '<div class="pbtns"><a href="es-contact.html" class="cta" style="margin-top:0;flex:1">Inscr&iacute;bete &rarr;</a>'
        '<a href="tel:+12122900278" class="cta-bd" style="flex:1">Llama (212) 290-0278</a></div>'
        if with_btns else ""
    )
    return (
        f'<section class="page-hero" style="background:linear-gradient(rgba(7,25,46,.72),'
        f"rgba(9,28,55,.9)),url('assets/img/pics/{img}') center/cover\">"
        f"<div class=\"crumb\"><a href='es.html'>Inicio</a> &rsaquo; {crumb_label}</div>"
        f"<h1>{title}</h1><p>{sub}</p>{btns}</section>"
    )


def write_page(key, body, title, desc, slug):
    (PAGES / f"{key}.body.html").write_text(body, encoding="utf-8")
    (PAGES / f"{key}.head.html").write_text(head(title, desc, slug), encoding="utf-8")
    (PAGES / f"{key}.json").write_text(json.dumps({"standalone": False, "lang": "es"}), encoding="utf-8")


# ───────────────────────── ABOUT ─────────────────────────
why = [
    "Licenciada por el Departamento de Educaci&oacute;n del Estado de Nueva York",
    "M&aacute;s de 30 a&ntilde;os sirviendo a la comunidad de NYC",
    "Instalaciones de &uacute;ltima generaci&oacute;n de 3,000 pies cuadrados en el centro de Manhattan",
    "Instructores expertos — King David tiene m&aacute;s de 30 a&ntilde;os de experiencia",
    "Entrenamiento pr&aacute;ctico con clientes reales desde las primeras semanas",
    "Oficina de colocaci&oacute;n laboral a tiempo completo para graduados",
    "Asistencia financiera: ACCES-VR, Post-9/11 GI Bill&reg;, beneficios de la VA aceptados",
    "Horarios de clases de ma&ntilde;ana, tarde y fin de semana",
]
instructors = [
    ("David Ayeoribe", "Instructor Principal Senior y Director",
     "&ldquo;King David&rdquo; es una pieza clave de American Barber Institute y uno de los nombres m&aacute;s respetados en la educaci&oacute;n de barber&iacute;a de Nueva York. Con m&aacute;s de 50 a&ntilde;os detr&aacute;s de la silla y m&aacute;s de 30 a&ntilde;os ense&ntilde;ando, es ampliamente reconocido como el instructor de barber&iacute;a con m&aacute;s a&ntilde;os de servicio en la ciudad de Nueva York."),
    ("Harold &ldquo;Barkim&rdquo; Brown", "Instructor Principal",
     "Nativo de Queens y maestro barbero, Harold es la clase de maestro que los estudiantes recuerdan por el resto de su carrera. Conocido en el oficio como el mejor barbero con un solo brazo del mundo, ha convertido cada duda en combustible — y ahora vierte esa misma energ&iacute;a en la pr&oacute;xima generaci&oacute;n de barberos."),
    ("Barry Brown", "Instructor",
     "La historia de Barry con la barber&iacute;a comenz&oacute; mucho antes de pisar un sal&oacute;n de clases. Empez&oacute; a cortar cabello de joven y r&aacute;pidamente demostr&oacute; lo que era obvio para cualquiera que lo viera trabajar: la barber&iacute;a corr&iacute;a por su sangre."),
]
about_body = (
    hero("abi-students-007.jpg", "Acerca de Nosotros", "American Barber Institute",
         "La &uacute;nica escuela de barber&iacute;a dedicada en Nueva York — cambiando vidas por m&aacute;s de 30 a&ntilde;os en Manhattan y el Bronx.")
    + '<section class="sec sw"><div class="slbl">Nuestra Misi&oacute;n</div>'
      '<div class="stit">Educaci&oacute;n de Barber&iacute;a Desde 1996</div>'
      '<div class="sdesc">En American Barber Institute nos dedicamos a la educaci&oacute;n de la barber&iacute;a y al desarrollo profesional. '
      'Licenciados por el Departamento de Educaci&oacute;n del Estado de Nueva York, llevamos m&aacute;s de 30 a&ntilde;os sirviendo a la comunidad neoyorquina. '
      'Nuestro Programa de Maestro Barbero ofrece un curr&iacute;culo integral dise&ntilde;ado para preparar a los estudiantes para el &eacute;xito. '
      'Durante cuatro meses, los estudiantes se sumergen en teor&iacute;a y habilidades pr&aacute;cticas, cubriendo sanitizaci&oacute;n, esterilizaci&oacute;n, '
      'historia de la barber&iacute;a, leyes y administraci&oacute;n de un negocio. Los graduados salen con un conjunto de habilidades vers&aacute;til, '
      'listos para trabajar en cualquier barber&iacute;a — o para abrir su propio negocio.</div></section>'
    + '<section class="sec sb"><div class="slbl">Ventajas</div><div class="stit">&iquest;Por Qu&eacute; Elegir ABI?</div>'
    + "".join(f'<div class="skill"><div class="ski">✂</div>{w}</div>' for w in why)
    + '<a href="es-contact.html" class="cta">Solicitar Informaci&oacute;n &rarr;</a></section>'
    + '<section class="sec sw"><div class="slbl">Admisiones</div><div class="stit">Requisitos de Ingreso</div>'
      '<div class="sdesc">Tarjeta de Seguro Social &middot; Diploma de Preparatoria (HSD) o GED — o aprobar el examen de entrada ATB en ABI &middot; '
      'Tener al menos 17 a&ntilde;os de edad &middot; Comprobante de domicilio &middot; Identificaci&oacute;n con foto v&aacute;lida o Licencia de Conducir &middot; '
      'Enganche de $500.</div>'
      '<div class="info"><h3>Manhattan</h3><p>48 West 39th Street, New York, NY 10018<br>'
      '<a href="tel:+12122902289" style="color:#1252A3;font-weight:800;text-decoration:none">(212) 290-2289</a></p></div>'
      '<div class="info"><h3>Bronx</h3><p>121 Westchester Square, Bronx, NY 10461<br>'
      '<a href="tel:+17186760640" style="color:#1252A3;font-weight:800;text-decoration:none">(718) 676-0640</a></p></div></section>'
    + '<section class="sec sb"><div class="slbl">Equipo</div><div class="stit">Nuestros Instructores</div>'
      '<div class="sdesc">Aprende de maestros barberos que aportan d&eacute;cadas de experiencia real en cada sesi&oacute;n.</div>'
    + "".join(f'<div class="info"><h3>{n}</h3><p style="font-weight:700;color:#1252A3;margin:0 0 6px">{role}</p><p>{bio}</p></div>'
             for n, role, bio in instructors)
    + '<a href="es-courses.html" class="cta">Ver Nuestros Programas &rarr;</a></section>'
)
write_page("es-about", about_body, "Acerca de Nosotros",
           "Conoce American Barber Institute — la única escuela de barbería dedicada en Nueva York, cambiando vidas por más de 30 años. Licenciada por el Estado de NY.",
           "es-about")

# ───────────────────────── FAQS ─────────────────────────
faqs = [
    ("&iquest;Cu&aacute;nto dura el programa?",
     "El Programa de Maestro Barbero de 500 Horas se puede completar en tan solo 4 meses, dependiendo del horario que elijas. El Curso de Actualizaci&oacute;n de 50 Horas es un intensivo de 2 semanas. El programa de Enfermedades Contagiosas de 3 Horas es una sola sesi&oacute;n."),
    ("&iquest;Cu&aacute;ndo empiezan las nuevas clases?",
     "Las nuevas clases empiezan el primer lunes de cada mes. Simplemente aplica, re&uacute;ne tus documentos y prep&aacute;rate para la pr&oacute;xima fecha de inicio."),
    ("&iquest;Qu&eacute; horarios hay disponibles?",
     "Ofrecemos tres horarios para el programa de 500 Horas: Plan A (Ma&ntilde;ana) Lun–Vie 8:00–14:00; Plan B (Tarde) Lun–Vie 14:00–20:00; Plan C (Fin de Semana) S&aacute;b–Dom 9:00–19:00."),
    ("&iquest;Cu&aacute;les son los requisitos de ingreso?",
     "Tarjeta de Seguro Social; Diploma de Preparatoria, GED o examen de entrada ATB; Al menos 17 a&ntilde;os de edad; Comprobante de domicilio; Identificaci&oacute;n con foto v&aacute;lida o Licencia de Conducir; Enganche de $500 (incluye cuota de inscripci&oacute;n de $100)."),
    ("&iquest;Cu&aacute;nto cuesta el programa?",
     "Maestro Barbero 500 Horas desde $4,600 (Tarde/Fin de Semana); Plan de Ma&ntilde;ana $5,600. Actualizaci&oacute;n 50 Horas: $1,500. Enfermedades Contagiosas: contactar para precio. Planes de pago disponibles para todos."),
    ("&iquest;Ofrecen planes de pago?",
     "S&iacute;. Planes de pago semanales flexibles despu&eacute;s del enganche inicial. Ejemplo Plan B: $500 enganche + 16 pagos semanales de $250 + pago final de $100."),
    ("&iquest;Qu&eacute; licencias o certificaciones recibir&eacute;?",
     "Al completar el Programa de 500 Horas estar&aacute;s preparado para el examen de la Junta Estatal de Barber&iacute;a de NY y obtener tu Licencia de Maestro Barbero (partes escrita y pr&aacute;ctica)."),
    ("&iquest;Ofrecen asistencia de colocaci&oacute;n laboral?",
     "S&iacute;. Oficina de Colocaci&oacute;n Laboral para explorar oportunidades de empleo, conectarse con empleadores y navegar los siguientes pasos."),
    ("&iquest;D&oacute;nde est&aacute;n sus ubicaciones?",
     "Manhattan: 48 West 39th Street, New York, NY 10018. Bronx: 121 Westchester Square, Bronx, NY 10461."),
    ("&iquest;Aceptan beneficios del GI Bill&reg; o de la VA?",
     "S&iacute;. ABI acepta beneficios del Post-9/11 GI Bill&reg; y de la VA. Cont&aacute;ctanos para detalles."),
    ("&iquest;Qu&eacute; es ACCES-VR?",
     "Adult Career and Continuing Education Services – Vocational Rehabilitation: programa del Estado de NY que apoya a individuos con discapacidades. Puede proveer asistencia financiera para estudiar en ABI."),
    ("&iquest;Necesito comprar mis propias herramientas?",
     "S&iacute;. Los estudiantes compran sus propias herramientas, libros y suministros — disponibles en ABI o con otros proveedores. Lista proporcionada al inscribirse."),
    ("&iquest;Est&aacute; ABI licenciada por el estado?",
     "S&iacute;. Licenciada por el Departamento de Educaci&oacute;n del Estado de Nueva York. M&aacute;s de 30 a&ntilde;os en el negocio."),
    ("&iquest;Puedo obtener un corte de cabello en ABI?",
     "S&iacute;. El p&uacute;blico puede obtener cortes asequibles hechos por estudiantes — t&iacute;picamente alrededor de $3."),
]
faq_html = ""
for i, (q, a) in enumerate(faqs):
    chev = "∧" if i == 0 else "∨"
    op = ' data-open="1"' if i == 0 else ""
    faq_html += (
        f'<div class="faq"><div class="faq-q"><div class="faq-qt"><span class="faq-num">{i+1:02d}</span>{q}</div>'
        f'<div class="faq-chev">{chev}</div></div><div class="faq-a"{op}>{a}</div></div>'
    )
faqs_body = (
    hero("abi-students-010.jpg", "Preguntas Frecuentes", "Preguntas Frecuentes",
         "Todo lo que necesitas saber sobre nuestros programas, inscripci&oacute;n, matr&iacute;cula y m&aacute;s.", with_btns=False)
    + '<section class="sec sw"><div class="slbl">FAQs</div><div class="stit">Tus Preguntas, Respondidas</div>'
    + faq_html
    + '<a href="tel:+12122900278" class="cta">&iquest;A&uacute;n tienes preguntas? Llama (212) 290-0278 &rarr;</a></section>'
)
write_page("es-faqs", faqs_body, "Preguntas Frecuentes",
           "Encuentra respuestas a las preguntas más comunes sobre los programas de barbería de ABI, requisitos de inscripción, horarios, matrícula y planes de pago.",
           "es-faqs")

# ───────────────────────── CONTACT ─────────────────────────
contact_body = (
    hero("contact-bg.jpeg", "Contacto", "Contacta a ABI",
         "&iquest;Tienes preguntas sobre la inscripci&oacute;n o nuestros programas? Llama, escribe un correo o env&iacute;a un mensaje — te respondemos r&aacute;pido.", with_btns=False)
    + '<section class="sec sw"><div class="slbl">Cont&aacute;ctanos</div><div class="stit">Ponte en Contacto</div>'
      '<div class="info"><h3>Campus Manhattan</h3><p>48 West 39th Street, New York, NY 10018<br>'
      '<a href="tel:+12122902289" style="color:#1252A3;font-weight:800;text-decoration:none">(212) 290-2289 EN</a></p></div>'
      '<div class="info"><h3>Campus Bronx</h3><p>121 Westchester Square, Bronx, NY 10461<br>'
      '<a href="tel:+17186760640" style="color:#1252A3;font-weight:800;text-decoration:none">(718) 676-0640</a> &middot; '
      '<a href="tel:+12122900278" style="color:#1252A3;font-weight:800;text-decoration:none">(212) 290-0278 ES</a></p></div>'
      '<div class="info"><h3>Correo &amp; Horario</h3><p>'
      '<a href="mailto:admission@abi.edu" style="color:#1252A3;font-weight:800;text-decoration:none">admission@abi.edu</a><br>'
      'Lun–Vie 8AM–8PM &middot; S&aacute;b–Dom 9AM–7PM</p></div></section>'
    + '<section class="form-sec" id="reserve"><div class="form-box"><div class="form-title">Reserva Tu Lugar</div>\n'
      '<label class="flbl">Nombre *</label><input class="fi" type="text" placeholder="Nombre">\n'
      '<label class="flbl">Apellido *</label><input class="fi" type="text" placeholder="Apellido">\n'
      '<label class="flbl">Tel&eacute;fono *</label><input class="fi" type="tel" placeholder="(917) 000-0000">\n'
      '<label class="flbl">Correo *</label><input class="fi" type="email" placeholder="nombre@correo.com">\n'
      '<label class="flbl">&iquest;Cu&aacute;l Ubicaci&oacute;n? *</label><select class="fs"><option value="">Selecciona una ubicaci&oacute;n</option>'
      '<option>Manhattan — 48 West 39th Street</option><option>Bronx — 121 Westchester Square</option></select>\n'
      '<label class="flbl">&iquest;Idioma Preferido? *</label><select class="fs"><option value="">Selecciona idioma</option>'
      '<option>Espa&ntilde;ol</option><option>English</option></select>\n'
      '<label class="flbl">Mensaje *</label><textarea class="ft" placeholder="Mensaje..."></textarea>\n'
      '<button class="fsub">Solicitar Mi Consulta Gratis &rarr;</button>\n'
      '<div class="fadv">Un asesor de admisiones se comunicar&aacute; contigo pronto.</div>\n'
      '<div class="fcon">Al hacer clic arriba, aceptas que ABI puede contactarte por tel&eacute;fono, SMS o correo para confirmaciones de citas u ofertas promocionales.</div>\n'
      '<div class="form-done"><div class="tk">✓</div><h4>&iexcl;Todo listo!</h4><p>Gracias — un asesor de admisiones de ABI se comunicar&aacute; contigo pronto.</p></div></div></section>'
)
write_page("es-contact", contact_body, "Contáctenos",
           "Comunícate con American Barber Institute — visita nuestro campus de Manhattan o el Bronx, llámanos o envía un mensaje. Respuestas sobre inscripción, horarios y ayuda financiera.",
           "es-contact")

# ───────────────────────── SCHEDULE ─────────────────────────
start_dates = [
    ("Jul 2026", "Lunes 6 (Pr&oacute;xima Clase)"), ("Ago 2026", "Lunes 3"),
    ("Sept 2026", "Martes 8"), ("Oct 2026", "Lunes 5"), ("Nov 2026", "Lunes 2"),
    ("Dic 2026", "Lunes 7"), ("Ene 2027", "Lunes 4"), ("Feb 2027", "Lunes 1"),
    ("Mar 2027", "Lunes 1"), ("Abr 2027", "Lunes 5"), ("May 2027", "Lunes 3"),
    ("Jun 2027", "Lunes 7"),
]
plans = [
    ("Plan A — Ma&ntilde;ana", "Lun–Vie · 8:00 – 14:00", "30 hrs/semana · 17 semanas", "$5,600",
     "Enganche $500 (incluye $100 de inscripci&oacute;n) + 17 pagos semanales de $300", False),
    ("Plan B — Tarde", "Lun–Vie · 14:00 – 20:00", "30 hrs/semana · 17 semanas", "$4,600",
     "Enganche $500 (incluye $100 de inscripci&oacute;n) + 16 pagos semanales de $250 + $100 final", True),
    ("Plan C — Fin de Semana", "S&aacute;b y Dom · 9:00 – 19:00", "18 hrs/semana · 27 semanas", "$4,600",
     "Enganche $550 + 27 pagos semanales de $150", False),
]
notes = [
    "Las nuevas clases empiezan el primer lunes de cada mes",
    "Libros, herramientas y suministros se venden por separado",
    "Asistencia financiera ACCES-VR disponible para quienes califiquen",
    "Se aceptan beneficios Post-9/11 GI Bill&reg; y de la VA",
    "Cont&aacute;ctanos para confirmar disponibilidad de cupos",
]
date_rows = "".join(
    f'<div class="kbox"><div class="kn" style="font-size:15px">{m}</div><div class="kl">{d}</div></div>'
    for m, d in start_dates
)
plan_cards = ""
for n, s, h, p, d, feat in plans:
    badge = '<div class="plan-badge">M&Aacute;S POPULAR</div>' if feat else ""
    cls = "plan ft" if feat else "plan"
    plan_cards += (
        f'<div class="{cls}">{badge}<div class="plan-n">{n}</div><div class="plan-s">{s}</div>'
        f'<div class="plan-h">{h}</div><div class="plan-p">{p}</div><div class="plan-d">{d}</div>'
        f'<a href="es-contact.html" class="plan-btn">Inscr&iacute;bete &rarr;</a></div>'
    )
schedule_body = (
    hero("banner-slide1.jpg", "Horario", "Horarios Flexibles para Tu Vida",
         "Elige sesiones de Ma&ntilde;ana, Tarde o Fin de Semana. Las nuevas clases empiezan el primer lunes de cada mes.")
    + '<section class="sec sw"><div class="slbl">Calendario</div><div class="stit">Pr&oacute;ximas 12 Fechas de Inicio</div>'
      f'<div class="kgrid">{date_rows}</div></section>'
    + '<section class="sec sb"><div class="slbl">Matr&iacute;cula</div><div class="stit">Tres Horarios, Una Meta</div>'
      '<div class="sdesc">El programa de 500 Horas se ofrece en ambos campus — Manhattan (48 West 39th Street &middot; (212) 290-2289) '
      'y Bronx (121 Westchester Square &middot; (718) 676-0640) — con los mismos planes y precios.</div>'
    + plan_cards + '</section>'
    + '<section class="sec sw"><div class="slbl">Programas Cortos</div><div class="stit">Cursos Especializados</div>'
      '<div class="info"><h3>Actualizaci&oacute;n — 50 Horas</h3><p>Horario flexible &middot; 2 semanas &middot; Para licenciados y cosmet&oacute;logos &middot; '
      '<strong style="color:#1252A3">$1,500</strong></p></div>'
      '<div class="info"><h3>Enfermedades Contagiosas — 3 Horas</h3><p>1 sesi&oacute;n &middot; Requerido para el examen del Estado de NY &middot; '
      '<strong style="color:#1252A3">$100</strong></p></div></section>'
    + '<section class="sec sb"><div class="stit">Notas Importantes</div>'
    + "".join(f'<div class="skill"><div class="ski">✂</div>{n}</div>' for n in notes)
    + '<a href="es-contact.html" class="cta">Inscr&iacute;bete Ahora &rarr;</a></section>'
)
write_page("es-schedule", schedule_body, "Horario de Clases",
           "Consulta las próximas fechas de inicio y los planes de horario para los programas de barbería de ABI en Manhattan y el Bronx. Nuevas clases el primer lunes de cada mes.",
           "es-schedule")

print("generated 4 ES prose pages: es-about, es-faqs, es-contact, es-schedule")
