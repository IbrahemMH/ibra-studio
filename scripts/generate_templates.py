# -*- coding: utf-8 -*-
"""Generate full bilingual Ibra Studio templates."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TDIR = ROOT / "templates"

# Common shell pieces
def shell(title, fonts, css, body, dict_js, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} · Ibra Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{fonts}" rel="stylesheet" />
  {extra_head}
  <style>
{css}
  </style>
</head>
<body>
  <div class="topbar">
    <a class="back" href="../../index.html" data-i18n="back">← Ibra Studio</a>
    <div class="lang">
      <button type="button" class="lang-btn active" data-lang="en">EN</button>
      <button type="button" class="lang-btn" data-lang="ar">ع</button>
    </div>
  </div>
{body}
  <script src="../shared/lang.js"></script>
  <script>
    IbraLang.init({dict_js});
  </script>
</body>
</html>
"""

BASE_CSS = """
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:var(--body),system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh}}
html[dir="rtl"] body{{font-family:"IBM Plex Sans Arabic",var(--body),system-ui,sans-serif}}
a{{color:inherit;text-decoration:none}}
.wrap{{width:min(100% - 2rem,var(--max,1040px));margin:0 auto}}
.topbar{{position:sticky;top:0;z-index:50;display:flex;justify-content:space-between;align-items:center;padding:.65rem 1rem;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}}
.back{{font-size:.85rem;font-weight:600;opacity:.85}}
.lang{{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}}
.lang-btn{{border:0;background:transparent;color:var(--muted);padding:.35rem .7rem;cursor:pointer;font-weight:700;font-size:.8rem}}
.lang-btn.active{{background:var(--accent-soft,rgba(255,255,255,.08));color:var(--accent)}}
nav.site{{display:flex;justify-content:space-between;align-items:center;padding:1.1rem 0;gap:1rem}}
.brand{{font-family:var(--display),serif;font-weight:700;font-size:1.25rem;letter-spacing:-.02em}}
.nav-links{{display:flex;gap:1.1rem;list-style:none;color:var(--muted);font-size:.92rem;flex-wrap:wrap}}
.btn{{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;padding:.75rem 1.2rem;font-weight:700;border:0;cursor:pointer}}
.btn-a{{background:var(--accent);color:var(--on-accent,#111)}}
.btn-g{{background:transparent;border:1px solid var(--line);color:var(--text)}}
.hero{{padding:2.5rem 0 2rem}}
.kicker{{color:var(--accent);font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:.75rem;margin-bottom:.75rem}}
h1{{font-family:var(--display),serif;font-size:clamp(2.1rem,5vw,3.4rem);line-height:1.05;letter-spacing:-.03em;margin-bottom:.85rem}}
.lead{{color:var(--muted);max-width:34rem;margin-bottom:1.35rem;font-size:1.05rem}}
.cta{{display:flex;flex-wrap:wrap;gap:.6rem;margin-bottom:1.5rem}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;padding:1rem 0 3rem}}
.grid2{{display:grid;grid-template-columns:1.1fr .9fr;gap:1.5rem;align-items:center}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.2rem}}
.card h3{{font-family:var(--display),serif;font-size:1.2rem;margin-bottom:.4rem}}
.card p{{color:var(--muted);font-size:.93rem}}
.price{{display:block;margin-top:.65rem;font-weight:800;color:var(--accent)}}
.panel{{border-radius:22px;border:1px solid var(--line);min-height:280px;background:var(--panel)}}
.section{{padding:1rem 0 3rem}}
.section h2{{font-family:var(--display),serif;font-size:1.7rem;margin-bottom:1rem;letter-spacing:-.02em}}
.footer{{border-top:1px solid var(--line);padding:1.5rem 0 2.5rem;color:var(--muted);font-size:.9rem;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.75rem}}
@media(max-width:800px){{.grid3,.grid2{{grid-template-columns:1fr}}.nav-links{{display:none}}}}
"""

