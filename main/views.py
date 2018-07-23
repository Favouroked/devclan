from django.shortcuts import render
from .models import Products
from .utils import get_jumia_data
from django.core import serializers
from django.http import HttpResponse, JsonResponse


# Create your views here.

def get_and_create_data():
    jumia_data = get_jumia_data()
    count = 0
    for data in jumia_data:
        j_data, created = Products.objects.get_or_create(
            name=data.get('name'),
            image=data.get('image'),
            link=data.get('link'),
            price=data.get('price')
        )
        count += 1
        print('Count {}'.format(count))
    return True

def get_products(request):
    # data = serializers.serialize('json', Products.objects.all(), fields=('name', 'image', 'price', 'link'))
    products = Products.objects.all().values()
    data = list(products)
    return JsonResponse(data, safe=False)
