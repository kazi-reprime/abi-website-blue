from gen import *
def sec(c,i): return f'<section class="sec {c}">{i}</section>'
def lbl(t): return f'<div class="slbl">{t}</div>'
def tit(t): return f'<div class="stit">{t}</div>'
def desc(t): return f'<div class="sdesc">{t}</div>'
def cta(t="Apply Now →",h="contact.html"): return f'<a href="{h}" class="cta">{t}</a>'
def ctao(t,h): return f'<a href="{h}" class="cta-out">{t}</a>'
def skills(items): return "".join(f'<div class="skill"><div class="ski">✂</div>{i}</div>' for i in items)
def reqs(items): return '<ul class="req-list">'+"".join(f'<li><span class="req-icon">›</span><span>{i}</span></li>' for i in items)+'</ul>'
def kgrid(cells): return '<div class="kgrid">'+"".join(f'<div class="kbox"><div class="kn">{n}</div><div class="kl">{l}</div></div>' for n,l in cells)+'</div>'
def plan(badge,n,s,h,p,d,ft=False):
    b=f'<div class="plan-badge">{badge}</div>' if badge else ''
    return f'<div class="plan{" ft" if ft else ""}">{b}<div class="plan-n">{n}</div><div class="plan-s">{s}</div><div class="plan-h">{h}</div><div class="plan-p">{p}</div><div class="plan-d">{d}</div><a href="contact.html" class="plan-btn">Enroll Now →</a></div>'

# INSTRUCTORS
def ic(av,clr,name,role,bio): return f'<div class="icard"><div class="iav" style="background:{clr}">{av}</div><div class="iname">{name}</div><div class="irole">{role}</div><div class="ibio">{bio}</div></div>'
i = hero("Our Instructors","Learn from master barbers who bring decades of real-world experience into every session. Every instructor is an ABI graduate.","<a href='about.html'>About</a> › Our Instructors")
man = '<div class="icampus">🗽 Manhattan Campus</div><div class="igrid">'+ \
 ic("KD","#0D2B4E","King David Ayeoribe","Lead Director · 50+ Yrs","Longest-serving barber instructor in NYC. NYSED licensed. 30+ years teaching.")+ \
 ic("HB","#1252A3","Harold &quot;Barkim&quot; Brown","Instructor · Emmy 2024","2024 NY Emmy winner. Known as the best one-armed barber in the world.")+ \
 ic("BB","#2980b9","Barry Brown","Instructor · Manhattan","Mentored by Harold Brown. Real barbershop experience.")+ \
 ic("FL","#16a085","Freddie Liciaga","Instructor · EN / ES","Bilingual English &amp; Spanish instructor; state-board prep specialist.")+ \
 ic("BS","#8e44ad","Benny Santamaria","Instructor · EN / ES","Youngest instructor. Bilingual EN/ES. Impeccable shaving skills.")+ \
 ic("RC","#c0392b","Richard Cancel","Instructor · EN / ES","Bilingual. Barbering &amp; tattooing expertise.")+'</div>'
brx = '<div class="icampus">🏙 Bronx Campus</div><div class="igrid">'+ \
 ic("TQ","#1a5276","Truth &quot;The Barber Artist&quot; Quinones","Founding Director · 40+ Yrs","Former NYS Board Examiner. Andis brand partner. Est. 1985.")+ \
 ic("OR","#117a65","Osvaldy &quot;Mr. O&quot; Rodriguez","Instructor · Bronx","Licensed Master Barber at 19. 8+ years. Award-winning competitor.")+ \
 '<div class="icard icenter"><div class="iav" style="background:#1f618d">NV</div><div class="iname">Noah Vera</div><div class="irole">Instructor · EN / ES</div><div class="ibio">Licensed Master Barber at 19. Bilingual EN/ES.</div></div>'+'</div>'
