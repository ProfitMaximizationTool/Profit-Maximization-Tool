# Generated by Django 4.0.2 on 2022-05-10 03:40

from django.db import migrations, models
import profitmaximizer.models


class Migration(migrations.Migration):

    dependencies = [
        ('profitmaximizer', '0017_businessowner_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessowner',
            name='photo',
            field=models.ImageField(default='photos/default.jpg', upload_to=profitmaximizer.models.business_owner_photos_dir),
        ),
    ]
