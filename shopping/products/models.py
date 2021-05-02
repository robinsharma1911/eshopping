from django.db import models

# Create your models here.


class Products_db(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_img = models.ImageField()
    Product_name = models.CharField(max_length=50)
    Product_desc = models.TextField()
    Product_price = models.FloatField()
    available = models.BooleanField(default=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.Product_name