# Generated by Django 4.0.2 on 2022-03-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profitmaximizer', '0004_productrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrecord',
            name='ingredients',
            field=models.JSONField(default=0),
        ),
    ]