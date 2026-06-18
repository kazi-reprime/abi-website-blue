from gen import *
def sec(c,i): return f'<section class="sec {c}">{i}</section>'
def lbl(t): return f'<div class="slbl">{t}</div>'
def tit(t): return f'<div class="stit">{t}</div>'
def desc(t): return f'<div class="sdesc">{t}</div>'
def cta(t="Apply Now →",h="contact.html"): return f'<a href="{h}" class="cta">{t}</a>'
def ctao(t,h): return f'<a href="{h}" class="cta-out">{t}</a>'
def skills(items): return "".join(f'<div class="skill"><div class="ski">✂</div>{i}</div>' for i in items)
def reqs(items,ic="›"): return '<ul class="req-list">'+"".join(f'<li><span class="req-icon">{ic}</span><span>{i}</span></li>' for i in items)+'</ul>'
def kgrid(cells): return '<div class="kgrid">'+"".join(f'<div class="kbox"><div class="kn">{n}</div><div class="kl">{l}</div></div>' for n,l in cells)+'</div>'
def plan(badge,n,s,h,p,d,ft=False):
    b=f'<div class="plan-badge">{badge}</div>' if badge else ''
    return f'<div class="plan{" ft" if ft else ""}">{b}<div class="plan-n">{n}</div><div class="plan-s">{s}</div><div class="plan-h">{h}</div><div class="plan-p">{p}</div><div class="plan-d">{d}</div><a href="contact.html" class="plan-btn">Enroll Now →</a></div>'
def faq(items):
    out=''
    for idx,(q,a) in enumerate(items):
        op=' data-open="1"' if idx==0 else ''
        chev='∧' if idx==0 else '∨'
        out+=f'<div class="faq"><div class="faq-q"><div class="faq-qt"><span class="faq-num">{idx+1:02d}</span>{q}</div><div class="faq-chev">{chev}</div></div><div class="faq-a"{op}>{a}</div></div>'
    return out

# SCHEDULE
s = hero("Flexible Schedules to Fit Your Life","Choose Morning, Afternoon, or Weekend sessions. New classes begin the first Monday of every month.","<a href='index.html'>Home</a> › Schedule")
s += sec("sw", lbl("Tuition")+tit("Three Schedules, One Goal")+
  plan("","Plan A — Morning","Mon–Fri · 8:00 AM – 2:00 PM","30 hrs/week · 17 weeks","$5,600","$500 down (incl. $100 registration) + 17 weekly payments of $300")+
  plan("MOST POPULAR","Plan B — Afternoon","Mon–Fri · 2:00 PM – 8:00 PM","30 hrs/week · 17 weeks","$4,600","$500 down (incl. $100 registration) + 16 weekly payments of $250 + final $100",ft=True)+
  plan("","Plan C — Weekend","Sat & Sun · 9:00 AM – 7:00 PM","18 hrs/week · 27 weeks","$4,600","$500 down (incl. $100 registration) + 27 weekly payments of $150"))
s += sec("sb", tit("Important Notes")+skills([
  "New classes begin the first Monday of each month","Books, tools and supplies sold separately","ACCES-VR financial assistance available for qualifying individuals",
  "Post-9/11 GI Bill® and VA benefits accepted","Contact us to confirm seat availability"])+cta())
page("schedule","Class Schedule | American Barber Institute","Flexible barber school schedules at ABI — Morning, Afternoon, and Weekend sessions. New classes begin the first Monday of every month. Payment plans available.",s)

# RESOURCES
rs = hero("Student Resources","Financial assistance options, licensing information, and everything you need to make the most of your ABI education.","<a href='index.html'>Home</a> › Resources",btns=False)
rs += sec("sw", lbl("Financial Assistance")+tit("Ways to Fund Your Training")+
  '<a class="lkcard" href="acces-vr.html"><div class="lkt">ACCES-VR Financial Assistance</div><div class="lkd">NY State vocational rehab may cover tuition, tools and supplies for eligible individuals with disabilities.</div></a>'+
  '<a class="lkcard" href="veterans.html"><div class="lkt">GI Bill® &amp; VA Benefits</div><div class="lkd">Post-9/11 GI Bill® (Ch.33), VR&amp;E (Ch.31), Montgomery (Ch.30) and DEA (Ch.35) accepted.</div></a>')
