from django.db import models

# Create your models here.
class Model_Forms(models.Model):
    name= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    company= models.CharField(max_length=50)
    message= models.CharField(max_length=100, default='')
    identifier = models.CharField(max_length=50, default='')
    date = models.CharField(max_length=50, default=False)
    terms = models.BooleanField(max_length=50, default=False)
