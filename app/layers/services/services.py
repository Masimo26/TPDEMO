# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
import requests
from app.layers.persistence.repositories import saveFavourite as save_fav_repo, getAllFavourites as get_favs_repo, deleteFavourite as delete_fav_repo

def conseguirimagenesAPI():
    url = "https://rickandmortyapi.com/api/character" 
    contenido = requests.get(url)
    if contenido.status_code == 200:
        return contenido.json().get('results', []) 
    return []


def getAllImages(input=None):
    
    json_collection = repositories.conseguirimagenesAPI() 
    
    images = []  
    
    for personaje in json_collection:

        card = {
        'nombre': personaje.get('name'),
        'url': personaje.get('image'),
        'estado': personaje.get('status'),
        'ultima_ubicacion': personaje.get('location', {}).get('name', 'Desconocido'),
        'episodio_inicial': personaje.get('origin', {}).get('name', 'Desconocido')  
    }
   
        if input:
            if input.lower() in card['nombre'].lower():
                images.append(card)
        else:
            images.append(card)
    
    return images


def saveFavourite(request, image_data):
    """Guardar un personaje como favorito"""
    user = request.user

    image = {
        'url': image_data['image'],
        'name': image_data['name'],
        'status': image_data['status'],
        'last_location': image_data['location']['name'] if image_data['location'] else 'Desconocido',
        'first_seen': image_data['origin']['name'] if image_data['origin'] else 'Desconocido',
        'user': user
    }

    return save_fav_repo(image)

def getAllFavourites(user):
    """Obtenemos todos los favoritos de un usuario"""
    return get_favs_repo(user)

def deleteFavourite(request, fav_id):
    """Eliminar un favorito por ID"""
    return delete_fav_repo(fav_id)

def saveFavourite(request):
    fav = '' 
    fav.user = '' 

    return repositories.saveFavourite(fav) 


def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] 
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' 
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.