TEMPLATES = [
  # ---- GYMS ----
  {
    "id": "gym-iron",
    "title": "Iron Forge Gym",
    "fonts": "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Source+Sans+3:wght@400;600;700&display=swap",
    "vars": "--bg:#0a0a0b;--text:#f4f4f5;--muted:#a1a1aa;--card:#141416;--line:rgba(255,255,255,.1);--accent:#ef4444;--on-accent:#fff;--accent-soft:rgba(239,68,68,.15);--panel:linear-gradient(145deg,#1c1c1f,#0a0a0b 55%,#3f0d0d);--display:'Bebas Neue';--body:'Source Sans 3';--max:1080px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Classes", "nav2": "Trainers", "nav3": "Pricing", "nav4": "Join",
      "kicker": "Amman · Strength · 24/7 access", "h1": "Forge a stronger you.",
      "lead": "Iron Forge is a serious training floor — power racks, coaches, and memberships built for results.",
      "cta1": "Start free week", "cta2": "View classes",
      "s_title": "Memberships", "c1t": "Starter", "c1p": "Gym floor + locker. Perfect to begin.", "c1pr": "29 JOD / mo",
      "c2t": "Athlete", "c2p": "Classes + coach check-ins twice a month.", "c2pr": "49 JOD / mo",
      "c3t": "Elite", "c3p": "Unlimited classes, plan, and guest passes.", "c3pr": "79 JOD / mo",
      "f1": "Open 24/7", "f2": "Pro coaches", "foot": "Iron Forge Gym · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الحصص", "nav2": "المدربين", "nav3": "الأسعار", "nav4": "انضم",
      "kicker": "عمّان · قوة · دخول 24/7", "h1": "اصنع نسخة أقوى منك.",
      "lead": "آيرون فورج صالة جدية — أجهزة قوة، مدربين، وعضويات مصممة للنتائج.",
      "cta1": "أسبوع مجاني", "cta2": "عرض الحصص",
      "s_title": "العضويات", "c1t": "مبتدئ", "c1p": "صالة + خزانة. مثالية للبداية.", "c1pr": "29 دينار / شهر",
      "c2t": "رياضي", "c2p": "حصص + متابعة مدرب مرتين شهرياً.", "c2pr": "49 دينار / شهر",
      "c3t": "نخبة", "c3p": "حصص بلا حدود وخطة وتذاكر ضيوف.", "c3pr": "79 دينار / شهر",
      "f1": "مفتوح 24/7", "f2": "مدربون محترفون", "foot": "نادي آيرون فورج · قالب من Ibra Studio",
    },
    "layout": "gym",
  },
  {
    "id": "gym-flow",
    "title": "Flow Wellness",
    "fonts": "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Outfit:wght@400;500;600&display=swap",
    "vars": "--bg:#f7f3ee;--text:#1f1a17;--muted:#6f655c;--card:#fffdf9;--line:#e7ddd2;--accent:#2f6f5e;--on-accent:#fff;--accent-soft:rgba(47,111,94,.12);--panel:linear-gradient(160deg,#d9ebe3,#f7f3ee 45%,#c9b8a4);--display:'Cormorant Garamond';--body:'Outfit';--max:1040px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Yoga", "nav2": "Pilates", "nav3": "Schedule", "nav4": "Book",
      "kicker": "Mind · Body · Breath", "h1": "Move gently. Feel stronger.",
      "lead": "Flow Wellness is a calm studio for yoga, pilates, and recovery — book your next class in minutes.",
      "cta1": "Book a class", "cta2": "See schedule",
      "s_title": "Popular sessions", "c1t": "Morning flow", "c1p": "45 min vinyasa for all levels.", "c1pr": "12 JOD",
      "c2t": "Core pilates", "c2p": "Reformer-inspired mat work.", "c2pr": "14 JOD",
      "c3t": "Restore", "c3p": "Stretch, breathwork, soft lighting.", "c3pr": "10 JOD",
      "f1": "Small groups", "f2": "EN + AR coaches", "foot": "Flow Wellness · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "يوغا", "nav2": "بيلاتس", "nav3": "الجدول", "nav4": "احجز",
      "kicker": "عقل · جسد · تنفّس", "h1": "تحرّك بهدوء. اشعر بالقوة.",
      "lead": "فلاو ويلنس استوديو هادئ لليوغا والبيلاتس والاستشفاء — احجز حصتك خلال دقائق.",
      "cta1": "احجز حصة", "cta2": "عرض الجدول",
      "s_title": "حصص مميزة", "c1t": "تدفق صباحي", "c1p": "45 دقيقة فينياسا لكل المستويات.", "c1pr": "12 دينار",
      "c2t": "بيلاتس كور", "c2p": "تمارين حصيرة بأسلوب الريformer.", "c2pr": "14 دينار",
      "c3t": "استشفاء", "c3p": "تمدد وتنفس وإضاءة هادئة.", "c3pr": "10 دينار",
      "f1": "مجموعات صغيرة", "f2": "مدربون عربي/إنجليزي", "foot": "فلاو ويلنس · قالب من Ibra Studio",
    },
    "layout": "gym",
  },
  {
    "id": "gym-box",
    "title": "Box 42 Training",
    "fonts": "https://fonts.googleapis.com/css2?family=Anton&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Barlow:wght@400;600;700&display=swap",
    "vars": "--bg:#11130f;--text:#f2f5e9;--muted:#a3ad93;--card:#1a1e16;--line:rgba(242,245,233,.12);--accent:#c8f542;--on-accent:#111;--accent-soft:rgba(200,245,66,.14);--panel:linear-gradient(135deg,#2a321c,#11130f 50%,#3d2a10);--display:'Anton';--body:'Barlow';--max:1060px",
    "en": {
      "back": "← Ibra Studio", "nav1": "WODs", "nav2": "Coaches", "nav3": "Drop-in", "nav4": "Join box",
      "kicker": "Cross-training community", "h1": "Show up. Work hard. Repeat.",
      "lead": "Box 42 is an industrial training floor with daily WODs, open gym, and a loud supportive community.",
      "cta1": "Try a drop-in", "cta2": "Today's WOD",
      "s_title": "This week", "c1t": "Engine", "c1p": "Intervals + rowing capacity.", "c1pr": "Mon / Wed",
      "c2t": "Strength", "c2p": "Squat focus and accessory work.", "c2pr": "Tue / Thu",
      "c3t": "Team WOD", "c3p": "Partner metcon — bring intensity.", "c3pr": "Saturday",
      "f1": "Daily programming", "f2": "All levels welcome", "foot": "Box 42 Training · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "التمارين", "nav2": "المدربين", "nav3": "حصة تجريبية", "nav4": "انضم",
      "kicker": "مجتمع تدريب متقاطع", "h1": "احضر. اجتهد. كرر.",
      "lead": "بوكس 42 صالة صناعية بتمارين يومية وصالة مفتوحة ومجتمع داعم بطاقة عالية.",
      "cta1": "جرّب حصة", "cta2": "تمرين اليوم",
      "s_title": "هذا الأسبوع", "c1t": "تحمّل", "c1p": "فواصل + تجديف.", "c1pr": "إثن / أربع",
      "c2t": "قوة", "c2p": "تركيز سكوات وتمارين مساعدة.", "c2pr": "ثلا / خميس",
      "c3t": "تمرين جماعي", "c3p": "ميتكون مع شريك — شدة عالية.", "c3pr": "السبت",
      "f1": "برنامج يومي", "f2": "لكل المستويات", "foot": "بوكس 42 · قالب من Ibra Studio",
    },
    "layout": "gym",
  },
  # ---- MARKETS ----
  {
    "id": "market-fresh",
    "title": "FreshBasket Market",
    "fonts": "https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap",
    "vars": "--bg:#fff8f0;--text:#1b2a1f;--muted:#5d6b60;--card:#ffffff;--line:#e7d7c4;--accent:#16a34a;--on-accent:#fff;--accent-soft:rgba(22,163,74,.12);--panel:linear-gradient(145deg,#bbf7d0,#fde68a 50%,#fdba74);--display:'Fredoka';--body:'Nunito';--max:1080px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Deals", "nav2": "Departments", "nav3": "Delivery", "nav4": "Shop now",
      "kicker": "Fresh today · Delivered fast", "h1": "Your weekly basket, filled smarter.",
      "lead": "FreshBasket is a friendly supermarket site — produce, bakery, deals of the week, and home delivery.",
      "cta1": "Order delivery", "cta2": "This week’s deals",
      "s_title": "Departments", "c1t": "Produce", "c1p": "Fruits & vegetables picked daily.", "c1pr": "Aisle 1–2",
      "c2t": "Dairy & eggs", "c2p": "Local brands and fresh milk.", "c2pr": "Aisle 4",
      "c3t": "Bakery", "c3p": "Warm bread every morning.", "c3pr": "Front",
      "f1": "Same-day delivery", "f2": "Weekly offers", "foot": "FreshBasket Market · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "العروض", "nav2": "الأقسام", "nav3": "التوصيل", "nav4": "تسوق الآن",
      "kicker": "طازج اليوم · توصيل سريع", "h1": "سلّتك الأسبوعية… بذكاء أكبر.",
      "lead": "فريش باسكت موقع سوبرماركت ودود — خضار، مخبز، عروض الأسبوع، وتوصيل للمنزل.",
      "cta1": "اطلب توصيل", "cta2": "عروض الأسبوع",
      "s_title": "الأقسام", "c1t": "الخضار والفواكه", "c1p": "منتجات تُختار يومياً.", "c1pr": "ممر 1–2",
      "c2t": "ألبان وبيض", "c2p": "ماركات محلية وحليب طازج.", "c2pr": "ممر 4",
      "c3t": "المخبز", "c3p": "خبز دافئ كل صباح.", "c3pr": "المدخل",
      "f1": "توصيل نفس اليوم", "f2": "عروض أسبوعية", "foot": "فريش باسكت · قالب من Ibra Studio",
    },
    "layout": "market",
  },
  {
    "id": "market-city",
    "title": "CityMart Hyper",
    "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Manrope:wght@400;600;700&family=Sora:wght@600;700&display=swap",
    "vars": "--bg:#0f172a;--text:#e2e8f0;--muted:#94a3b8;--card:#1e293b;--line:rgba(226,232,240,.1);--accent:#38bdf8;--on-accent:#0f172a;--accent-soft:rgba(56,189,248,.14);--panel:linear-gradient(145deg,#1e3a5f,#0f172a 55%,#164e63);--display:'Sora';--body:'Manrope';--max:1100px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Categories", "nav2": "Hours", "nav3": "Locations", "nav4": "Find store",
      "kicker": "Hypermarket · City-wide", "h1": "Everything under one bright roof.",
      "lead": "CityMart is a modern hypermarket template — categories, opening hours, and a clean store-first layout.",
      "cta1": "Browse categories", "cta2": "Store hours",
      "s_title": "Shop by category", "c1t": "Electronics", "c1p": "Phones, home tech, accessories.", "c1pr": "Floor 2",
      "c2t": "Home & living", "c2p": "Kitchen, furniture, décor.", "c2pr": "Floor 1",
      "c3t": "Grocery", "c3p": "Food court + full supermarket.", "c3pr": "Ground",
      "f1": "Open 9–12", "f2": "Parking available", "foot": "CityMart Hyper · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "التصنيفات", "nav2": "الأوقات", "nav3": "الفروع", "nav4": "اعثر على فرع",
      "kicker": "هايبر ماركت · على مستوى المدينة", "h1": "كل ما تحتاجه تحت سقف واحد.",
      "lead": "سيتي مارت قالب هايبر حديث — تصنيفات، أوقات عمل، وتخطيط واضح يركز على المتجر.",
      "cta1": "تصفح التصنيفات", "cta2": "أوقات العمل",
      "s_title": "تسوق حسب القسم", "c1t": "إلكترونيات", "c1p": "هواتف وتقنية منزلية.", "c1pr": "طابق 2",
      "c2t": "المنزل", "c2p": "مطبخ وأثاث وديكور.", "c2pr": "طابق 1",
      "c3t": "البقالة", "c3p": "سوبرماركت كامل + فود كورت.", "c3pr": "الأرضي",
      "f1": "٩ ص – ١٢ م", "f2": "موقف سيارات", "foot": "سيتي مارت · قالب من Ibra Studio",
    },
    "layout": "market",
  },
  {
    "id": "market-organic",
    "title": "GreenLeaf Organic",
    "fonts": "https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Karla:wght@400;600;700&display=swap",
    "vars": "--bg:#f4f7f2;--text:#1c2b1f;--muted:#5b6b5e;--card:#ffffff;--line:#d5e0d4;--accent:#4d7c0f;--on-accent:#fff;--accent-soft:rgba(77,124,15,.12);--panel:linear-gradient(160deg,#d9f99d,#f4f7f2 40%,#bbf7d0);--display:'Fraunces';--body:'Karla';--max:1020px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Farm", "nav2": "Products", "nav3": "Story", "nav4": "Order box",
      "kicker": "Organic · Local farms", "h1": "Clean food from soil you can trust.",
      "lead": "GreenLeaf is a soft organic grocery brand — seasonal boxes, pantry staples, and a farm-to-table story.",
      "cta1": "Get a weekly box", "cta2": "Our farms",
      "s_title": "This season", "c1t": "Harvest box", "c1p": "8–10 seasonal items every week.", "c1pr": "18 JOD",
      "c2t": "Pantry", "c2p": "Oils, grains, honey, spices.", "c2pr": "Shop",
      "c3t": "Dairy", "c3p": "Small-batch yogurt and cheese.", "c3pr": "Chilled",
      "f1": "No fake labels", "f2": "Jordan farms", "foot": "GreenLeaf Organic · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "المزارع", "nav2": "المنتجات", "nav3": "قصتنا", "nav4": "اطلب صندوقاً",
      "kicker": "عضوي · مزارع محلية", "h1": "طعام نظيف من تربة تثق بها.",
      "lead": "جرين ليف علامة بقالة عضوية هادئة — صناديق موسمية ومؤن وقصة من المزرعة للمائدة.",
      "cta1": "صندوق أسبوعي", "cta2": "مزارعنا",
      "s_title": "هذا الموسم", "c1t": "صندوق الحصاد", "c1p": "٨–١٠ أصناف موسمية أسبوعياً.", "c1pr": "18 دينار",
      "c2t": "المؤن", "c2p": "زيوت وحبوب وعسل وتوابل.", "c2pr": "تسوق",
      "c3t": "ألبان", "c3p": "لبنة وأجبان دفعات صغيرة.", "c3pr": "مبرد",
      "f1": "بدون تسميات وهمية", "f2": "مزارع أردنية", "foot": "جرين ليف · قالب من Ibra Studio",
    },
    "layout": "market",
  },
  # ---- CLINICS ----
  {
    "id": "clinic-care",
    "title": "CarePlus Clinic",
    "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;600;700&family=Libre+Franklin:wght@600;700&display=swap",
    "vars": "--bg:#f0f7ff;--text:#0f2744;--muted:#5b7391;--card:#ffffff;--line:#d7e6f5;--accent:#2563eb;--on-accent:#fff;--accent-soft:rgba(37,99,235,.12);--panel:linear-gradient(145deg,#bfdbfe,#eff6ff 45%,#93c5fd);--display:'Libre Franklin';--body:'Plus Jakarta Sans';--max:1040px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Services", "nav2": "Doctors", "nav3": "Insurance", "nav4": "Book visit",
      "kicker": "Multi-specialty clinic", "h1": "Care that feels clear and human.",
      "lead": "CarePlus helps patients book visits, meet doctors, and understand services — calm medical design that builds trust.",
      "cta1": "Book appointment", "cta2": "Meet doctors",
      "s_title": "Services", "c1t": "General medicine", "c1p": "Checkups and chronic care follow-up.", "c1pr": "Same week",
      "c2t": "Diagnostics", "c2p": "Labs and basic imaging referrals.", "c2pr": "On-site",
      "c3t": "Pediatrics", "c3p": "Child wellness and vaccinations.", "c3pr": "Family",
      "f1": "Licensed doctors", "f2": "Evening hours", "foot": "CarePlus Clinic · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الخدمات", "nav2": "الأطباء", "nav3": "التأمين", "nav4": "احجز زيارة",
      "kicker": "عيادة متعددة التخصصات", "h1": "رعاية واضحة وإنسانية.",
      "lead": "كير بلس يساعد المرضى على حجز الزيارات والتعرف على الأطباء وفهم الخدمات — تصميم طبي هادئ يبني الثقة.",
      "cta1": "احجز موعداً", "cta2": "تعرّف على الأطباء",
      "s_title": "الخدمات", "c1t": "طب عام", "c1p": "فحوصات ومتابعة أمراض مزمنة.", "c1pr": "نفس الأسبوع",
      "c2t": "تشخيص", "c2p": "مختبرات وتحويلات تصوير.", "c2pr": "في العيادة",
      "c3t": "أطفال", "c3p": "متابعة صحة الطفل والتطعيمات.", "c3pr": "عائلي",
      "f1": "أطباء مرخّصون", "f2": "مواعيد مسائية", "foot": "عيادة كير بلس · قالب من Ibra Studio",
    },
    "layout": "clinic",
  },
  {
    "id": "clinic-dental",
    "title": "BrightSmile Dental",
    "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Poppins:wght@400;600;700&family=Quicksand:wght@600;700&display=swap",
    "vars": "--bg:#fafcff;--text:#16324f;--muted:#6b7c93;--card:#ffffff;--line:#e2ebf5;--accent:#0ea5e9;--on-accent:#fff;--accent-soft:rgba(14,165,233,.12);--panel:linear-gradient(150deg,#e0f2fe,#ffffff 40%,#bae6fd);--display:'Quicksand';--body:'Poppins';--max:1020px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Treatments", "nav2": "Smile gallery", "nav3": "FAQ", "nav4": "Book smile",
      "kicker": "Dental clinic · Family & cosmetic", "h1": "Brighter smiles start here.",
      "lead": "BrightSmile is a fresh dental clinic template — whitening, cleanings, implants, and easy booking.",
      "cta1": "Book cleaning", "cta2": "Whitening offer",
      "s_title": "Popular treatments", "c1t": "Cleaning", "c1p": "Gentle hygiene with full check.", "c1pr": "From 25 JOD",
      "c2t": "Whitening", "c2p": "In-clinic brightening session.", "c2pr": "From 90 JOD",
      "c3t": "Aligners consult", "c3p": "Assessment for clear aligners.", "c3pr": "Free visit",
      "f1": "Painless focus", "f2": "Kids welcome", "foot": "BrightSmile Dental · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "العلاجات", "nav2": "معرض الابتسامات", "nav3": "أسئلة", "nav4": "احجز",
      "kicker": "عيادة أسنان · تجميل وعائلة", "h1": "ابتسامة أسطع تبدأ من هنا.",
      "lead": "ابتسامة مشرقة قالب عيادة أسنان عصري — تبييض وتنظيف وزراعة وحجز سهل.",
      "cta1": "احجز تنظيفاً", "cta2": "عرض التبييض",
      "s_title": "علاجات شائعة", "c1t": "تنظيف", "c1p": "عناية لطيفة مع فحص كامل.", "c1pr": "من 25 دينار",
      "c2t": "تبييض", "c2p": "جلسة تبييض داخل العيادة.", "c2pr": "من 90 دينار",
      "c3t": "استشارة تقويم شفاف", "c3p": "تقييم للتقويم الشفاف.", "c3pr": "زيارة مجانية",
      "f1": "تركيز على الراحة", "f2": "نستقبل الأطفال", "foot": "ابتسامة مشرقة · قالب من Ibra Studio",
    },
    "layout": "clinic",
  },
  {
    "id": "clinic-family",
    "title": "Family Health Hub",
    "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Literata:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap",
    "vars": "--bg:#fff7ed;--text:#3b2a1a;--muted:#7c6654;--card:#fffdf8;--line:#f0e0cc;--accent:#ea580c;--on-accent:#fff;--accent-soft:rgba(234,88,12,.12);--panel:linear-gradient(145deg,#fed7aa,#fff7ed 50%,#fdba74);--display:'Literata';--body:'Source Sans 3';--max:1040px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Family care", "nav2": "Labs", "nav3": "Hours", "nav4": "Call clinic",
      "kicker": "Neighborhood family practice", "h1": "One clinic for the whole family.",
      "lead": "Family Health Hub covers kids, adults, labs, and follow-ups — warm design for a trusted local clinic.",
      "cta1": "Book for family", "cta2": "Lab services",
      "s_title": "Why families choose us", "c1t": "Kids & adults", "c1p": "Care under one roof.", "c1pr": "All ages",
      "c2t": "On-site labs", "c2p": "Fast results, clear reports.", "c2pr": "Same day*",
      "c3t": "Easy follow-up", "c3p": "Reminders and simple booking.", "c3pr": "WhatsApp",
      "f1": "Walk-ins welcome", "f2": "Arabic & English staff", "foot": "Family Health Hub · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "رعاية العائلة", "nav2": "المختبر", "nav3": "الأوقات", "nav4": "اتصل بالعيادة",
      "kicker": "عيادة عائلية في الحي", "h1": "عيادة واحدة لكل العائلة.",
      "lead": "مركز صحة العائلة يغطي الأطفال والكبار والمختبرات والمتابعة — تصميم دافئ لعيادة محلية موثوقة.",
      "cta1": "احجز للعائلة", "cta2": "خدمات المختبر",
      "s_title": "لماذا تختاره العائلات", "c1t": "أطفال وكبار", "c1p": "رعاية تحت سقف واحد.", "c1pr": "كل الأعمار",
      "c2t": "مختبر في الموقع", "c2p": "نتائج سريعة وتقارير واضحة.", "c2pr": "نفس اليوم*",
      "c3t": "متابعة سهلة", "c3p": "تذكير وحجز بسيط.", "c3pr": "واتساب",
      "f1": "نستقبل بدون موعد", "f2": "طاقم عربي وإنجليزي", "foot": "مركز صحة العائلة · قالب من Ibra Studio",
    },
    "layout": "clinic",
  },
  # ---- RESTAURANTS (extra 2; original upgraded separately) ----
  {
    "id": "restaurant-bistro",
    "title": "Noon Bistro",
    "fonts": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=DM+Sans:wght@400;500;700&display=swap",
    "vars": "--bg:#faf6f1;--text:#1c1917;--muted:#78716c;--card:#ffffff;--line:#e7e0d6;--accent:#b45309;--on-accent:#fff;--accent-soft:rgba(180,83,9,.12);--panel:linear-gradient(150deg,#fde68a,#faf6f1 40%,#fdba74);--display:'DM Serif Display';--body:'DM Sans';--max:1000px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Menu", "nav2": "Brunch", "nav3": "Location", "nav4": "Reserve",
      "kicker": "Daytime bistro · Amman", "h1": "Sunlit plates. Slow brunch.",
      "lead": "Noon Bistro is a light modern restaurant template for brunch, coffee, and neighborhood lunches.",
      "cta1": "See brunch menu", "cta2": "Get directions",
      "s_title": "On the table", "c1t": "Shakshuka board", "c1p": "Eggs, herbs, warm flatbread.", "c1pr": "7.5 JOD",
      "c2t": "Garden bowl", "c2p": "Grains, greens, citrus dressing.", "c2pr": "6.5 JOD",
      "c3t": "Lemon tart", "c3p": "Bright finish with cream.", "c3pr": "4 JOD",
      "f1": "Open 8–5", "f2": "Weekend brunch", "foot": "Noon Bistro · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "القائمة", "nav2": "برانش", "nav3": "الموقع", "nav4": "احجز",
      "kicker": "بيسترو نهاري · عمّان", "h1": "أطباق مشمسة. برانش هادئ.",
      "lead": "نون بيسترو قالب مطعم خفيف وعصري للبرانش والقهوة وغداء الحي.",
      "cta1": "قائمة البرانش", "cta2": "الاتجاهات",
      "s_title": "على الطاولة", "c1t": "شكشوكة", "c1p": "بيض وأعشاب وخبز دافئ.", "c1pr": "7.5 دينار",
      "c2t": "صحن الحديقة", "c2p": "حبوب وخضار وصوص حمضيات.", "c2pr": "6.5 دينار",
      "c3t": "تارت ليمون", "c3p": "ختام منعش مع كريمة.", "c3pr": "4 دينار",
      "f1": "٨ ص – ٥ م", "f2": "برانش نهاية الأسبوع", "foot": "نون بيسترو · قالب من Ibra Studio",
    },
    "layout": "food",
  },
  {
    "id": "restaurant-grill",
    "title": "Charcoal Grill House",
    "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Oswald:wght@500;600;700&family=Roboto:wght@400;500;700&display=swap",
    "vars": "--bg:#120e0c;--text:#f5ebe0;--muted:#b9a99a;--card:#1c1613;--line:rgba(245,235,224,.1);--accent:#f97316;--on-accent:#1c1008;--accent-soft:rgba(249,115,22,.14);--panel:linear-gradient(145deg,#3b2114,#120e0c 50%,#7c2d12);--display:'Oswald';--body:'Roboto';--max:1040px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Grill menu", "nav2": "Combos", "nav3": "Catering", "nav4": "Order now",
      "kicker": "Fire · Smoke · Meat", "h1": "Charcoal. Cut. Serve hot.",
      "lead": "A bold grill-house template for mixed grills, combos, and late-night meat cravings.",
      "cta1": "Order mixed grill", "cta2": "View combos",
      "s_title": "From the fire", "c1t": "Mixed grill", "c1p": "Kebab, chicken, lamb chops.", "c1pr": "14 JOD",
      "c2t": "Ribs platter", "c2p": "Slow smoke, sticky glaze.", "c2pr": "16 JOD",
      "c3t": "Family combo", "c3p": "Feeds 4 with sides & bread.", "c3pr": "32 JOD",
      "f1": "Open late", "f2": "Delivery ready", "foot": "Charcoal Grill House · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "قائمة الشواء", "nav2": "الوجبات", "nav3": "تموين", "nav4": "اطلب الآن",
      "kicker": "نار · دخان · لحم", "h1": "فحم. تقطيع. تقديم ساخن.",
      "lead": "قالب مطعم مشاوي جريء للمشاوي المشكلة والوجبات وطلبات الليل.",
      "cta1": "اطلب مشاوي", "cta2": "عرض الوجبات",
      "s_title": "من النار", "c1t": "مشاوي مشكلة", "c1p": "كباب ودجاج وريش غنم.", "c1pr": "14 دينار",
      "c2t": "طبق أضلاع", "c2p": "شواء بطيء وصوص لزج.", "c2pr": "16 دينار",
      "c3t": "وجبة عائلية", "c3p": "تكفي 4 مع مقبلات وخبز.", "c3pr": "32 دينار",
      "f1": "مفتوح لوقت متأخر", "f2": "جاهز للتوصيل", "foot": "بيت الشواء · قالب من Ibra Studio",
    },
    "layout": "food",
  },
  # ---- EXTRA ----
  {
    "id": "salon-luxe",
    "title": "Luxe Hair Studio",
    "fonts": "https://fonts.googleapis.com/css2?family=Cormorant:wght@600;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Jost:wght@400;500;600&display=swap",
    "vars": "--bg:#1a1420;--text:#f7f0f8;--muted:#b5a6b8;--card:#241b2b;--line:rgba(247,240,248,.1);--accent:#e879f9;--on-accent:#1a1420;--accent-soft:rgba(232,121,249,.14);--panel:linear-gradient(145deg,#4a1d4a,#1a1420 55%,#701a75);--display:'Cormorant';--body:'Jost';--max:1000px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Services", "nav2": "Stylists", "nav3": "Gallery", "nav4": "Book",
      "kicker": "Hair · Color · Care", "h1": "Your next look, crafted.",
      "lead": "Luxe Hair Studio is an elegant salon template — cuts, color, bridal, and easy appointment booking.",
      "cta1": "Book appointment", "cta2": "View services",
      "s_title": "Signature services", "c1t": "Cut & style", "c1p": "Consultation + finish.", "c1pr": "From 20 JOD",
      "c2t": "Color", "c2p": "Balayage, gloss, full color.", "c2pr": "From 45 JOD",
      "c3t": "Bridal trial", "c3p": "Hair & soft glam prep.", "c3pr": "From 60 JOD",
      "f1": "Senior stylists", "f2": "Products on site", "foot": "Luxe Hair Studio · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الخدمات", "nav2": "المصففين", "nav3": "المعرض", "nav4": "احجز",
      "kicker": "شعر · لون · عناية", "h1": "إطلالتك القادمة… بإتقان.",
      "lead": "لوكس قالب صالون أنيق — قص وصبغ وعرايس وحجز مواعيد سهل.",
      "cta1": "احجز موعداً", "cta2": "عرض الخدمات",
      "s_title": "خدمات مميزة", "c1t": "قص وتصفيف", "c1p": "استشارة + تشطيب.", "c1pr": "من 20 دينار",
      "c2t": "صبغ", "c2p": "بالاياح ولمعة ولون كامل.", "c2pr": "من 45 دينار",
      "c3t": "تجربة عروس", "c3p": "شعر ومكياج ناعم.", "c3pr": "من 60 دينار",
      "f1": "مصففون خبراء", "f2": "منتجات في الصالون", "foot": "لوكس للشعر · قالب من Ibra Studio",
    },
    "layout": "salon",
  },
  {
    "id": "cafe-brew",
    "title": "Brew & Bean Cafe",
    "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Libre+Baskerville:wght@700&family=Work+Sans:wght@400;600;700&display=swap",
    "vars": "--bg:#f3ebe3;--text:#2c1810;--muted:#7a5c4c;--card:#fffaf6;--line:#e4d4c6;--accent:#6f4e37;--on-accent:#fff;--accent-soft:rgba(111,78,55,.12);--panel:linear-gradient(150deg,#d6b89c,#f3ebe3 45%,#a67c52);--display:'Libre Baskerville';--body:'Work Sans';--max:980px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Drinks", "nav2": "Food", "nav3": "Hours", "nav4": "Visit us",
      "kicker": "Specialty coffee · Neighborhood", "h1": "Slow cups. Good beans.",
      "lead": "Brew & Bean is a cozy cafe template — espresso menu, light bites, and warm local hours.",
      "cta1": "See drink menu", "cta2": "Opening hours",
      "s_title": "Favorites", "c1t": "Flat white", "c1p": "Silky milk, rich espresso.", "c1pr": "3.2 JOD",
      "c2t": "V60 pour-over", "c2p": "Single origin rotation.", "c2pr": "3.8 JOD",
      "c3t": "Date oat cookie", "c3p": "Baked every morning.", "c3pr": "1.5 JOD",
      "f1": "Wi‑Fi friendly", "f2": "Beans to go", "foot": "Brew & Bean Cafe · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "المشروبات", "nav2": "الطعام", "nav3": "الأوقات", "nav4": "زورنا",
      "kicker": "قهوة مختصة · في الحي", "h1": "فناجين بطيئة. حبوب ممتازة.",
      "lead": "برو آند بين قالب مقهى دافئ — قائمة إسبريسو ووجبات خفيفة وأوقات الحي.",
      "cta1": "قائمة المشروبات", "cta2": "أوقات العمل",
      "s_title": "الأكثر طلباً", "c1t": "فلات وايت", "c1p": "حليب ناعم وإسبريسو غني.", "c1pr": "3.2 دينار",
      "c2t": "V60", "c2p": "محصول أحادي بالتناوب.", "c2pr": "3.8 دينار",
      "c3t": "كوكيز تمر وشوفان", "c3p": "يُخبز كل صباح.", "c3pr": "1.5 دينار",
      "f1": "واي فاي", "f2": "حبوب للمنزل", "foot": "برو آند بين · قالب من Ibra Studio",
    },
    "layout": "food",
  },
  {
    "id": "realestate-keys",
    "title": "Keystone Homes",
    "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Playfair+Display:wght@600;700&family=Source+Sans+3:wght@400;600;700&display=swap",
    "vars": "--bg:#0c1222;--text:#e8eefc;--muted:#9aa8c7;--card:#141b2f;--line:rgba(232,238,252,.1);--accent:#d4a017;--on-accent:#1a1408;--accent-soft:rgba(212,160,23,.14);--panel:linear-gradient(145deg,#1e3a5f,#0c1222 50%,#3b2f15);--display:'Playfair Display';--body:'Source Sans 3';--max:1080px",
    "en": {
      "back": "← Ibra Studio", "nav1": "Listings", "nav2": "Agents", "nav3": "Sell", "nav4": "Contact",
      "kicker": "Real estate agency", "h1": "Find the key to your next home.",
      "lead": "Keystone Homes showcases listings, agents, and a strong contact path for buyers and sellers.",
      "cta1": "Browse homes", "cta2": "Talk to an agent",
      "s_title": "Featured listings", "c1t": "Abdoun apartment", "c1p": "3 bed · city view · parking.", "c1pr": "185,000 JOD",
      "c2t": "Khalda villa", "c2p": "Garden · maid room · quiet street.", "c2pr": "320,000 JOD",
      "c3t": "Jbeiha duplex", "c3p": "Near schools · ready to move.", "c3pr": "210,000 JOD",
      "f1": "Verified listings", "f2": "Buyer + seller support", "foot": "Keystone Homes · Template by Ibra Studio",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "العقارات", "nav2": "الوسطاء", "nav3": "بِع معنا", "nav4": "تواصل",
      "kicker": "وكالة عقارية", "h1": "اعثر على مفتاح بيتك القادم.",
      "lead": "كي ستون يعرض العقارات والوسطاء ومسار تواصل واضح للمشترين والبائعين.",
      "cta1": "تصفح المنازل", "cta2": "تحدث مع وسيط",
      "s_title": "عقارات مميزة", "c1t": "شقة عبدون", "c1p": "3 غرف · إطلالة · موقف.", "c1pr": "185,000 دينار",
      "c2t": "فيلا خلدا", "c2p": "حديقة · غرفة خادمة · شارع هادئ.", "c2pr": "320,000 دينار",
      "c3t": "دوبلكس الجبيهة", "c3p": "قرب المدارس · جاهز للسكن.", "c3pr": "210,000 دينار",
      "f1": "عقارات موثّقة", "f2": "دعم مشتري وبائع", "foot": "كي ستون للعقارات · قالب من Ibra Studio",
    },
    "layout": "estate",
  },
]


