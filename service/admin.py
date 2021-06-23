from django.contrib import admin

from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('nom', 'date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)


@admin.register(models.Marque)
class MarqueAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('nom','active', 'date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('images_view', 'date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)

    def images_view(self, obj):
        '''
            Permet d'avoir un aperçu des images
        '''
        return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin



@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('images_view','nom','prix','date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)

    def images_view(self, obj):
        if obj:
            return mark_safe(f'<img src="{obj.image.url}" style="height:50px; width:100px">')
        else:
            return '_'
    images_view.short_description = 'Aperçu des images' # 


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('total','date_add', 'date_update', 'status')
    ordering = ['-date_add']
    list_editable = ('status',)

# Register your models here.
