from website import models as models_website
from service import models as models_service


def website (request): 

    website = models_website.website.objects.filter(status=True).first()
    config =  models_website.Configuration.objects.filter(status=True).first()

    return locals()


