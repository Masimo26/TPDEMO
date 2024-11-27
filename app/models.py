from django.db import models
from django.conf import settings

class Favourite(models.Model):
    url = models.TextField()
    name = models.CharField(max_length=200)
    status = models.TextField()
    last_location = models.TextField()
    first_seen = models.TextField()

    # Relación con el usuario
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'url', 'name', 'status', 'last_location', 'first_seen'),)

    def __str__(self):
        return self.name