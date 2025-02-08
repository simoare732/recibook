from django.shortcuts import render

from recipe.models import Recipe, Category, Ingredient

def home_page(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'pages/home_page.html', {
        'recipes': recipes,
        'categories': categories,
        'ingredients': ingredients,
    })