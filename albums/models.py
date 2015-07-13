from django.db import models

from artists.models import Artist

class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='albums')
    artist = models.ForeignKey(Artist) #Esto referencia a la tabla artista de la base de datos

# Create your models here.