rs += sec("sb", lbl("Licensing")+tit("NY State Board of Barbering")+skills([
  "Full exam prep included in the 500 Hour program","Written and practical components covered","Master Barber License required to work in NY",
  "ABI graduates are exam-ready upon completion"])+ctao("Contact Admissions →","contact.html"))
page("resources","Student Resources | American Barber Institute","Financial assistance, licensing information, and student resources at ABI — ACCES-VR, GI Bill® & VA benefits, NY State Board of Barbering.",rs)

# ACCES-VR
av = hero("ACCES-VR Financial Assistance","If you have a disability, New York State's ACCES-VR program may cover your tuition at ABI — helping you launch your barber career at little or no cost.","<a href='resources.html'>Resources</a> › ACCES-VR")
av += sec("sw", lbl("Overview")+tit("What is ACCES-VR?")+desc("ACCES-VR (Adult Career and Continuing Education Services – Vocational Rehabilitation) is a program of the NY State Education Department that supports individuals with disabilities in preparing for and obtaining employment — including funding for barber school.")+
  tit("What ACCES-VR May Cover")+skills(["Tuition and program fees (most approved cases)","Books and educational materials","Barbering tools and supplies (case-dependent)","Transportation assistance (case-dependent)","Support services during training"]))
av += sec("sb", lbl("Step by Step")+tit("How to Use ACCES-VR at ABI")+
  ''.join(f'<div class="step"><div class="step-n">0{n}</div><div class="step-t">{t}</div><div class="step-b">{b}</div></div>' for n,t,b in [
   (1,"Check Eligibility","ACCES-VR serves individuals with disabilities that create a barrier to employment. Contact your local office to see if you qualify."),
   (2,"Apply to ACCES-VR","You'll be assigned a Vocational Rehabilitation Counselor who builds your Individualized Plan for Employment (IPE)."),
   (3,"List ABI as Your School","We provide all documentation your counselor needs."),
   (4,"ABI Coordinates","Once approved, ABI coordinates directly with ACCES-VR for tuition and covered costs."),
   (5,"Start Training","Begin your path to a Master Barber license — with financial barriers removed.")])+cta())
av += sec("sw", lbl("FAQ")+tit("Common Questions")+faq([
  ("What disabilities qualify?","ACCES-VR serves a wide range of physical, mental health, learning, sensory, and other disabilities. Eligibility is assessed case-by-case by your VR counselor."),
  ("Is there a cost to apply?","No. Applying to ACCES-VR and working with a counselor is free."),
  ("How long does approval take?","Typically several weeks after your initial application — start as early as possible."),
  ("Can ABI help with the process?","Yes. Our admissions team is experienced with ACCES-VR referrals and provides all necessary documentation.")]))
page("acces-vr","ACCES-VR Financial Assistance | American Barber Institute","New York State's ACCES-VR program may cover your barber school tuition at ABI if you have a disability. Learn what's covered and how to apply.",av)

# VETERANS
v = hero("GI Bill® & VA Education Benefits","ABI accepts VA education benefits. Veterans, service members, and eligible dependents can use their GI Bill® to train at ABI.","<a href='resources.html'>Resources</a> › Veterans")
v += sec("sw", lbl("Overview")+tit("Your Service Earns Your Education")+desc("We accept Post-9/11 GI Bill® benefits and other VA education programs to make your training affordable. Our admissions team is experienced with VA benefits and can certify your enrollment quickly.")+
  tit("What VA Benefits May Cover")+skills(["Tuition and program fees (up to 100% with Post-9/11 GI Bill®)","Monthly housing allowance (Post-9/11 GI Bill®)","Books and supplies stipend up to $1,000/year","Full tuition for eligible VR&amp;E (Ch.31) recipients","Monthly stipend for Montgomery GI Bill® recipients"]))
