
from django.urls import path
from . import views 

from service.api import api_add_to_cart


urlpatterns = [
    path('', views.index , name='index'),
    path('cart/', views.cart , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('shop/', views.shop , name='shop'),
    path('product-detail/<int:id>/', views.product_detail , name='product-detail'),
    path('search/', views.search , name='search'),


    #API 

    path('api/api_add_to_cart', api_add_to_cart , name='api_add_to_cart'),



]
