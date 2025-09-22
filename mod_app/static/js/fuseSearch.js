import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

console.log("search script loaded");

// fuse.js search configurations
const filmOptions = {
  threshold: 0.2, // lower value equals a stricter match
  includeScore: true,
  keys: [
    { name: "title", weight: 0.6 },
    { name: "release_date", weight: 0.3 },
    { name: "synopsis", weight: 0.1 },
  ],
};

const analysisOptions = {
  threshold: 0.2, // lower value equals a stricter match
  includeScore: true,
  keys: [
    { name: "title", weight: 0.6 },
    { name: "summary", weight: 0.3 },
  ],
};

function fuseSearch(array, searchQuery, fuseSearchConfigurations) {
  const fuse = new Fuse(array, fuseSearchConfigurations);
  const result = fuse.search(searchQuery);
  console.log("Search successful:", result);
  return result;
}

const filmSearchForm = document.getElementById("film-search");
const analysisSearchForm = document.getElementById("analysis-search");
console.log(window.location.origin);

// function getCSRFToken() {
//   // fetches csrf token from cookie for django
//   const match = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]+)/);
//   return match ? decodeURIComponent(match[1]) : "";
// }

async function renderSearchResults(isFilm, fuseResults) {
  const items = fuseResults.map((r) => r.item);
  const ids = items.map((x) => x.pk ?? x.pk);
  console.log("mapped film ids:", ids);
  if (isFilm === true) {
    let url = "/films?id=" + ids.join(",");
    console.log("url:", url);
    await fetch(url);
    window.location = url;
  } else {
    let url = "/analyses?id=" + ids.join(",");
    console.log("url:", url);
    await fetch(url);
    window.location = url;
  }
  // const modelName = isFilm ? "Film" : "Analysis";
  // const partialURL = isFilm ? "films" : "analyses";
  // const partialURL = window.location.origin + "/cards-partial";
  // console.log(partialURL);

  // const url = window.location.origin + "/" + url + "?id=" + ids.join(",");
  // const result = await fetch("/cards-partial", {
  //   method: "GET",
  //   headers: {
  //     "Content-Type": "application/json",
  //     "X-CSRFToken": getCSRFToken(),
  //     Accept: "text/html",
  //   },
  //   body: JSON.stringify({ ids, model: { modelName } }),
  // });

  // replace card grid with search results
  // const html = await result.text();
  // console.log("HTML response:", html);
  // const cardGrid = document.getElementsByClassName("card-grid");
  // console.log("cardgrid:", cardGrid[0]);
  // // cardGrid[0].outerHTML = html;
  // console.log(cardGrid[0]);
}

if (filmSearchForm) {
  filmSearchForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const isFilm = true;
    const url = window.location.origin + "/films?film_data=json";
    const response = await fetch(url);
    const filmData = await response.json();
    const searchValue = document.getElementById("search-bar").value;
    const results = fuseSearch(filmData, searchValue, filmOptions);
    console.log(results);
    await renderSearchResults(isFilm, results);
  });
} else {
  analysisSearchForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const isFilm = false;
    const url = window.location.origin + "/analyses?analysis_data=json";
    const response = await fetch(url);
    const analysisData = await response.json();
    const searchValue = document.getElementById("search-bar").value;
    const results = fuseSearch(analysisData, searchValue, analysisOptions);
    await renderSearchResults(isFilm, results);
  });
}
