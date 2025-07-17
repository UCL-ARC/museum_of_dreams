function openImageLink(url) {
  window.open(url, "_blank").focus();
}
function getActiveSlide() {
  const activeSlides = document.querySelectorAll("div.swiper-slide.swiper-slide-active");

  for (let i = 0; i < activeSlides.length; i++) {
    let activeSlideImage = activeSlides[i].querySelector("img.slide__image");
    let button = activeSlides[i].querySelector("button.swiper-slide__description__button");
    button.addEventListener("click", window.open(activeSlideImage.src, "_blank").focus());
  }
}

function openTab(evt, tabName) {
  var selected;
  selected = evt.currentTarget.name;
  contentElems = document.getElementsByClassName("tab__content");
  tabs = document.getElementsByClassName("tab__link");

  [...tabs].forEach((tab) => {
    if (tab.name !== selected) tab.classList.remove("active");
  });
  [...contentElems].forEach((tab) => {
    if (tab.name !== selected) tab.classList.remove("active");
  });

  selectedTabNContent = document.querySelectorAll(`[name="${CSS.escape(selected)}"]`);

  selectedTabNContent.forEach((elem) => elem.classList.add("active"));

  if (tabName === "collections") {
    console.log("collection is clicked");

    setTimeout(() => {
      getActiveSlide();
    }, 500);

    const swipers = document.querySelectorAll(".swiper");
    swipers.forEach(function (swiper) {
      // selects swiper instance from swiper DOM elements
      const swiperInstance = swiper.swiper;

      swiperInstance.on("slideChange", () => {
        console.log("slide changed");

        getActiveSlide();
      });
    });
  }
}
