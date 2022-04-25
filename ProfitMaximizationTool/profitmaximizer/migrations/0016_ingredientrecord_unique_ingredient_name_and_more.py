# Generated by Django 4.0.2 on 2022-03-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profitmaximizer', '0015_alter_ingredientrecord_ingredient_name_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ingredientrecord',
            constraint=models.UniqueConstraint(fields=('owner', 'ingredient_name'), name='unique_ingredient_name'),
        ),
        migrations.AddConstraint(
            model_name='productionrecord',
            constraint=models.UniqueConstraint(fields=('owner', 'date'), name='unique_production_date'),
        ),
        migrations.AddConstraint(
            model_name='productrecord',
            constraint=models.UniqueConstraint(fields=('owner', 'product_name'), name='unique_product_name'),
        ),
        migrations.AddConstraint(
            model_name='salesrecord',
            constraint=models.UniqueConstraint(fields=('owner', 'date'), name='unique_sales_date'),
        ),
    ]