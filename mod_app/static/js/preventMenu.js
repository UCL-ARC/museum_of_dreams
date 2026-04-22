export function addPreventMenuListener() {
  document.querySelectorAll("img, video").forEach(function (element) {
    document.addEventListener(
      "contextmenu",
      function (e) {
        e.preventDefault();
      },
      false,
    );
  });
}
