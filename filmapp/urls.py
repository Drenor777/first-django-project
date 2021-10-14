from django.urls import path
from filmapp.views import homepage, new_film, edit_film, delete_film

urlpatterns = [
    path('', homepage),
    path('new/', new_film),
    path('edit/<int:id>/', edit_film),
    path('delete/<int:id>/', delete_film),
]
