# Start Django

***************************

1. Création et activation de l'environnement virtuel

    `python -m venv venv`

    `source venv/bin/activate`

2. Téléchargement de django

    `pip install django` | `pip install django==(version_specifique)`

3. Création d'un projet django

    `django-admin startproject nom_du_projet`

    * Mise en route du serveur de développement

        `cd nom_du_projet`

        `python manage.py runserver`

    * Faire une migration

        `python manage.py makemigrations`

        `python manage.py migrate`

    * Création de l’administrateur

        `python manage.py createsuperuser`

4. Création d'une nouvelle application

    `python manage.py startapp app_name`

## Configuration des medias static

* Dans le fichier **settings.py** du projet

    ```Python

	TEMPLATES = [
	    {
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],
		'APP_DIRS': True,
		...
	    }
	]

        STATIC_URL = '/static/'

        MEDIA_URL = '/media/'

        STATICFILES_DIRS = [BASE_DIR /'static']

        STATIC_ROOT = BASE_DIR / 'static_cdn'

        MEDIA_ROOT = BASE_DIR / 'media_cdn'
    ```

* Dans le fichier **urls.py** du projet

    ```Python

        from django.conf import settings
        from django.conf.urls.static import static

        if settings.DEBUG :
            urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
            urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    ```


## Création de model

```Python

    class ExModel(models.Model):
        # Création des différents champs
        message = models.TextField()           # Zone d’édition de texte multiline
        nom = models.CharField(max_length=255) # Zone d’édition de texte oneline
        email = models.EmailField()            # Zone de texte de type Email

        # Champs obligatoires (Convention de NaN)
        date_add = models.DateTimeField(auto_now_add=True)
        date_update = models.DateTimeField(auto_now=True)
        status = models.BooleanField(default=True)

        class Meta():
            verbose_name = 'ExModel'
            verbose_name_plural = 'ExModels'

        def __str__(self):
            return self.nom
```

* `max_length` : 

* `auto_now_add`: 

* `auto_now` : 


## Administration des models

* Version Basique

```Python

    from . import models

    admin.site.register(models.ExModel)
```

* Version Amélioré

    ```Python

        from . import models
        from django.utils.safestring import mark_safe

	@admin.register(models.ExModel)
        class ExModelAdmin(admin.ModelAdmin):

            # Liste des champs a afficher
            list_display = ('nom', 'email', 'date_add', 'date_update', 'status')

            # Liste des champs à partir desquels nous pourrons filtrer les entrées
            list_filter = ('nom', 'email')

            # Configuration du champ de recherche
            search_fields = ('nom', 'email')

            # Configuration de l'affichage des champs de type many2many
            filter_horizontal = ('tag', )

            # Permet de filtrer par date de façon intuitive
            date_hierarchy = 'date_add'

            # Ajout de lien sur les noms pour accéder aux détails
            list_display_links = ['nom']

            # Tri par défaut du tableau
            ordering = ['date_add']

            # Créer une pagination (10 éléments par page)
            list_per_page = 10

            # rendre des champs editable depuis la liste d'affichage
            list_editable = ('nom', 'email',)

            fieldsets = [
                ('Info Contact', {'fields': ['nom', 'email', 'message']}),
                ('Standare', {'fields': ['status']})
            ]

            def images_view(self, obj):
                '''
                    Permet d'avoir un aperçu des images
                '''
                return mark_safe('<img src="{obj.image.url}" style="height:50px; width:100px">'.format(url=obj.image.url))

            images_view.short_description = 'Aperçu des images' # Titre de l'onglet dans l'admin


        # Changer le titre de l'administration
        admin.site.site_header = 'Mon Admin'

        # Titre du site à la page d'acceuil de l'admin
        admin.site.index_title = 'my web site Admin'
        
        # Titre du site
        admin.site.site_title = 'my web site'

        # Rendre des action accessible dans toute l'administration
        admin.site.actions = ('liste', 'des', 'actions')

        # Ajouter une action dans toute l'admin
        admin.site.add_action(mon_action, 'titre_de_mon_action')

        # Definir l'attribut date_hierarchy pour toute l'admin
        admin.site.date_hierarchy = 'date_add'
    ```

## Création d'inlines

```Python

    # Peut hériter de admins.TabulareInline ou de admin.StackedInline
    class TestInline(admins.TabulareInline)
        model = models.ExModel
        extra = 1

    class TestInline(admin.StackedInline):
        model = models.ExModel
        extra = 1

    # utilisation
    class UtilisationAdmin(admin.ModelAdmin):
        inlines = [TestInline]
```

## Rendre des champs non modifiables

```Python

    # Pour cela il faut ajouter l'attribut suivant en indiquant les champs concernés
    readonly_fields = ['champs', 'non', 'modifiables']

    # La redéfinition de cette méthode empêche l'ajout de nouvelles entrées en retirant le bouton qui permettait cela
    def has_add_permission(self, request):
        return False
```

## Création d'actions

```Python
    class MyModelAdmin(admin.ModelAdmin):
        ...
        
        actions = ["activate", "deactivate"]

        def deactivate(self, request, queryset):
            queryset.update(status=False)

            # Message a afficher a l'utilisateur après réalisation de l'action
            self.message_user(request, "Désactivation(s) effectué(s)")

        # Renommage de l'action de manière plus esthétique
        deactivate.short_description = "Désactiver les éléments sélectionnés"

        def activate(self, request, queryset):
            queryset.update(status=True)
            self.message_user(request, "Activation(s) effectué(s)")
        activate.short_description = "Activer les éléments sélectionnés"
```
