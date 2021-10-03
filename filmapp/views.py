from django.shortcuts import render
from django.http import HttpResponse
from .models import Film


def homepage(request):
    save_films = Film.objects.all()
    return render(request, 'Films.html', {'films': save_films})


