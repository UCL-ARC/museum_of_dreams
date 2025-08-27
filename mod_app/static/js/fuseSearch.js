import Fuse from "https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs";

const options = {
  includeScore: true,
};

const fuse = new Fuse(list, options);

const result = fuse.search("od man");

function getSearchForm() {
  document.getElementById;
}
