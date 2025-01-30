# Generated by Django 5.1.5 on 2025-01-30 20:47

import recipe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cost',
            field=models.CharField(choices=[('low', 'Basso'), ('medium', 'Medio'), ('high', 'Alto')], default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='difficult',
            field=models.CharField(choices=[('easy', 'Facile'), ('medium', 'Media'), ('hard', 'Difficile')], default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=recipe.models.product_image_path),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation',
            field=models.IntegerField(default=0),
        ),
    ]
