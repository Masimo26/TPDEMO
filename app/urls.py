from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),
<<<<<<< HEAD
    path('exit/', views.exit, name='exit'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
=======

    path('exit/', views.exit, name='exit'),
>>>>>>> 5e876d0f40ac7faadccc567c7875634633d27533
]