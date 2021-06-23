from django.db import models


class Base(models.Model):

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField()

    class Meta:

        abstract = True




class Newsletter(Base):
    
    email = models.EmailField( max_length=250)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'



class Sociaux (Base):
    
    url = models.URLField( max_length=250)
    nom = models.CharField( max_length=250)


    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Sociaux'


class website (Base):
    
    nom_site = models.CharField( max_length=250)
    logo_site = models.FileField(upload_to='images')  

    def __str__(self):
        return self.nom_site

    class Meta:
        verbose_name = 'website'
        verbose_name_plural = 'websites'


class Configuration (Base):
    
    description_newsletter = models.TextField()
    copyrigths = models.CharField( max_length=250)


    def __str__(self):
        return self.copyrigths

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'



# Create your models here.
