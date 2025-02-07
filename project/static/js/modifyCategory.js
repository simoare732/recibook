document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".category-card").forEach(card => {
        card.addEventListener("dblclick", function () {
            let nameElement = this.querySelector(".category-name");
            let editElement = this.querySelector(".category-edit");

            nameElement.style.display = "none";
            editElement.style.display = "block";
            editElement.focus();

            editElement.addEventListener("blur", function () {
                let newName = editElement.value;
                let categoryId = card.getAttribute("data-id");

                fetch(`/recipe/updateCategory/${categoryId}/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken")
                    },
                    body: JSON.stringify({ name: newName })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        nameElement.innerText = newName;
                    } else {
                        alert("Error updating category");
                    }
                    nameElement.style.display = "block";
                    editElement.style.display = "none";
                });
            });
        });
        card.querySelector(".delete-category").addEventListener("click", function () {
            let categoryId = card.getAttribute("data-id");

            fetch(`/recipe/deleteCategory/${categoryId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
                }
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        card.remove();
                    } else {
                        alert("Error deleting category");
                    }
                });
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}