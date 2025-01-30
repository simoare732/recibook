// This script is used to filter the recipe by name
document.getElementById('searchInput').addEventListener('keyup', function() {
    // Get the search value and convert it to lowercase for case-insensitive comparison
    var searchValue = this.value.toLowerCase();
    // Get all the elements with the class 'card'
    var recipeCards = document.querySelectorAll('.card');
    // For every recipe card do the following
    recipeCards.forEach(function(card) {
        // Get the title of the recipe and convert it to lowercase for case-insensitive comparison
        var title = card.querySelector('.card-title').innerText.toLowerCase();
        // If the title includes the search value, display the card, otherwise hide it
        if (title.includes(searchValue)) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
});