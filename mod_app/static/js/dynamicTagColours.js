// make the tag colours on the page semi random
export function setTagColours() {
  const tags = document.querySelectorAll(".tag");
  // when we know the tags, perhaps we assign the colours as fixed?
  const colors = [
    "--camo-9",
    "--pink-10",
    "--deep-blue",
    "--violet-6",
    "--blue-7",
    "--teal-9",
  ];
  tags.forEach((tag, index) => {
    tag.style.backgroundColor = `var(${colors[index % colors.length]})`;

    // var dot = tag.querySelector(".dot");
    // if (dot) {
    //   console.log("tag:", tag, "dot:", dot);
    //   dot.style.color = `var(${colors[index % colors.length]})`;
    // }
  });
}
