from django import forms
from .models import *
from django.forms import inlineformset_factory


class recipeForm(forms.ModelForm):
    name = forms.CharField(
        label='Titolo',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    preparation = forms.CharField(
        label='Preparazione',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'step 1: ... \nstep 2: ...'})
    )
    category = forms.ModelChoiceField(
        label='Categoria',
        required=True,
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        label='Immagine',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Recipe
        fields = ['name', 'category',  'image', 'preparation']


class recipeIngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(
        label='Ingrediente',
        required=True,
        queryset=Ingredient.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantity = forms.CharField(
        label='Quantità',
        required=True,
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    unit_of_measure = forms.ChoiceField(
        label='Unità di misura',
        required=True,
        choices=RecipeIngredient.UNIT,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit_of_measure']


class ingredientForm(forms.ModelForm):
    name = forms.CharField(
        label='Nome',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Ingredient
        fields = ['name']

class categoryForm(forms.ModelForm):
    name = forms.CharField(
        label='Nome',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Category
        fields = ['name']

class noteForm(forms.ModelForm):
    text = forms.CharField(
        label='Note',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Note
        fields = ['text']


RecipeIngredientFormSet = inlineformset_factory(
    Recipe,  # The parent model
    RecipeIngredient,  # The child model
    form=recipeIngredientForm,  # Use the custom form
    extra=1,  # Initial extra empty forms
    can_delete=False,  # Allow deletion of forms
)