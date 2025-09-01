import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

// if its films or analyses
// function getContextData(object_type) {
//   if (object_type === "film") {
const titles = document.querySelectorAll(".card__body__title");
const yearOfReleases = document.querySelectorAll(".card__release-date");
const synopses = document.querySelectorAll(".card__body__description");

let titleArray = Array.from(titles);
titleArray.forEach((title) => {
  title = title.innerHTMl;
});

// fetch("/film_data")
//   .then((res) => res.json())
//   .then((data) => {
//     console.log(data);
//   });

console.log("Film titles:", titles);
console.log("Film years:", yearOfReleases);
console.log("Film synopsis:", synopses);
//   }
//   elif(object_type === "analysis");
//   {
//     const title = document.querySelectorAll(".card__body__title");
//     const yearOfRelease = document.querySelectorAll(".card__release-date");
//     const synopsis = document.querySelectorAll(".card__body__description");
//   }
// }

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
  // const form = new FormData(event.target);
  // // output as an object
  // console.log(form.entries());
  const valueById = document.getElementById("search-bar").value;
  console.log("By ID:", valueById);
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
