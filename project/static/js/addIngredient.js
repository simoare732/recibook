document.addEventListener("DOMContentLoaded", function () {
    let formsetContainer = document.getElementById("formset-container");
    let addButton = document.getElementById("add-ingredient");
    let totalForms = document.getElementById("id_recipeingredient_set-TOTAL_FORMS");

    // Funzione per aggiornare gli indici dei form dopo una rimozione o aggiunta
    function updateFormIndices() {
        let forms = document.querySelectorAll("#formset-container .formset-item");
        forms.forEach((formItem, index) => {
            // Aggiorna gli attributi name e id di ogni input/select/textarea
            formItem.querySelectorAll("input, select, textarea").forEach(function(input) {
                if (input.name) {
                    input.name = input.name.replace(/recipeingredient_set-\d+-/, "recipeingredient_set-" + index + "-");
                }
                if (input.id) {
                    input.id = input.id.replace(/id_recipeingredient_set-\d+-/, "id_recipeingredient_set-" + index + "-");
                }
            });
        });
        totalForms.value = forms.length;
    }

    // Gestione della rimozione tramite event delegation
    formsetContainer.addEventListener("click", function(event) {
        if (event.target && event.target.classList.contains("remove-ingredient")) {
            let formItem = event.target.closest(".formset-item");
            if (formItem) {
                formItem.remove();
                updateFormIndices();
            }
        }
    });

    // Gestione del pulsante per aggiungere un nuovo ingrediente
    addButton.addEventListener("click", function () {
        let currentFormCount = parseInt(totalForms.value);
        // Recupera il template dell'empty form
        let emptyFormTemplate = document.getElementById("empty-form").innerHTML;
        // Sostituisci il placeholder __prefix__ con il nuovo indice
        let newFormHtml = emptyFormTemplate.replace(/__prefix__/g, currentFormCount);

        // Aggiungi il nuovo form al container
        formsetContainer.insertAdjacentHTML('beforeend', newFormHtml);
        updateFormIndices();
    });
});
