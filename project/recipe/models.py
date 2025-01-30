import shutil

from django.db import models
import os


# Define path to save images of products
def product_image_path(instance, filename):
    # Ensure that the instance has a pk
    if not instance.pk:
        # Temporaneamente salva l'istanza senza immagine per ottenere un pk
        temp_image = instance.image
        instance.image = None
        instance.save()  # Questo salvataggio iniziale genera il pk
        instance.image = temp_image

    # Genera il percorso dell'immagine usando il pk
    return os.path.join(f'recipe/imgs/{instance.pk}', filename)
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preparation = models.TextField()
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True)

    DIFFICULTIES = [
        ('easy', 'Facile'),
        ('medium', 'Media'),
        ('hard', 'Difficile'),
    ]
    COSTS = [
        ('low', 'Basso'),
        ('medium', 'Medio'),
        ('high', 'Alto'),
    ]
    difficult = models.CharField(max_length=255, choices=DIFFICULTIES)
    time_preparation = models.IntegerField(default=0) # Time of preparation in minutes
    cooking = models.IntegerField(default=0) # Time of cooking in minutes
    servings = models.IntegerField(default=0) # Number of servings
    cost = models.CharField(max_length=255, choices=COSTS) # Cost of the recipe


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

    def delete(self, *args, **kwargs):
        # Obtain the path of the folder containing the images of the product
        product_folder = os.path.join('recipe/imgs', str(self.pk))

        # Verify that the folder exists and if there is, delete it
        if os.path.exists(product_folder) and os.path.isdir(product_folder):
            shutil.rmtree(product_folder)  # Remove the folder and its content

        # Delete the product from the database
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    UNIT = [
        ('g', 'Grammi'),
        ('kg', 'Chilogrammi'),
        ('ml', 'Millilitri'),
        ('l', 'Litri'),
        ('pz', 'Pezzi'),
        ('cup', 'Tazze'),
        ('tbsp', 'Cucchiai'),
        ('tsp', 'Cucchiaini'),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)
    unit_of_measure = models.CharField(max_length=255, choices=UNIT)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'


class Note(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return f'Note for {self.recipe.name} of {self.date.strftime("%Y-%m-%d")}'