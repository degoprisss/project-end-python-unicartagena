# Generated by Django 3.2 on 2022-07-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinventory', '0002_inventory_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='category',
            field=models.CharField(choices=[('teclado', 'teclado'), ('monitor', 'monitor'), ('mouse', 'mouse'), ('cpu', 'cpu'), ('camara', 'camara')], max_length=20),
        ),
    ]
