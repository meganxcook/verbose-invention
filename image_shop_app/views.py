import requests
from django.shortcuts import redirect, render
from django.conf import settings
from decouple import config
from .models import Image
UNSPLASH_KEY = config('UNSPLASH_KEY')


def home(request):
    return render(request, 'pages/home.html')

def search(request):
    # print("This is a search function")
    url = f"https://api.unsplash.com/search/photos?page=1&query={request.POST['search']}&per_page=8"

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
    id_list = request.POST.getlist('id')
    payload={}
    headers = {
    'Authorization': f'Client-ID {UNSPLASH_KEY}'
    }

    for id in id_list:
        url = f"https://api.unsplash.com/photos/{id}"
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        id = data['id']
        desc = data['alt_description'] or 'no description'
        thumb_url = data['urls']['thumb']
        image_url = data['urls']['regular']
        Image.objects.create(user=user, image_id=id, image_alt_description=desc, image_url=image_url, thumb_url=thumb_url)

    shopping_cart_list = Image.objects.filter(user=user, cart_item=True)
    context = {
        'shopping_cart_images': shopping_cart_list
    }
    return render(request, 'pages/cart.html', context)

def checkout(request):
    ids_of_purchased = request.POST.getlist('id')

    for id in ids_of_purchased:
        image = Image.objects.get(id=id)
        image.cart_item = False
        image.owned_item = True
        image.save()
    return render(request, 'pages/checkout.html')

def delete_image(request, id):
    print('id:', id)
    image = Image.objects.get(id=id)
    image.delete()
    return redirect('cart')



