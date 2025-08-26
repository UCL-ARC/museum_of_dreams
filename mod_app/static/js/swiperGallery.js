import Swiper from "https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.mjs";
export { swiper };
const swiperSlides = document.querySelectorAll(".swiper-slide");
const swiper = new Swiper(".swiper", {
  // grabCursor: true,
  centeredSlides: true,

  // loop and rewind conflicts with each other, so it shouldn't be set to true at the same time
  loop: swiperSlides.length > 2,
  rewind: swiperSlides.length === 2,
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
