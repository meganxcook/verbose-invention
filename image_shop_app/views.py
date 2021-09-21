import requests
from django.shortcuts import render
from django.conf import settings
from decouple import config
from .models import User, Image


def home(request):
    return render(request, 'pages/home.html')

def search(request):
    UNSPLASH_KEY = config('UNSPLASH_KEY')
    # print("This is a search function")
    url = f"https://api.unsplash.com/search/photos?page=1&query={request.POST['search']}&per_page=3"

    payload={}
    headers = {
    'Authorization': f'Client-ID {UNSPLASH_KEY}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    photos = data['results']
    list_photos = []

    for photo in photos:
        photo_dict = {}
        photo_dict['id'] = photo['id']
        photo_dict['thumb'] = photo['urls']['thumb']
        list_photos.append(photo_dict)


    context = {
        'photos': list_photos
    }
    # print(list_thumbs)
    return render(request, 'pages/gallery.html', context)

def shopping_cart(request):
    user = request.user
    print(request.POST)
    images = request.POST['id']
    print(images)
    for image in images:
        Image.objects.create(user=user, image_id=image, image_alt_description='text', image_url='test44')

    return render(request, 'pages/cart.html')
