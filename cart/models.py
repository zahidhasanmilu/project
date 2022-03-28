from django.db import models


# Create your models here.


class cartItem(models.Model):
    cid = models.IntegerField(primary_key=True, auto_created=True)
    uid = models.IntegerField()
    pid = models.IntegerField()
    qty = models.SmallIntegerField()
    in_cart = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cid)
