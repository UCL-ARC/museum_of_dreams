import Swiper from "https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.mjs";

document.addEventListener("DOMContentLoaded", function () {
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

  console.log(swiperSlides);

  const activeSlide = document.getElementsByClassName("swiper-slide-active");
  const modalImage = activeSlide[0].getElementsByTagName("img")[0];

  console.log(activeSlide);
  console.log(modalImage);

  // want to apply to image and video as well later
  modalImage.addEventListener("click", function () {
    const modal = document.getElementsByClassName("swiper-modal")[0];
    modal.appendChild(modalImage);
    // open modal
    console.log("test click");
    modal.style.display = "block";
  });

  // when clicking on the active slide, open a window
});
