from django.db import models
from django.conf import settings

<<<<<<< HEAD
=======
# Modelo para un favorito.
>>>>>>> 5e876d0f40ac7faadccc567c7875634633d27533
class Favourite(models.Model):
    url = models.TextField()
    name = models.CharField(max_length=200)
    status = models.TextField()
    last_location = models.TextField()
    first_seen = models.TextField()

<<<<<<< HEAD
    # Relación con el usuario
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'url', 'name', 'status', 'last_location', 'first_seen'),)

    def __str__(self):
        return self.name
=======
    # Asociamos el favorito con el usuario en cuestión.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'url', 'name', 'status', 'last_location', 'first_seen'),)
>>>>>>> 5e876d0f40ac7faadccc567c7875634633d27533
