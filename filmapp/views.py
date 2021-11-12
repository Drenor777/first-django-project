from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film, ExtraInfo, Opinion
from .forms import FilmForm, ExtraInfoForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def homepage(request):
    all_films = Film.objects.all()
    first_film = [Film.objects.get(id=1)]
    same_date_films = Film.objects.filter(year=1996)
    unique_date_film = Film.objects.filter(year=1998)
    return render(request, 'Films.html', {'films': all_films})


@login_required
def new_film(request):
    film_form = FilmForm(request.POST or None, request.FILES or None)
    extra_form = ExtraInfoForm(request.POST or None)
    if all([film_form.is_valid(), extra_form.is_valid()]):
        film = film_form.save(commit=False)
        extra = extra_form.save()
        film.extra = extra
        film.save()
        return redirect(homepage)

    return render(request, 'film_form.html', {'film_form': film_form, 'extra_form': extra_form, 'new': True})


@login_required
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    rating = Opinion.objects.filter(film_title=film)
    try:
        extra = ExtraInfo.objects.get(film=film.id)
    except ExtraInfo.DoesNotExist:
        extra = None
    film_form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    extra_form = ExtraInfoForm(request.POST or None, instance=extra)

    if all([film_form.is_valid(), extra_form.is_valid()]):
        film = film_form.save(commit=False)
        extra = extra_form.save()
        film.extra = extra
        film.save()
        return redirect(homepage)

    return render(request, 'film_form.html',
                  {'film_form': film_form, 'extra_form': extra_form, 'new': False, 'rating': rating})


@login_required
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == 'POST':
        film.delete()
        return redirect(homepage)
    return render(request, 'confirm_delete.html', {'film': film})
