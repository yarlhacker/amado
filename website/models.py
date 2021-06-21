from django.db import models


class Base(models.Model):

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField()

    class Meta:

        abstract = True



# Create your models here.
