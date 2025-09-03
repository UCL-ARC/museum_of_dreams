import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

// const titles = document.querySelectorAll(".card__body__title");
// const yearOfReleases = document.querySelectorAll(".card__release-date");
// const synopses = document.querySelectorAll(".card__body__description");
// console.log("Film titles:", titles);
// console.log("Film years:", yearOfReleases);
// console.log("Film synopsis:", synopses);
// const films = JSON.parse(document.getElementById("film_data"));
// console.log(films);
// console.log(typeof films);

// const films_dict = films.map(({ key, value }) => ({ [key]: value }));
// console.log(films_dict);
// console.log(Array.isArray(films));

// const film_list = {};

// films.forEach((film) => {
//   console.log(film.pk, film.title);
// });

console.log("search script loaded");

// get search value
const fuseOptions = {
  // Search in `author` and in `tags` array
  threshold: 0.3,
  keys: ["title", "release_date", "synopsis"],
};

function search(list, query, options) {
  const fuse = new Fuse(list, options);
  const result = fuse.search(query);
  console.log("Search successful:", result);
}

const filmSearchForm = document.getElementById("film-search");
console.log(window.location.origin);

filmSearchForm.addEventListener("submit", async (event) => {
  const url = window.location.origin + "/films?film_data=json";
  event.preventDefault();
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    const filmData = await response.json();
    // const filmDataArray = Object.values(filmData);
    console.log("Data received:", filmData);
    console.log(typeof filmData);
    console.log(Array.isArray(filmData));
    console.log("First film:", filmData[1]);
    const searchValue = document.getElementById("search-bar").value;
    console.log("Search Value:", searchValue);

    search(filmData, searchValue, fuseOptions);
  } catch (error) {
    console.error("Fetch error:", error);
  }
});
