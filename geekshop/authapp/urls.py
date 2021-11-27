from django.urls import path
from authapp.views import login, register, logout
# from authapp.views import

app_name = 'authapp'
urlpatterns = [
    # path('', products, name='authapp'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
