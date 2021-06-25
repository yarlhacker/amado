from django.db import models
from website.models import Base



class Checkout(Base):


    CHOIX = (
        ('F', 'France'),
        ('C', 'Canada'),
        ('G', 'Germany'),
    )

    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pays = models.CharField(max_length=1, choices=CHOIX)
    adresse = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    commentaire =  models.TextField()
    create_acount = models.BooleanField(default=False)
    ship_address= models.BooleanField(default=False)


    def __str__(self):
        return self.nom

    
    class Meta :

        verbose_name ='checkout'
        verbose_name_plural ='checkouts'


class Payement(Base):

    checkout =  models.ForeignKey('checkout.Checkout', related_name='checkout_payement', on_delete=models.CASCADE)
    article = models.ForeignKey('service.Article', related_name='article_payement', on_delete=models.CASCADE)
    prix = models.CharField(max_length=255)
    quantite = models.CharField(max_length=255)


    def __str__(self):
        return self.prix

    
    class Meta :

        verbose_name ='Payement'
        verbose_name_plural ='Payements'

 

 





    



# Create your models here.
