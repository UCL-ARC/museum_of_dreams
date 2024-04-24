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
