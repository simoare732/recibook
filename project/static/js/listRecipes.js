// This script is used to filter the recipe by name
document.getElementById('searchInput').addEventListener('keyup', function() {
    // Get the search value and convert it to lowercase for case-insensitive comparison
    var searchValue = this.value.toLowerCase();
    // Get all the elements with the class 'recipe-container'
    var recipeContainers = document.querySelectorAll('.recipe-container');
    // For every recipe container do the following
    recipeContainers.forEach(function(container) {
        // Get the title of the recipe and convert it to lowercase for case-insensitive comparison
        var title = container.querySelector('.card-title').innerText.toLowerCase();

        // If the title includes the search value, display the container, otherwise hide it
        if (title.includes(searchValue)) {
            container.style.display = '';
            container.classList.add('d-flex');
        } else {
            container.classList.remove('d-flex');
            container.style.display = 'none';
            console.log(title)
        }
    });
});