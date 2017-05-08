from django.db import models

# Create your models here.

class Customer(models.Model):

    userId=models.IntegerField()
    userName=models.CharField(max_length=40)

