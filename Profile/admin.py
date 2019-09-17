from django.contrib import admin
from .models import Food
from .models import UserFood
from .models import ProfileUser

admin.site.register(Food)
admin.site.register(UserFood)
admin.site.register(ProfileUser)
