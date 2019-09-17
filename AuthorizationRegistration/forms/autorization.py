from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        labels = {
            'email': 'Эл.почта',
            'username': 'Логин',
            'password': 'Пароль',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
