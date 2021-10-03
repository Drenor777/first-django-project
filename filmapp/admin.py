from django.contrib import admin
from .models import Film
# Register your models here.

# admin.site.register(Film)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ['title', 'prize', 'year', 'review', 'premiere', 'imbd_rating']
    exclude = ['poster']
    list_display = ['title', 'year', 'imbd_rating']
    list_filter = ['title', 'year', 'imbd_rating']
    search_fields = ['title', 'review']
