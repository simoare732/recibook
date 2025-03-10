import shutil

from django.db import models
from django.conf import settings
import os

from django.contrib.auth.models import User


# Define path to save images of products

def product_image_path(instance, filename):
    # Crea il percorso dell'immagine basato sul pk della ricetta
    return os.path.join('recipe/imgs', str(instance.pk), filename)


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preparation = models.TextField()
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True)

    DIFFICULTIES = [
        ('Facile', 'Facile'),
        ('Media', 'Media'),
        ('Difficile', 'Difficile'),
    ]
    COSTS = [
        ('Basso', 'Basso'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
    ]
    difficult = models.CharField(max_length=255, choices=DIFFICULTIES)
    time_preparation = models.IntegerField(default=0)  # Time of preparation in minutes
    cooking = models.IntegerField(default=0)  # Time of cooking in minutes
    servings = models.IntegerField(default=0)  # Number of servings
    cost = models.CharField(max_length=255, choices=COSTS)  # Cost of the recipe

    date = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        # Salva normalmente se l'oggetto ha già un pk
        if self.pk:
            super().save(*args, **kwargs)
        else:
            # Temporaneamente salva senza immagine per ottenere il pk
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)  # Salvataggio iniziale
            self.image = temp_image
            super().save(*args, **kwargs)  # Salvataggio finale con immagine

            # Crea la cartella per l'immagine, se non esiste
            if self.image:
                product_folder = os.path.join(settings.MEDIA_ROOT, 'recipe/imgs', str(self.pk))
                if not os.path.exists(product_folder):
                    os.makedirs(product_folder)

    def delete(self, *args, **kwargs):
        # Rimuovi l'immagine dalla cartella specifica
        if self.image:
            image_path = self.image.path
            if os.path.exists(image_path):
                os.remove(image_path)  # Rimuove l'immagine

        # Rimuovi la cartella
        product_folder = os.path.join(settings.MEDIA_ROOT, 'recipe/imgs', str(self.pk))
        if os.path.exists(product_folder) and os.path.isdir(product_folder):
            shutil.rmtree(product_folder)  # Rimuove la cartella e il suo contenuto

        # Elimina l'oggetto dalla base dati
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    UNIT = [
        ('g', 'Grammi'),
        ('kg', 'Kilogrammi'),
        ('ml', 'Millilitri'),
        ('l', 'Litri'),
        ('pz', 'Pezzi'),
        ('cup', 'Tazze'),
        ('tbsp', 'Cucchiai'),
        ('tsp', 'Cucchiaini'),
        ('qb', 'Quanto basta'),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipes')
    quantity = models.CharField(max_length=255)
    unit_of_measure = models.CharField(max_length=255, choices=UNIT)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'


class Note(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return f'Note for {self.recipe.name}'