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
  threshold: 0.2,
  includeScore: true,
  keys: [
    { name: "title", weight: 0.6 },
    { name: "release_date", weight: 0.3 },
    { name: "synopsis", weight: 0.1 },
  ],
};

function search(list, query, options) {
  const fuse = new Fuse(list, options);
  const result = fuse.search(query);
  console.log("Search successful:", result);
  return result;
}

const filmSearchForm = document.getElementById("film-search");
console.log(window.location.origin);

function getCSRFToken() {
  // Standard Django cookie helper
  const m = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]+)/);
  return m ? decodeURIComponent(m[1]) : "";
}

async function renderCardsFromFuseResults(fuseResultsOrItems) {
  const items = Array.isArray(fuseResultsOrItems) && fuseResultsOrItems.length && fuseResultsOrItems[0].item ? fuseResultsOrItems.map((r) => r.item) : fuseResultsOrItems;
  const PARTIAL_URL = window.location.origin + "/films/cards-partial/";
  const ids = items.map((x) => x.pk ?? x.pk); // adapt to your field name
  console.log("mapped film ids:", ids);

  const res = await fetch(PARTIAL_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
      Accept: "text/html",
    },
    body: JSON.stringify({ ids }),
  });

  const html = await res.text();
  console.log(html);
  const cardGrid = document.getElementsByClassName("card-grid");
  console.log("cardgrid:", cardGrid[0]);
  cardGrid[0].outerHTML = html;
  console.log(cardGrid[0]);
}

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
    const searchValue = document.getElementById("search-bar").value;
    console.log("Search Value:", searchValue);

    const results = search(filmData, searchValue, fuseOptions);
    console.log("results:", results);
    await renderCardsFromFuseResults(results);
  } catch (error) {
    console.error("Fetch error:", error);
  }
});
