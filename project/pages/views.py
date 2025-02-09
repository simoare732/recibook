from django.shortcuts import render

from recipe.models import Recipe, Category, Ingredient

def home_page(request):
    recipes = Recipe.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    ingredients = Ingredient.objects.all().order_by('name')
    return render(request, 'pages/home_page.html', {
        'recipes': recipes,
        'categories': categories,
        'ingredients': ingredients,
    })