v += sec("sb", lbl("Programs")+tit("VA Education Benefit Programs")+
  '<div class="info"><h3>Post-9/11 GI Bill® (Ch. 33)</h3><p>Tuition &amp; fees up to 100%, monthly housing allowance, and a $1,000/year books stipend for those who served after Sept. 10, 2001.</p></div>'+
  '<div class="info"><h3>Montgomery GI Bill® (Ch. 30)</h3><p>Monthly education benefit for veterans who contributed while on active duty.</p></div>'+
  '<div class="info"><h3>VR&amp;E (Ch. 31)</h3><p>For veterans with service-connected disabilities — can cover full tuition plus a subsistence allowance.</p></div>'+
  '<div class="info"><h3>DEA (Ch. 35)</h3><p>Education benefits for eligible dependents of qualifying veterans.</p></div>'+
  '<div class="plan-note">*GI BILL® is a registered trademark of the U.S. Department of Veterans Affairs (VA). Eligibility and amounts are determined by the VA, not ABI.</div>')
v += sec("sw", lbl("Veterans FAQ")+tit("Common Questions")+faq([
  ("Is ABI approved to accept GI Bill® benefits?","Yes. ABI is an approved institution for VA education benefits. Contact admissions for our VA facility code."),
  ("How much of my tuition will the GI Bill® cover?","Under Post-9/11 (Ch.33) with 100% eligibility, tuition and fees are covered in full. Other programs pay a monthly stipend."),
  ("How long until benefits start?","After ABI certifies your enrollment, payment typically begins within 4–8 weeks."),
  ("Can dependents use benefits at ABI?","Yes — eligible dependents may use Ch.35 (DEA) or transferred Post-9/11 entitlements.")])+cta())
page("veterans","Veterans & GI Bill® Benefits | American Barber Institute","ABI accepts VA education benefits. Veterans, service members, and eligible dependents can use the Post-9/11 GI Bill® and other programs to train at ABI.",v)

# FAQS
fq = hero("Frequently Asked Questions","Everything you need to know about our programs, enrollment, tuition, and more.","<a href='index.html'>Home</a> › FAQs",btns=False)
fq += sec("sw", lbl("FAQs")+tit("Barber School Questions, Answered")+faq([
  ("How long does the program take?","The 500 Hour Master Barber Program can be completed in as little as 4 months depending on schedule. The 50 Hour Refresher is a 2-week intensive. The 3 Hour Contagious Diseases program is a single session."),
  ("When do new classes start?","New classes begin the first Monday of every month."),
  ("What schedules are available?","Plan A Morning (Mon–Fri 8AM–2PM), Plan B Afternoon (Mon–Fri 2PM–8PM), Plan C Weekend (Sat–Sun 9AM–7PM)."),
  ("What are the entrance requirements?","SSN card; HS Diploma/GED or ATB exam at ABI; at least 17; proof of address; photo ID; $500 down payment."),
  ("How much does the program cost?","The 500 Hour program starts at $4,600 (afternoon/weekend) or $5,600 (morning). The 50 Hour Refresher is $1,500. Payment plans available."),
  ("Do you offer payment plans?","Yes — flexible weekly plans after your down payment. Plan B: $500 down + 16×$250 + final $100."),
  ("What license will I receive?","You'll be prepared for the NY State Board of Barbering Exam and your Master Barber License."),
  ("Do you offer job placement?","Yes — our Job Placement Office helps graduates connect with employers and explore opportunities."),
  ("Where are your locations?","Manhattan: 48 West 39th Street, NY 10018. Bronx: 121 Westchester Square, NY 10461."),
  ("Do you accept GI Bill® or VA benefits?","Yes — Post-9/11 GI Bill® and VA education benefits are accepted."),
  ("What is ACCES-VR?","A NY State program that may fund vocational training for eligible individuals with disabilities."),
  ("Do I need to buy my own tools?","Yes — tools, books and supplies are purchased separately, from ABI or other suppliers."),
  ("Is ABI licensed by the state?","Yes — licensed by the New York State Department of Education, 30+ years in business."),
  ("Can I get a haircut at ABI?","Yes — affordable student haircuts (around $3). See the Haircuts page.")])+
  '<a href="tel:+12122902289" class="cta">Still Have Questions? Call (212) 290-2289 →</a>')
