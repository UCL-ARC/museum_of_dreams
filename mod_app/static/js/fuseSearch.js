import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

console.log("search script loaded");

// fuse.js search configurations
const fuseOptions = {
  threshold: 0.2, // lower value equals a stricter match
  includeScore: true,
  keys: [
    { name: "title", weight: 0.6 },
    { name: "release_date", weight: 0.3 },
    { name: "synopsis", weight: 0.1 },
  ],
};

function fuseSearch(array, searchQuery, fuseSearchConfigurations) {
  const fuse = new Fuse(array, fuseSearchConfigurations);
  const result = fuse.search(searchQuery);
  console.log("Search successful:", result);
  return result;
}

const filmSearchForm = document.getElementById("film-search");
console.log(window.location.origin);

function getCSRFToken() {
  // fetches csrf token from cookie for django
  const match = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]+)/);
  return match ? decodeURIComponent(match[1]) : "";
}

async function renderSearchResults(fuseResults) {
  const items = fuseResults.map((r) => r.item);
  const PARTIAL_URL = window.location.origin + "/films/cards-partial/";
  const ids = items.map((x) => x.pk ?? x.pk);
  console.log("mapped film ids:", ids);

  const result = await fetch(PARTIAL_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
      Accept: "text/html",
    },
    body: JSON.stringify({ ids }),
  });

  // replace cardgrid with card grid of results
  const html = await result.text();
  console.log(html);
  const cardGrid = document.getElementsByClassName("card-grid");
  console.log("cardgrid:", cardGrid[0]);
  cardGrid[0].outerHTML = html;
  console.log(cardGrid[0]);
}

filmSearchForm.addEventListener("submit", async (event) => {
  const url = window.location.origin + "/films?film_data=json";
  event.preventDefault();
  const response = await fetch(url);
  // if (!response.ok) {
  //   throw new Error("Network response was not ok " + response.statusText);
  // }
  const filmData = await response.json();
  const searchValue = document.getElementById("search-bar").value;

  const results = fuseSearch(filmData, searchValue, fuseOptions);
  await renderSearchResults(results);
});
