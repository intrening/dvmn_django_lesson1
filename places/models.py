from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.CharField('Короткое описание', max_length=300)
    description_long = HTMLField('Длинное описание')
    lng = models.CharField('Longitude', max_length=20)
    lat = models.CharField('Latitude', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField('Изображение')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

        ordering = ['my_order']

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)
