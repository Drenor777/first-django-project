from django.urls import path
from filmapp.views import homepage, new_film

urlpatterns = [
    path('', homepage),
    path('new/', new_film),
]
