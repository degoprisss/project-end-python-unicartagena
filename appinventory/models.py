from django.db import models
# Create your models here.

class Inventory(models.Model):
    category_choices = [
        ('teclado', 'teclado'),
        ('monitor', 'monitor'),
        ('mouse', 'mouse'),
        ('cpu', 'cpu'),
        ('camara', 'camara')
    ]

    category = models.CharField(choices=category_choices, max_length=20)
    consecutive = models.CharField(max_length=50)
    date_fabrication = models.DateField()
    count = models.IntegerField(null=True)


