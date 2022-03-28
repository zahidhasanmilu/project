from django.db import models

# Create your models here.


class Order(models.Model):
    oid = models.IntegerField(primary_key=True, auto_created=True)
    pid = models.IntegerField()
    uid = models.IntegerField()
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    town = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    price = models.IntegerField()
    comment = models.TextField()
    qty = models.SmallIntegerField()

    def __str__(self):
        return str(self.oid)
