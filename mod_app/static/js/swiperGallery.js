import Swiper from "https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.mjs";

document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll(".swiper-slide");
  const swiper = new Swiper(".swiper", {
    grabCursor: true,
    centeredSlides: true,
    loop: slides.length > 1,
    slidesPerView: 1,
    spaceBetween: 0,
    effect: "coverflow",
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
});
