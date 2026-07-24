/* JOD base prices → display JOD or USD */
(function () {
  var RATE = 1.41; // 1 JOD ≈ 1.41 USD

  function getCurrency() {
    try {
      var c = localStorage.getItem("ibra_currency");
      return c === "USD" ? "USD" : "JOD";
    } catch (e) {
      return "JOD";
    }
  }

  function setCurrency(c) {
    c = c === "USD" ? "USD" : "JOD";
    try {
      localStorage.setItem("ibra_currency", c);
    } catch (e) {}
    applyAll();
    document.dispatchEvent(new CustomEvent("ibra-currency", { detail: c }));
  }

  function formatJod(amount) {
    var n = Number(amount);
    if (isNaN(n)) return "";
    var cur = getCurrency();
    if (cur === "USD") {
      var usd = Math.round(n * RATE);
      return "$" + usd.toLocaleString("en-US");
    }
    return n.toLocaleString("en-US") + " JOD";
  }

  function applyAll() {
    var cur = getCurrency();
    document.querySelectorAll(".currency-toggle button").forEach(function (btn) {
      btn.classList.toggle("active", btn.getAttribute("data-currency") === cur);
    });
    document.querySelectorAll("[data-jod]").forEach(function (el) {
      var jod = el.getAttribute("data-jod");
      var suffix = el.getAttribute("data-suffix") || "";
      var prefix = el.getAttribute("data-prefix") || "";
      el.textContent = prefix + formatJod(jod) + suffix;
    });
    document.querySelectorAll("[data-jod-range]").forEach(function (el) {
      var parts = el.getAttribute("data-jod-range").split("-");
      var a = formatJod(parts[0]);
      var b = formatJod(parts[1]);
      var prefix = el.getAttribute("data-prefix") || "From ";
      el.textContent = prefix + a + " – " + b;
    });
  }

  function init() {
    document.querySelectorAll(".currency-toggle button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        setCurrency(btn.getAttribute("data-currency"));
      });
    });
    applyAll();
  }

  window.IbraMoney = {
    getCurrency: getCurrency,
    setCurrency: setCurrency,
    formatJod: formatJod,
    applyAll: applyAll,
    init: init,
    RATE: RATE,
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
