from django.db import models
from website.models import Base
# Create your models here.
class Categorie(Base):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

class Marque(Base):

    nom = models.CharField(max_length=255)
    active = models.BooleanField(False)


    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'Marque'
        verbose_name_plural = 'Marques'

class Image(Base):
    
    image = models.FileField(upload_to='images')
    article = models.ForeignKey("service.Article", on_delete=models.CASCADE , related_name='articlesimages')


    def __str__(self):
        return f"self.article"
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

class Article(Base):
    image_principal = models.FileField(upload_to='images')  
    image = models.FileField(upload_to='images')  
    prix = models.IntegerField(default=0)
    nom = models.CharField( max_length=250)
    description = models.TextField()
    categorie = models.ForeignKey("service.Categorie", on_delete=models.CASCADE , related_name='categorieArticle')
    quantite  = models.IntegerField(default=0)
    stock = models.BooleanField(default=True)


    def __str__(self):
            return self.nom
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    
    