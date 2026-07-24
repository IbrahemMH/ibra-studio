# -*- coding: utf-8 -*-
"""Generate full bilingual templates with images, brand kits, dual currency."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TDIR = ROOT / "templates"

TEMPLATES = [
  {
    "id": "gym-iron", "title": "Iron Forge Gym", "img": "gym",
    "fonts_css": "Bebas+Neue&family=Source+Sans+3:wght@400;600;700",
    "font_display": "Bebas Neue", "font_body": "Source Sans 3",
    "vars": "--bg:#0a0a0b;--text:#f4f4f5;--muted:#a1a1aa;--card:#141416;--line:rgba(255,255,255,.12);--accent:#ef4444;--on-accent:#fff;--max:1080px",
    "colors": [
      {"hex": "#0a0a0b", "en": "Ink black", "ar": "أسود حبر"},
      {"hex": "#ef4444", "en": "Forge red", "ar": "أحمر القوة"},
      {"hex": "#f4f4f5", "en": "Soft white", "ar": "أبيض ناعم"},
      {"hex": "#a1a1aa", "en": "Steel gray", "ar": "رمادي فولاذي"},
      {"hex": "#141416", "en": "Charcoal card", "ar": "فحمي"},
    ],
    "prices": [29, 49, 79],
    "en": {
      "back": "← Ibra Studio", "nav1": "Classes", "nav2": "Trainers", "nav3": "Pricing", "nav4": "Join",
      "kicker": "Amman · Strength · 24/7", "h1": "Forge a stronger you.",
      "lead": "Serious training floor - power racks, coaches, memberships built for results.",
      "cta1": "Start free week", "cta2": "View classes",
      "s_title": "Memberships", "c1t": "Starter", "c1p": "Gym floor + locker.",
      "c2t": "Athlete", "c2p": "Classes + coach check-ins.", "c3t": "Elite", "c3p": "Unlimited + guest passes.",
      "suffix": " / mo", "f1": "Open 24/7", "f2": "Pro coaches",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Iron Forge Gym · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الحصص", "nav2": "المدربين", "nav3": "الأسعار", "nav4": "انضم",
      "kicker": "عمّان · قوة · 24/7", "h1": "اصنع نسخة أقوى منك.",
      "lead": "صالة جدية - أجهزة قوة ومدربين وعضويات للنتائج.",
      "cta1": "أسبوع مجاني", "cta2": "عرض الحصص",
      "s_title": "العضويات", "c1t": "مبتدئ", "c1p": "صالة + خزانة.",
      "c2t": "رياضي", "c2p": "حصص + متابعة مدرب.", "c3t": "نخبة", "c3p": "بلا حدود + ضيوف.",
      "suffix": " / شهر", "f1": "مفتوح 24/7", "f2": "مدربون محترفون",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "آيرون فورج · قالب Ibra Studio",
    },
  },
  {
    "id": "gym-flow", "title": "Flow Wellness", "img": "wellness",
    "fonts_css": "Cormorant+Garamond:wght@600;700&family=Outfit:wght@400;500;600",
    "font_display": "Cormorant Garamond", "font_body": "Outfit",
    "vars": "--bg:#f7f3ee;--text:#1f1a17;--muted:#6f655c;--card:#fffdf9;--line:#e7ddd2;--accent:#2f6f5e;--on-accent:#fff;--max:1040px",
    "colors": [
      {"hex": "#f7f3ee", "en": "Warm sand", "ar": "رمل دافئ"},
      {"hex": "#2f6f5e", "en": "Sage green", "ar": "أخضر حكيم"},
      {"hex": "#1f1a17", "en": "Deep earth", "ar": "تراب عميق"},
      {"hex": "#6f655c", "en": "Clay muted", "ar": "طين هادئ"},
      {"hex": "#fffdf9", "en": "Paper white", "ar": "أبيض ورقي"},
    ],
    "prices": [12, 14, 10],
    "en": {
      "back": "← Ibra Studio", "nav1": "Yoga", "nav2": "Pilates", "nav3": "Schedule", "nav4": "Book",
      "kicker": "Mind · Body · Breath", "h1": "Move gently. Feel stronger.",
      "lead": "Calm studio for yoga, pilates, and recovery - book in minutes.",
      "cta1": "Book a class", "cta2": "See schedule",
      "s_title": "Popular sessions", "c1t": "Morning flow", "c1p": "45 min vinyasa.",
      "c2t": "Core pilates", "c2p": "Mat strength work.", "c3t": "Restore", "c3p": "Stretch & breathwork.",
      "suffix": "", "f1": "Small groups", "f2": "EN + AR coaches",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Flow Wellness · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "يوغا", "nav2": "بيلاتس", "nav3": "الجدول", "nav4": "احجز",
      "kicker": "عقل · جسد · تنفّس", "h1": "تحرّك بهدوء. اشعر بالقوة.",
      "lead": "استوديو هادئ لليوغا والبيلاتس - احجز خلال دقائق.",
      "cta1": "احجز حصة", "cta2": "عرض الجدول",
      "s_title": "حصص مميزة", "c1t": "تدفق صباحي", "c1p": "45 دقيقة فينياسا.",
      "c2t": "بيلاتس كور", "c2p": "تمارين حصيرة.", "c3t": "استشفاء", "c3p": "تمدد وتنفس.",
      "suffix": "", "f1": "مجموعات صغيرة", "f2": "مدربون عربي/إنجليزي",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "فلاو ويلنس · قالب Ibra Studio",
    },
  },
  {
    "id": "gym-box", "title": "Box 42 Training", "img": "crossfit",
    "fonts_css": "Anton&family=Barlow:wght@400;600;700",
    "font_display": "Anton", "font_body": "Barlow",
    "vars": "--bg:#11130f;--text:#f2f5e9;--muted:#a3ad93;--card:#1a1e16;--line:rgba(242,245,233,.12);--accent:#c8f542;--on-accent:#111;--max:1060px",
    "colors": [
      {"hex": "#11130f", "en": "Box black", "ar": "أسود البوكس"},
      {"hex": "#c8f542", "en": "Acid lime", "ar": "ليموني حمضي"},
      {"hex": "#f2f5e9", "en": "Bone white", "ar": "أبيض عظمي"},
      {"hex": "#a3ad93", "en": "Olive mute", "ar": "زيتوني خافت"},
      {"hex": "#1a1e16", "en": "Mat green", "ar": "أخضر سجادة"},
    ],
    "prices": [15, 15, 20],
    "en": {
      "back": "← Ibra Studio", "nav1": "WODs", "nav2": "Coaches", "nav3": "Drop-in", "nav4": "Join box",
      "kicker": "Cross-training community", "h1": "Show up. Work hard. Repeat.",
      "lead": "Industrial floor with daily WODs and a loud supportive community.",
      "cta1": "Try a drop-in", "cta2": "Today's WOD",
      "s_title": "This week", "c1t": "Engine", "c1p": "Intervals + capacity.",
      "c2t": "Strength", "c2p": "Squat focus day.", "c3t": "Team WOD", "c3p": "Partner metcon.",
      "suffix": " drop-in", "f1": "Daily programming", "f2": "All levels",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Box 42 · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "التمارين", "nav2": "المدربين", "nav3": "تجريبي", "nav4": "انضم",
      "kicker": "مجتمع تدريب متقاطع", "h1": "احضر. اجتهد. كرر.",
      "lead": "صالة صناعية بتمارين يومية ومجتمع داعم.",
      "cta1": "جرّب حصة", "cta2": "تمرين اليوم",
      "s_title": "هذا الأسبوع", "c1t": "تحمّل", "c1p": "فواصل وقدرة.",
      "c2t": "قوة", "c2p": "يوم سكوات.", "c3t": "جماعي", "c3p": "ميتكون مع شريك.",
      "suffix": " حصة", "f1": "برنامج يومي", "f2": "لكل المستويات",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "بوكس 42 · قالب Ibra Studio",
    },
  },
  {
    "id": "market-fresh", "title": "FreshBasket Market", "img": "market",
    "fonts_css": "Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700",
    "font_display": "Fredoka", "font_body": "Nunito",
    "vars": "--bg:#fff8f0;--text:#1b2a1f;--muted:#5d6b60;--card:#ffffff;--line:#e7d7c4;--accent:#16a34a;--on-accent:#fff;--max:1080px",
    "colors": [
      {"hex": "#fff8f0", "en": "Cream aisle", "ar": "كريمي"},
      {"hex": "#16a34a", "en": "Fresh green", "ar": "أخضر طازج"},
      {"hex": "#1b2a1f", "en": "Leaf dark", "ar": "ورقي داكن"},
      {"hex": "#fdba74", "en": "Citrus orange", "ar": "برتقال حمضي"},
      {"hex": "#ffffff", "en": "Clean white", "ar": "أبيض نظيف"},
    ],
    "prices": [0, 0, 0],
    "price_mode": "label",
    "en": {
      "back": "← Ibra Studio", "nav1": "Deals", "nav2": "Departments", "nav3": "Delivery", "nav4": "Shop now",
      "kicker": "Fresh today · Delivered fast", "h1": "Your weekly basket, filled smarter.",
      "lead": "Friendly supermarket - produce, bakery, weekly deals, home delivery.",
      "cta1": "Order delivery", "cta2": "This week's deals",
      "s_title": "Departments", "c1t": "Produce", "c1p": "Fruits & vegetables daily.",
      "c2t": "Dairy & eggs", "c2p": "Local brands, fresh milk.", "c3t": "Bakery", "c3p": "Warm bread every morning.",
      "c1pr": "Aisle 1-2", "c2pr": "Aisle 4", "c3pr": "Front",
      "suffix": "", "f1": "Same-day delivery", "f2": "Weekly offers",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "FreshBasket · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "العروض", "nav2": "الأقسام", "nav3": "التوصيل", "nav4": "تسوق",
      "kicker": "طازج اليوم · توصيل سريع", "h1": "سلّتك الأسبوعية… بذكاء.",
      "lead": "سوبرماركت ودود - خضار ومخبز وعروض وتوصيل.",
      "cta1": "اطلب توصيل", "cta2": "عروض الأسبوع",
      "s_title": "الأقسام", "c1t": "خضار وفواكه", "c1p": "تُختار يومياً.",
      "c2t": "ألبان وبيض", "c2p": "ماركات محلية.", "c3t": "المخبز", "c3p": "خبز دافئ كل صباح.",
      "c1pr": "ممر 1-2", "c2pr": "ممر 4", "c3pr": "المدخل",
      "suffix": "", "f1": "توصيل نفس اليوم", "f2": "عروض أسبوعية",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "فريش باسكت · قالب Ibra Studio",
    },
  },
  {
    "id": "market-city", "title": "CityMart Hyper", "img": "hyper",
    "fonts_css": "Sora:wght@600;700&family=Manrope:wght@400;600;700",
    "font_display": "Sora", "font_body": "Manrope",
    "vars": "--bg:#0f172a;--text:#e2e8f0;--muted:#94a3b8;--card:#1e293b;--line:rgba(226,232,240,.1);--accent:#38bdf8;--on-accent:#0f172a;--max:1100px",
    "colors": [
      {"hex": "#0f172a", "en": "Night navy", "ar": "كحلي ليلي"},
      {"hex": "#38bdf8", "en": "Sky accent", "ar": "سماوي"},
      {"hex": "#e2e8f0", "en": "Ice text", "ar": "نص جليدي"},
      {"hex": "#1e293b", "en": "Slate card", "ar": "أردوازي"},
      {"hex": "#94a3b8", "en": "Cool mute", "ar": "رمادي بارد"},
    ],
    "prices": [0, 0, 0], "price_mode": "label",
    "en": {
      "back": "← Ibra Studio", "nav1": "Categories", "nav2": "Hours", "nav3": "Locations", "nav4": "Find store",
      "kicker": "Hypermarket · City-wide", "h1": "Everything under one bright roof.",
      "lead": "Modern hypermarket - categories, hours, store-first layout.",
      "cta1": "Browse categories", "cta2": "Store hours",
      "s_title": "Shop by category", "c1t": "Electronics", "c1p": "Phones & home tech.",
      "c2t": "Home & living", "c2p": "Kitchen and décor.", "c3t": "Grocery", "c3p": "Full supermarket floor.",
      "c1pr": "Floor 2", "c2pr": "Floor 1", "c3pr": "Ground",
      "suffix": "", "f1": "Open 9-12", "f2": "Parking",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "CityMart · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "التصنيفات", "nav2": "الأوقات", "nav3": "الفروع", "nav4": "اعثر على فرع",
      "kicker": "هايبر ماركت", "h1": "كل ما تحتاجه تحت سقف واحد.",
      "lead": "هايبر حديث - تصنيفات وأوقات وتخطيط واضح.",
      "cta1": "تصفح التصنيفات", "cta2": "أوقات العمل",
      "s_title": "تسوق حسب القسم", "c1t": "إلكترونيات", "c1p": "هواتف وتقنية.",
      "c2t": "المنزل", "c2p": "مطبخ وديكور.", "c3t": "البقالة", "c3p": "سوبرماركت كامل.",
      "c1pr": "طابق 2", "c2pr": "طابق 1", "c3pr": "الأرضي",
      "suffix": "", "f1": "٩ ص - ١٢ م", "f2": "موقف",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "سيتي مارت · قالب Ibra Studio",
    },
  },
  {
    "id": "market-organic", "title": "GreenLeaf Organic", "img": "organic",
    "fonts_css": "Fraunces:wght@600;700&family=Karla:wght@400;600;700",
    "font_display": "Fraunces", "font_body": "Karla",
    "vars": "--bg:#f4f7f2;--text:#1c2b1f;--muted:#5b6b5e;--card:#ffffff;--line:#d5e0d4;--accent:#4d7c0f;--on-accent:#fff;--max:1020px",
    "colors": [
      {"hex": "#f4f7f2", "en": "Leaf mist", "ar": "ضباب ورقي"},
      {"hex": "#4d7c0f", "en": "Organic green", "ar": "أخضر عضوي"},
      {"hex": "#1c2b1f", "en": "Forest ink", "ar": "حبر غابة"},
      {"hex": "#d9f99d", "en": "Fresh lime", "ar": "ليموني فاتح"},
      {"hex": "#ffffff", "en": "Pure white", "ar": "أبيض نقي"},
    ],
    "prices": [18, 0, 0], "price_mode": "mixed",
    "en": {
      "back": "← Ibra Studio", "nav1": "Farm", "nav2": "Products", "nav3": "Story", "nav4": "Order box",
      "kicker": "Organic · Local farms", "h1": "Clean food from soil you can trust.",
      "lead": "Soft organic grocery - seasonal boxes and farm-to-table story.",
      "cta1": "Get a weekly box", "cta2": "Our farms",
      "s_title": "This season", "c1t": "Harvest box", "c1p": "8-10 seasonal items.",
      "c2t": "Pantry", "c2p": "Oils, grains, honey.", "c3t": "Dairy", "c3p": "Small-batch yogurt.",
      "c2pr": "Shop", "c3pr": "Chilled",
      "suffix": " / week", "f1": "No fake labels", "f2": "Jordan farms",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "GreenLeaf · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "المزارع", "nav2": "المنتجات", "nav3": "قصتنا", "nav4": "اطلب صندوقاً",
      "kicker": "عضوي · مزارع محلية", "h1": "طعام نظيف من تربة تثق بها.",
      "lead": "بقالة عضوية - صناديق موسمية وقصة من المزرعة.",
      "cta1": "صندوق أسبوعي", "cta2": "مزارعنا",
      "s_title": "هذا الموسم", "c1t": "صندوق الحصاد", "c1p": "٨-١٠ أصناف موسمية.",
      "c2t": "المؤن", "c2p": "زيوت وحبوب وعسل.", "c3t": "ألبان", "c3p": "دفعات صغيرة.",
      "c2pr": "تسوق", "c3pr": "مبرد",
      "suffix": " / أسبوع", "f1": "بدون تسميات وهمية", "f2": "مزارع أردنية",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "جرين ليف · قالب Ibra Studio",
    },
  },
  {
    "id": "clinic-care", "title": "CarePlus Clinic", "img": "clinic",
    "fonts_css": "Libre+Franklin:wght@600;700&family=Plus+Jakarta+Sans:wght@400;600;700",
    "font_display": "Libre Franklin", "font_body": "Plus Jakarta Sans",
    "vars": "--bg:#f0f7ff;--text:#0f2744;--muted:#5b7391;--card:#ffffff;--line:#d7e6f5;--accent:#2563eb;--on-accent:#fff;--max:1040px",
    "colors": [
      {"hex": "#f0f7ff", "en": "Clinic blue mist", "ar": "أزرق عيادي"},
      {"hex": "#2563eb", "en": "Trust blue", "ar": "أزرق ثقة"},
      {"hex": "#0f2744", "en": "Deep navy", "ar": "كحلي عميق"},
      {"hex": "#5b7391", "en": "Soft steel", "ar": "فولاذ ناعم"},
      {"hex": "#ffffff", "en": "Sterile white", "ar": "أبيض معقم"},
    ],
    "prices": [25, 40, 30],
    "en": {
      "back": "← Ibra Studio", "nav1": "Services", "nav2": "Doctors", "nav3": "Insurance", "nav4": "Book visit",
      "kicker": "Multi-specialty clinic", "h1": "Care that feels clear and human.",
      "lead": "Book visits, meet doctors, understand services - calm medical design.",
      "cta1": "Book appointment", "cta2": "Meet doctors",
      "s_title": "Services", "c1t": "General medicine", "c1p": "Checkups & follow-up.",
      "c2t": "Diagnostics", "c2p": "Labs & imaging referrals.", "c3t": "Pediatrics", "c3p": "Child wellness visits.",
      "suffix": " visit", "f1": "Licensed doctors", "f2": "Evening hours",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "CarePlus · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الخدمات", "nav2": "الأطباء", "nav3": "التأمين", "nav4": "احجز زيارة",
      "kicker": "عيادة متعددة التخصصات", "h1": "رعاية واضحة وإنسانية.",
      "lead": "احجز زيارات وتعرّف على الأطباء - تصميم طبي هادئ.",
      "cta1": "احجز موعداً", "cta2": "الأطباء",
      "s_title": "الخدمات", "c1t": "طب عام", "c1p": "فحوصات ومتابعة.",
      "c2t": "تشخيص", "c2p": "مختبرات وتصوير.", "c3t": "أطفال", "c3p": "متابعة صحة الطفل.",
      "suffix": " زيارة", "f1": "أطباء مرخّصون", "f2": "مواعيد مسائية",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "كير بلس · قالب Ibra Studio",
    },
  },
  {
    "id": "clinic-dental", "title": "BrightSmile Dental", "img": "dental",
    "fonts_css": "Quicksand:wght@600;700&family=Poppins:wght@400;600;700",
    "font_display": "Quicksand", "font_body": "Poppins",
    "vars": "--bg:#fafcff;--text:#16324f;--muted:#6b7c93;--card:#ffffff;--line:#e2ebf5;--accent:#0ea5e9;--on-accent:#fff;--max:1020px",
    "colors": [
      {"hex": "#fafcff", "en": "Smile white", "ar": "أبيض ابتسامة"},
      {"hex": "#0ea5e9", "en": "Bright sky", "ar": "سماوي مشرق"},
      {"hex": "#16324f", "en": "Deep teal text", "ar": "نص عميق"},
      {"hex": "#bae6fd", "en": "Soft aqua", "ar": "مائي ناعم"},
      {"hex": "#6b7c93", "en": "Quiet gray", "ar": "رمادي هادئ"},
    ],
    "prices": [25, 90, 0], "price_mode": "mixed",
    "en": {
      "back": "← Ibra Studio", "nav1": "Treatments", "nav2": "Gallery", "nav3": "FAQ", "nav4": "Book smile",
      "kicker": "Dental · Family & cosmetic", "h1": "Brighter smiles start here.",
      "lead": "Fresh dental clinic - whitening, cleanings, easy booking.",
      "cta1": "Book cleaning", "cta2": "Whitening offer",
      "s_title": "Popular treatments", "c1t": "Cleaning", "c1p": "Gentle hygiene + check.",
      "c2t": "Whitening", "c2p": "In-clinic brightening.", "c3t": "Aligners consult", "c3p": "Clear aligner assessment.",
      "c3pr": "Free visit",
      "suffix": "", "f1": "Painless focus", "f2": "Kids welcome",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "BrightSmile · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "العلاجات", "nav2": "المعرض", "nav3": "أسئلة", "nav4": "احجز",
      "kicker": "أسنان · تجميل وعائلة", "h1": "ابتسامة أسطع تبدأ من هنا.",
      "lead": "عيادة أسنان عصرية - تبييض وتنظيف وحجز سهل.",
      "cta1": "احجز تنظيفاً", "cta2": "عرض التبييض",
      "s_title": "علاجات شائعة", "c1t": "تنظيف", "c1p": "عناية لطيفة + فحص.",
      "c2t": "تبييض", "c2p": "جلسة داخل العيادة.", "c3t": "استشارة تقويم", "c3p": "تقييم تقويم شفاف.",
      "c3pr": "زيارة مجانية",
      "suffix": "", "f1": "تركيز على الراحة", "f2": "نستقبل الأطفال",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "ابتسامة مشرقة · قالب Ibra Studio",
    },
  },
  {
    "id": "clinic-family", "title": "Family Health Hub", "img": "family",
    "fonts_css": "Literata:wght@600;700&family=Source+Sans+3:wght@400;600;700",
    "font_display": "Literata", "font_body": "Source Sans 3",
    "vars": "--bg:#fff7ed;--text:#3b2a1a;--muted:#7c6654;--card:#fffdf8;--line:#f0e0cc;--accent:#ea580c;--on-accent:#fff;--max:1040px",
    "colors": [
      {"hex": "#fff7ed", "en": "Warm cream", "ar": "كريمي دافئ"},
      {"hex": "#ea580c", "en": "Care orange", "ar": "برتقالي رعاية"},
      {"hex": "#3b2a1a", "en": "Cocoa text", "ar": "نص كاكاو"},
      {"hex": "#fed7aa", "en": "Soft peach", "ar": "خوخي ناعم"},
      {"hex": "#7c6654", "en": "Warm mute", "ar": "دافئ خافت"},
    ],
    "prices": [20, 15, 0], "price_mode": "mixed",
    "en": {
      "back": "← Ibra Studio", "nav1": "Family care", "nav2": "Labs", "nav3": "Hours", "nav4": "Call clinic",
      "kicker": "Neighborhood family practice", "h1": "One clinic for the whole family.",
      "lead": "Kids, adults, labs, follow-ups - warm design for a trusted local clinic.",
      "cta1": "Book for family", "cta2": "Lab services",
      "s_title": "Why families choose us", "c1t": "Kids & adults", "c1p": "Care under one roof.",
      "c2t": "On-site labs", "c2p": "Fast clear reports.", "c3t": "Easy follow-up", "c3p": "Reminders via WhatsApp.",
      "c3pr": "WhatsApp",
      "suffix": "", "f1": "Walk-ins welcome", "f2": "Arabic & English",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Family Health Hub · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "رعاية العائلة", "nav2": "المختبر", "nav3": "الأوقات", "nav4": "اتصل",
      "kicker": "عيادة عائلية في الحي", "h1": "عيادة واحدة لكل العائلة.",
      "lead": "أطفال وكبار ومختبرات - تصميم دافئ لعيادة موثوقة.",
      "cta1": "احجز للعائلة", "cta2": "المختبر",
      "s_title": "لماذا العائلات", "c1t": "أطفال وكبار", "c1p": "رعاية تحت سقف واحد.",
      "c2t": "مختبر في الموقع", "c2p": "تقارير واضحة سريعة.", "c3t": "متابعة سهلة", "c3p": "تذكير عبر واتساب.",
      "c3pr": "واتساب",
      "suffix": "", "f1": "بدون موعد", "f2": "عربي وإنجليزي",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "صحة العائلة · قالب Ibra Studio",
    },
  },
  {
    "id": "restaurant", "title": "Olive & Ember", "img": "restaurant",
    "fonts_css": "Cormorant+Garamond:wght@600;700&family=Nunito:wght@400;600;700",
    "font_display": "Cormorant Garamond", "font_body": "Nunito",
    "vars": "--bg:#1c1410;--text:#f7efe6;--muted:#cbb8a4;--card:#261c16;--line:rgba(247,239,230,.1);--accent:#e2b87a;--on-accent:#24180f;--max:980px",
    "colors": [
      {"hex": "#1c1410", "en": "Ember black", "ar": "أسود جمر"},
      {"hex": "#e2b87a", "en": "Gold olive", "ar": "ذهبي زيتوني"},
      {"hex": "#f7efe6", "en": "Linen cream", "ar": "كتان كريمي"},
      {"hex": "#261c16", "en": "Wood brown", "ar": "بني خشبي"},
      {"hex": "#cbb8a4", "en": "Warm mute", "ar": "دافئ خافت"},
    ],
    "prices": [8.5, 16, 6],
    "en": {
      "back": "← Ibra Studio", "nav1": "Menu", "nav2": "Reserve", "nav3": "Location", "nav4": "Book table",
      "kicker": "Amman · Dinner · Fire kitchen", "h1": "Slow food. Warm nights.",
      "lead": "Fine-dining warmth with menu cards and a clear reservation path.",
      "cta1": "Reserve a table", "cta2": "View menu",
      "s_title": "Evening menu", "c1t": "Ember flatbread", "c1p": "Labneh, chili oil, herbs.",
      "c2t": "Citrus lamb", "c2p": "Burnt orange, freekeh.", "c3t": "Date & tahini cake", "c3p": "Sesame, cardamom cream.",
      "suffix": "", "f1": "Dinner 6-11", "f2": "Private table",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Olive & Ember · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "القائمة", "nav2": "احجز", "nav3": "الموقع", "nav4": "احجز طاولة",
      "kicker": "عمّان · عشاء · نار", "h1": "طعام بطيء. ليالٍ دافئة.",
      "lead": "أجواء مطعم راقٍ مع قائمة ومسار حجز واضح.",
      "cta1": "احجز طاولة", "cta2": "القائمة",
      "s_title": "قائمة المساء", "c1t": "خبز إمبر", "c1p": "لبنة وزيت فلفل.",
      "c2t": "خروف بالحمضيات", "c2p": "برتقال محروق وفريكة.", "c3t": "كعكة تمر وطحينة", "c3p": "سمسم وكريمة هيل.",
      "suffix": "", "f1": "عشاء ٦-١١", "f2": "طاولة خاصة",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "أوليف آند إمبر · قالب Ibra Studio",
    },
  },
  {
    "id": "restaurant-bistro", "title": "Noon Bistro", "img": "bistro",
    "fonts_css": "DM+Serif+Display&family=DM+Sans:wght@400;500;700",
    "font_display": "DM Serif Display", "font_body": "DM Sans",
    "vars": "--bg:#faf6f1;--text:#1c1917;--muted:#78716c;--card:#ffffff;--line:#e7e0d6;--accent:#b45309;--on-accent:#fff;--max:1000px",
    "colors": [
      {"hex": "#faf6f1", "en": "Brunch linen", "ar": "كتان برانش"},
      {"hex": "#b45309", "en": "Amber spice", "ar": "عنبر توابل"},
      {"hex": "#1c1917", "en": "Espresso text", "ar": "نص إسبريسو"},
      {"hex": "#fde68a", "en": "Sun yellow", "ar": "أصفر شمس"},
      {"hex": "#78716c", "en": "Stone mute", "ar": "حجري"},
    ],
    "prices": [7.5, 6.5, 4],
    "en": {
      "back": "← Ibra Studio", "nav1": "Menu", "nav2": "Brunch", "nav3": "Location", "nav4": "Reserve",
      "kicker": "Daytime bistro · Amman", "h1": "Sunlit plates. Slow brunch.",
      "lead": "Light modern bistro for brunch, coffee, and neighborhood lunches.",
      "cta1": "See brunch menu", "cta2": "Get directions",
      "s_title": "On the table", "c1t": "Shakshuka board", "c1p": "Eggs, herbs, flatbread.",
      "c2t": "Garden bowl", "c2p": "Grains, greens, citrus.", "c3t": "Lemon tart", "c3p": "Bright finish with cream.",
      "suffix": "", "f1": "Open 8-5", "f2": "Weekend brunch",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Noon Bistro · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "القائمة", "nav2": "برانش", "nav3": "الموقع", "nav4": "احجز",
      "kicker": "بيسترو نهاري", "h1": "أطباق مشمسة. برانش هادئ.",
      "lead": "بيسترو خفيف للبرانش والقهوة وغداء الحي.",
      "cta1": "قائمة البرانش", "cta2": "الاتجاهات",
      "s_title": "على الطاولة", "c1t": "شكشوكة", "c1p": "بيض وأعشاب وخبز.",
      "c2t": "صحن الحديقة", "c2p": "حبوب وخضار وصوص.", "c3t": "تارت ليمون", "c3p": "ختام منعش.",
      "suffix": "", "f1": "٨ ص - ٥ م", "f2": "برانش نهاية الأسبوع",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "نون بيسترو · قالب Ibra Studio",
    },
  },
  {
    "id": "restaurant-grill", "title": "Charcoal Grill House", "img": "grill",
    "fonts_css": "Oswald:wght@500;600;700&family=Roboto:wght@400;500;700",
    "font_display": "Oswald", "font_body": "Roboto",
    "vars": "--bg:#120e0c;--text:#f5ebe0;--muted:#b9a99a;--card:#1c1613;--line:rgba(245,235,224,.1);--accent:#f97316;--on-accent:#1c1008;--max:1040px",
    "colors": [
      {"hex": "#120e0c", "en": "Charcoal night", "ar": "فحمي ليلي"},
      {"hex": "#f97316", "en": "Flame orange", "ar": "برتقالي لهب"},
      {"hex": "#f5ebe0", "en": "Smoke cream", "ar": "كريمي دخان"},
      {"hex": "#1c1613", "en": "Grill dark", "ar": "شواء داكن"},
      {"hex": "#b9a99a", "en": "Ash mute", "ar": "رماد خافت"},
    ],
    "prices": [14, 16, 32],
    "en": {
      "back": "← Ibra Studio", "nav1": "Grill menu", "nav2": "Combos", "nav3": "Catering", "nav4": "Order now",
      "kicker": "Fire · Smoke · Meat", "h1": "Charcoal. Cut. Serve hot.",
      "lead": "Bold grill-house for mixed grills, combos, and late-night cravings.",
      "cta1": "Order mixed grill", "cta2": "View combos",
      "s_title": "From the fire", "c1t": "Mixed grill", "c1p": "Kebab, chicken, chops.",
      "c2t": "Ribs platter", "c2p": "Slow smoke, sticky glaze.", "c3t": "Family combo", "c3p": "Feeds 4 with sides.",
      "suffix": "", "f1": "Open late", "f2": "Delivery ready",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Charcoal Grill · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الشواء", "nav2": "الوجبات", "nav3": "تموين", "nav4": "اطلب الآن",
      "kicker": "نار · دخان · لحم", "h1": "فحم. تقطيع. تقديم ساخن.",
      "lead": "مطعم مشاوي جريء للمشاوي والوجبات وطلبات الليل.",
      "cta1": "اطلب مشاوي", "cta2": "الوجبات",
      "s_title": "من النار", "c1t": "مشاوي مشكلة", "c1p": "كباب ودجاج وريش.",
      "c2t": "طبق أضلاع", "c2p": "شواء بطيء وصوص.", "c3t": "وجبة عائلية", "c3p": "تكفي 4 مع مقبلات.",
      "suffix": "", "f1": "مفتوح متأخراً", "f2": "جاهز للتوصيل",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "بيت الشواء · قالب Ibra Studio",
    },
  },
  {
    "id": "cafe-brew", "title": "Brew & Bean Cafe", "img": "cafe",
    "fonts_css": "Libre+Baskerville:wght@700&family=Work+Sans:wght@400;600;700",
    "font_display": "Libre Baskerville", "font_body": "Work Sans",
    "vars": "--bg:#f3ebe3;--text:#2c1810;--muted:#7a5c4c;--card:#fffaf6;--line:#e4d4c6;--accent:#6f4e37;--on-accent:#fff;--max:980px",
    "colors": [
      {"hex": "#f3ebe3", "en": "Latte foam", "ar": "رغوة لاتيه"},
      {"hex": "#6f4e37", "en": "Coffee bean", "ar": "حب القهوة"},
      {"hex": "#2c1810", "en": "Roast dark", "ar": "تحميص داكن"},
      {"hex": "#a67c52", "en": "Caramel", "ar": "كراميل"},
      {"hex": "#7a5c4c", "en": "Cocoa mute", "ar": "كاكاو خافت"},
    ],
    "prices": [3.2, 3.8, 1.5],
    "en": {
      "back": "← Ibra Studio", "nav1": "Drinks", "nav2": "Food", "nav3": "Hours", "nav4": "Visit us",
      "kicker": "Specialty coffee", "h1": "Slow cups. Good beans.",
      "lead": "Cozy cafe - espresso menu, light bites, neighborhood hours.",
      "cta1": "See drink menu", "cta2": "Opening hours",
      "s_title": "Favorites", "c1t": "Flat white", "c1p": "Silky milk, rich espresso.",
      "c2t": "V60 pour-over", "c2p": "Single origin rotation.", "c3t": "Date oat cookie", "c3p": "Baked every morning.",
      "suffix": "", "f1": "Wi‑Fi friendly", "f2": "Beans to go",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Brew & Bean · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "المشروبات", "nav2": "الطعام", "nav3": "الأوقات", "nav4": "زورنا",
      "kicker": "قهوة مختصة", "h1": "فناجين بطيئة. حبوب ممتازة.",
      "lead": "مقهى دافئ - إسبريسو ووجبات خفيفة وأوقات الحي.",
      "cta1": "قائمة المشروبات", "cta2": "أوقات العمل",
      "s_title": "الأكثر طلباً", "c1t": "فلات وايت", "c1p": "حليب ناعم وإسبريسو.",
      "c2t": "V60", "c2p": "محصول أحادي.", "c3t": "كوكيز تمر", "c3p": "يُخبز كل صباح.",
      "suffix": "", "f1": "واي فاي", "f2": "حبوب للمنزل",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "برو آند بين · قالب Ibra Studio",
    },
  },
  {
    "id": "salon-luxe", "title": "Luxe Hair Studio", "img": "salon",
    "fonts_css": "Cormorant:wght@600;700&family=Jost:wght@400;500;600",
    "font_display": "Cormorant", "font_body": "Jost",
    "vars": "--bg:#1a1420;--text:#f7f0f8;--muted:#b5a6b8;--card:#241b2b;--line:rgba(247,240,248,.1);--accent:#e879f9;--on-accent:#1a1420;--max:1000px",
    "colors": [
      {"hex": "#1a1420", "en": "Velvet night", "ar": "ليلي مخملي"},
      {"hex": "#e879f9", "en": "Luxe fuchsia", "ar": "فوشيا فاخر"},
      {"hex": "#f7f0f8", "en": "Soft lilac white", "ar": "أبيض ليلكي"},
      {"hex": "#241b2b", "en": "Plum card", "ar": "برقوقي"},
      {"hex": "#b5a6b8", "en": "Mauve mute", "ar": "موف خافت"},
    ],
    "prices": [20, 45, 60],
    "en": {
      "back": "← Ibra Studio", "nav1": "Services", "nav2": "Stylists", "nav3": "Gallery", "nav4": "Book",
      "kicker": "Hair · Color · Care", "h1": "Your next look, crafted.",
      "lead": "Elegant salon - cuts, color, bridal, easy booking.",
      "cta1": "Book appointment", "cta2": "View services",
      "s_title": "Signature services", "c1t": "Cut & style", "c1p": "Consultation + finish.",
      "c2t": "Color", "c2p": "Balayage, gloss, full color.", "c3t": "Bridal trial", "c3p": "Hair & soft glam.",
      "suffix": " from", "f1": "Senior stylists", "f2": "Products on site",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Luxe Hair · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الخدمات", "nav2": "المصففين", "nav3": "المعرض", "nav4": "احجز",
      "kicker": "شعر · لون · عناية", "h1": "إطلالتك القادمة… بإتقان.",
      "lead": "صالون أنيق - قص وصبغ وعرايس وحجز.",
      "cta1": "احجز موعداً", "cta2": "الخدمات",
      "s_title": "خدمات مميزة", "c1t": "قص وتصفيف", "c1p": "استشارة + تشطيب.",
      "c2t": "صبغ", "c2p": "بالاياح ولمعة ولون.", "c3t": "تجربة عروس", "c3p": "شعر ومكياج ناعم.",
      "suffix": " من", "f1": "مصففون خبراء", "f2": "منتجات في الصالون",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "لوكس · قالب Ibra Studio",
    },
  },
  {
    "id": "realestate-keys", "title": "Keystone Homes", "img": "realestate",
    "fonts_css": "Playfair+Display:wght@600;700&family=Source+Sans+3:wght@400;600;700",
    "font_display": "Playfair Display", "font_body": "Source Sans 3",
    "vars": "--bg:#0c1222;--text:#e8eefc;--muted:#9aa8c7;--card:#141b2f;--line:rgba(232,238,252,.1);--accent:#d4a017;--on-accent:#1a1408;--max:1080px",
    "colors": [
      {"hex": "#0c1222", "en": "Estate navy", "ar": "كحلي عقاري"},
      {"hex": "#d4a017", "en": "Key gold", "ar": "ذهبي مفتاح"},
      {"hex": "#e8eefc", "en": "Cloud text", "ar": "نص سحابي"},
      {"hex": "#141b2f", "en": "Ink panel", "ar": "لوحة حبر"},
      {"hex": "#9aa8c7", "en": "Steel mute", "ar": "فولاذ خافت"},
    ],
    "prices": [185000, 320000, 210000],
    "en": {
      "back": "← Ibra Studio", "nav1": "Listings", "nav2": "Agents", "nav3": "Sell", "nav4": "Contact",
      "kicker": "Real estate agency", "h1": "Find the key to your next home.",
      "lead": "Listings, agents, and a strong contact path for buyers and sellers.",
      "cta1": "Browse homes", "cta2": "Talk to an agent",
      "s_title": "Featured listings", "c1t": "Abdoun apartment", "c1p": "3 bed · city view · parking.",
      "c2t": "Khalda villa", "c2p": "Garden · maid room.", "c3t": "Jbeiha duplex", "c3p": "Near schools · ready.",
      "suffix": "", "f1": "Verified listings", "f2": "Buyer + seller support",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Keystone Homes · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "العقارات", "nav2": "الوسطاء", "nav3": "بِع معنا", "nav4": "تواصل",
      "kicker": "وكالة عقارية", "h1": "اعثر على مفتاح بيتك القادم.",
      "lead": "عقارات ووسطاء ومسار تواصل واضح.",
      "cta1": "تصفح المنازل", "cta2": "تحدث مع وسيط",
      "s_title": "عقارات مميزة", "c1t": "شقة عبدون", "c1p": "3 غرف · إطلالة · موقف.",
      "c2t": "فيلا خلدا", "c2p": "حديقة · غرفة خادمة.", "c3t": "دوبلكس الجبيهة", "c3p": "قرب المدارس · جاهز.",
      "suffix": "", "f1": "عقارات موثّقة", "f2": "دعم مشتري وبائع",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "كي ستون · قالب Ibra Studio",
    },
  },
  {
    "id": "saas-landing", "title": "NovaPulse", "img": "saas",
    "fonts_css": "Outfit:wght@600;700&family=DM+Sans:wght@400;500;700",
    "font_display": "Outfit", "font_body": "DM Sans",
    "vars": "--bg:#07090f;--text:#eef2ff;--muted:#93a0b8;--card:#111622;--line:rgba(255,255,255,.08);--accent:#7c5cff;--on-accent:#fff;--max:1040px",
    "colors": [
      {"hex": "#07090f", "en": "Void black", "ar": "أسود فراغ"},
      {"hex": "#7c5cff", "en": "Pulse violet", "ar": "بنفسجي نبض"},
      {"hex": "#eef2ff", "en": "Ice white", "ar": "أبيض جليد"},
      {"hex": "#22d3ee", "en": "Cyan signal", "ar": "سماوي إشارة"},
      {"hex": "#93a0b8", "en": "Cool mute", "ar": "رمادي بارد"},
    ],
    "prices": [0, 29, 79], "price_mode": "saas",
    "en": {
      "back": "← Ibra Studio", "nav1": "Product", "nav2": "Pricing", "nav3": "Docs", "nav4": "Start free",
      "kicker": "SaaS landing template", "h1": "Ship updates customers notice.",
      "lead": "Dark conversion landing for apps and tools - hero, features, strong CTA.",
      "cta1": "Get started", "cta2": "View demo",
      "s_title": "Plans", "c1t": "Free", "c1p": "Try core features.",
      "c2t": "Pro", "c2p": "Teams & integrations.", "c3t": "Business", "c3p": "Scale with support.",
      "c1pr": "Free",
      "suffix": " / mo", "f1": "No backend needed", "f2": "Mobile ready",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "NovaPulse · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "المنتج", "nav2": "الأسعار", "nav3": "التوثيق", "nav4": "ابدأ مجاناً",
      "kicker": "قالب صفحة منتج", "h1": "أطلق تحديثات يلاحظها عملاؤك.",
      "lead": "صفحة هبوط داكنة للتطبيقات - بطل ومميزات ودعوة واضحة.",
      "cta1": "ابدأ الآن", "cta2": "عرض تجريبي",
      "s_title": "الخطط", "c1t": "مجاني", "c1p": "جرّب الميزات الأساسية.",
      "c2t": "احترافي", "c2p": "فرق وتكاملات.", "c3t": "أعمال", "c3p": "توسّع مع دعم.",
      "c1pr": "مجاني",
      "suffix": " / شهر", "f1": "بدون خادم", "f2": "متوافق مع الجوال",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "نوفا بالس · قالب Ibra Studio",
    },
  },
  {
    "id": "portfolio", "title": "Aria Cole Portfolio", "img": "portfolio",
    "fonts_css": "Fraunces:wght@600;700&family=Schibsted+Grotesk:wght@400;500;600",
    "font_display": "Fraunces", "font_body": "Schibsted Grotesk",
    "vars": "--bg:#f6f1e8;--text:#1a1410;--muted:#6b5e52;--card:#fffdf8;--line:#e6dccf;--accent:#c45c26;--on-accent:#fff;--max:1000px",
    "colors": [
      {"hex": "#f6f1e8", "en": "Paper warm", "ar": "ورقي دافئ"},
      {"hex": "#c45c26", "en": "Clay accent", "ar": "طيني"},
      {"hex": "#1a1410", "en": "Ink brown", "ar": "بني حبر"},
      {"hex": "#d9c3a8", "en": "Sand tone", "ar": "رملي"},
      {"hex": "#6b5e52", "en": "Muted cocoa", "ar": "كاكاو خافت"},
    ],
    "prices": [0, 0, 0], "price_mode": "label",
    "en": {
      "back": "← Ibra Studio", "nav1": "Work", "nav2": "About", "nav3": "Contact", "nav4": "Hire me",
      "kicker": "Creative portfolio", "h1": "Design with room to breathe.",
      "lead": "Editorial portfolio for freelancers - big type and project cards.",
      "cta1": "View selected work", "cta2": "About",
      "s_title": "Selected projects", "c1t": "Brand system", "c1p": "Identity and packaging.",
      "c2t": "Studio website", "c2p": "Clean motion-ready layout.", "c3t": "Festival booklet", "c3p": "Typography-led print.",
      "c1pr": "Case study", "c2pr": "Web", "c3pr": "Print",
      "suffix": "", "f1": "Available for work", "f2": "Remote friendly",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Portfolio · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "الأعمال", "nav2": "نبذة", "nav3": "تواصل", "nav4": "وظّفني",
      "kicker": "بورتفوليو إبداعي", "h1": "تصميم بمساحة للتنفّس.",
      "lead": "معرض أعمال للمستقلين - خطوط كبيرة وبطاقات مشاريع.",
      "cta1": "عرض الأعمال", "cta2": "نبذة",
      "s_title": "مشاريع مختارة", "c1t": "نظام هوية", "c1p": "هوية وتغليف.",
      "c2t": "موقع استوديو", "c2p": "تخطيط نظيف.", "c3t": "كتيّب مهرجان", "c3p": "طباعة تعتمد على الخط.",
      "c1pr": "دراسة حالة", "c2pr": "ويب", "c3pr": "طباعة",
      "suffix": "", "f1": "متاح للعمل", "f2": "عن بُعد",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "بورتفوليو · قالب Ibra Studio",
    },
  },
  {
    "id": "ecommerce", "title": "Forma Store", "img": "shop",
    "fonts_css": "Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600;700",
    "font_display": "Space Grotesk", "font_body": "Inter",
    "vars": "--bg:#fafafa;--text:#111;--muted:#667085;--card:#fff;--line:#e7e7ea;--accent:#111;--on-accent:#fff;--max:1040px",
    "colors": [
      {"hex": "#fafafa", "en": "Gallery gray", "ar": "رمادي معرض"},
      {"hex": "#111111", "en": "Ink black", "ar": "أسود حبر"},
      {"hex": "#ffffff", "en": "Product white", "ar": "أبيض منتج"},
      {"hex": "#667085", "en": "UI mute", "ar": "واجهة خافتة"},
      {"hex": "#dbe4ff", "en": "Soft indigo", "ar": "نيلي ناعم"},
    ],
    "prices": [63, 170, 25],  # approx JOD from $89/$240/$36
    "en": {
      "back": "← Ibra Studio", "nav1": "Shop", "nav2": "New", "nav3": "About", "nav4": "Cart",
      "kicker": "Product shop template", "h1": "Everyday objects, sharper form.",
      "lead": "Lightweight shop with product cards and a strong collection hero.",
      "cta1": "Shop collection", "cta2": "New arrivals",
      "s_title": "Featured", "c1t": "Arc Lamp", "c1p": "Matte steel finish.",
      "c2t": "Soft Chair", "c2p": "Wool blend comfort.", "c3t": "Desk Tray", "c3p": "Oak / black options.",
      "suffix": "", "f1": "Free shipping*", "f2": "Easy returns",
      "brand_title": "Brand kit", "fonts_label": "Fonts", "colors_label": "Colors",
      "font_roles": "Headings · Body", "foot": "Forma Store · Ibra Studio template",
    },
    "ar": {
      "back": "← Ibra Studio", "nav1": "تسوق", "nav2": "جديد", "nav3": "عنّا", "nav4": "السلة",
      "kicker": "قالب متجر منتجات", "h1": "أشياء يومية… بشكل أحدّ.",
      "lead": "متجر خفيف مع بطاقات منتجات وبطل مجموعة.",
      "cta1": "تسوق المجموعة", "cta2": "وصل حديثاً",
      "s_title": "مميز", "c1t": "مصباح آرك", "c1p": "فولاذ مطفي.",
      "c2t": "كرسي ناعم", "c2p": "مزيج صوف.", "c3t": "صينية مكتب", "c3p": "سنديان / أسود.",
      "suffix": "", "f1": "شحن مجاني*", "f2": "إرجاع سهل",
      "brand_title": "هوية العلامة", "fonts_label": "الخطوط", "colors_label": "الألوان",
      "font_roles": "عناوين · نص", "foot": "فورما · قالب Ibra Studio",
    },
  },
]

BASE_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--body),system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.55;min-height:100vh}
html[dir="rtl"] body{font-family:"IBM Plex Sans Arabic",var(--body),system-ui,sans-serif}
a{color:inherit;text-decoration:none}
img{display:block;max-width:100%;height:100%;object-fit:cover}
.wrap{width:min(100% - 2rem,var(--max,1040px));margin:0 auto}
.topbar{position:sticky;top:0;z-index:50;display:flex;justify-content:space-between;align-items:center;gap:.75rem;padding:.55rem 1rem;background:rgba(0,0,0,.4);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);flex-wrap:wrap}
.back{font-size:.85rem;font-weight:600;opacity:.9}
.toggles{display:flex;gap:.45rem;align-items:center;flex-wrap:wrap}
.lang,.currency-toggle{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;background:rgba(0,0,0,.15)}
.lang-btn,.currency-toggle button{border:0;background:transparent;color:var(--muted);padding:.32rem .65rem;cursor:pointer;font-weight:700;font-size:.78rem}
.lang-btn.active,.currency-toggle button.active{background:rgba(255,255,255,.12);color:var(--accent)}
nav.site{display:flex;justify-content:space-between;align-items:center;padding:1.1rem 0;gap:1rem}
.brand{font-family:var(--display),serif;font-weight:700;font-size:1.3rem;letter-spacing:-.02em}
.nav-links{display:flex;gap:1rem;list-style:none;color:var(--muted);font-size:.9rem;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;padding:.72rem 1.15rem;font-weight:700;border:0;cursor:pointer}
.btn-a{background:var(--accent);color:var(--on-accent,#111)}
.btn-g{background:transparent;border:1px solid var(--line);color:var(--text)}
.hero{padding:2rem 0 1.5rem}
.grid2{display:grid;grid-template-columns:1.05fr .95fr;gap:1.4rem;align-items:center}
.kicker{color:var(--accent);font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:.72rem;margin-bottom:.7rem}
h1{font-family:var(--display),serif;font-size:clamp(2rem,4.8vw,3.2rem);line-height:1.05;letter-spacing:-.03em;margin-bottom:.75rem}
.lead{color:var(--muted);max-width:34rem;margin-bottom:1.2rem}
.cta{display:flex;flex-wrap:wrap;gap:.55rem;margin-bottom:1.1rem}
.meta{display:flex;gap:1.1rem;flex-wrap:wrap;color:var(--muted);font-size:.9rem}
.hero-photo{border-radius:22px;border:1px solid var(--line);min-height:300px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.25)}
.hero-photo img{width:100%;height:100%;min-height:300px;object-fit:cover}
.section{padding:1.2rem 0 2.5rem}
.section h2{font-family:var(--display),serif;font-size:1.55rem;margin-bottom:1rem}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}
.card-img{aspect-ratio:16/11;overflow:hidden}
.card-img img{width:100%;height:100%;object-fit:cover}
.card-body{padding:1rem}
.card h3{font-family:var(--display),serif;font-size:1.15rem;margin-bottom:.3rem}
.card p{color:var(--muted);font-size:.9rem}
.price{display:block;margin-top:.55rem;font-weight:800;color:var(--accent)}
.brand-kit{margin:1rem 0 2.5rem;padding:1.25rem;border:1px solid var(--line);border-radius:18px;background:var(--card)}
.brand-kit h2{font-family:var(--display),serif;font-size:1.25rem;margin-bottom:.85rem}
.brand-row{margin-bottom:1rem}
.brand-row:last-child{margin-bottom:0}
.brand-label{font-size:.75rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:.45rem}
.font-lines{display:grid;gap:.35rem;font-size:.95rem}
.font-lines strong{color:var(--accent)}
.swatches{display:flex;flex-wrap:wrap;gap:.75rem}
.swatch{display:flex;align-items:center;gap:.5rem;min-width:140px}
.swatch-sq{width:28px;height:28px;border-radius:7px;border:1px solid rgba(128,128,128,.45);flex-shrink:0;box-shadow:inset 0 0 0 1px rgba(255,255,255,.15)}
.swatch-meta{display:flex;flex-direction:column;line-height:1.25}
.swatch-name{font-size:.82rem;font-weight:600}
.swatch-hex{font-size:.75rem;color:var(--muted);font-family:ui-monospace,monospace}
.footer{border-top:1px solid var(--line);padding:1.3rem 0 2rem;color:var(--muted);font-size:.88rem;display:flex;flex-wrap:wrap;justify-content:space-between;gap:.6rem}
@media(max-width:800px){.grid2,.grid3{grid-template-columns:1fr}.nav-links{display:none}}
"""


