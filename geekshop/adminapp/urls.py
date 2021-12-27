from django.urls import path

from adminapp.views import index

# from authapp.views import

app_name = 'adminapp'
urlpatterns = [
    # path('', products, name='authapp'),
    path('', index, name='index'),
]
