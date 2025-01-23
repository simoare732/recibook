$(document).ready(function() {
    let formsetContainer = $('#formset-container');
    let totalForms = $('#id_form-TOTAL_FORMS');

    // Aggiungi un nuovo form quando si clicca il tasto "+"
    $('#add-ingredient').click(function() {
        let newFormIndex = totalForms.val();
        let emptyFormHtml = formsetContainer.children('.formset-item:last').html();
        let newFormHtml = emptyFormHtml.replace(/-0-/g, `-${newFormIndex}-`).replace(/__prefix__/g, newFormIndex);

        formsetContainer.append(`<div class="formset-item">${newFormHtml}</div>`);
        totalForms.val(parseInt(newFormIndex) + 1);
    });
});