from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    review = models.TextField()
