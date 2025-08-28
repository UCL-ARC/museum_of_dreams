import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

console.log("search script loaded");
document.addEventListener("DOMContentLoaded", () => {});
const filmSearchForm = document.getElementById("film-search-form");
// const analysisSearchForm = document.getElementById("analysis-search-form");
filmSearchForm.addEventListener("submit", (event) => {
  event.preventDefault;
  let form = getData(event.target);
  let formData = new FormData(form);
  // output as an object
  console.log(Object.fromEntries(formData));
});
// analysisSearchForm.addEventListener("submit", (event) => {});

// const options = {
//   includeScore: true,
// };

// const fuse = new Fuse(list, options);

// const result = fuse.search("od man");
