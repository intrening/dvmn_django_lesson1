from django.shortcuts import render
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
                    "detailsUrl": "{% static 'places/moscow_legends.json' %}"
                }
            },
        )

    return render(request, 'index.html', context = {
        'places_json': places_json,
    })
