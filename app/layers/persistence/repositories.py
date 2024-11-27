# capa DAO de acceso/persistencia de datos.

def saveFavourite(url, name, status, last_location, first_seen, user):
    try:
        # Guardar los datos directamente en la base de datos
        # Sin necesidad de importar Favourite en este archivo
        from app.models import(Favourite)  # Este import solo lo hacemos aquí adentro para no causar conflicto

        fav = Favourite.objects.create(
            url=url,
            name=name,
            status=status,
            last_location=last_location,
            first_seen=first_seen,
            user=user
        )
        return fav
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

# Eliminar un favorito por su ID
def deleteFavourite(id):
    try:
        # Usamos getattr para obtener el modelo Favourite sin necesidad de importarlo
        Favourite = getattr(__import__('app.models', fromlist=['Favourite']), 'Favourite')
        favourite = Favourite.objects.get(id=id)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:
        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False