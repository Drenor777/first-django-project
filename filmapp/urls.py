from django.urls import path
from filmapp.views import homepage, new_film, edit_film, delete_film

urlpatterns = [
    path('', homepage, name="homepage"),
    path('new/', new_film, name="new_film"),
    path('edit/<int:id>/', edit_film, name='edit_film'),
    path('delete/<int:id>/', delete_film, name="delete_film"),
]
