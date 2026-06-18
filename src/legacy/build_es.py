from gen import *
def sec(c,i): return f'<section class="sec {c}">{i}</section>'
def skills(items): return "".join(f'<div class="skill"><div class="ski">✂</div>{i}</div>' for i in items)
es = '<section class="page-hero"><div class="crumb"><a href="index.html">EN</a> · <strong style="color:#fff">ES</strong></div><h1>Conviértete en Barbero con Licencia en 4 Meses</h1><p>La única escuela dedicada exclusivamente a la barbería en Nueva York — cambiando vidas por más de 30 años. Mañana, tarde y fin de semana.</p><div class="pbtns"><a href="contact.html" class="cta" style="margin-top:0;flex:1">Inscríbete →</a><a href="tel:+12122900278" class="cta-bd" style="flex:1">Llama (212) 290-0278</a></div></section>'
es += sec("sw", '<div class="slbl">Lo Que Obtienes</div><div class="stit">Todo Para Tener Éxito</div>'+skills([
  "Licenciado por el Departamento de Educación del Estado de NY (BPSS)","Entrenamiento práctico con clientes reales desde las primeras semanas",
  "Preparación para el Examen de la Junta Estatal","Asistencia de colocación laboral","Campus de 3,000 pies² · Manhattan y el Bronx",
  "GI Bill® y ACCES-VR aceptados","Más de 30 años · 10,000+ graduados","Nuevas clases el primer lunes de cada mes"]))
es += sec("sb", '<div class="slbl">Planes de Pago</div><div class="stit">Planes de Pago Flexibles</div>'+
  '<div class="plan"><div class="plan-n">Plan A — Mañana</div><div class="plan-s">Lun–Vie · 8:00 AM – 2:00 PM</div><div class="plan-p">$5,600</div><div class="plan-d">$500 de enganche + 17 pagos semanales de $300</div><a href="contact.html" class="plan-btn">Inscríbete →</a></div>'+
  '<div class="plan ft"><div class="plan-badge">MÁS POPULAR</div><div class="plan-n">Plan B — Tarde</div><div class="plan-s">Lun–Vie · 2:00 PM – 8:00 PM</div><div class="plan-p">$4,600</div><div class="plan-d">$500 de enganche + 16 pagos de $250 + $100 final</div><a href="contact.html" class="plan-btn">Inscríbete →</a></div>'+
  '<div class="plan"><div class="plan-n">Plan C — Fin de Semana</div><div class="plan-s">Sáb y Dom · 9:00 AM – 7:00 PM</div><div class="plan-p">$4,600</div><div class="plan-d">$500 de enganche + 27 pagos semanales de $150</div><a href="contact.html" class="plan-btn">Inscríbete →</a></div>')
es += sec("sw", '<div class="slbl">Información Gratis</div><div class="stit">¿Listo para Empezar?</div><div class="sdesc">Completa el formulario y un asesor de admisiones te llamará. Las clases comienzan el primer lunes de cada mes.</div><a href="contact.html" class="cta">Solicitar Información →</a>')
page("es","American Barber Institute | Escuela de Barbería en NYC","La única escuela dedicada exclusivamente a la barbería en Nueva York. Programa de Barbero Maestro de 500 horas con licencia del Estado de NY. GI Bill® y ACCES-VR.",es)
print("es done")
