from django.forms import ModelForm
from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'prize', 'year', 'review', 'premiere', 'imbd_rating', 'poster']
        exclude = []



