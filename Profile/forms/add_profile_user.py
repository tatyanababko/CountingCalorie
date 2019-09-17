from django import forms
from Profile.models import ProfileUser
from .widgets import BootstrapDateTimePickerInput


class AddProfileUser(forms.ModelForm):
    photo = forms.FileField(label="Фото профиля")
    date_born = forms.DateTimeField(
        widget=BootstrapDateTimePickerInput,
        input_formats=['%d/%m/%Y %H:%M'],
        label="Дата рождения"
    )

    class Meta:
        model = ProfileUser
        fields = ['date_born', 'weight', 'height', 'photo']
