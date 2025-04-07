// hide footnote
const footnoteSection = document.querySelector("section.footnotes");

// opening references as modal
document.addEventListener("DOMContentLoaded", function () {
  const markers = document.querySelector(".tabbed-area").querySelectorAll("sup>a[rel='footnote']");
  const referenceModal = document.getElementById("reference-modal");
  const referenceModalText = referenceModal.querySelector("#modal__text");
  const closeBtn = document.getElementById("modal__btn--close");

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

      // modal.style.display = "block";
      // referenceModal.classList.add("visible");
      referenceModal.showModal()

      closeBtn.onclick = function () {
        referenceModal.close()
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

const mentions = document.querySelectorAll(".bib-mention");
console.log("mentions", mentions);
const bibModal = document.getElementById("bibliography-modal");
const bibModalContent = bibModal.querySelector(".modal__content");
const closeButton = document.getElementById("modal__btn--close");

closeButton.addEventListener("click", () => {
  dialog.close();
});

mentions.forEach((mention) => {
  mention.addEventListener("click", function (e) {
    e.preventDefault();
    console.log(e)
    const id = e.target.getAttribute("data-bib-id");
    console.log("data-bib-id", id);
    const bib = document.querySelector(`[data-bib-citation-id="${id}"]`);
    bibModalContent.innerHTML = bib.innerHTML;
    // bibModal.showModal();
    
  });
});
