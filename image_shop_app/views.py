import requests
from django.shortcuts import render
from django.conf import settings
from decouple import config


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

# def result(request):
#     if request.method == 'POST':
#         result_images = request.POST['']