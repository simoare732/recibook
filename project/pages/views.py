from django.shortcuts import render

from recipe.models import Recipe

def home_page(request):
    recipes = Recipe.objects.all()
    return render(request, 'pages/home_page.html', {'recipes': recipes})
