// hide footnote
const footnoteSection = document.querySelector("section.footnotes");


// placeholder event handler code 
document.addEventListener('DOMContentLoaded', function () {
    const markers = document.querySelector(".tabbed-area").querySelectorAll("sup>a[rel='footnote']");
    const modal = document.getElementById('referenceModal');
    const modalText = document.getElementById('modalText');
    const closeBtn = document.getElementById('closeModal');

    markers.forEach((link) => {
        link.addEventListener('click', function (e) {
        e.preventDefault();

        let id = e.target.id;

        // get the tag information of element that was clicked on
        const anchor = document.getElementById(id);
        // trace back to the href attribute (e.g., "#footnote-1")
        const footnoteId = anchor.getAttribute('href').substring(1); // removes '#'

        // Find the footnote associated with that id ref
        const footnoteItem = document.getElementById(footnoteId);

        // Get the citation text from the footnote
        const cite = footnoteItem.querySelector('cite');

        modalText.innerHTML = cite.textContent;
        modal.style.display = 'block';
      });
    });
  
    closeBtn.onclick = function () {
      modal.style.display = 'none';
    };
  
    window.onclick = function (e) {
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    };
  });

