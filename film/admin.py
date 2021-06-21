from django.contrib import admin
from .models import FilmGenre, Film, Review
# Register your models here.

admin.site.register(FilmGenre)
admin.site.register(Film)
admin.site.register(Review)