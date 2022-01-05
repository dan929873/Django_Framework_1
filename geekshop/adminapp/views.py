from django.shortcuts import render

from authapp.models import User


def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    contesxt = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', contesxt)
