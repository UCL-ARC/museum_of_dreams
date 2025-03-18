import { logToConsole } from "../second.js";
import { setTagColours } from "./dynamicTagColours.js";
import { prevSlide, nextSlide } from "./carousel.js";
import { toggleMenuDrawer } from "./menuDrawer.js";

logToConsole("js ready");
setTagColours();
toggleMenuDrawer();

document.addEventListener("DOMContentLoaded", function () {
  // const lightDarkToggle = document.querySelector(".toggle-container");
  // lightDarkToggle.addEventListener("click", toggleMode());
  // function toggleMode() {
  // 	const body = document.body;
  // 	const currentMode = body.classList.contains("dark-mode")
  // 		? "light-mode"
  // 		: "dark-mode";
  // 	console.log("chanigng mode");
  // 	body.classList.remove(currentMode);
  // 	body.classList.add(currentMode);
  // }

  if (document.querySelector(".carousel")) {
    const carouselButtonNext = document.querySelector(".carousel__buttons--next");
    const carouselButtonPrev = document.querySelector(".carousel__buttons--prev");
    carouselButtonNext.addEventListener("click", nextSlide);
    carouselButtonPrev.addEventListener("click", prevSlide);
  }
});
