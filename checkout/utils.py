import datetime
import os 

from random import randint
from website.cart import Cart

from checkout.models import Checkout 
from checkout.models import Payement


def checkout(request ,nom, prenom, email, pays, town, phone, zipcode, company, adresse, commentaire):

    cart = Cart(request)

    order = Checkout( nom=nom, prenom=prenom, email=email, pays=pays, town=town, phone=phone, zipcode=zipcode, company=company, adresse=adresse,commentaire=commentaire)
    order.save()
    
    for item in cart:
        Payement.objects.create(checkout=order, article=item['product'], prix=item['price'], quantite=item['quantity'] )

    return order.id





