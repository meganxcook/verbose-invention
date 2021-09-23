from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('gallery/', views.search, name = 'search'),
    path('cart/', views.shopping_cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('delete/<int:id>/', views.delete_image, name = 'delete'),



]