i += sec("sw", lbl("Our Instructors")+tit("Every Instructor is an ABI Graduate")+desc("Working professionals who bring decades of real barbering experience into every class.")+man+brx)
i += sec("sb", lbl("How We Teach")+tit("Our Teaching Philosophy")+
  '<div class="step"><div class="step-n">01</div><div class="step-t">Hands-On From the First Weeks</div><div class="step-b">Students work on real clients early, building confidence through practice.</div></div>'+
  '<div class="step"><div class="step-n">02</div><div class="step-t">Real-World Ready</div><div class="step-b">Every technique reflects what students need in a professional barbershop.</div></div>'+
  '<div class="step"><div class="step-n">03</div><div class="step-t">Mentorship &amp; Support</div><div class="step-b">Instructors support you throughout training and NY State Board Exam prep.</div></div>'+cta())
page("instructors","Our Instructors | American Barber Institute","Meet ABI's master barber instructors — King David, Harold 'Barkim' Brown, Truth Quinones and the full Manhattan & Bronx teaching teams.",i)

# VIRTUAL TOUR
vt = hero("Virtual Tour","Explore our state-of-the-art 3,000 sq ft two-floor facility in Midtown Manhattan — drag, zoom, and look around.","<a href='about.html'>About</a> › Virtual Tour", btns=False)
vt += sec("sw", lbl("Step Inside")+tit("Take a 360° Walkthrough")+
  '<div style="border-radius:10px;overflow:hidden;aspect-ratio:16/10;background:#111;margin-bottom:10px"><iframe src="https://www.google.com/maps/embed?pb=!4v1714867200000!6m8!1m7!1sAF1QipMn4z36MWL8RnpmT7OHGNtlSBoWp57C-9zZCjtF!2m2!1d40.7524073!2d-73.9845358!3f215.05!4f-4.71!5f0.7820865974627469" width="100%" height="100%" style="border:0;display:block" allowfullscreen loading="lazy"></iframe></div>'+
  '<a class="glink" href="https://www.google.com/maps/@40.7524073,-73.9845358,3a,66.6y,215.05h,85.29t/data=!3m6!1e1!3m4!1sAF1QipMn4z36MWL8RnpmT7OHGNtlSBoWp57C-9zZCjtF!2e10!7i13312!8i6656">Open full tour in Google Maps →</a>')
vt += sec("sb", lbl("Watch the Story")+tit("Become a Master Barber at ABI")+
  '<div style="border-radius:10px;overflow:hidden;aspect-ratio:16/9;background:#111;margin-bottom:10px"><iframe src="https://www.youtube.com/embed/TFpNNqsc_EA" width="100%" height="100%" style="border:0;display:block" allowfullscreen loading="lazy"></iframe></div>'+cta())
page("virtual-tour","Virtual Tour | American Barber Institute","Take a 360° virtual tour of ABI. Explore our 3,000 sq ft two-floor Midtown Manhattan facility before you visit in person.",vt)

# COURSES (index)
c = hero("Barber Programs — NYC","Licensed by the New York State Department of Education. New classes start the first Monday of every month.","<a href='index.html'>Home</a> › Programs", btns=False)
c += sec("sw", lbl("Programs")+tit("Choose Your Path")+
  '<a class="lkcard" href="course-500-master.html"><div class="lkt">500 Hour Master Barber Program</div><div class="lkd">Flagship · ~4 months · from $4,600 · full NY State Board prep.</div></a>'+
  '<a class="lkcard" href="course-500-bronx.html"><div class="lkt">500 Hour Master Barber — Bronx</div><div class="lkd">The full Master Barber program at our Bronx campus.</div></a>'+
  '<a class="lkcard" href="course-50-refresher.html"><div class="lkt">50 Hour Barber Refresher</div><div class="lkd">2-week intensive for licensed pros · $1,500 · certificate.</div></a>'+
  '<a class="lkcard" href="course-3-contagious.html"><div class="lkt">3 Hour Contagious Diseases</div><div class="lkd">Required HIV/Contagious Diseases course for the NY State Board.</div></a>')
