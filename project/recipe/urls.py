from django.urls import path
from .views import *

app_name = 'recipe'

urlpatterns = [
    path('createRecipe/', RecipeCreateView.as_view(), name='create_recipe'),
    path('createIngredient/', IngredientCreateView.as_view(), name='create_ingredient'),
]