def price_html(t, idx, key):
    mode = t.get("price_mode", "money")
    en = t["en"]
    label_key = f"c{idx}pr"
    if mode == "label" or (mode == "mixed" and t["prices"][idx - 1] == 0):
        # static i18n label
        return f'<span class="price" data-i18n="{label_key}">{en.get(label_key, "")}</span>'
    if mode == "saas" and idx == 1:
        return f'<span class="price" data-i18n="c1pr">Free</span>'
    jod = t["prices"][idx - 1]
    # show decimal if needed
    jod_s = str(int(jod)) if float(jod) == int(jod) else str(jod)
    return f'<span class="price" data-jod="{jod_s}" data-suffix=""></span>'


def brand_swatches(t):
    parts = []
    for c in t["colors"]:
        parts.append(
            f'''<div class="swatch">
          <span class="swatch-sq" style="background:{c["hex"]}" title="{c["hex"]}"></span>
          <span class="swatch-meta">
            <span class="swatch-name" data-color-en="{c["en"]}" data-color-ar="{c["ar"]}">{c["en"]}</span>
            <span class="swatch-hex">{c["hex"]}</span>
          </span>
        </div>'''
        )
    return "\n        ".join(parts)


def write_one(t):
    folder = TDIR / t["id"]
    folder.mkdir(parents=True, exist_ok=True)
    img = t["img"]
    base = f"../../assets/images/{img}"
    # price spans with suffix from lang - apply via JS after i18n
    p1 = price_html(t, 1, "c1")
    p2 = price_html(t, 2, "c2")
    p3 = price_html(t, 3, "c3")
    # For money prices, suffix applied in applyMoneySuffix after lang
    for i, p in enumerate([p1, p2, p3], 1):
        if f'data-jod="{t["prices"][i-1]}"' in p or "data-jod=" in p:
            pass

    # Fix price_html to use actual jod values
    def ph(i):
        mode = t.get("price_mode", "money")
        jod = t["prices"][i - 1]
        label_key = f"c{i}pr"
        if mode == "label":
            return f'<span class="price" data-i18n="{label_key}"></span>'
        if mode == "saas" and i == 1:
            return f'<span class="price" data-i18n="c1pr"></span>'
        if mode == "mixed" and jod == 0:
            return f'<span class="price" data-i18n="{label_key}"></span>'
        jod_s = str(int(jod)) if float(jod) == int(float(jod)) else str(jod)
        return f'<span class="price money-price" data-jod="{jod_s}"></span>'

    p1, p2, p3 = ph(1), ph(2), ph(3)
    dict_js = json.dumps({"en": t["en"], "ar": t["ar"]}, ensure_ascii=False)
    colors_js = json.dumps(t["colors"], ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t["title"]} · Ibra Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;600;700&family={t["fonts_css"]}&display=swap" rel="stylesheet" />
  <style>
