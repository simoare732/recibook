from django.db import models
import os


# Define path to save images of products
def product_image_path(instance, filename):
    # Ensure that the instance has a pk
    if not instance.pk:
        instance.save()  # Save the instance to obtain a pk

    # Generate the path to save the image
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
    image = models.ImageField(upload_to=product_image_path)

    date = models.DateTimeField(auto_now_add=True, editable=False, null=True)

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
        unique_together = ('ricetta', 'ingrediente')

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'


class Note(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return f'Note for {self.recipe.name} of {self.date.strftime("%Y-%m-%d")}'