from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    # def __init__(self, *args, **kwargs):
    #     super(UserLoginForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
    #     self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите почту'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите  фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
    #     self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл.почты'
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'Введите  имя'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Введите  фамилию'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control py-4'
