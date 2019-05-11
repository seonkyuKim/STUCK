from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    context = {
        "users": [
            {
                "username": "seonkyu1",
                "followers": 110,
                "influence_point": 321,
                "influence": {
                    "Seoul": 13,
                    "Junction": 30,
                },
            },
            {
                "username": "Matt",
                "followers": 100,
                "influence_point": 21,
                "influence": {
                    "Seoul": 1,
                    "Junction": 20,
                    "Photo": 3,
                }

            }
        ]
    }

    return render(request, 'ecommerce.html', context)
