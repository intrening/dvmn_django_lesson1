from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Длинное описание', blank=True)
    lng = models.DecimalField('Долгота', max_digits=22, decimal_places=16)
    lat = models.DecimalField('Широта', max_digits=22, decimal_places=16)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images',
    )
    image = models.ImageField('Изображение')
    order = models.PositiveIntegerField('Порядковый номер', default=0)

    class Meta(object):
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['order']

    def __str__(self):
        return self.place.title

    @property
    def get_absolute_image_url(self):
        return self.image.url
