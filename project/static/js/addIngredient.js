document.addEventListener("DOMContentLoaded", function () {
    let formsetContainer = document.getElementById("formset-container");
    let addButton = document.getElementById("add-ingredient");
    let totalForms = document.getElementById("id_recipeingredient_set-TOTAL_FORMS");

    addButton.addEventListener("click", function () {
        let currentFormCount = parseInt(totalForms.value);
        let newForm = formsetContainer.children[1].cloneNode(true); // Cloniamo un modulo esistente
        newForm.style.display = "block"; // Assicuriamoci che sia visibile

        // Aggiorniamo i nomi degli input con il nuovo indice
        newForm.innerHTML = newForm.innerHTML.replace(/-\d+-/g, `-${currentFormCount}-`);

        // Puliamo i campi input del modulo clonato
        newForm.querySelectorAll("input, select").forEach(input => {
            if (input.type !== "hidden") {
                input.value = "";
            }
        });

        formsetContainer.appendChild(newForm);
        totalForms.value = currentFormCount + 1; // Aggiorniamo il contatore totale
    });
});