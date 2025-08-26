async function downloadAnalysis(event, pk) {
  const downloadBtn = event.currentTarget;
  const downloadBtnText = downloadBtn.querySelector("p");
  const downloadLoader = downloadBtn.querySelector(".loader");
  const url = `/download-analysis/${pk}`;

  downloadBtn.disabled = true;
  downloadBtn.classList.toggle("in-progress");
  downloadBtnText.classList.toggle("hidden");
  downloadLoader.classList.toggle("hidden");

  const response = await fetch(url);

  if (response.ok) {
    // Retrieve the filename from the Content-Disposition header
    const contentDisposition = response.headers.get("Content-Disposition");
    let filename = "download.pdf"; // Default filename if not specified
    if (contentDisposition) {
      const filenameMatch = contentDisposition.match(/filename="?(.+)"?/);
      if (filenameMatch.length === 2) {
        filename = filenameMatch[1];
      }
    }

    // Convert the response body to a Blob
    const blob = await response.blob();
    const blobUrl = window.URL.createObjectURL(blob);

    // Create a temporary anchor element and trigger the download
    const a = document.createElement("a");
    a.href = blobUrl;
    a.download = filename;
    document.body.appendChild(a); // Append to the document
    a.click(); // Trigger the download

    // Clean up by revoking the object URL and removing the temporary anchor element
    window.URL.revokeObjectURL(blobUrl);
    document.body.removeChild(a);
  } else {
    // Handle errors or unsuccessful responses
    console.error("Failed to download PDF:", response.statusText);
  }

  downloadBtn.disabled = false;
  downloadBtn.classList.toggle("in-progress");
  downloadBtnText.classList.toggle("hidden");
  downloadLoader.classList.toggle("hidden");
}
