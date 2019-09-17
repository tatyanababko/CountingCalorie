from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .forms.registrationforms import SignUpForm
from .forms.autorization import LoginForm
from django.contrib.auth import login
from django.contrib.auth import logout


class AutorizationFormView(FormView):
    form_class = LoginForm
    template_name = "autorization.html"
    success_url = '/profile/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(AutorizationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(AutorizationFormView, self).form_invalid(form)


class RegisterFormView(FormView):
    form_class = SignUpForm
    template_name = "registration.html"
    success_url = "/"


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
