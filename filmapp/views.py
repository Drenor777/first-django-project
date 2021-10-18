from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required


def homepage(request):
    all_films = Film.objects.all()
    first_film = [Film.objects.get(id=1)]
    same_date_films = Film.objects.filter(year=1996)
    unique_date_film = Film.objects.filter(year=1998)
    return render(request, 'Films.html', {'films': all_films})


@login_required
def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'film_form.html', {'form': form})


@login_required
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(homepage)
    return render(request, 'film_form.html', {'form': form})


@login_required
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == 'POST':
        film.delete()
        return redirect(homepage)
    return render(request, 'confirm_delete.html', {'film': film})
