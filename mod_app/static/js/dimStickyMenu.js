const menu = document.querySelector(".tab-selection");
const sentinel = document.querySelector(".tab-selection__sentinel");
const observer = new IntersectionObserver(
  ([entry]) => {
    menu.classList.toggle("is-sticky", !entry.isIntersecting);
  },
  { threshold: [0], rootMargin: "0px 0px 0px 0px" }
);

observer.observe(sentinel);
