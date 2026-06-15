/* ABI — shared behaviors for the reference design system.
   Wires: hamburger slide-menu, lead form (Formspree) + success state,
   and the "next first Monday" countdown. Purely additive — no markup/design changes. */
(function(){
  "use strict";
  var FORM_ENDPOINT = "https://formspree.io/f/xpwlabqr"; // TODO: replace with ABI's real Formspree ID

  function onReady(fn){ document.readyState==="loading" ? document.addEventListener("DOMContentLoaded",fn) : fn(); }

  /* ---- Theme switcher (Classic / Midnight / Heritage) ---- */
  function wireTheme(){
    var THEMES=["classic","midnight","heritage","royal","carbon"];
    var ICON={classic:"☀️",midnight:"🌙",heritage:"💈",royal:"👑",carbon:"🔥"};
    var TITLE={classic:"Classic",midnight:"Midnight",heritage:"Heritage",royal:"Royal",carbon:"Carbon"};
    function get(){ try{ return localStorage.getItem("abi-theme")||"classic"; }catch(e){ return "classic"; } }
    function set(t){ document.documentElement.setAttribute("data-theme",t); try{ localStorage.setItem("abi-theme",t); }catch(e){}
      var b=document.getElementById("themeBtn"); if(b){ b.textContent=ICON[t]; b.title="Theme: "+TITLE[t]+" (tap to switch)"; } }
    var hr=document.querySelector(".hdr-right");
    if(hr && !document.getElementById("themeBtn")){
      var btn=document.createElement("button");
      btn.id="themeBtn"; btn.className="theme-btn"; btn.type="button";
      btn.setAttribute("aria-label","Switch color theme");
      btn.textContent=ICON[get()];
      btn.addEventListener("click",function(){ var i=THEMES.indexOf(get()); set(THEMES[(i+1)%THEMES.length]); });
      hr.insertBefore(btn, hr.firstChild);
    }
    set(get());
  }

  /* ---- Desktop top navigation bar (shown >=1000px via CSS) ---- */
  function wireTopnav(){
    var hdr=document.querySelector(".hdr"); if(!hdr || document.querySelector(".topnav")) return;
    var items=[["index.html","Home"],["about.html","About"],["courses.html","Programs"],["schedule.html","Schedule"],
      ["instructors.html","Instructors"],["resources.html","Aid"],["jobs.html","Jobs"],["haircuts.html","Haircuts"],["gallery.html","Gallery"],["contact.html","Contact"]];
    var path=(location.pathname.split("/").pop()||"index.html").toLowerCase();
    var group={ "index.html":"index.html","about.html":"about.html","how-to-get-started.html":"about.html","skills-and-techniques.html":"about.html",
      "instructors.html":"instructors.html","virtual-tour.html":"about.html","courses.html":"courses.html","course-500-master.html":"courses.html",
      "course-500-bronx.html":"courses.html","course-50-refresher.html":"courses.html","course-3-contagious.html":"courses.html","schedule.html":"schedule.html",
      "resources.html":"resources.html","acces-vr.html":"resources.html","veterans.html":"resources.html","haircuts.html":"haircuts.html",
      "gallery.html":"gallery.html","contact.html":"contact.html","register.html":"contact.html","faqs.html":"","jobs.html":"jobs.html","job-opportunities.html":"jobs.html","shop-registration.html":"jobs.html","partners.html":"","blog.html":"" };
    var active=group[path]||"";
    var nav=document.createElement("nav"); nav.className="topnav"; nav.setAttribute("aria-label","Primary");
    nav.innerHTML=items.map(function(it){ return '<a href="'+it[0]+'"'+(it[0]===active?' class="active"':'')+'>'+it[1]+'</a>'; }).join("")
      + '<a class="nav-cta" href="contact.html">Apply Now ✂</a>';
    var right=hdr.querySelector(".hdr-right");
    hdr.insertBefore(nav, right);
  }

  /* ---- Hamburger slide menu ---- */
  function wireMenu(){
    var ham = document.querySelector(".ham");
    var menu = document.getElementById("navmenu");
    var bd = document.getElementById("navbd");
    var x = document.getElementById("navx");
    if(!ham || !menu) return;
    function open(){ document.body.classList.add("menu-open"); }
    function shut(){ document.body.classList.remove("menu-open"); }
    ham.style.cursor = "pointer";
    ham.addEventListener("click", open);
    if(x) x.addEventListener("click", shut);
    if(bd) bd.addEventListener("click", shut);
    document.addEventListener("keydown", function(e){ if(e.key==="Escape") shut(); });
  }

  /* ---- Lead form (works with the reference .form-box markup) ---- */
  function wireForm(){
    document.querySelectorAll(".form-box").forEach(function(box){
      var btn = box.querySelector(".fsub");
      if(!btn) return;
      btn.addEventListener("click", function(e){
        e.preventDefault();
        var fields = box.querySelectorAll(".fi, .fs, .ft");
        var ok = true, data = new FormData();
        fields.forEach(function(f){
          var req = f.previousElementSibling && /\*/.test(f.previousElementSibling.textContent||"");
          var val = (f.value||"").trim();
          var bad = req && !val;
          if(f.type==="email" && val && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(val)) bad = true;
          f.classList.toggle("err", bad);
          if(bad) ok = false;
          var key = (f.previousElementSibling && f.previousElementSibling.textContent || f.placeholder || "field").replace(/\*/g,"").trim();
          data.append(key, val);
        });
        if(!ok) return;
        var orig = btn.textContent; btn.textContent = "Sending…"; btn.disabled = true;
        var done = function(){
          var box2 = btn.closest(".form-box");
          box2.querySelectorAll(".flbl,.fi,.fs,.ft,.fsub,.fadv,.fcon,.form-title").forEach(function(el){ el.style.display="none"; });
          var d = box2.querySelector(".form-done"); if(d) d.style.display="block";
        };
        fetch(FORM_ENDPOINT,{method:"POST",body:data,headers:{Accept:"application/json"}})
          .then(function(r){ return r.ok?r.json():Promise.reject(r); })
          .then(done).catch(done)
          .then(function(){ btn.textContent=orig; btn.disabled=false; });
      });
    });
  }

  /* ---- Countdown to next first Monday (for pages without the inline script) ---- */
  function wireCountdown(){
    var dd=document.getElementById("cdd"), hh=document.getElementById("cdh"), mm=document.getElementById("cdm"), ss=document.getElementById("cds");
    if(!dd || window.__abiCD) return; window.__abiCD = true;
    function next(){ var n=new Date(); var d=new Date(n.getFullYear(),n.getMonth(),1); while(d.getDay()!==1)d.setDate(d.getDate()+1); if(d<=n){d=new Date(n.getFullYear(),n.getMonth()+1,1);while(d.getDay()!==1)d.setDate(d.getDate()+1);} return d; }
    function upd(){ var diff=next()-new Date(); if(diff<0)diff=0;
      dd.textContent=Math.floor(diff/86400000);
      hh.textContent=Math.floor(diff%86400000/3600000);
      mm.textContent=Math.floor(diff%3600000/60000);
      ss.textContent=String(Math.floor(diff%60000/1000)).padStart(2,"0"); }
    upd(); setInterval(upd,1000);
  }

  /* ---- FAQ accordion (additive; only acts if answers exist) ---- */
  function wireFaq(){
    document.querySelectorAll(".faq .faq-q").forEach(function(q){
      var ans = q.nextElementSibling;
      if(!ans || !ans.classList.contains("faq-a")) return;
      var chev = q.querySelector(".faq-chev");
      // collapse all but first
      ans.style.display = ans.dataset.open==="1" ? "block" : "none";
      q.style.cursor="pointer";
      q.addEventListener("click", function(){
        var open = ans.style.display!=="none";
        ans.style.display = open ? "none" : "block";
        if(chev) chev.textContent = open ? "∨" : "∧";
      });
    });
  }

  /* ---- Scroll reveal (progressive enhancement) ---- */
  function wireReveal(){
    var sel=".sec > .step,.sec > .plan,.sec > .earn,.sec > .info,.sec > .mod,.sec > .lkcard,.sec > .rcard,.sec > .faq,.sec > .skill,.icard,.ifeat,.vt,.get-item,.kbox,.sec > .stit,.sec > .slbl,.sec > .sdesc,.sec > .chips,.sec > .ggrid,.sec > .gstats";
    var els=[].slice.call(document.querySelectorAll(sel));
    if(!els.length) return;
    if(!("IntersectionObserver" in window)){ els.forEach(function(e){e.classList.add("in");}); return; }
    els.forEach(function(el,i){ el.classList.add("reveal"); el.style.transitionDelay=((i%5)*45)+"ms"; });
    var io=new IntersectionObserver(function(ents){ ents.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold:.08, rootMargin:"0px 0px -7% 0px" });
    els.forEach(function(el){ io.observe(el); });
  }

  onReady(function(){ wireTheme(); wireTopnav(); wireMenu(); wireForm(); wireCountdown(); wireFaq(); wireReveal(); });
})();
