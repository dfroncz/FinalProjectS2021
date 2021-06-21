from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FilmGenre(models.Model):
    genrename=models.CharField(max_length=255)
    genredescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.genrename

    class Meta:
        db_table='FilmGenre'
        verbose_name_plural='FilmGenres'

class Film(models.Model):
    filmname=models.CharField(max_length=255)
    filmgenre=models.ForeignKey(FilmGenre, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    releasedate=models.DateField()
    url=models.URLField(null=True, blank=True)
    filmdescription=models.TextField()

    def __str__(self):
        return self.filmname

    class Meta:
        db_table='Film'
        verbose_name_plural='Films'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    film=models.ForeignKey(Film, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='Review'
        verbose_name_plural='Reviews'