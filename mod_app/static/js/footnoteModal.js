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

      const bibReferenceId = event.target.getAttribute("data-bib-id");
      const bibCitationId = document.querySelector(`[data-bib-citation-id="${bibReferenceId}"]`);
      const closeBtn = bibModal.querySelector(".modal__btn--close");

      bibModalContent.innerHTML = bibCitationId.innerHTML;
      bibModal.showModal();
      closeModalOnOutsideClick(bibModal);
      closeBtn.onclick = function (e) {
        e.target.parentNode.close();
      };
    });
  });
}

function footnoteModalHandler(footnoteReferences, footnoteModal, footnoteModalContent) {
  footnoteReferences.forEach((footnoteReference) => {
    footnoteReference.addEventListener("click", function (event) {
      event.preventDefault();

      const footnoteReferenceId = event.target.id;
      const referencedAnchor = document.getElementById(footnoteReferenceId);

      // trace back to the href attribute (e.g., "#footnote-1")
      const footnoteItemId = referencedAnchor.getAttribute("href").substring(1); // removes '#'

      // Find the footnote associated with that id ref
      const footnoteItem = document.getElementById(footnoteItemId);

      // Get content from the footnote anchor
      const footnoteContent = footnoteItem.querySelector("cite");

      const closeBtn = footnoteModal.querySelector(".modal__btn--close");

      footnoteModalContent.innerHTML = footnoteContent.innerHTML;
      footnoteModal.showModal();
      closeModalOnOutsideClick(footnoteModal);
      bibModalHandler(bibModal, bibModalContent);

      closeBtn.onclick = function () {
        e.target.parentNode.close();
      };
    });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const footnoteReferences = document.querySelector(".tabbed-area").querySelectorAll("sup>a[rel='footnote']");
  const footnoteModal = document.getElementById("footnote-modal");
  const footnoteModalContent = footnoteModal.querySelector(".footnote-modal__content");

  const bibMentions = document.querySelectorAll(".bib-mention");
  const bibModal = document.getElementById("bibliography-modal");
  const bibModalContent = bibModal.querySelector(".bib-modal__content");

  footnoteModalHandler(footnoteReferences, footnoteModal, footnoteModalContent);
  bibModalHandler(bibMentions, bibModal, bibModalContent);
});
