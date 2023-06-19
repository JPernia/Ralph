from django.db import models

from apps.base.models import BaseModel


# Create your models here.
class Product(BaseModel):

    cod = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['create_date']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Almacen(BaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    ubicacion =  models.CharField(max_length=255, blank=True, null=True)



class Seriales(models.Model):

    cod_prod =  models.ManyToManyField(Product)
    almacen = models.ManyToManyField(Almacen)
    serial = models.CharField(max_length=255, blank=True, null=True)