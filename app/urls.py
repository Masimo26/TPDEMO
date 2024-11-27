from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),  # Página inicial
    path('login/', views.index_page, name='login'),  # Página de login
    path('home/', views.home, name='home'),  # Página principal del buscador
    path('search/', views.search, name='search'),  # Ruta para el buscador
    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),  # Lista de favoritos
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),  # Agregar a favoritos
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),  # Eliminar de favoritos
    path('exit/', views.exit, name='exit'),  # Salida o cierre de sesión
]
