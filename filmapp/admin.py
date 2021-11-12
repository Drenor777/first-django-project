from django.contrib import admin
from .models import Film, ExtraInfo, Opinion, Actor
# Register your models here.


# @admin.register(Film)
# class FilmAdmin(admin.ModelAdmin):
#     fields = ['title', 'prize', 'year', 'review', 'premiere', 'imbd_rating', 'poster']
#     # exclude = ['poster']
#     list_display = ['title', 'year', 'imbd_rating']
#     list_filter = ['title', 'year', 'imbd_rating']
#     search_fields = ['title', 'review']

admin.site.register(ExtraInfo)
admin.site.register(Film)
admin.site.register(Opinion)
admin.site.register(Actor)
