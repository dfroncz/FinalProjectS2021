from django.shortcuts import render, get_object_or_404
from .models import FilmGenre, Film, Review
from django.urls import reverse_lazy
from .forms import FilmForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'film/index.html')

def films(request):
    film_list=Film.objects.all()
    return render(request, 'film/films.html', {'film_list': film_list})

def filmDetail(request, id):
    film=get_object_or_404(Film, pk=id)
    return render(request, 'film/filmDetail.html', {'film' : film})

@login_required
def newFilm(request):
    form=FilmForm

    if request.method=='POST':
        form=FilmForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=FilmForm()
    else:
        form=FilmForm()
    return render(request, 'film/newfilm.html', {'form': form})

def loginmessage(request):
    return render(request, 'film/loginmessage.html')

def logoutmessage(request):
    return render(request, 'film/logoutmessage.html')
