
from django.urls import path
from . import views 

from service.api import api_add_to_cart 
from service.api import  api_remove_from_cart
from service.api import  api_checkout
from service.api import  create_checkout_session

urlpatterns = [
    path('', views.index , name='index'),
    path('cart/', views.cart_detail , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('shop/', views.shop , name='shop'),
    path('product-detail/<int:id>/', views.product_detail , name='product-detail'),
    path('search/', views.search , name='search'),
    path('newsletter/', views.newsletter , name='newsletter'),


    #API 

    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/api_remove_from_cart', api_remove_from_cart , name='api_remove_from_cart'),
    path('api/api_checkout', api_checkout , name='api_checkout'),
    path('api/create_checkout_session', create_checkout_session , name='create_checkout_session'),






]
