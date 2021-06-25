from django.contrib import admin
from . import models

@admin.register(models.Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('nom', 'prenom','email','phone','date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)




@admin.register(models.Payement)
class PayementAdmin(admin.ModelAdmin):
    
    # Liste des champs a afficher
    list_display = ('quantite', 'prix','date_add', 'date_update', 'status')
    ordering = ['date_add']
    list_editable = ('status',)


# Register your models here.
