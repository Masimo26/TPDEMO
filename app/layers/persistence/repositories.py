# capa DAO de acceso/persistencia de datos.

from app.models import Favourite

def saveFavourite(url, name, status, last_location, first_seen, user):
    try:
        fav = Favourite.objects.create(
            url=url,
            name=name,
            status=status,
            last_location=last_location,
            first_seen=first_seen,
            user=user
        )
        return fav  # Retorna el objeto creado
    except Exception as e:
        print(f"Error al guardar el favorito: {e}")
        return None

def getAllFavourites(user):

    try:
        # Usamos getattr para obtener el modelo Favourite sin necesidad de importarlo
        Favourite = getattr(__import__('app.models', fromlist=['Favourite']), 'Favourite')
        favourite_list = Favourite.objects.filter(user=user).values('id', 'url', 'name', 'status', 'last_location', 'first_seen')
        return list(favourite_list)
    except Exception as e:
        print(f"Error al obtener los favoritos: {e}")
        return []


def deleteFavourite(id):
    try:

        favourite = Favourite.objects.get(id=id)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:


        print(f"El favorito con ID {id} no existe.")

        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False