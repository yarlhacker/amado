from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('email', 'date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)


@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('url','nom', 'date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)



@admin.register(models.website)
class websiteAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('images_view','nom_site', 'date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)

    def images_view(self, obj):

        if obj:
            return mark_safe(f'<img src="{obj.logo_site.url}" style="height:50px; width:100px">')
        else:
            return '_'

    images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('copyrigths', 'date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)
# Register your models here.
