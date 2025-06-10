function openTab(evt, tabName) {
  var selected, content, tab;
  selected = evt.currentTarget.name;
  contentElems = document.getElementsByClassName("tab__content");
  tabs = document.getElementsByClassName("tab__link");

  [...tabs].forEach((tab) => {
    if (tab.name !== selected) tab.classList.remove("active");
  });
  [...contentElems].forEach((tab) => {
    if (tab.name !== selected) tab.classList.remove("active");
  });

  selectedTabNContent = document.querySelectorAll(`[name="${CSS.escape(selected)}"]`);

  selectedTabNContent.forEach((elem) => elem.classList.add("active"));
}
