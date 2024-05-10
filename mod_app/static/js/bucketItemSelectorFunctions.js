function handleCKEditorSelection(CKEDITORFuncNum, selectedItemValue) {
  window.opener.CKEDITOR.tools.callFunction(CKEDITORFuncNum, selectedItemValue);
  window.close();
}

function handlePopupSelection(selectedItemValue) {
  var message = {
    source: "s3-browser-window-selection",
    value: selectedItemValue,
  };
  var validLoc = window.opener.location.origin;
  window.opener.postMessage(message, validLoc);
  window.close();
}

function filterBy(elemType) {
  const cardWrappers = document.querySelectorAll(".s3-browser__card__wrapper");
  cardWrappers.forEach((wrapper) => {
    if (elemType == "none") {
      wrapper.classList.remove("no-display");
    } else {
      if (!wrapper.querySelector(elemType)) {
        wrapper.classList.add("no-display");
      } else {
        wrapper.classList.remove("no-display");
      }
    }
  });
}