def dict_to_js(d):
    return json.dumps(d, ensure_ascii=False)


def body_standard(t):
    return f"""
  <div class="wrap">
    <nav class="site">
      <div class="brand">{t['title']}</div>
      <ul class="nav-links">
        <li data-i18n="nav1">Classes</li>
        <li data-i18n="nav2">Trainers</li>
        <li data-i18n="nav3">Pricing</li>
      </ul>
      <a class="btn btn-a" href="#" data-i18n="nav4">Join</a>
    </nav>
    <header class="hero grid2">
      <div>
        <div class="kicker" data-i18n="kicker"></div>
        <h1 data-i18n="h1"></h1>
        <p class="lead" data-i18n="lead"></p>
        <div class="cta">
          <a class="btn btn-a" href="#" data-i18n="cta1"></a>
          <a class="btn btn-g" href="#" data-i18n="cta2"></a>
        </div>
        <div class="cta" style="gap:1.25rem;opacity:.9;font-size:.92rem;color:var(--muted)">
          <span data-i18n="f1"></span>
          <span data-i18n="f2"></span>
        </div>
      </div>
      <div class="panel" aria-hidden="true"></div>
    </header>
    <section class="section">
      <h2 data-i18n="s_title"></h2>
      <div class="grid3">
        <article class="card"><h3 data-i18n="c1t"></h3><p data-i18n="c1p"></p><span class="price" data-i18n="c1pr"></span></article>
        <article class="card"><h3 data-i18n="c2t"></h3><p data-i18n="c2p"></p><span class="price" data-i18n="c2pr"></span></article>
        <article class="card"><h3 data-i18n="c3t"></h3><p data-i18n="c3p"></p><span class="price" data-i18n="c3pr"></span></article>
      </div>
    </section>
    <footer class="footer">
      <span data-i18n="foot"></span>
      <span>EN · AR</span>
    </footer>
  </div>
"""


