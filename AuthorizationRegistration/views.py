# from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms.registrationforms import SignUpForm


class RegisterFormView(FormView):
    form_class = SignUpForm

    # Cсылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который используется при отображении представления.
    template_name = "registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)
