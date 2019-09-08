from django.urls import path
from .views import RegisterFormView

urlpatterns = [
    path('registration/', RegisterFormView.as_view(), name="registration"),
]
