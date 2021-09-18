import requests
from django.shortcuts import render
from django.conf import settings
from decouple import config


def home(request):
    return render(request, 'pages/home.html')

def search(request):
    UNSPLASH_KEY = config('UNSPLASH_KEY')
    # print("This is a search function")

    url = "https://api.unsplash.com/search/photos?page=1&query=tree"

    payload={}
    headers = {
    'Authorization': f'Client-ID {UNSPLASH_KEY}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    data = response.json()
    results = data['results'] 
    list_thumbs = []

    for thumb in results:
        list_thumbs.append(thumb['urls']['thumb'])
        
    context = {
        'thumbs': list_thumbs
    }
    # print(list_thumbs)
    return render(request, 'pages/gallery.html', context)

# def result(request):
#     if request.method == 'POST':
#         result_images = request.POST['']