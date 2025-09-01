import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

// const titles = document.querySelectorAll(".card__body__title");
// const yearOfReleases = document.querySelectorAll(".card__release-date");
// const synopses = document.querySelectorAll(".card__body__description");
// console.log("Film titles:", titles);
// console.log("Film years:", yearOfReleases);
// console.log("Film synopsis:", synopses);

const films = JSON.parse(document.getElementById("film_data").innerHTML);
console.log(films);

// const options = {
//   includeScore: true,
// };

// function search(list, query) {
//   const fuse = new Fuse(list, options);
//   const result = fuse.search(query);
//   return result;
// }

console.log("search script loaded");
const filmSearchForm = document.getElementById("film-search");

// const analysisSearchForm = document.getElementById("analysis-search-form");
filmSearchForm.addEventListener("submit", function (event) {
  event.preventDefault();
  const searchValue = document.getElementById("search-bar").value;
  console.log("Search Value:", searchValue);
});

// if theres 4 digit numbers
// film title
// film synopsis

// analysisSearchForm.addEventListener("submit", (event) => {});

// const options = {
//   includeScore: true,
// };

// const fuse = new Fuse(list, options);

// const result = fuse.search("od man");
