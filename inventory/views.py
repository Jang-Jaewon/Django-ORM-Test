from django.db import IntegrityError
from django.http import HttpResponse
from .models import Brand


def new(request):
    try:
        Brand.objects.get(brand_id=100)
    except Brand.DoesNotExist:
        return HttpResponse("Sorry we couldn't find")

    return HttpResponse("Hi")
