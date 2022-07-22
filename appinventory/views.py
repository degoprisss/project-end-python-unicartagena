from django.shortcuts import render, redirect
from .form import InventaryForm, CreateInventary
from .models import Inventory


# Create your views here.

def create_inventary(request):
    inventoryData = Inventory.objects.all()
    if request.method == 'POST':
        form = CreateInventary(request.POST)
        formSearch = InventaryForm(request.POST)
        if form.is_valid():
            form.save()
            context = { 'inventory': inventoryData, 'form': formSearch}
            return redirect('/')
        else:
            return render(request, 'proof.html')
    else: 
        form = CreateInventary()
        return render(request, 'createForm.html', { 'form': form })


def list_inventary(request):
    inventoryData = Inventory.objects.all()
    if request.method == 'POST':
        form = InventaryForm(request.POST)
        if form.is_valid():
            categoryForm = form.cleaned_data['category']
            form = InventaryForm()
            filterCategory = Inventory.objects.filter(category = categoryForm )
            context = { 'inventory': filterCategory, 'form': form}
            return render(request, 'list.html', context)
        else:
            return render(request, 'proof.html')
    else: 
        form = InventaryForm()
        return render(request, 'list.html', { 'inventory': inventoryData, 'form': form })


def delete_register(request, id=None):
    deleteInventory = Inventory.objects.get(id = id)
    deleteInventory.delete()
    return redirect('/')

