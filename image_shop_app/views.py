import requests
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def search(request):
    # print("This is a search function")

    url = "https://api.unsplash.com/search/photos?page=1&query=office"

    payload={}
    headers = {
    'Authorization': 'Client-ID pdXvDWUQ3vl_vduMEqjjRhbi1pTKJaZb0oz7OEfMw4o'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    
    return render(request, 'pages/gallery.html')






# Create your views here.
