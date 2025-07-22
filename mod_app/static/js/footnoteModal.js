function closeModalOnOutsideClick(modal) {
  modal.addEventListener("click", function (event) {
    // get modal box's boundaries
    const modalBox = modal.getBoundingClientRect();

    // sets True if the click is within the modal, False elsewise
    const isInModal = event.clientX >= modalBox.left && event.clientX <= modalBox.right && event.clientY >= modalBox.top && event.clientY <= modalBox.bottom;

    // close dialog (modal) if click is outside of the modal box
    if (!isInModal) {
      modal.close();
    }
  });
}

function bibModalHandler(bibMentions, bibModal, bibModalContent) {
  bibMentions.forEach((bibMention) => {
    bibMention.addEventListener("click", function (event) {
      event.preventDefault();

      const id = event.target.getAttribute("data-bib-id");
      const bib = document.querySelector(`[data-bib-citation-id="${id}"]`);

      bibModalContent.innerHTML = bib.innerHTML;
      bibModal.showModal();
    });
  });
}

function footnoteModalHandler(footnoteModal) {}

// opening references as modal
document.addEventListener("DOMContentLoaded", function () {
  const footnoteReferences = document.querySelector(".tabbed-area").querySelectorAll("sup>a[rel='footnote']");
  const footnoteModal = document.getElementById("footnote-modal");
  const footnoteModalText = footnoteModal.querySelector(".footnote-modal__text");

  const bibMentions = document.querySelectorAll(".bib-mention");
  const bibModal = document.getElementById("bibliography-modal");
  const bibModalContent = bibModal.querySelector(".bib-modal__content");

  const closeBtn = document.querySelectorAll(".modal__btn--close");

  closeBtn.forEach((button) => {
    button.onclick = function (e) {
      e.target.parentNode.close();
    };
  });

  closeModalOnOutsideClick(footnoteModal);
  closeModalOnOutsideClick(bibModal);

  footnoteReferences.forEach((footnoteReference) => {
    footnoteReference.addEventListener("click", function (e) {
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

      footnoteModalText.innerHTML = cite.innerHTML;
      footnoteModal.showModal();
      bibModalHandler(bibModal, bibModalContent);

      closeBtn.onclick = function () {
        e.target.parentNode.close();
      };
    });
  });
  bibModalHandler(bibMentions, bibModal, bibModalContent);
});
