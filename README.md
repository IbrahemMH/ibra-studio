# Ibra Studio

**Website design studio by Ibrahim** - modern bilingual templates and full sites ready to go live.

| | |
|---|---|
| **Live site** | https://ibrahemmh.github.io/ibra-studio/ |
| **Email** | ibraheem.ha2@hotmail.com |
| **Phone / WhatsApp** | +962 792939802 |
| **Languages** | English · العربية |

---

## What this site is

A professional offer page where people can:

1. Browse **6 featured** templates (18 total demos)
2. Preview each template in **English and Arabic**
3. Switch **JOD | USD** next to language
4. See **pricing packages** (`pricing.html` + `PRICING.md`)
5. Open templates with real photos + **brand kit** (fonts + color squares)

See **PRICING.md** for full package explanation and default prices.

---

## Template categories

| Category | Templates |
|----------|-----------|
| **Gym** | Iron Forge, Flow Wellness, Box 42 |
| **Supermarket** | FreshBasket, CityMart, GreenLeaf Organic |
| **Clinic** | CarePlus, BrightSmile Dental, Family Health Hub |
| **Restaurant / Cafe** | Olive & Ember, Noon Bistro, Charcoal Grill, Brew & Bean |
| **Salon** | Luxe Hair Studio |
| **Business** | NovaPulse SaaS, Keystone Homes |
| **Creative / Shop** | Portfolio, Forma Store |

Every template has **EN | ع** toggle and remembers language via `localStorage`.

---

## Project structure

```text
ibra-studio/
├── index.html
├── css/styles.css
├── js/
│   ├── catalog.js          # Gallery list (EN + AR titles)
│   └── main.js             # Site i18n, filters, contact
├── templates/
│   ├── shared/lang.js      # Shared bilingual engine
│   ├── gym-iron/ …
│   ├── market-fresh/ …
│   ├── clinic-care/ …
│   └── …
├── scripts/generate_templates.py
└── README.md
```

---

## Preview on your PC

```powershell
cd "D:\AI Assistant\opencode\offer-site"
start index.html
```

---

## Update GitHub Pages

```powershell
cd "D:\AI Assistant\opencode\offer-site"
git add .
git commit -m "Update site"
git push
```

Live: **https://ibrahemmh.github.io/ibra-studio/**

---

## Contact

**Ibrahim** · Ibra Studio  

- Email: ibraheem.ha2@hotmail.com  
- WhatsApp: +962 792939802  

© Ibrahim · Ibra Studio
