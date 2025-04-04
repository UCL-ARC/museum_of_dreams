// hide footnote
const footnoteSection = document.querySelector("section.footnotes");

// opening references as modal
document.addEventListener("DOMContentLoaded", function () {
  const markers = document.querySelector(".tabbed-area").querySelectorAll("sup>a[rel='footnote']");
  const modal = document.getElementById("referenceModal");
  const modalText = document.getElementById("modalText");
  const closeBtn = document.getElementById("closeModal");

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

      modalText.innerHTML = cite.innerHTML;
      console.log(cite.innerHTML);

      modal.style.display = "block";
      // bibliography reference
      let bibs = modalText.getElementsByTagName("strong");
      //console.log(bib);
      // replace it with a link
      // link should open modal of full-citation biblography
      //

      closeBtn.onclick = function () {
        modal.style.display = "none";
      };

      window.onclick = function (e) {
        if (e.target === modal) {
          modal.style.display = "none";
        }
      };
      // });

      // dialog modal box
      // document.addEventListener('DOMContentLoaded',function(){
      //   const markers = document.querySelector(".tabbed-area").querySelectorAll("sup>a[rel='footnote']");
      //   const dialog = document.querySelector("dialog-modal");
      //   const modalText = document.getElementById('modalText');
      //   const closeButton = document.querySelector("dialog button");

      //   markers.forEach((link) => {
      //     link.addEventListener('click', function (e) {
      //     e.preventDefault();
      //     let id = e.target.id;
      //     // get the tag information of element that was clicked on
      //     const anchor = document.getElementById(id);
      //     // trace back to the href attribute (e.g., "#footnote-1")
      //     const footnoteId = anchor.getAttribute('href').substring(1); // removes '#'
      //     // Find the footnote associated with that id ref
      //     const footnoteItem = document.getElementById(footnoteId);
      //     // Get the citation text from the footnote
      //     const cite = footnoteItem.querySelector('cite');
      //     modalText.innerHTML = cite.innerHTML;
      //     dialog.showModal();
      //   });
      //   closeButton.addEventListener("click", () => {
      //     dialog.close();
      //   });

      // });});
    });
  });
});

document.querySelectorAll(".bib-mention").forEach(function (strong) {
  addEventListener("click", function (e) {
    e.preventDefault();
    const id = e.target.getAttribute("data-bib-id");
    console.log(id);

    const bib = document.querySelector(`[data-bib-citation-id="${id}"]`);
    console.log(bib);
    //make the div of data-bib-citation-{{id}} visible
    // get the tag information of element that was clicked on
    if (bib.style.display === "none") {
      //  block of code to be executed if the condition is true
      bib.style.display = "block";
    } else {
      //  block of code to be executed if the condition is false
      bib.style.display = "none";
    }
  });
});
