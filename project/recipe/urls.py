from django.urls import path
from .views import *

app_name = 'recipe'

urlpatterns = [
    path('createRecipe/', RecipeCreateView.as_view(), name='create_recipe'),
    path('createIngredient/', IngredientCreateView.as_view(), name='create_ingredient'),
    path('createBulkIngredient/', BulkIngredientCreateView.as_view(), name='create_bulk_ingredient'),
    path('deleteRecipe/<int:pk>/', RecipeDeleteView.as_view(), name='delete_recipe'),
    path('updateRecipe/<int:pk>/', RecipeUpdateView.as_view(), name='update_recipe'),
    path('listIngredients/', IngredientListView.as_view(), name='list_ingredients'),
    path('updateIngredient/<int:pk>/', update_ingredient, name='update_ingredient'),
    path('deleteIngredient/<int:pk>/', delete_ingredient, name='delete_ingredient'),
    path('createCategory/', CategoryCreateView.as_view(), name='create_category'),
    path('listCategories/', CategoryListView.as_view(), name='list_categories'),
    path('updateCategory/<int:pk>/', update_category, name='update_category'),
    path('deleteCategory/<int:pk>/', delete_category, name='delete_category'),
    path('detailRecipe/<int:pk>/', RecipeDetailView.as_view(), name='detail_recipe'),

]