// make the tag colours on the page semi random
export function setTagColours() {
	const tags = document.querySelectorAll(".tag");
	const colors = [
		"--camo-9",
		"--bright-red",
		"--tan",
		"--violet-6",
		"--blue-7",
	];
	tags.forEach((tag, index) => {
		var dot = tag.querySelector(".dot");
		tag.style.color = `var(${colors[index % colors.length]})`;
		console.log("tag:", tag, "dot:", dot);
		dot.style.color = `var(${colors[index % colors.length]})`;
	});
}
