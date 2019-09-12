# from django.shortcuts import render
from django.views.generic.base import TemplateView


class ProfileFormView(TemplateView):
    template_name = "profile_user.html"
