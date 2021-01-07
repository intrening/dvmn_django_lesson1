from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.TextField('Короткое описание')
    long_description = HTMLField('Длинное описание')
    lng = models.CharField('Долгота', max_length=20)
    lat = models.CharField('Широта', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField('Изображение')
    my_order = models.PositiveIntegerField('Порядковый номер', default=0, blank=False, null=False)

    class Meta(object):
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

        ordering = ['my_order']

    @property
    def get_absolute_image_url(self):
        return "{0}".format(self.image.url)
