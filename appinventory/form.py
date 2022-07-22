from django import forms
from .models import Inventory

category_choices = [
        ('teclado', 'teclado'),
        ('monitor', 'monitor'),
        ('mouse', 'mouse'),
        ('cpu', 'cpu'),
        ('camara', 'camara')
    ]

class InventaryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ['category']

        # labels = {
        #     'category': 'Categoría'
        # }

        # widgets = {
        #     'category': forms.SelectMultiple()
        # }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category']


class CreateInventary(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['category', 'consecutive', 'date_fabrication', 'count']

        # labels = {
        #     'category': 'Categoría',
        #     'consecutive': 'Consecutivo',
        #     'date_fabrication': 'Fecha de fabricación',
        #     'count': 'Cantidad'
        # }

        # widgets = {
        #     'category': forms.SelectMultiple(attrs={'class': 'from-control'}),
        #     'consecutive': forms.TextInput(),
        #     'date_fabrication': forms.DateInput(),
        #     'count': forms.NumberInput()
        # }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['category'].widget.attrs.update({'class': 'form-control'})
            self.fields['consecutive'].widget.attrs.update({'class': 'form-control'})
            self.fields['date_fabrication'].widget.attrs.update({'class': 'form-control'})
            self.fields['count'].widget.attrs.update({'class': 'form-control'})



    