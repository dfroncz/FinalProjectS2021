from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.films, name='films'),
    path('filmDetail/<int:id>', views.filmDetail, name='detail'),
]