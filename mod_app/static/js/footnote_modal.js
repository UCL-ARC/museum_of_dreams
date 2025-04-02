// hide footnote
document.querySelector("section.footnotes").style.display = "none";

// placeholder code
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('referenceModal');
    const modalText = document.getElementById('modalText');
    const closeBtn = document.getElementById('closeModal');
  
    document.querySelectorAll('.ref-link').forEach(link => {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        const id = this.dataset.id;
        const content = document.getElementById('ref-content-' + id).innerHTML;
        modalText.innerHTML = content;
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

