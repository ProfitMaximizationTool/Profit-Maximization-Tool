# Generated by Django 4.0.2 on 2022-03-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profitmaximizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessowner',
            name='full_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
