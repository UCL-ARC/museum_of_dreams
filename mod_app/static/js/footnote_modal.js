// hide footnote
const footnoteSection = document.querySelector("section.footnotes");

// opening references as modal
document.addEventListener("DOMContentLoaded", function () {
  const markers = document.querySelector(".tabbed-area").querySelectorAll("sup>a[rel='footnote']");
  const referenceModal = document.getElementById("reference-modal");
  const referenceModalText = referenceModal.querySelector(".modal__text");

  const bibModal = document.getElementById("bibliography-modal");
  const bibModalContent = bibModal.querySelector(".modal__content");
  const closeBtn = document.querySelectorAll(".modal__btn--close");

  closeBtn.forEach((button) => {
    button.onclick = function (e) {
      e.target.parentNode.close();
    };
  });

  markers.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();

      const id = e.target.id;

      // get the tag information of element that was clicked on
      const anchor = document.getElementById(id);

      // trace back to the href attribute (e.g., "#footnote-1")
      const footnoteId = anchor.getAttribute("href").substring(1); // removes '#'

      // Find the footnote associated with that id ref
      const footnoteItem = document.getElementById(footnoteId);

      // Get the citation text from the footnote
      let cite = footnoteItem.querySelector("cite");

      referenceModalText.innerHTML = cite.innerHTML;
      referenceModal.showModal();

      const mentions = document.querySelectorAll(".bib-mention");
      mentions.forEach((mention) => {
        mention.addEventListener("click", function (e) {
          e.preventDefault();
          const id = e.target.getAttribute("data-bib-id");
          const bib = document.querySelector(`[data-bib-citation-id="${id}"]`);
          bibModalContent.innerHTML = bib.innerHTML;
          bibModal.showModal();
        });
      });

      closeBtn.onclick = function () {
        e.target.parentNode.close();
      };

      //window.onclick = function (e) {
      // todo: make into if not modal clicked, close modal?
      // if (e.target === referenceModal) {
      //   modal.style.display = "none";
      // }
      //};
    });
  });
});
