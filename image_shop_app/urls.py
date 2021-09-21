from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('gallery/', views.search, name = 'search'),
    path('cart/', views.shopping_cart, name = 'cart')



]
