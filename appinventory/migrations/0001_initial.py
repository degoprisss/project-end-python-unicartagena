# Generated by Django 3.2 on 2022-07-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('te', 'teclado'), ('mo', 'monitor'), ('ma', 'mouse'), ('cpu', 'cpu'), ('cam', 'camara')], max_length=3)),
                ('consecutive', models.CharField(max_length=50)),
                ('date_fabrication', models.DateField()),
            ],
        ),
    ]