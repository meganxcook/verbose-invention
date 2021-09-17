from django.shortcuts import render
from django.conf import settings
from decouple import config


def home(request):
    return render(request, 'pages/home.html')

def search(request):
    UNSPLASH_KEY = config('UNSPLASH_KEY')
    # print("This is a search function")

    url = "https://api.unsplash.com/search/photos?page=1&query=office"

    payload={}
    headers = {
    'Authorization': f'Client-ID {UNSPLASH_KEY}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    return render(request, 'pages/gallery.html')






# Create your views here.
