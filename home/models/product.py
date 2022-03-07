from django.db import models
from home.models.catagory import Catagory
#from home.models.subcatagory import subCatagory

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="media/producct/")
    
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
    def __str__(self):
        return self.name