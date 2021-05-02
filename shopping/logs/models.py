from django.db import models

# Create your models here.

class log_db(models.Model):
    email = models.EmailField(primary_key=True,unique=True,max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email