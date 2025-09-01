import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

// if its films or analyses
// function getContextData(object_type) {
//   if (object_type === "film") {
//     const title = document.querySelectorAll(".card__body__title");
//     const yearOfRelease = document.querySelectorAll(".card__release-date");
//     const synopsis = document.querySelectorAll(".card__body__description");
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
console.log(filmSearchForm);

// const analysisSearchForm = document.getElementById("analysis-search-form");
filmSearchForm.addEventListener("submit", function (event) {
  event.preventDefault();
  // const form = new FormData(event.target);
  // // output as an object
  // console.log(form.entries());
  const valueById = document.getElementById("search-bar").value;
  console.log("By ID:", valueById);
});
// analysisSearchForm.addEventListener("submit", (event) => {});

// const options = {
//   includeScore: true,
// };

// const fuse = new Fuse(list, options);

// const result = fuse.search("od man");
