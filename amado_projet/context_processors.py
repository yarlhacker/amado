from website import models as models_website
from service import models as models_service
from website.cart import Cart 


def website (request): 

    website = models_website.website.objects.filter(status=True).first()
    config =  models_website.Configuration.objects.filter(status=True).first()
    cart =  Cart(request)

    return locals()




