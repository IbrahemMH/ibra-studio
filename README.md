# Ibra Studio

**Website design studio by Ibrahim** — modern templates, custom design, and full sites ready to go live.

| | |
|---|---|
| **Live site** | https://IbrahemMH.github.io/ibra-studio/ |
| **Email** | ibraheem.ha2@hotmail.com |
| **Phone / WhatsApp** | +962 792939802 |
| **Languages** | English · العربية |

---

## What this site is

A professional offer page where people can:

1. Browse **live website templates**
2. Request **design-only** or a **full site online**
3. Contact Ibrahim by **email** or **WhatsApp**

Built as static HTML/CSS/JS — free hosting on **GitHub Pages**, no server required.

---

## Project structure

```text
ibra-studio/
├── index.html                 # Main landing (EN + AR)
├── css/
│   └── styles.css             # Design system
├── js/
│   └── main.js                # Language toggle, filters, contact
├── templates/                 # Live demo mini-sites
│   ├── saas-landing/          # Product / startup landing
│   ├── portfolio/             # Creative portfolio
│   ├── restaurant/            # Local business / food
│   └── ecommerce/             # Small shop / products
├── assets/                    # Images & brand files (optional)
├── .gitignore
└── README.md
```

---

## Features

- Bilingual UI (**EN | ع**) with RTL support for Arabic  
- Template gallery with live previews  
- Services: template customize · custom design · full site online  
- Contact form (opens email) + WhatsApp button  
- Mobile-friendly layout  

---

## Preview on your PC

```powershell
cd "D:\AI Assistant\opencode\offer-site"
start index.html
```

Or double-click `index.html` in File Explorer.

---

## Deploy / update GitHub Pages

Already set up for account **IbrahemMH**, repo **ibra-studio**.

After you change files:

```powershell
cd "D:\AI Assistant\opencode\offer-site"
git add .
git commit -m "Update site"
git push
```

Site updates at:  
**https://IbrahemMH.github.io/ibra-studio/**

Pages settings (if needed): repo → **Settings → Pages** → branch `main` → folder `/ (root)`.

---

## Customize

| Change | File |
|--------|------|
| Brand name / page text (HTML) | `index.html` |
| EN & AR translations | `js/main.js` → `i18n` |
| Email / phone / WhatsApp | `js/main.js` → `EMAIL`, `PHONE_*` |
| Colors & layout | `css/styles.css` |
| Add a template | New folder under `templates/` + card in `index.html` |

---

## Contact

**Ibrahim** · Ibra Studio  

- Email: [ibraheem.ha2@hotmail.com](mailto:ibraheem.ha2@hotmail.com)  
- WhatsApp: [+962 792939802](https://wa.me/962792939802)  

---

© Ibrahim · Ibra Studio
