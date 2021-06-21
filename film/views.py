from django.shortcuts import render, get_object_or_404
from .models import FilmGenre, Film, Review

# Create your views here.
def index(request):
    return render(request, 'film/index.html')

def films(request):
    film_list=Film.objects.all()
    return render(request, 'film/films.html', {'film_list': film_list})

def filmDetail(request, id):
    film=get_object_or_404(Film, pk=id)
    return render(request, 'film/filmDetail.html', {'film' : film})