document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    const ingredientSelect = document.getElementById('ingredientSelect');
    const selectedIngredientsContainer = document.getElementById('selectedIngredients');
    
    // Array per memorizzare gli ingredienti selezionati (in minuscolo per uniformità)
    let selectedIngredients = [];

    // Funzione per aggiornare la visualizzazione dei tag degli ingredienti selezionati
    function updateSelectedIngredientsDisplay() {
        // Svuota il container
        selectedIngredientsContainer.innerHTML = "";
        // Per ogni ingrediente selezionato crea un tag
        selectedIngredients.forEach(ing => {
            const span = document.createElement('span');
            // Uso una classe badge per evidenziare il filtro, con stile text-muted e dimensione ridotta
            span.className = "badge bg-light text-muted me-2";
            span.style.cursor = "pointer";
            span.innerText = ing;
            // Se si clicca sul tag, l'ingrediente viene rimosso dalla lista dei filtri
            span.addEventListener('click', function() {
                selectedIngredients = selectedIngredients.filter(item => item !== ing);
                updateSelectedIngredientsDisplay();
                filterRecipes();
            });
            selectedIngredientsContainer.appendChild(span);
        });
    }

    // Funzione per filtrare le ricette in base a ricerca, categoria e ingredienti selezionati
    function filterRecipes() {
        const searchValue = searchInput.value.toLowerCase();
        const selectedCategory = categoryFilter.value.toLowerCase();
        
        const recipeContainers = document.querySelectorAll('.recipe-container');
        recipeContainers.forEach(function(container) {
            // Estrai i dati: titolo, categoria e ingredienti (convertiti in array)
            const title = container.querySelector('.card-title').innerText.toLowerCase();
            const recipeCategory = container.getAttribute('data-category').toLowerCase();
            const ingredientsData = container.getAttribute('data-ingredients').toLowerCase();
            const recipeIngredients = ingredientsData.split(',').map(item => item.trim());
            
            // Verifica se il titolo contiene il testo della ricerca
            const matchesSearch = title.includes(searchValue);
            // Verifica il filtro per categoria (se vuoto, accetta tutte)
            const matchesCategory = (selectedCategory === '' || recipeCategory === selectedCategory);
            // Verifica che, se sono stati selezionati degli ingredienti, la ricetta li contenga tutti
            let matchesIngredients = true;
            if (selectedIngredients.length > 0) {
                selectedIngredients.forEach(ing => {
                    if (!recipeIngredients.includes(ing)) {
                        matchesIngredients = false;
                    }
                });
            }
            
            // Mostra la ricetta solo se tutte le condizioni sono soddisfatte
            if (matchesSearch && matchesCategory && matchesIngredients) {
                container.style.display = '';
                container.classList.add('d-flex');
            } else {
                container.style.display = 'none';
                container.classList.remove('d-flex');
            }
        });
    }

    // Event listener per la barra di ricerca
    searchInput.addEventListener('keyup', filterRecipes);
    
    // Event listener per il filtro categoria
    categoryFilter.addEventListener('change', filterRecipes);

    // Event listener per il filtro ingredienti tramite SELECT
    ingredientSelect.addEventListener('change', function() {
        const selectedValue = this.value;
        if (selectedValue !== "") {
            // Trasformiamo in minuscolo per uniformità
            const ingLower = selectedValue.toLowerCase();
            // Se non è già presente nella lista, lo aggiunge
            if (!selectedIngredients.includes(ingLower)) {
                selectedIngredients.push(ingLower);
                updateSelectedIngredientsDisplay();
                filterRecipes();
            }
        }
        // Resetta la select al valore predefinito
        this.value = "";
    });
});
