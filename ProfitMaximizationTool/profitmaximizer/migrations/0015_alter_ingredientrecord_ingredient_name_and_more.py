# Generated by Django 4.0.2 on 2022-03-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profitmaximizer', '0014_alter_ingredientrecord_ingredient_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecord',
            name='ingredient_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='productrecord',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='salesrecord',
            name='date',
            field=models.DateField(null=True),
        ),
    ]