# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.core.exceptions import ValidationError
from .layers.persistence.repositories import saveFavourite as save_fav_repo, getAllFavourites as get_favs_repo, deleteFavourite as delete_fav_repo
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



    
    favourite_list = get_favs_repo(request.user)  

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})
def search(request):
    search_msg = request.POST.get('query', '').strip()  

    if search_msg:  
        link = f'https://rickandmortyapi.com/api/character/?name={search_msg}'

        try:
            contenido = requests.get(link)
            contenido.raise_for_status()  
            data = contenido.json()

            if 'results' in data:
                images = [{
                    'nombre': character['name'],
                    'url': character['image'],
                    'estado': character['status'],
                    'ultima_ubicacion': character['location']['name'] if character['location'] else 'Desconocido',
                    'episodio_inicial': character['origin']['name'] if character['origin'] else 'Desconocido'
                } for character in data['results']]
            else:
                images = []  
        except requests.exceptions.RequestException:
            images = []  

        return render(request, 'home.html', {'images': images, 'query': search_msg})
    else:
       
        return redirect('home')



@login_required
def getAllFavouritesByUser(request):
    favourite_list = get_favs_repo(request.user)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    if request.method == 'POST':
        
        url = request.POST.get('url')
        name = request.POST.get('name')
        status = request.POST.get('status')
        last_location = request.POST.get('last_location')
        first_seen = request.POST.get('first_seen')

        
        if not all([url, name, status, last_location, first_seen]):
            print("Faltan datos:", {
                'url': url,
                'name': name,
                'status': status,
                'last_location': last_location,
                'first_seen': first_seen
            })  
            return HttpResponseBadRequest("Faltan datos requeridos")

        
        from app.models import(Favourite)
        if Favourite.objects.filter(user=request.user, url=url).exists():
            return HttpResponseBadRequest("Este personaje ya está en tus favoritos")

        
        saved_fav = save_fav_repo(url, name, status, last_location, first_seen, request.user)

        if saved_fav:
            return redirect('favoritos')  
        else:
            return HttpResponseBadRequest("Error al guardar el favorito")

    return HttpResponseBadRequest("Método no permitido")

@login_required
def deleteFavourite(request):
    if request.method == "POST":
        fav_id = request.POST.get('id')
        
        delete_fav_repo(fav_id)
        return redirect('favoritos')
    return HttpResponseBadRequest("Invalid request")

@login_required
def exit(request):
    logout(request)  
    return redirect('login')