c += sec("sb", lbl("Why Choose ABI")+tit("Everything You Need to Succeed")+skills([
  "NY State licensed by the Dept. of Education","Hands-on with real clients from the first few weeks","Morning, Afternoon &amp; Weekend schedules",
  "Dedicated job placement office","ACCES-VR, Post-9/11 GI Bill® &amp; VA benefits accepted","New classes every first Monday of the month"])+cta())
page("courses","Barber Training Programs | American Barber Institute NYC","Explore ABI's NY State licensed barber programs: 500 Hour Master Barber, 50 Hour Refresher, and 3 Hour Contagious Diseases.",c)

# COURSE 500 MASTER
m = hero("500 Hour Master Barber Program","Become a licensed Master Barber in New York in as little as 4 months. Comprehensive hands-on training and full NY State Board Exam prep.","<a href='courses.html'>Programs</a> › 500 Hour Master Barber")
m += sec("sw", kgrid([("~4 Mo","Duration"),("500","Total Hours"),("$4,600","Starting Price")])+
  lbl("Overview")+tit("About the Program")+desc("Over four months, students immerse themselves in theory and practical skills — sanitation, sterilization, barber history, laws, and shop management — with hands-on experience on a diverse clientele. We prepare you fully for the New York State Board Exam, and connect you with our job placement office on completion.")+
  '<div class="chips">'+"".join(f'<div class="chip">✂ {x}</div>' for x in ["Classic Tapers","Low/Mid/High Fades","Razor Lineups","Pompadours","Beard Trims","Shape Ups","Clipper Over Comb","Scissor Over Comb","Shaving &amp; Facial Massage"])+'</div>')
m += sec("sb", lbl("Curriculum")+tit("Course Modules")+
  '<div class="mod"><div class="mod-n">01 · Theory &amp; Science</div>'+skills(["Sanitation &amp; Sterilization","Barber History","NY State Laws &amp; Regulations","Shop Management","Professional Ethics"])+'</div>'+
  '<div class="mod"><div class="mod-n">02 · Cutting Techniques</div>'+skills(["Fades (Low, Mid, High)","Tapers &amp; Classic Cuts","Clipper Over Comb","Scissor Over Comb","Flat Tops &amp; High-Top Fades"])+'</div>'+
  '<div class="mod"><div class="mod-n">03 · Styling &amp; Finishing</div>'+skills(["Razor Lineups &amp; Shape Ups","Blowouts &amp; Pompadours","Afro &amp; Mohawk Styling","Beard Trims","Shampoo &amp; Conditioning"])+'</div>'+
  '<div class="mod"><div class="mod-n">04 · Shaving &amp; Skin Care</div>'+skills(["Straight Razor Shaving","Facial Massage","Hot Towel Treatments","Skin &amp; Scalp Analysis","Safety &amp; Hygiene"])+'</div>'+
  '<div class="mod"><div class="mod-n">05 · Business &amp; Career</div>'+skills(["Client Consultation","Barbershop Operations","Building a Clientele","Job Placement Prep","NY State Board Exam Prep"])+'</div>')
m += sec("sw", lbl("Tuition")+tit("Flexible Payment Plans")+desc("Students purchase their own tools, books and supplies. A list of acceptable tools is provided upon registration.")+
  plan("","Plan A — Morning","Mon–Fri · 8:00 AM – 2:00 PM","30 hrs/week · 17 weeks","$5,600","$500 down (incl. $100 registration) + 17 weekly payments of $300")+
  plan("MOST POPULAR","Plan B — Afternoon","Mon–Fri · 2:00 PM – 8:00 PM","30 hrs/week · 17 weeks","$4,600","$500 down (incl. $100 registration) + 16 weekly payments of $250 + final $100",ft=True)+
  plan("","Plan C — Weekend","Sat & Sun · 9:00 AM – 7:00 PM","18 hrs/week · 27 weeks","$4,600","$500 down (incl. $100 registration) + 27 weekly payments of $150")+
  '<div class="plan-note">Additional fees: books, tools and supplies. ACCES-VR financial assistance available. Post-9/11 GI Bill® and VA benefits accepted.</div>'+cta())
