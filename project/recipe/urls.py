from django.urls import path
from .views import *

app_name = 'recipe'

urlpatterns = [
    path('createRecipe/', RecipeCreateView.as_view(), name='create_recipe'),
    path('createIngredient/', IngredientCreateView.as_view(), name='create_ingredient'),
    path('createBulkIngredient/', BulkIngredientCreateView.as_view(), name='create_bulk_ingredient'),
    path('deleteRecipe/<int:pk>/', RecipeDeleteView.as_view(), name='delete_recipe'),
]