page("faqs","Frequently Asked Questions | American Barber Institute","Answers about ABI's barber programs, enrollment, tuition, payment plans, licensing, job placement, GI Bill® and ACCES-VR assistance, and student haircuts.",fq)

# JOBS
j = hero("We Help You Land Your Dream Job","Your journey doesn't end at graduation. Our dedicated job placement team connects you with top barbershops across NYC and beyond.","<a href='index.html'>Home</a> › Job Placement")
j += sec("sw", lbl("Job Placement")+tit("Career Placement Program")+kgrid([("90%+","Placement rate"),("500+","Partner shops"),("Free","Assistance")])+
  skills(["One-on-one career counseling","Resume and portfolio building guidance","Interview preparation and coaching","Direct connections to partner barbershops","Exclusive job listings for ABI graduates","Support for barbers opening their own shop"]))
j += sec("sb", '<div class="rcard"><div class="stars">★★★★★</div><div class="rtxt">"ABI didn\'t just train me to cut hair — they helped me find a shop and launch my career within two weeks of graduating."</div><div class="rauth"><div class="rav" style="background:#1252A3">JM</div><div><div class="rname">Jerrick M.</div><div class="rrole">ABI Graduate</div></div></div></div>'+cta())
page("jobs","Barber Job Placement | American Barber Institute NYC","ABI's job placement team connects graduates with top barbershops across NYC. 90%+ placement rate, 500+ partner shops, free placement assistance.",j)

# HAIRCUTS
hc = hero("Get a Haircut at ABI","Affordable student haircuts — just $3. Help our trainee barbers practice, reach their hours, and perfect their craft.","<a href='index.html'>Home</a> › $3 Haircuts",btns=False)
hc += '<a href="contact.html" style="text-decoration:none"><div class="haircut-bar"><div class="haircut-txt">$3 Student Haircuts<br><span style="font-size:11px;font-weight:600;opacity:.8">Public Welcome · Manhattan &amp; Bronx</span></div><div class="haircut-price">$3</div></div></a>'
hc += sec("sw", lbl("Simple Process")+tit("How It Works")+
  '<div class="step"><div class="step-n">01</div><div class="step-t">Sign Up</div><div class="step-b">Call or fill out our contact form. Walk-ins welcome based on availability.</div></div>'+
  '<div class="step"><div class="step-n">02</div><div class="step-t">Come In</div><div class="step-b">Visit during business hours. Students are supervised by experienced instructors.</div></div>'+
  '<div class="step"><div class="step-n">03</div><div class="step-t">Get Your Cut</div><div class="step-b">Describe your style and relax — classic cuts, fades, trims, all at great value.</div></div>')
hc += sec("sb", lbl("Menu")+tit("Styles Available")+'<div class="chips">'+"".join(f'<div class="chip">{x}</div>' for x in ["Classic Tapers","Low Fades","Mid Fades","High Fades","Caesars","Flat Tops","Shape Ups","Razor Lineups","Beard Trims","Shampoos","Blowouts","Mohawks","Afro","Pompadours","Bald Head Shaves","Scissor Cuts","Clipper Cuts","Fohawks"])+'</div>')
hc += sec("sw", lbl("Student Work")+tit("Fresh Cuts, Real Students")+'<div class="ggrid">'+"".join(f'<img class="gimg" src="assets/img/pics/abi-students-{n}.jpg" alt="Student haircut">' for n in ["006","007","008","009","010","011"])+'</div>'+ctao("See Our Gallery →","gallery.html"))
page("haircuts","Student Haircuts from $3 | American Barber Institute","Get an affordable $3 student haircut at ABI. Help trainee barbers practice and perfect their craft. Manhattan & Bronx, walk-ins welcome.",hc)

