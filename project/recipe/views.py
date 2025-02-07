import json

from django.contrib.messages.context_processors import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView, FormView

from .models import *
from .forms import *


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = recipeForm
    template_name = 'recipe/createRecipe.html'
    success_url = reverse_lazy('pages:home_page')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_formset'] = RecipeIngredientFormSet(self.request.POST)
        else:
            context['ingredient_formset'] = RecipeIngredientFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_formset = context['ingredient_formset']

        if ingredient_formset.is_valid():
            self.object = form.save()  # Salva la ricetta
            ingredient_formset.instance = self.object  # Associa gli ingredienti alla ricetta
            ingredient_formset.save()  # Salva il formset
            return redirect(self.success_url)
        else:
            # Se il formset non è valido, ritorna il form con gli errori
            return self.render_to_response(self.get_context_data(form=form))


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = ingredientForm
    template_name = 'recipe/createIngredient.html'

    def get_success_url(self):
        return reverse('pages:home_page')

class CategoryCreateView(CreateView):
    model = Category
    form_class = categoryForm
    template_name = 'recipe/createCategory.html'

    def get_success_url(self):
        return reverse('pages:home_page')


class BulkIngredientCreateView(FormView):
    model = Ingredient
    form_class = bulkIngredientForm
    template_name = 'recipe/createBulkIngredient.html'
    success_url = reverse_lazy('pages:home_page')


    def form_valid(self, form):
        ingredients = form.cleaned_data['ingredients'].split('\n')
        for ingredient in ingredients:
            ingredient = ingredient.capitalize().strip()
            Ingredient.objects.get_or_create(name=ingredient)

        return super().form_valid(form)


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe/deleteRecipe.html'
    success_url = reverse_lazy('pages:home_page')

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = recipeForm
    template_name = 'recipe/updateRecipe.html'
    success_url = reverse_lazy('pages:home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_formset'] = RecipeIngredientFormSet(self.request.POST, instance=self.object)
        else:
            context['ingredient_formset'] = RecipeIngredientFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_formset = context['ingredient_formset']

        if ingredient_formset.is_valid():
            self.object = form.save()  # Salva la ricetta
            ingredient_formset.instance = self.object  # Associa gli ingredienti alla ricetta
            ingredient_formset.save()  # Salva il formset
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'recipe/ingredientList.html'

    def get_queryset(self):
        return Ingredient.objects.all().order_by('name')

def update_ingredient(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            ingredient.name = data['name']
            ingredient.save()
            return JsonResponse({'success': True})
        except Ingredient.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Ingredient not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def delete_ingredient(request, pk):
    if request.method == 'POST':
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            ingredient.delete()
            return JsonResponse({'success': True})
        except Ingredient.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Ingredient not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


class CategoryListView(ListView):
    model = Category
    template_name = 'recipe/categoryList.html'

    def get_queryset(self):
        return Category.objects.all().order_by('name')


def update_category(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            category = Category.objects.get(pk=pk)
            category.name = data['name']
            category.save()
            return JsonResponse({'success': True})
        except Ingredient.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Category not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def delete_category(request, pk):
    if request.method == 'POST':
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return JsonResponse({'success': True})
        except Ingredient.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Category not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})