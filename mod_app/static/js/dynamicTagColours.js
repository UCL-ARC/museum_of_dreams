// make the tag colours on the page semi random
export function setTagColours() {
  const tags = document.querySelectorAll(".columnar-area .tag");
  // when we know the tags, perhaps we assign the colours as fixed for consistency?
  const colors = ["--camo-9", "--pink-10", "--deep-blue", "--violet-6", "--blue-7", "--teal-9"];
  tags.forEach((tag, index) => {
    tag.style.borderColor = `var(${colors[index % colors.length]})`;
  });
}
