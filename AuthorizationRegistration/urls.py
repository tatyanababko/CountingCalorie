from django.urls import path
from .views import RegisterFormView
from .views import AutorizationFormView
from .views import LogoutView


urlpatterns = [
    path('', AutorizationFormView.as_view(), name="autorization"),
    path('registration/', RegisterFormView.as_view(), name="registration"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
