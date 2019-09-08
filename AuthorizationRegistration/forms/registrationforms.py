from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2',)
        labels = {
            'email': 'Адрес электронной почты*',
            'first_name': 'Имя*',
            'last_name': 'Фамилия*',
            'username': 'Логин',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }