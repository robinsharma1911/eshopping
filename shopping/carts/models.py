from django.db import models

from logs import models as logsmodels
from products import models as productsmodels
# Create your models here.

class carts_db(models.Model):
    order_no = models.AutoField(primary_key=True)
    user_email =models.ForeignKey(logsmodels.log_db,on_delete=models.CASCADE)
    product_id =models.ForeignKey(productsmodels.Products_db,on_delete=models.CASCADE)  

    def __str__(self):
        return self.user_email