/* Shared EN/AR for all Ibra Studio templates — reads ibra_lang from localStorage */
(function () {
  function apply(dict, lang) {
    const t = dict[lang] || dict.en;
    const dir = lang === "ar" ? "rtl" : "ltr";
    document.documentElement.lang = lang;
    document.documentElement.dir = dir;
    document.body && document.body.setAttribute("dir", dir);
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      if (t[key] != null) el.textContent = t[key];
    });
    document.querySelectorAll("[data-i18n-html]").forEach(function (el) {
      var key = el.getAttribute("data-i18n-html");
      if (t[key] != null) el.innerHTML = t[key];
    });
    document.querySelectorAll("[data-i18n-placeholder]").forEach(function (el) {
      var key = el.getAttribute("data-i18n-placeholder");
      if (t[key] != null) el.setAttribute("placeholder", t[key]);
    });
    document.querySelectorAll(".lang-btn").forEach(function (btn) {
      btn.classList.toggle("active", btn.getAttribute("data-lang") === lang);
    });
    try {
      localStorage.setItem("ibra_lang", lang);
    } catch (e) {}
  }

  window.IbraLang = {
    init: function (dict) {
      var saved = "en";
      try {
        saved = localStorage.getItem("ibra_lang") || "en";
      } catch (e) {}
      if (saved !== "ar" && saved !== "en") saved = "en";
      apply(dict, saved);
      document.querySelectorAll(".lang-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
          apply(dict, btn.getAttribute("data-lang"));
        });
      });
    },
  };
})();
