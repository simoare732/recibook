from django.shortcuts import render

from recipe.models import Recipe, Category, Ingredient

def home_page(request):
    if request.user.is_authenticated:
        recipes = Recipe.objects.filter(user=request.user).order_by('name')
        categories = Category.objects.filter(user=request.user).order_by('name')
        ingredients = Ingredient.objects.filter(user=request.user).order_by('name')
        return render(request, 'pages/home_page.html', {
            'recipes': recipes,
            'categories': categories,
            'ingredients': ingredients,
        })
    return render(request, 'pages/home_page.html')