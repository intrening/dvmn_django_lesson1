from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place

def index_view(request):
    places_json = {
        "type": "FeatureCollection",
        "features": [],
    }
    for place in Place.objects.all():
        places_json["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(place.lng), float(place.lat)]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": reverse('places-json-view', args=[place.pk])
                }
            },
        )
    return render(request, 'index.html', context = {
        'places_json': places_json,
    })


def places_json_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    response_data = {
        'title': place.title,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'imgs': [
            image.get_absolute_image_url for image in place.images.all()
        ],
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        }
    }
    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False, 'indent': 2})
