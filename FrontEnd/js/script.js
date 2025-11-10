// Image Slider
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

// Scroll Reveal Animation
document.addEventListener("DOMContentLoaded", function () {
    const reveals = document.querySelectorAll(".reveal");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }
        });
    }, { threshold: 0.2 });

    reveals.forEach(reveal => {
        observer.observe(reveal);
    });
});

// Back to Top Button
const backToTopBtn = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
    if (window.pageYOffset > 300) {
        backToTopBtn.style.display = "block";
    } else {
        backToTopBtn.style.display = "none";
    }
});

backToTopBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});


// Prediction Form Submission
document.querySelector("form").addEventListener("submit", async function(event){
    event.preventDefault();

    let inputData = {
        brand: document.getElementById("brand").value,
        assembly: document.getElementById("assembly").value,
        product_category: document.getElementById("category").value,
        payment_method: document.getElementById("payment").value,
        payment_timing: document.getElementById("timing").value,
        product_subcategory: document.getElementById("subcategory").value
    };

    let response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(inputData)
    });

    let result = await response.json();

    // Display result beautifully
    alert("Predicted Delivery Status: " + result.delivery_status_prediction);
});

