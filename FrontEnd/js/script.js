let slideIndex = 0;
const slides = document.querySelectorAll('.slides img');

function showSlides() {
  slides.forEach(slide => slide.classList.remove('active'));
  slides[slideIndex].classList.add('active');
}

function moveSlide(step) {
  slideIndex = (slideIndex + step + slides.length) % slides.length;
  showSlides();
}

setInterval(() => moveSlide(1), 3000); // auto-slide every 3 seconds

showSlides();
