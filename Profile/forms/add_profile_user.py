from django import forms
from Profile.models import ProfileUser
from Profile.models import UserFood
from .widgets import BootstrapDateTimePickerInput


class AddProfileUser(forms.ModelForm):
    photo = forms.FileField(label="Фото профиля")
    date_born = forms.DateTimeField(
        widget=BootstrapDateTimePickerInput,
        input_formats=['%d/%m/%Y'],
        label="Дата рождения"
    )

    class Meta:
        model = ProfileUser
        fields = ['weight', 'height', 'date_born', 'photo']


class ChoseProductUser(forms.ModelForm):
    food_calories = forms.FloatField(label="КилоКалории на 100гр.")
    count_calories = forms.FloatField(label="Расчетные КилоКалории")

    data_time_add_product = forms.DateTimeField(
        widget=BootstrapDateTimePickerInput,
        input_formats=['%d/%m/%Y %H:%M'],
        label="Дата употребления продукта"
    )

    class Meta:
        model = UserFood
        fields = ['name_product', 'amount_food', 'data_time_add_product']
