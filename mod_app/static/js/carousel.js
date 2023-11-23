let slideIndex = 0;

function showSlides() {
	const slides = document.querySelectorAll(".slide");
	for (let i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	}
	if (slideIndex >= slides.length) {
		slideIndex = 0;
	}
	if (slideIndex < 0) {
		slideIndex = slides.length - 1;
	}
	slides[slideIndex].style.display = "block";
}

export function nextSlide() {
	slideIndex++;
	showSlides();
	console.log("next slide");
}

export function prevSlide() {
	slideIndex--;
	showSlides();
	console.log("prev slide");
}
