from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=300)
    description_long = HTMLField()
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField()
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)
