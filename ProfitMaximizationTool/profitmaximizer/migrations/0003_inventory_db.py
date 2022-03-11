# Generated by Django 4.0.2 on 2022-03-10 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profitmaximizer', '0002_businessowner_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('units', models.IntegerField()),
                ('daily_units', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profitmaximizer.businessowner')),
            ],
        ),
    ]
