# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home_view(request):
    input_query = request.POST.get('query', None)  # Obtén el término de búsqueda del formulario
    images = services.getAllImages(input_query)  # Llama a la función para obtener las imágenes
    print(images)
    return render(request, 'home.html', {'images': images})
def index_page(request):

    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
import requests

def home(request):
    DEFAULT_PAGE = '1'
    link = f'https://rickandmortyapi.com/api/character?page={DEFAULT_PAGE}'
    

    contenido = requests.get(link)
    data = contenido.json() 

   
    images = [{
        'name': character['name'],
        'url': character['image'],
        'status': character['status'],
        'last_location': character['location']['name'] if character['location'] else 'Desconocido',
        'first_seen': character['episode'][0] if character['episode'] else 'Desconocido'
    } for character in data['results']]


    favourite_list = [
        'https://rickandmortyapi.com/api/character/1',
        'https://rickandmortyapi.com/api/character/3'
    ]
    

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})


def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        pass
    else:
        return redirect('home')


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass