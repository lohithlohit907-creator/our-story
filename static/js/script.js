// ==========================================
// PAGE 1 — ANNIVERSARY AUTHENTICATION
// ==========================================

const enterButton = document.getElementById("enter-button");
const errorMessage = document.getElementById("error-message");

if (enterButton) {

    enterButton.addEventListener("click", function () {

        const day = Number(document.getElementById("day").value);
        const month = Number(document.getElementById("month").value);
        const year = Number(document.getElementById("year").value);

        // Our anniversary ❤️
        const correctDay = 19;
        const correctMonth = 7;
        const correctYear = 2024;

        if (
            day === correctDay &&
            month === correctMonth &&
            year === correctYear
        ) {

            errorMessage.textContent =
                "Welcome back to our story... ❤️";

            errorMessage.style.opacity = "1";

            setTimeout(() => {
                window.location.href = "/story";
            }, 1500);

        } else {

            errorMessage.textContent =
                "Hmm... that's not the day our story began. ❤️";

            errorMessage.style.opacity = "1";
        }

    });

}


// ==========================================
// PAGE 2 — CONTINUE TO OUR STORY
// ==========================================

const continueStoryButton =
    document.getElementById("continue-story");

if (continueStoryButton) {

    continueStoryButton.addEventListener("click", function () {

        window.location.href = "/beginning";

    });

}

// Page 3 → Chapter 1

const startStoryButton =
    document.getElementById("start-story");

if (startStoryButton) {

    startStoryButton.addEventListener("click", function () {

        window.location.href = "/chapter1";

    });

}