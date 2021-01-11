import os
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает новые места с указанной ссылки на json-файл'

    def add_arguments(self, parser):
        parser.add_argument('json_url', help='Ссылка на json файл')

    def handle(self, *args, **options):
        response = requests.get(url=options['json_url'])
        response.raise_for_status()
        place_raw = response.json()

        place, _ = Place.objects.update_or_create(
            title=place_raw['title'],
            lng=place_raw['coordinates']['lng'],
            lat=place_raw['coordinates']['lat'],
            defaults={
                'long_description': place_raw['description_long'],
                'short_description': place_raw['description_short'],
            }
        )

        for image_url in place_raw['imgs']:
            response = requests.get(url=image_url)
            response.raise_for_status()
            content_file = ContentFile(response.content)
            image = Image(place=place)
            image.image.save(os.path.basename(image_url), content_file, save=True)