page("course-500-master","500 Hour Master Barber Program | American Barber Institute","Become a licensed Master Barber in NY in as little as 4 months. 500-hour hands-on training, flexible schedules, job placement, NY State Board prep. From $4,600.",m)

# COURSE 500 BRONX
b = hero("500 Hour Master Barber — Bronx","The full Master Barber curriculum at our Bronx campus on Westchester Square — led by Founding Director Truth Quinones.","<a href='courses.html'>Programs</a> › 500 Hour Master Barber — Bronx")
b += sec("sw", kgrid([("~4 Mo","Duration"),("500","Total Hours"),("$4,600","From")])+
  lbl("Overview")+tit("About the Bronx Program")+desc("The same comprehensive 500-hour curriculum — sanitation, cutting, styling, shaving, business, and full NY State Board Exam prep — in the heart of Westchester Square. Led by Truth &quot;The Barber Artist&quot; Quinones (40+ years, former NYS Board Examiner) with bilingual instructors Osvaldy Rodriguez and Noah Vera.")+
  reqs(["Morning, Afternoon &amp; Weekend schedules","Bilingual instruction (English &amp; Spanish)","ACCES-VR &amp; GI Bill® accepted","121 Westchester Square, Bronx, NY 10461 · (718) 676-0640"])+cta())
page("course-500-bronx","500 Hour Master Barber — Bronx | American Barber Institute","The full 500 Hour Master Barber Program at ABI's Bronx campus, led by Founding Director Truth 'The Barber Artist' Quinones.",b)

# COURSE 50 REFRESHER
r = hero("Barber Refresher Program","A two-week, 50-hour intensive for licensed professionals. Sharpen your skills and prep for the NY State Board.","<a href='courses.html'>Programs</a> › 50 Hour Refresher")
r += sec("sw", kgrid([("2 Wks","Duration"),("50","Hours"),("$1,500","Tuition")])+
  lbl("Overview")+tit("About the Program")+desc("Designed for licensed individuals, cosmetologists, hairdressers, and apprentices. Covers the most in-demand techniques plus NY State Board prep. Includes a 50 Hour Refresher certificate and job placement support.")+
  skills(["Classical haircutting","Straight razor shaving","Fades &amp; tapers · scissor over comb","Modern hairstyles &amp; trends","Beard trims &amp; shape ups","NY State Board Exam preparation","Sanitation &amp; sterilization review","Client consultation"]))
r += sec("sb", tit("Who Is This For?")+reqs(["Licensed barbers upgrading skills","Licensed cosmetologists transitioning to barbering","Hairdressers seeking barber certification","Barber apprentices needing additional hours"])+cta())
page("course-50-refresher","50 Hour Barber Refresher Program | American Barber Institute","A two-week, 50-hour intensive for licensed barbers, cosmetologists, and apprentices. $1,500, certificate included, NY State Board prep.",r)

# COURSE 3 CONTAGIOUS
ct = hero("Contagious Diseases Program","The required HIV/Contagious Diseases course for the NY State Board of Barbering Exam. Open to all prospective and current students.","<a href='courses.html'>Programs</a> › 3 Hour Contagious Diseases")
ct += sec("sw", kgrid([("3 Hrs","Duration"),("1","Session"),("Required","NY Board")])+
  lbl("Overview")+tit("About the Program")+desc("A mandatory 3-hour course for the NY State Board of Barbering Exam covering HIV/AIDS awareness, bloodborne pathogen safety, and NY State compliance standards.")+
  skills(["HIV/AIDS awareness &amp; prevention","Bloodborne pathogen safety","Contagious disease identification","Sanitation &amp; sterilization standards","NY State regulations compliance","Client &amp; workplace safety"])+ctao("Get Pricing &amp; Register →","contact.html"))
page("course-3-contagious","3 Hour Contagious Diseases Program | American Barber Institute","The required HIV/Contagious Diseases course for the New York State Board of Barbering Exam. A single 3-hour session.",ct)
print("batch 2 done")
