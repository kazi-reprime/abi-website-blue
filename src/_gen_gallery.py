#!/usr/bin/env python3
"""Generate ABI 'blue' 3D gallery (institutional style).

Builds src/pages/gallery.body.html from:
  - assets/img/gallery/*.jpg            (curated multi-people photos, committed)
  - src/data/gallery_videos.json        (videos embedded from public CDN, NOT in git)
Photos: perspective tilt-cards + lightbox. Videos: 9:16 click-to-play reels.
Injects a .g3d-* CSS block into abi-add.css (idempotent).
Run:  python3 src/_gen_gallery.py   (then python3 src/build.py)
"""
import json, glob, os, pathlib

REPO  = pathlib.Path(__file__).resolve().parent.parent
PAGES = REPO / "src" / "pages"
CSS   = REPO / "assets" / "css" / "abi-add.css"

imgs = sorted(os.path.basename(p) for p in glob.glob(str(REPO / "assets/img/gallery/*.jpg")))
vids = [v for v in json.load(open(REPO / "src/data/gallery_videos.json", encoding="utf-8"))
        if v.get("ext") == "mp4"]  # mp4 = cross-browser; .mov skipped for reliability

photo_cards = "".join(
    f'<button class="g3d-card" data-full="assets/img/gallery/{n}">'
    f'<img loading="lazy" src="assets/img/gallery/{n}" '
    f'alt="ABI barber students and instructors at work in NYC"></button>'
    for n in imgs
)

def reel_card(v):
    poster = f' data-poster="{v["poster"]}"' if v.get("poster") else ""
    return (f'<button class="g3d-reel" data-src="{v["url"]}"{poster}>'
            f'<span class="g3d-play">&#9658;</span></button>')

reel_cards = "".join(reel_card(v) for v in vids)

JS = """<script>(function(){
var cards=[].slice.call(document.querySelectorAll('.g3d-card'));
cards.forEach(function(c){
 c.addEventListener('mousemove',function(e){var r=c.getBoundingClientRect();
  var x=(e.clientX-r.left)/r.width-0.5,y=(e.clientY-r.top)/r.height-0.5;
  c.style.transform='rotateY('+(x*10).toFixed(2)+'deg) rotateX('+(-y*10).toFixed(2)+'deg) translateZ(6px)';});
 c.addEventListener('mouseleave',function(){c.style.transform='';});
});
var lb=document.getElementById('g3dlb'),im=document.getElementById('g3dlbimg'),idx=0;
var fulls=cards.map(function(c){return c.getAttribute('data-full');});
function show(i){idx=(i+fulls.length)%fulls.length;im.src=fulls[idx];lb.classList.add('on');}
cards.forEach(function(c,i){c.addEventListener('click',function(){show(i);});});
document.getElementById('g3dx').addEventListener('click',function(){lb.classList.remove('on');});
document.querySelector('.g3d-nav.prev').addEventListener('click',function(){show(idx-1);});
document.querySelector('.g3d-nav.next').addEventListener('click',function(){show(idx+1);});
lb.addEventListener('click',function(e){if(e.target===lb)lb.classList.remove('on');});
document.addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;
 if(e.key==='Escape')lb.classList.remove('on');if(e.key==='ArrowRight')show(idx+1);if(e.key==='ArrowLeft')show(idx-1);});
[].slice.call(document.querySelectorAll('.g3d-reel')).forEach(function(r){
 r.addEventListener('click',function(){if(r.dataset.loaded)return;r.dataset.loaded=1;
  var v=document.createElement('video');v.src=r.dataset.src;v.controls=true;v.autoplay=true;
  v.playsInline=true;v.setAttribute('playsinline','');if(r.dataset.poster)v.poster=r.dataset.poster;
  r.innerHTML='';r.appendChild(v);});
});
})();</script>"""

