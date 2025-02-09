from django import forms
from .models import *
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet


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
    difficult = forms.ChoiceField(
        label='Difficoltà',
        required=True,
        choices=Recipe.DIFFICULTIES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    time_preparation = forms.IntegerField(
        label='Tempo di preparazione (minuti)',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    cooking = forms.IntegerField(
        label='Tempo di cottura (minuti) / Tempo di riposo (minuti)',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    servings = forms.IntegerField(
        label='Dosi',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    cost = forms.ChoiceField(
        label='Costo',
        required=True,
        choices=Recipe.COSTS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    image = forms.ImageField(
        label='Immagine',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Recipe
        fields = ['name', 'category', 'difficult', 'preparation', 'cooking', 'servings', 'cost', 'image', 'time_preparation']


class recipeIngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(
        label='Ingrediente',
        required=True,
        queryset=Ingredient.objects.none(),
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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Ottieni l'utente dai kwargs
        super().__init__(*args, **kwargs)
        if user:
            self.fields['ingredient'].queryset = Ingredient.objects.filter(user=user).order_by('name')


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
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Note sulle ricetta'})
    )

    class Meta:
        model = Note
        fields = ['text']

class BaseRecipeIngredientFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.user = self.user
            form.fields['ingredient'].queryset = Ingredient.objects.filter(user=self.user).order_by('name')


RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    form=recipeIngredientForm,
    formset=BaseRecipeIngredientFormSet,
    extra=1,
    can_delete=True,
)

class bulkIngredientForm(forms.Form):
    ingredients = forms.CharField(
        label='Inserisci gli ingredienti (uno per riga)',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Esempio:\nFarina\nZucchero\nUova\nLatte',
            'rows': 10,
        })
    )