from django.shortcuts import render
import json
import os

# Create your views here.
from mainapp.models import Product, ProductCategory

MODULE_DIR =os.path.dirname(__file__)

def index(request):
    context = {
        'title': 'Geelshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    context = {'title': 'Geelshop | Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context.update({'products': products})
    else:
        context.update({'products': Product.objects.all()})

    return render(request, 'mainapp/products.html', context)