:root{{--display:'{t["font_display"]}';--body:'{t["font_body"]}';{t["vars"]}}}
{BASE_CSS}
  </style>
</head>
<body>
  <div class="topbar">
    <a class="back" href="../../index.html" data-i18n="back">← Ibra Studio</a>
    <div class="toggles">
      <div class="lang" aria-label="Language">
        <button type="button" class="lang-btn active" data-lang="en">EN</button>
        <button type="button" class="lang-btn" data-lang="ar">ع</button>
      </div>
      <div class="currency-toggle" aria-label="Currency">
        <button type="button" data-currency="JOD" class="active">JOD</button>
        <button type="button" data-currency="USD">USD</button>
      </div>
    </div>
  </div>
  <div class="wrap">
    <nav class="site">
      <div class="brand">{t["title"]}</div>
      <ul class="nav-links">
        <li data-i18n="nav1"></li>
        <li data-i18n="nav2"></li>
        <li data-i18n="nav3"></li>
      </ul>
      <a class="btn btn-a" href="#" data-i18n="nav4"></a>
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
        <div class="meta">
          <span data-i18n="f1"></span>
          <span data-i18n="f2"></span>
        </div>
      </div>
      <div class="hero-photo"><img src="{base}/hero.jpg" alt="{t["title"]}" width="800" height="600" /></div>
    </header>
    <section class="section">
      <h2 data-i18n="s_title"></h2>
      <div class="grid3">
        <article class="card">
          <div class="card-img"><img src="{base}/card1.jpg" alt="" loading="lazy" /></div>
          <div class="card-body"><h3 data-i18n="c1t"></h3><p data-i18n="c1p"></p>{p1}</div>
        </article>
        <article class="card">
          <div class="card-img"><img src="{base}/card2.jpg" alt="" loading="lazy" /></div>
          <div class="card-body"><h3 data-i18n="c2t"></h3><p data-i18n="c2p"></p>{p2}</div>
        </article>
        <article class="card">
          <div class="card-img"><img src="{base}/card3.jpg" alt="" loading="lazy" /></div>
          <div class="card-body"><h3 data-i18n="c3t"></h3><p data-i18n="c3p"></p>{p3}</div>
        </article>
      </div>
    </section>
    <section class="brand-kit" id="brand-kit">
      <h2><span data-i18n="brand_title">Brand kit</span> · {t["title"]}</h2>
      <div class="brand-row">
        <div class="brand-label" data-i18n="fonts_label">Fonts</div>
        <div class="font-lines">
          <div><strong>{t["font_display"]}</strong> - <span data-i18n="font_roles">Headings · Body</span> (display)</div>
          <div><strong>{t["font_body"]}</strong> - body</div>
        </div>
      </div>
      <div class="brand-row">
        <div class="brand-label" data-i18n="colors_label">Colors</div>
        <div class="swatches">
        {brand_swatches(t)}
        </div>
      </div>
    </section>
    <footer class="footer">
      <span data-i18n="foot"></span>
      <span>EN · AR · JOD · USD</span>
    </footer>
  </div>
  <script src="../shared/lang.js"></script>
  <script src="../../js/currency.js"></script>
  <script>
    var DICT = {dict_js};
    var COLORS = {colors_js};
    function paintColorNames(lang) {{
      document.querySelectorAll("[data-color-en]").forEach(function (el) {{
        el.textContent = lang === "ar" ? el.getAttribute("data-color-ar") : el.getAttribute("data-color-en");
      }});
    }}
    function applySuffix() {{
      var lang = document.documentElement.lang === "ar" ? "ar" : "en";
      var suf = (DICT[lang] && DICT[lang].suffix) || "";
      document.querySelectorAll(".money-price").forEach(function (el) {{
        el.setAttribute("data-suffix", suf);
      }});
      if (window.IbraMoney) IbraMoney.applyAll();
    }}
    var _init = IbraLang.init;
    IbraLang.init = function (dict) {{
      _init(dict);
      paintColorNames(document.documentElement.lang === "ar" ? "ar" : "en");
      applySuffix();
      document.querySelectorAll(".lang-btn").forEach(function (btn) {{
        btn.addEventListener("click", function () {{
          setTimeout(function () {{
            paintColorNames(btn.getAttribute("data-lang"));
            applySuffix();
          }}, 0);
        }});
      }});
    }};
    IbraLang.init(DICT);
    document.addEventListener("ibra-currency", applySuffix);
  </script>
</body>
</html>
"""
    (folder / "index.html").write_text(html, encoding="utf-8")
    print("wrote", t["id"])


def main():
    for t in TEMPLATES:
        write_one(t)
    print("done", len(TEMPLATES))


if __name__ == "__main__":
    main()
