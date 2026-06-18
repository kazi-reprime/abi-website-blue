from gen import *

def sec(cls, inner): return f'<section class="sec {cls}">{inner}</section>'
def lbl(t): return f'<div class="slbl">{t}</div>'
def tit(t): return f'<div class="stit">{t}</div>'
def desc(t): return f'<div class="sdesc">{t}</div>'
def cta(t="Apply Now →", href="contact.html"): return f'<a href="{href}" class="cta">{t}</a>'
def ctao(t, href): return f'<a href="{href}" class="cta-out">{t}</a>'
def skills(items): return "".join(f'<div class="skill"><div class="ski">✂</div>{i}</div>' for i in items)
def reqs(items): return '<ul class="req-list">'+"".join(f'<li><span class="req-icon">›</span><span>{i}</span></li>' for i in items)+'</ul>'

# ---------- ABOUT ----------
about = hero("American Barber Institute","New York's only dedicated barber school — changing lives for over 30 years in Manhattan and the Bronx.","<a href='index.html'>Home</a> › About")
about += sec("sw", lbl("Our Story")+tit("Our Mission")+desc("At American Barber Institute, we're dedicated to grooming education and professional development. Licensed by the New York State Department of Education, we've served the New York community for over 30 years.")+
  "<div class='skill'><div class='ski'>✂</div>Over four months, students master theory and practical skills</div>"+
  "<div class='skill'><div class='ski'>✂</div>Sanitation, sterilization, barber history, laws & shop management</div>"+
  "<div class='skill'><div class='ski'>✂</div>Graduates ready for any barber shop — or to open their own</div>")
about += sec("sb", tit("Why Choose ABI?")+skills([
  "Licensed by the New York State Department of Education","30+ years serving the NYC community",
  "State-of-the-art 3,000 sq ft two-floor Midtown facility","Expert instructors — King David has 30+ years experience",
  "Hands-on training with real clients within the first few weeks","Full-time job placement office for graduates",
  "Financial assistance: ACCES-VR, Post-9/11 GI Bill®, VA benefits","Morning, Afternoon, and Weekend schedules"])+ctao("How to Get Started →","how-to-get-started.html"))
about += sec("sw", lbl("Admissions")+tit("Entrance Requirements")+reqs([
  "Social Security Card","High School Diploma (HSD) or GED — or pass the ATB exam at ABI","At least 17 years of age",
  "Proof of residential address","Valid photo ID or Driver's License","$500 Down Payment"]))
about += sec("sb", lbl("Explore")+tit("Explore More About ABI")+
  '<a class="lkcard" href="how-to-get-started.html"><div class="lkt">How to Get Started</div><div class="lkd">Step-by-step guide to enrolling at ABI.</div></a>'+
  '<a class="lkcard" href="skills-and-techniques.html"><div class="lkt">Skills &amp; Techniques</div><div class="lkd">Every cut, style and technique you will master.</div></a>'+
  '<a class="lkcard" href="instructors.html"><div class="lkt">Our Instructors</div><div class="lkd">Meet the expert team behind our programs.</div></a>'+
  '<a class="lkcard" href="virtual-tour.html"><div class="lkt">Virtual Tour</div><div class="lkd">Take a virtual look inside our Manhattan facility.</div></a>')
page("about","About Us | American Barber Institute","Learn about American Barber Institute — New York's only dedicated barber school, changing lives for over 30 years. NY State licensed, hands-on training, job placement.",about)

# ---------- HOW TO GET STARTED ----------
g = hero("How to Get Started","Enrolling at ABI is simple. Follow these six steps to become a licensed Master Barber in New York.","<a href='about.html'>About</a> › How to Get Started")
steps=[("01","Call or Visit Us","Contact ABI by phone or visit our Manhattan or Bronx location. Our staff answers all your questions about programs, schedules, and costs."),
("02","Choose Your Program &amp; Schedule","Pick the 500 Hour Master Barber Program and a schedule — Morning, Afternoon, or Weekend. New classes start the first Monday of every month."),
("03","Gather Your Documents","Prepare all required documents before enrollment for a smooth, fast admission."),
("04","Submit Pre-Registration","Fill out and submit your pre-registration online or in person. Our team reviews it promptly."),
("05","Make Your Down Payment","Secure your seat with a $500 down payment (includes the $100 registration fee). Payment plans available."),
("06","Start Your Training","Begin hands-on training with real clients within the first few weeks. ~4 months for the 500-hour program.")]
g += sec("sw", lbl("Simple Process")+tit("Six Steps to Enroll")+"".join(f'<div class="step"><div class="step-n">{n}</div><div class="step-t">{t}</div><div class="step-b">{b}</div></div>' for n,t,b in steps)+cta("Apply Now →"))
g += sec("sb", lbl("Documents Needed")+tit("Entrance Requirements")+reqs([
  "Social Security Card (original or certified copy)","High School Diploma or GED — or pass the ATB exam at ABI","Age 17 or older",
  "Proof of residential address","Valid photo ID or Driver's License","$500 down payment (includes $100 registration fee)"]))
page("how-to-get-started","How to Get Started | American Barber Institute","Enrolling at ABI is simple. Follow six steps to become a licensed Master Barber in New York. New classes begin the first Monday of every month.",g)

# ---------- SKILLS & TECHNIQUES ----------
s = hero("Skills &amp; Techniques","A complete, professional skill set — from timeless classics to modern trending styles.","<a href='about.html'>About</a> › Skills &amp; Techniques")
groups=[("Classic Cuts",["Classic Tapers","Caesars","Classical Haircuts","Flat Tops","Bald Heads"]),
("Fades &amp; Modern Styles",["Low Fades","Mid Fades","High Fades","High-Top Fades","Fohawks","Mohawks","Afro"]),
("Styling &amp; Finishing",["Pompadours","Blowouts","Shape Ups","Razor Lineups","Shampoos &amp; Conditioning"]),
("Shaving &amp; Skin Care",["Straight Razor Shaving","Beard Trims &amp; Shaping","Facial Massage","Hot Towel Treatments","Skin &amp; Scalp Analysis"]),
("Advanced Techniques",["Clipper Over Comb","Scissor Over Comb","Safety &amp; Hygiene","Client Consultation"])]
inner = lbl("Full Curriculum")+tit("Complete Curriculum Overview")+desc("Master every technique from the fundamentals to advanced styling — all in one 500-hour program.")
for gt,items in groups:
    inner += f'<div class="mod"><div class="mod-n">{gt.upper()}</div>'+"".join(f'<div class="skill"><div class="ski">✂</div>{i}</div>' for i in items)+'</div>'
inner += ctao("View the 500 Hour Program →","course-500-master.html")
s += sec("sw", inner)
s += sec("sb", lbl("See It in Action")+tit("Watch Our Students Work")+
  '<div class="vt"><img src="https://i.ytimg.com/vi/iU0fUj3a8uw/hqdefault.jpg" alt="ABI training"><div class="vplay">▶</div></div><div class="vcap">ABI training session</div>'+
  '<div class="vt"><img src="https://i.ytimg.com/vi/5tTUkkVqOOE/hqdefault.jpg" alt="Barber techniques"><div class="vplay">▶</div></div><div class="vcap">Barber techniques demo</div>'+cta())
page("skills-and-techniques","Skills & Techniques | American Barber Institute","The complete ABI barber curriculum — classic cuts, fades, styling, shaving & skin care, and advanced techniques mastered in the 500-hour program.",s)

print("batch 1 done")
