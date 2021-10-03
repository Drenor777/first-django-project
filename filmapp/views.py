from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return HttpResponse(
        '<body>'
        '<h1>Blog Home</h1>'
        '<p>Welcome</p>'
        '</body>'
    )
