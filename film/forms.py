from django import forms
from .models import FilmGenre, Film, Review

class FilmForm(forms.ModelForm):
    class Meta:
        model=Film
        fields='__all__'
        