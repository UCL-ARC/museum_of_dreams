import { setTagColours } from "./dynamicTagColours.js";
import { prevSlide, nextSlide } from "./carousel.js";
import { addPreventMenuListener } from "./preventMenu.js";

setTagColours();

document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.querySelector(".menu-toggle");
  const menu = document.querySelector(".menu-items");

  toggle.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", isOpen);
  });
  addPreventMenuListener();

  if (document.querySelector(".carousel")) {
    const carouselButtonNext = document.querySelector(".carousel__buttons--next");
    const carouselButtonPrev = document.querySelector(".carousel__buttons--prev");
    carouselButtonNext.addEventListener("click", nextSlide);
    carouselButtonPrev.addEventListener("click", prevSlide);
  }
});