# GALLERY
gl = hero("Gallery","A look inside our school, our students, and the work they create.","<a href='index.html'>Home</a> › Gallery",btns=False)
gimgs=["pics/hair-art-mohawk.jpg","pics/graduation-1.jpeg","pics/barber-battle-trophy.png","pics/graduation-2.jpeg","pics/certificate-presentation.jpeg","pics/abi-students-008.jpg","pics/abi-students-011.jpg","pics/barbershop-full-shop.jpeg"]
gl += sec("sw", lbl("Photos")+tit("Life At ABI")+'<div class="ggrid">'+"".join(f'<img class="gimg" src="assets/img/{x}" alt="ABI gallery">' for x in gimgs)+'</div>')
gl += sec("sb", lbl("Video")+tit("Watch Us In Action")+
  '<div class="vt"><img src="https://i.ytimg.com/vi/TFpNNqsc_EA/hqdefault.jpg" alt="ABI"><div class="vplay">▶</div></div><div class="vcap">Become a Master Barber at ABI</div>'+
  '<div class="vt"><img src="https://i.ytimg.com/vi/ozV_RcSk0P4/hqdefault.jpg" alt="ABI"><div class="vplay">▶</div></div><div class="vcap">Inside the ABI classroom</div>'+cta())
page("gallery","Gallery | American Barber Institute Student Work","A look inside ABI — our school, our students, and the work they create. Photos and video of student work, campus life, graduations, and barber battles.",gl)

# PARTNERS
pt = hero("Where Our Graduates Work","Real shops. Real careers. One school behind every chair.","<a href='index.html'>Home</a> › Partner Shops")
pt += sec("sw", lbl("Our Partners")+tit("Partner Barbershops")+'<div class="chips">'+"".join(f'<div class="chip">✂ {x}</div>' for x in ["Diamond Fades Barbershop","Levels Barbershop","BK's Imperial Kutz Masters","Untouchable Cutz","Expo Gentlemen Salon","Otis &amp; Finn","NYC Barber Shop Museum","+ Many more NYC shops"])+'</div>'+desc("ABI maintains a full-time job placement office. Many students graduate with multiple job offers waiting."))
pt += sec("sb", tit("Own a Shop? Hire ABI Graduates")+desc("Connect with our job placement office to post openings and meet exam-ready, professionally trained barbers.")+ctao("Job Placement →","jobs.html")+cta())
page("partners","Partner Shops | American Barber Institute","Where ABI graduates work — real barbershops across New York hiring ABI-trained barbers, from Diamond Fades and Levels to the NYC Barber Shop Museum.",pt)

# BLOG
bl = hero("The ABI Blog","Careers, licensing, financial aid, and stories from NYC's only dedicated barber school.","<a href='index.html'>Home</a> › Blog",btns=False)
posts=[("How to Become a Licensed Barber in New York","Your step-by-step roadmap from the 500-hour program to passing the NY State Board.","course-500-master.html"),
("Using Your GI Bill® for Barber School","How veterans and dependents apply VA education benefits at ABI.","veterans.html"),
("Choosing the Right Class Schedule","Morning, afternoon, or weekend — pick the plan that fits your life.","schedule.html"),
("Why $3 Student Haircuts Matter","How affordable cuts help trainees reach their hours and serve the neighborhood.","haircuts.html"),
("Meet King David: 50 Years Behind the Chair","The story of NYC's longest-serving barber instructor.","instructors.html"),
("Life After Graduation: Job Placement","How our placement office connects graduates with 500+ partner shops.","jobs.html")]
bl += sec("sw", lbl("Latest")+tit("News &amp; Tips")+"".join(f'<a class="lkcard" href="{h}"><div class="lkt">{t}</div><div class="lkd">{d}</div></a>' for t,d,h in posts)+cta())
page("blog","Blog | American Barber Institute","News, tips, and stories from the American Barber Institute — barbering careers, NY State licensing, financial aid, and life at NYC's only dedicated barber school.",bl)

