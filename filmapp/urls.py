from django.urls import path
from filmapp.views import homepage

urlpatterns = [
    path('', homepage)
]
