export function toggleMenuDrawer() {
	document.getElementById("menu-icon").addEventListener("click", function () {
		const drawer = document.getElementById("drawer");
		drawer.classList.toggle("open");
	});

	document.addEventListener("click", function (event) {
		const drawer = document.getElementById("drawer");
		const menuIcon = document.getElementById("menu-icon");

		// Close the drawer if clicking outside the drawer or on the icon again
		if (!drawer.contains(event.target) && event.target !== menuIcon) {
			drawer.classList.remove("open");
		}
	});
}
