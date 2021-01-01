from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=300)
    description_long = models.TextField()
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)

class Image(models.Model):
    places = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField()
