# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
import requests

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


<<<<<<< HEAD
# Guardar un favorito
from app.layers.persistence.repositories import saveFavourite as save_fav_repo, getAllFavourites as get_favs_repo, deleteFavourite as delete_fav_repo



# Servicio para agregar un favorito
def saveFavourite(request, image_data):
    """Guardar un personaje como favorito"""
    user = request.user

    # Creamos el diccionario con la información del personaje
    image = {
        'url': image_data['image'],
        'name': image_data['name'],
        'status': image_data['status'],
        'last_location': image_data['location']['name'] if image_data['location'] else 'Desconocido',
        'first_seen': image_data['origin']['name'] if image_data['origin'] else 'Desconocido',
        'user': user
    }

    # Llamamos a la función del repositorio para guardar el favorito
    return save_fav_repo(image)

# Servicio para obtener todos los favoritos de un usuario
def getAllFavourites(user):
    """Obtenemos todos los favoritos de un usuario"""
    return get_favs_repo(user)

# Servicio para eliminar un favorito
def deleteFavourite(request, fav_id):
    """Eliminar un favorito por ID"""
    return delete_fav_repo(fav_id)
=======
# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
>>>>>>> 5e876d0f40ac7faadccc567c7875634633d27533
