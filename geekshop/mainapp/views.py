from django.shortcuts import render
{% load static %}

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context ={
        'products': [
            {'cardimgtop':'{% static "vendor/img/products/Adidas-hoodie.png"%}',
             'cardtitle':'Худи черного цвета с монограммами adidas Originals',
             'price':'6 090,00 руб.',
             'cardtext':'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'cardimgtop': "{% static 'vendor/img/products/Blue-jacket-The-North-Face.png'%}",
             'cardtitle': 'Синяя куртка The North Face',
             'price': '23 725,00 руб.',
             'cardtext': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'cardimg-top': "{% static 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'%}",
             'cardtitle': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00 руб.',
             'cardtext': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'cardimg-top': "{% static 'vendor/img/products/Black-Nike-Heritage-backpack.png'%}",
             'cardtitle': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00 руб.',
             'cardtext': 'Плотная ткань. Легкий материал.'},
            {'cardimg-top': "{% static 'vendor/img/products/Black-Dr-Martens-shoes.png'%}",
             'cardtitle': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00 руб.',
             'cardtext': 'Гладкий кожаный верх. Натуральный материал.'},
            {'cardimg-top': "{% static 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'%}",
             'cardtitle': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00 руб.',
             'cardtext': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},

        ]
    }

    return render(request, 'mainapp/products.html', context)
