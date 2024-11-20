# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home_view(request):
    consulta = request.POST.get('query', None)  
    images = services.getAllImages(consulta)  
    print(images)
    return render(request, 'home.html', {'images': images})
def index_page(request):

    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
import requests

def home(request):
    Pagina_default = '1'
    link = f'https://rickandmortyapi.com/api/character?page={Pagina_default}'
    

    contenido = requests.get(link)
    data = contenido.json() 

   
    images = [{
        'nombre': character['name'],
        'url': character['image'],
        'estado': character['status'],
        'ultima_ubicacion': character['location']['name'] if character['location'] else 'Desconocido',
        'episodio_inicial': character['origin']['name'] if character['origin'] else 'Desconocido'

    } for character in data['results']]


    favourite_list = []
    

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