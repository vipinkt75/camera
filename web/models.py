from django.db import models

# Create your models here.


class Product (models.Model):
    name = models.CharField(max_length=100)
    price=models.FloatField()
    image=models.ImageField(upload_to='prodect_image')


class form(models.Model):
    name= models.CharField(max_length=20)
    message= models.CharField(max_length=40)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=50)


    def __str__(self):
        return self.name

    
class Product (models.Model):
    name = models.CharField(max_length=100)
    price=models.FloatField()
    image=models.ImageField(upload_to='prodect_image')