import Swiper from "https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.mjs";

const swiperSlides = document.querySelectorAll(".swiper-slide");
const swiper = new Swiper(".swiper", {
  grabCursor: true,
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

// when clicking on the active slide, open a window
console.log(swiperSlides);

let activeSlide = document.getElementsByClassName("swiper-slide-active");
const modalImage = activeSlide[0].getElementsByTagName("img")[0];
const closeBtn = document.getElementsByClassName("swiper-modal__btn--close")[0];

console.log("active slides:" + activeSlide);
console.log(modalImage);
const modal = document.getElementsByClassName("swiper-modal")[0];

// want to apply to image and video as well later
modalImage.addEventListener("click", function () {
  modal.appendChild(modalImage.cloneNode(true));
  // open modal
  console.log("test click");
  modal.showModal();
});

closeBtn.addEventListener("click", function () {
  modal.close();
});
