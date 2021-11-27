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


def products(request):
    # file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geelshop | Каталог',
    }
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    # context['products'] = json.load(open(file_path, encoding='utf-8'))
    return render(request, 'mainapp/products.html', context)
