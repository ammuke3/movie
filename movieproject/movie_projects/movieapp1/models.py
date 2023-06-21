from django.db import models


# Create your models here.
class Movielist(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='movie_pics')
