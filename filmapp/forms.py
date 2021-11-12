from django.forms import ModelForm
from .models import Film, ExtraInfo


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'prize', 'year', 'review', 'premiere', 'imbd_rating', 'poster']


class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = ['duration', 'film_genre']