def write_template(t):
    folder = TDIR / t["id"]
    folder.mkdir(parents=True, exist_ok=True)
    css = f":root{{{t['vars']}}}\n" + BASE_CSS
    body = body_standard(t)
    d = {"en": t["en"], "ar": t["ar"]}
    html = shell(t["title"], t["fonts"], css, body, dict_to_js(d))
    (folder / "index.html").write_text(html, encoding="utf-8")
    print("wrote", t["id"])


def upgrade_existing():
    """Rewrite original 4 templates with full EN/AR + shared lang."""
    extras = [
        {
            "id": "restaurant",
            "title": "Olive & Ember",
            "fonts": "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Nunito:wght@400;600;700&display=swap",
            "vars": "--bg:#1c1410;--text:#f7efe6;--muted:#cbb8a4;--card:#261c16;--line:rgba(247,239,230,.1);--accent:#e2b87a;--on-accent:#24180f;--accent-soft:rgba(226,184,122,.14);--panel:linear-gradient(160deg,#5a3a28,#2a1b14 55%,#120d0a);--display:'Cormorant Garamond';--body:'Nunito';--max:980px",
            "en": {
                "back": "← Ibra Studio", "nav1": "Menu", "nav2": "Reserve", "nav3": "Location", "nav4": "Book table",
                "kicker": "Amman · Dinner · Fire kitchen", "h1": "Slow food. Warm nights.",
                "lead": "Fine-dining warmth with menu cards and a clear reservation path.",
                "cta1": "Reserve a table", "cta2": "View menu",
                "s_title": "Evening menu", "c1t": "Ember flatbread", "c1p": "Labneh, chili oil, herbs.", "c1pr": "8.5 JOD",
                "c2t": "Citrus lamb", "c2p": "Burnt orange glaze, freekeh.", "c2pr": "16 JOD",
                "c3t": "Date & tahini cake", "c3p": "Sesame brittle, cardamom cream.", "c3pr": "6 JOD",
                "f1": "Dinner 6–11", "f2": "Private table", "foot": "Olive & Ember · Template by Ibra Studio",
            },
            "ar": {
                "back": "← Ibra Studio", "nav1": "القائمة", "nav2": "احجز", "nav3": "الموقع", "nav4": "احجز طاولة",
                "kicker": "عمّان · عشاء · مطبخ نار", "h1": "طعام بطيء. ليالٍ دافئة.",
                "lead": "أجواء مطعم راقٍ دافئة مع بطاقات قائمة ومسار حجز واضح.",
                "cta1": "احجز طاولة", "cta2": "عرض القائمة",
                "s_title": "قائمة المساء", "c1t": "خبز إمبر", "c1p": "لبنة وزيت فلفل وأعشاب.", "c1pr": "8.5 دينار",
                "c2t": "خروف بالحمضيات", "c2p": "صوص برتقال محروق وفريكة.", "c2pr": "16 دينار",
                "c3t": "كعكة تمر وطحينة", "c3p": "سمسم وكريمة هيل.", "c3pr": "6 دينار",
                "f1": "عشاء ٦–١١", "f2": "طاولة خاصة", "foot": "أوليف آند إمبر · قالب من Ibra Studio",
            },
        },
        {
            "id": "saas-landing",
            "title": "NovaPulse",
            "fonts": "https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Outfit:wght@600;700&display=swap",
            "vars": "--bg:#07090f;--text:#eef2ff;--muted:#93a0b8;--card:#111622;--line:rgba(255,255,255,.08);--accent:#7c5cff;--on-accent:#fff;--accent-soft:rgba(124,92,255,.16);--panel:linear-gradient(160deg,rgba(124,92,255,.35),#07090f 55%,rgba(34,211,238,.2));--display:'Outfit';--body:'DM Sans';--max:1040px",
            "en": {
                "back": "← Ibra Studio", "nav1": "Product", "nav2": "Pricing", "nav3": "Docs", "nav4": "Start free",
                "kicker": "SaaS landing template", "h1": "Ship updates customers notice.",
                "lead": "Dark conversion-focused landing for apps and tools — hero, features, and strong CTA.",
                "cta1": "Get started", "cta2": "View demo",
                "s_title": "Why teams switch", "c1t": "Fast onboarding", "c1p": "Clear hero and CTA above the fold.", "c1pr": "Launch",
                "c2t": "Feature grid", "c2p": "Benefits, integrations, pricing teases.", "c2pr": "Scale",
                "c3t": "Host anywhere", "c3p": "Static HTML ready for GitHub Pages.", "c3pr": "Ship",
                "f1": "No backend needed", "f2": "Mobile ready", "foot": "NovaPulse · Template by Ibra Studio",
            },
            "ar": {
                "back": "← Ibra Studio", "nav1": "المنتج", "nav2": "الأسعار", "nav3": "التوثيق", "nav4": "ابدأ مجاناً",
                "kicker": "قالب صفحة منتج", "h1": "أطلق تحديثات يلاحظها عملاؤك.",
                "lead": "صفحة هبوط داكنة للتحويل للتطبيقات والأدوات — بطل ومميزات ودعوة واضحة.",
                "cta1": "ابدأ الآن", "cta2": "عرض تجريبي",
                "s_title": "لماذا يتحول الفريق", "c1t": "انضمام سريع", "c1p": "بطل واضح ودعوة فوق الطية.", "c1pr": "إطلاق",
                "c2t": "شبكة مميزات", "c2p": "فوائد وتكاملات وأسعار.", "c2pr": "توسّع",
                "c3t": "استضافة سهلة", "c3p": "HTML جاهز لـ GitHub Pages.", "c3pr": "انشر",
                "f1": "بدون خادم", "f2": "متوافق مع الجوال", "foot": "نوفا بالس · قالب من Ibra Studio",
            },
        },
        {
            "id": "portfolio",
            "title": "Aria Cole Portfolio",
            "fonts": "https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Schibsted+Grotesk:wght@400;500;600&display=swap",
            "vars": "--bg:#f6f1e8;--text:#1a1410;--muted:#6b5e52;--card:#fffdf8;--line:#e6dccf;--accent:#c45c26;--on-accent:#fff;--accent-soft:rgba(196,92,38,.12);--panel:linear-gradient(160deg,#d9c3a8,#8f6a4a 55%,#2b211c);--display:'Fraunces';--body:'Schibsted Grotesk';--max:1000px",
            "en": {
                "back": "← Ibra Studio", "nav1": "Work", "nav2": "About", "nav3": "Contact", "nav4": "Hire me",
                "kicker": "Creative portfolio", "h1": "Design with room to breathe.",
                "lead": "Editorial portfolio for freelancers and personal brands — big type and project cards.",
                "cta1": "View selected work", "cta2": "About",
                "s_title": "Selected projects", "c1t": "Brand system", "c1p": "Identity and packaging direction.", "c1pr": "Case study",
                "c2t": "Studio website", "c2p": "Clean layout with motion-ready sections.", "c2pr": "Web",
                "c3t": "Festival booklet", "c3p": "Typography-led print series.", "c3pr": "Print",
                "f1": "Available for work", "f2": "Remote friendly", "foot": "Creative Portfolio · Template by Ibra Studio",
            },
            "ar": {
                "back": "← Ibra Studio", "nav1": "الأعمال", "nav2": "نبذة", "nav3": "تواصل", "nav4": "وظّفني",
                "kicker": "بورتفوليو إبداعي", "h1": "تصميم بمساحة للتنفّس.",
                "lead": "معرض أعمال تحريري للمستقلين والعلامات الشخصية — خطوط كبيرة وبطاقات مشاريع.",
                "cta1": "عرض الأعمال", "cta2": "نبذة",
                "s_title": "مشاريع مختارة", "c1t": "نظام هوية", "c1p": "هوية واتجاه تغليف.", "c1pr": "دراسة حالة",
                "c2t": "موقع استوديو", "c2p": "تخطيط نظيف جاهز للحركة.", "c2pr": "ويب",
                "c3t": "كتيّب مهرجان", "c3p": "سلسلة مطبوعة تعتمد على الخط.", "c3pr": "طباعة",
                "f1": "متاح للعمل", "f2": "عمل عن بُعد", "foot": "بورتفوليو إبداعي · قالب من Ibra Studio",
            },
        },
        {
            "id": "ecommerce",
            "title": "Forma Store",
            "fonts": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600;700&display=swap",
            "vars": "--bg:#fafafa;--text:#111;--muted:#667085;--card:#fff;--line:#e7e7ea;--accent:#111;--on-accent:#fff;--accent-soft:rgba(17,17,17,.08);--panel:linear-gradient(145deg,#dbe4ff,#f5f5f7 40%,#111 40%,#333);--display:'Space Grotesk';--body:'Inter';--max:1040px",
            "en": {
                "back": "← Ibra Studio", "nav1": "Shop", "nav2": "New", "nav3": "About", "nav4": "Cart",
                "kicker": "Product shop template", "h1": "Everyday objects, sharper form.",
                "lead": "Lightweight ecommerce layout with product cards and a strong collection hero.",
                "cta1": "Shop collection", "cta2": "New arrivals",
                "s_title": "Featured", "c1t": "Arc Lamp", "c1p": "Matte steel finish.", "c1pr": "$89",
                "c2t": "Soft Chair", "c2p": "Wool blend comfort.", "c2pr": "$240",
                "c3t": "Desk Tray", "c3p": "Oak / black options.", "c3pr": "$36",
                "f1": "Free shipping*", "f2": "Easy returns", "foot": "Forma Store · Template by Ibra Studio",
            },
            "ar": {
                "back": "← Ibra Studio", "nav1": "تسوق", "nav2": "جديد", "nav3": "عنّا", "nav4": "السلة",
                "kicker": "قالب متجر منتجات", "h1": "أشياء يومية… بشكل أحدّ.",
                "lead": "تخطيط متجر خفيف مع بطاقات منتجات وبطل مجموعة قوي.",
                "cta1": "تسوق المجموعة", "cta2": "وصل حديثاً",
                "s_title": "مميز", "c1t": "مصباح آرك", "c1p": "تشطيب فولاذ مطفي.", "c1pr": "89$",
                "c2t": "كرسي ناعم", "c2p": "راحة من مزيج صوف.", "c2pr": "240$",
                "c3t": "صينية مكتب", "c3p": "خيارات سنديان / أسود.", "c3pr": "36$",
                "f1": "شحن مجاني*", "f2": "إرجاع سهل", "foot": "متجر فورما · قالب من Ibra Studio",
            },
        },
    ]
    for t in extras:
        write_template(t)


def main():
    for t in TEMPLATES:
        write_template(t)
    upgrade_existing()
    print("done", len(TEMPLATES) + 4, "templates")


if __name__ == "__main__":
    main()
