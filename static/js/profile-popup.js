document.addEventListener("DOMContentLoaded", function () {
    const trigger = document.getElementById("openProfileModal");
    const modalElement = document.getElementById("profileModal");
    const modalContent = document.getElementById("profileModalContent");

    if (trigger) {
        trigger.addEventListener("click", function (e) {
            e.preventDefault();
            const url = this.getAttribute("href");

            fetch(url)
                .then(response => response.text())
                .then(html => {
                    modalContent.innerHTML = html;
                    const modal = new bootstrap.Modal(modalElement);
                    modal.show();
                });
        });
    }
});
