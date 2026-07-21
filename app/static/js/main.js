/**
 * D-Tech Dynamics — Core JS
 * Handles sticky navbar scroll state and mobile navigation toggle.
 * Vanilla JS only — no frameworks.
 */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    initStickyNav();
    initMobileNav();
  });

  function initStickyNav() {
    var navbar = document.querySelector(".navbar");
    if (!navbar) return;

    function onScroll() {
      if (window.scrollY > 12) {
        navbar.classList.add("is-scrolled");
      } else {
        navbar.classList.remove("is-scrolled");
      }
    }

    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function initMobileNav() {
    var toggle = document.querySelector(".navbar__toggle");
    var links = document.querySelector(".navbar__links");
    if (!toggle || !links) return;

    toggle.addEventListener("click", function () {
      var isOpen = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    // Close mobile menu when a link is clicked.
    links.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }
})();
