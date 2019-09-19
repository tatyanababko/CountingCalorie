from django.urls import path
from .views import ProfileFormView


urlpatterns = [
    path('', ProfileFormView.as_view(), name="profile"),
]