# CONTACT (with form)
co = hero("Contact ABI","Have questions about enrollment or our programs? Call, email, or send a message — we'll respond fast.","<a href='index.html'>Home</a> › Contact",btns=False)
co += sec("sw", lbl("Reach Us")+tit("Get in Touch")+
  '<div class="info"><h3>Manhattan Campus</h3><p>48 West 39th Street, New York, NY 10018<br><a href="tel:+12122902289" style="color:#1252A3;font-weight:800;text-decoration:none">(212) 290-2289</a></p></div>'+
  '<div class="info"><h3>Bronx Campus</h3><p>121 Westchester Square, Bronx, NY 10461<br><a href="tel:+17186760640" style="color:#1252A3;font-weight:800;text-decoration:none">(718) 676-0640</a> · <a href="tel:+12122900278" style="color:#1252A3;font-weight:800;text-decoration:none">(212) 290-0278 ES</a></p></div>'+
  '<div class="info"><h3>Email &amp; Hours</h3><p><a href="mailto:admission@abi.edu" style="color:#1252A3;font-weight:800;text-decoration:none">admission@abi.edu</a><br>Mon–Fri 8AM–8PM · Sat–Sun 9AM–7PM</p></div>')
co += FORM
page("contact","Contact ABI | American Barber Institute","Contact American Barber Institute. Manhattan & Bronx campuses. Call (212) 290-2289, email admission@abi.edu, or apply online.",co)

# REGISTER (with form)
rg = hero("Two Ways to Get Started","Call us directly or fill out the pre-registration form. New classes begin the first Monday of every month.","<a href='index.html'>Home</a> › Enroll",btns=False)
rg += sec("sw", lbl("Option 01")+tit("Call or Visit Us")+
  '<div class="info"><h3>Speak with a licensed agent</h3><p><a href="tel:+12122902289" style="color:#1252A3;font-weight:800;text-decoration:none">English (212) 290-2289</a><br><a href="tel:+12122900278" style="color:#1252A3;font-weight:800;text-decoration:none">Spanish (212) 290-0278</a><br><a href="tel:+17186760640" style="color:#1252A3;font-weight:800;text-decoration:none">Bronx (718) 676-0640</a><br><br>48 West 39th Street, New York, NY 10018<br>121 Westchester Square, Bronx, NY 10461</p></div>')
rg += FORM.replace('id="reserve"','id="reserve"').replace('Reserve Your Spot','Option 02 — Pre-Registration')
page("register","Enroll / Pre-Registration | American Barber Institute","Two ways to get started at ABI — call a licensed agent or complete the online pre-registration form. New classes begin the first Monday of every month.",rg)

# LOGIN
lg = hero("Student Sign In","Access your enrollment, schedule, and progress.","<a href='index.html'>Home</a> › Sign In",btns=False)
lg += '<section class="form-sec"><div class="form-box"><div class="form-title">Student Sign In</div><label class="flbl">Email or Student ID</label><input class="fi" type="text" placeholder="you@email.com"><label class="flbl">Password</label><input class="fi" type="password" placeholder="••••••••"><button class="fsub" onclick="document.getElementById(\'ln\').style.display=\'block\';return false;">Sign In</button><div id="ln" class="fcon" style="display:none;color:#9FE1CB">Student portal coming soon — call (212) 290-2289 for account help.</div><div class="fadv"><a href="register.html" style="color:#9FE1CB;text-decoration:none">New student? Pre-register here →</a></div></div></section>'
page("login","Student Sign In | American Barber Institute","Sign in to your American Barber Institute student account.",lg)

# PRIVACY
pv = hero("Privacy Policy","How American Barber Institute collects, uses, and protects your information.","<a href='index.html'>Home</a> › Privacy",btns=False)
pv += sec("sw", desc("American Barber Institute (ABI) respects your privacy. We collect contact information you submit through our forms (name, phone, email, preferred location and language, and your message) solely to respond to your inquiry and provide admissions information.")+
  tit("How We Use Your Information")+skills(["To contact you about programs, schedules and enrollment","To respond to your questions via phone, SMS or email","We do not sell your personal information"])+
  tit("Contact")+desc("Questions about this policy? Email <a href='mailto:admission@abi.edu' style='color:#1252A3;font-weight:700'>admission@abi.edu</a> or call (212) 290-2289."))
page("privacy","Privacy Policy | American Barber Institute","How American Barber Institute collects, uses, and protects your information.",pv)
print("batch 3 done")
