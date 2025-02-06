document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("formset-container").addEventListener("click", function (event) {
        if (event.target.classList.contains("delete-ingredient")) {
            let formsetItem = event.target.closest(".formset-item");
            let deleteInput = formsetItem.querySelector("input[type='hidden'][name$='-DELETE']");
            if (deleteInput) {
                deleteInput.value = "on";
            } else {
                // If the delete input doesn't exist, create it
                deleteInput = document.createElement("input");
                deleteInput.type = "hidden";
                deleteInput.name = formsetItem.querySelector("input, select").name.replace(/(\d+)-(\w+)/, "$1-DELETE");
                deleteInput.value = "on";
                formsetItem.appendChild(deleteInput);
            }
            formsetItem.style.display = "none";
        }
    });
});