from django.urls import path

from adminapp.views import index, admin_users_read

# from authapp.views import

app_name = 'adminapp'
urlpatterns = [
    # path('', products, name='authapp'),
    path('', index, name='index'),
    path('admin-users-read', admin_users_read, name='admin_users_read'),
]
