from django.test import TestCase
from django.contrib.auth.models import User
from .models import FilmGenre, Film, Review
import datetime

# Create your tests here.
class FilmGenreTest(TestCase):
    def setUp(self):
        self.genre=FilmGenre(genrename='Marvel')
    
    def test_genrestring(self):
        self.assertEqual(str(self.genre), 'Marvel')
    
    def test_tablename(self):
        self.assertEqual(str(FilmGenre._meta.db_table), 'FilmGenre')

class FilmTest(TestCase):
    def setUp(self):
        self.genre=FilmGenre(genrename='Marvel')
        self.user=User(username='user1')
        self.film=Film(filmname='Winter Soldier', filmgenre='Marvel', user=self.user, releasedate=(2017,3,17), url='wikipedia', filmdescription='A great movie')
    
    def test_string(self):
        self.assertEqual(str(film), 'Winter Soldier')
        

