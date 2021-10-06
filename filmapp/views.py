from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm


def homepage(request):
    all_films = Film.objects.all()
    first_film = [Film.objects.get(id=1)]
    same_date_films = Film.objects.filter(year=1996)
    unique_date_film = Film.objects.filter(year=1998)
    return render(request, 'Films.html', {'films': all_films})


def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'new_film.html', {'form': form})




