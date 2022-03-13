from django.db import models
from home.models.catagory import Catagory


class Products(models.Model):
    pid = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="media/producct/")
    delivery = models.SmallIntegerField(default='3')
    stock = models.BooleanField(default=True)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_catagories(catagory_id):
        if catagory_id:
            return Products.objects.filter(catagory=catagory_id)
        else:
            return Products.objects.all()

    def __str__(self):
        return self.title