body = (
    "<section class=\"page-hero\" style=\"background:linear-gradient(rgba(7,25,46,.72),"
    "rgba(9,28,55,.9)),url('assets/img/gallery/gallery-07.jpg') center/cover\">"
    "<div class=\"crumb\"><a href='index.html'>Home</a> &rsaquo; Gallery</div><h1>Gallery</h1>"
    "<p>Real students, instructors and moments from NYC's only dedicated barber school.</p></section>"
    "<section class=\"sec sw g3d-wrap\"><div class=\"slbl\">Photos</div><div class=\"stit\">Inside ABI</div>"
    "<div class=\"sdesc\">Hover to explore &mdash; tap any photo to enlarge.</div>"
    f"<div class=\"g3d-grid\">{photo_cards}</div></section>"
    "<section class=\"sec sb g3d-wrap\"><div class=\"slbl\">Reels</div><div class=\"stit\">ABI in Motion</div>"
    f"<div class=\"sdesc\">{len(vids)} clips from the floor &mdash; tap to play.</div>"
    f"<div class=\"g3d-reels\">{reel_cards}</div></section>"
    "<div class=\"g3d-lb\" id=\"g3dlb\"><button class=\"g3d-lb-x\" id=\"g3dx\" aria-label=\"Close\">&times;</button>"
    "<button class=\"g3d-nav prev\" aria-label=\"Previous\">&lsaquo;</button>"
    "<img id=\"g3dlbimg\" alt=\"ABI gallery photo\">"
    "<button class=\"g3d-nav next\" aria-label=\"Next\">&rsaquo;</button></div>"
    + JS
)
(PAGES / "gallery.body.html").write_text(body, encoding="utf-8")

CSS_BLOCK = """
/* g3d — blue 3D gallery (institutional tilt) */
.g3d-wrap{perspective:1400px}
.g3d-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px;margin-top:14px}
.g3d-card{border:0;padding:0;cursor:pointer;background:#0b1a33;border-radius:14px;overflow:hidden;aspect-ratio:3/4;box-shadow:0 10px 30px rgba(7,20,46,.28);transform-style:preserve-3d;transition:transform .18s ease,box-shadow .25s ease}
.g3d-card img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s ease}
.g3d-card:hover{box-shadow:0 26px 60px rgba(7,20,46,.45)}
.g3d-card:hover img{transform:scale(1.06)}
.g3d-reels{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px;margin-top:14px}
.g3d-reel{position:relative;border:0;cursor:pointer;background:linear-gradient(160deg,#0f2a52,#071a33);border-radius:14px;aspect-ratio:9/16;overflow:hidden;box-shadow:0 10px 30px rgba(7,20,46,.3);transition:transform .18s ease}
.g3d-reel video{width:100%;height:100%;object-fit:cover;display:block}
.g3d-reel:hover{transform:translateY(-4px) scale(1.02)}
.g3d-play{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:30px;color:#fff;background:radial-gradient(circle,rgba(0,0,0,.12),rgba(0,0,0,.5))}
.g3d-lb{position:fixed;inset:0;z-index:300;background:rgba(5,12,26,.94);display:none;align-items:center;justify-content:center;padding:20px}
.g3d-lb.on{display:flex}
.g3d-lb img{max-width:94vw;max-height:88vh;border-radius:10px;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.g3d-lb-x{position:absolute;top:14px;right:20px;font-size:32px;color:#fff;background:0;border:0;cursor:pointer;line-height:1}
.g3d-nav{position:absolute;top:50%;transform:translateY(-50%);font-size:44px;color:#fff;background:0;border:0;cursor:pointer;padding:8px 14px;line-height:1}
.g3d-nav.prev{left:6px}.g3d-nav.next{right:6px}
@media(prefers-reduced-motion:reduce){.g3d-card,.g3d-card img,.g3d-reel{transition:none}.g3d-card:hover img{transform:none}}
"""
css = CSS.read_text(encoding="utf-8")
if "g3d — blue 3D gallery" not in css:
    CSS.write_text(css + CSS_BLOCK, encoding="utf-8")
    print("injected g3d CSS")
print(f"blue gallery: {len(imgs)} photos + {len(vids)} mp4 reels")
