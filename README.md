# Ibra Studio — Offer Site

Professional website design showcase. Templates + contact so people can hire you to design or build a full site.

**Brand:** Ibra Studio  
**Contact:** ibraheem.ha2@hotmail.com · +962 792939802  
**Languages:** English + Arabic (toggle on the site)

## Local preview

Open in a browser:

```text
D:\AI Assistant\opencode\offer-site\index.html
```

Or from this folder:

```powershell
start index.html
```

## Publish to GitHub Pages

### 1. Log in to GitHub CLI (one time)

```powershell
gh auth login
```

Choose: **GitHub.com** → **HTTPS** → **Login with a web browser**

### 2. Create repo + push + enable Pages

From this folder (`offer-site`):

```powershell
cd "D:\AI Assistant\opencode\offer-site"
git init
git add .
git commit -m "Initial Ibra Studio offer site"
gh repo create ibra-studio --public --source=. --remote=origin --push
gh api -X POST repos/:owner/ibra-studio/pages -f build_type=legacy -f source='{"branch":"main","path":"/"}'
```

If the Pages API line fails, do it in the browser:

1. Open your repo on GitHub  
2. **Settings → Pages**  
3. **Source:** Deploy from a branch  
4. **Branch:** `main` · folder `/ (root)` → **Save**

### 3. Your live URL

```text
https://YOUR-USERNAME.github.io/ibra-studio/
```

Replace `YOUR-USERNAME` with your GitHub username.

## Project structure

```text
offer-site/
├── index.html                 # Main bilingual landing page
├── css/styles.css
├── js/main.js
├── templates/
│   ├── saas-landing/          # Live demo
│   ├── portfolio/
│   ├── restaurant/
│   └── ecommerce/
└── README.md
```

## Customize later

| What | Where |
|------|--------|
| Brand name | `index.html` logo text |
| Email / phone | `js/main.js` (`EMAIL`, `PHONE_*`) |
| EN/AR text | `js/main.js` (`i18n` object) |
| New template | Add folder under `templates/` + card in `index.html` |
