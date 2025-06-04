function openTab(evt) {
  const selected = evt.currentTarget.name;
  const contentElems = document.getElementsByClassName("tab__content");
  const tabs = document.getElementsByClassName("tab__link");

  [...tabs].forEach((tab) => {
    if (tab.name !== selected) tab.classList.remove("active");
  });
  [...contentElems].forEach((tab) => {
    if (tab.name !== selected) tab.classList.remove("active");
  });

  selectedTabNContent = document.querySelectorAll(`[name=${selected}]`);

  selectedTabNContent.forEach((elem) => elem.classList.add("active"));
}
