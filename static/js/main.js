document.addEventListener("DOMContentLoaded", function () {

    // Mobile navbar toggle
    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const navbarMenu = document.getElementById("navbarMenu");

    if (mobileMenuBtn && navbarMenu) {
        mobileMenuBtn.addEventListener("click", function () {
            navbarMenu.classList.toggle("show");
        });
    }

    // Auto hide alert messages after 4 seconds
    const alerts = document.querySelectorAll(".custom-alert");

    alerts.forEach(function (alertBox) {
        setTimeout(function () {
            alertBox.style.transition = "opacity 0.5s ease";
            alertBox.style.opacity = "0";

            setTimeout(function () {
                alertBox.remove();
            }, 500);

        }, 4000);
    });

    // Add simple loading state on form submit
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function () {
            const submitButton = form.querySelector("button[type='submit'], button:not([type])");

            if (submitButton) {
                submitButton.disabled = true;
                submitButton.innerText = "Please wait...";
            }
        });
    });

});