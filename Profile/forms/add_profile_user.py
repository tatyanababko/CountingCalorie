from django import forms
from Profile.models import ProfileUser
from Profile.models import UserFood


class AddProfileUser(forms.ModelForm):
    photo = forms.FileField(label="Фото профиля")

    class Meta:
        model = ProfileUser
        fields = ['weight', 'height', 'date_born', 'photo']


class ChoseProductUser(forms.ModelForm):
    count_calories = forms.FloatField(label="Расчетные КилоКалории")

    class Meta:
        model = UserFood
        fields = ['name_product', 'amount_food', 'data_time_add_product', 'count_calories']
