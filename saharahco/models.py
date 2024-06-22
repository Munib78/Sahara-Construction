from django.db import models

# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(max_length= 30)

    email = models.EmailField(max_length=40, unique=True)

    message = models.TextField()

    date = models.DateField()


class Services(models.Model):
    img = models.ImageField(upload_to='static/service_img',  blank=True, null=True)

    service_name = models.CharField(max_length=35, default='Default Service Name')

    service_des = models.TextField(null=True)


