from pyexpat import model
from django.db import models
from django.forms import IntegerField
from home.models.catagory import Catagory
#from home.models.subcatagory import subCatagory


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="media/producct/")
    delivery = models.SmallIntegerField(default='3')
    stock = models.BooleanField(default=True)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_catagories(catagory_id):
        if catagory_id:
            return Product.objects.filter(catagory=catagory_id)
        else:
            return Product.objects.all()

    def __str__(self):
        return self.name
