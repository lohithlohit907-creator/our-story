// ==========================================
// REVIEW PAGE ❤️
// ==========================================

const reviewButtons = document.querySelectorAll(".review-option");
const selectedReview = document.getElementById("selected-review");

let chosenReview = "";


// ==========================================
// REVIEW OPTION
// ==========================================

reviewButtons.forEach(button => {

    button.addEventListener("click", () => {

        reviewButtons.forEach(btn => {
            btn.classList.remove("selected");
        });

        button.classList.add("selected");

        chosenReview = button.dataset.review;

        selectedReview.textContent = chosenReview;

        selectedReview.classList.remove("show");

        setTimeout(() => {
            selectedReview.classList.add("show");
        }, 50);

    });

});


// ==========================================
// SEND REVIEW
// ==========================================

const sendButton = document.getElementById("send-review");
const messageBox = document.getElementById("message");
const finalMessage = document.getElementById("final-message");

sendButton.addEventListener("click", () => {

    const message = messageBox.value.trim();

    if (!chosenReview && !message) {

        selectedReview.textContent =
            "Choose something first... I really want to know. 🥹❤️";

        selectedReview.classList.add("show");

        return;
    }


    // Hide form
    document.querySelector(".review-options").style.display = "none";
    document.querySelector(".message-section").style.display = "none";
    sendButton.style.display = "none";
    selectedReview.style.display = "none";


    // Show final message
    finalMessage.classList.add("show");


    // Create celebration hearts
    createHeartExplosion();

});


// ==========================================
// HEART EXPLOSION ❤️
// ==========================================

function createHeartExplosion() {

    for (let i = 0; i < 30; i++) {

        const heart = document.createElement("span");

        heart.innerHTML = ["❤️", "💗", "💕", "💖", "💓"][
            Math.floor(Math.random() * 5)
        ];

        heart.className = "explosion-heart";

        heart.style.left = "50%";
        heart.style.top = "50%";

        heart.style.setProperty(
            "--x",
            `${(Math.random() - 0.5) * 600}px`
        );

        heart.style.setProperty(
            "--y",
            `${(Math.random() - 0.5) * 600}px`
        );

        document.body.appendChild(heart);

        setTimeout(() => {
            heart.remove();
        }, 2500);

    }
}


// ==========================================
// FLOATING HEARTS ❤️
// ==========================================

const heartsContainer =
    document.querySelector(".hearts-container");

function createFloatingHeart() {

    const heart = document.createElement("span");

    heart.innerHTML =
        ["❤️", "♡", "💗", "💕"][Math.floor(Math.random() * 4)];

    heart.className = "floating-heart";

    heart.style.left =
        Math.random() * 100 + "%";

    heart.style.animationDuration =
        (6 + Math.random() * 6) + "s";

    heart.style.fontSize =
        (10 + Math.random() * 18) + "px";

    heartsContainer.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, 12000);
}

setInterval(createFloatingHeart, 700);


// ==========================================
// FALLING SNOW / PETALS ❄️
// ==========================================

const snowContainer =
    document.querySelector(".snow-container");

function createSnow() {

    const snow = document.createElement("span");

    snow.innerHTML =
        Math.random() > 0.5 ? "❄" : "✦";

    snow.className = "snow";

    snow.style.left =
        Math.random() * 100 + "%";

    snow.style.animationDuration =
        (7 + Math.random() * 8) + "s";

    snow.style.fontSize =
        (8 + Math.random() * 12) + "px";

    snowContainer.appendChild(snow);

    setTimeout(() => {
        snow.remove();
    }, 15000);
}

setInterval(createSnow, 350);