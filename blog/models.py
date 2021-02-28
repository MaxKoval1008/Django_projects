from django.db import models


class Review(models.Model):
    username = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=15, null=None)
    prise = models.FloatField()
    image = models.ImageField()
    amount = models.IntegerField()
    options = models.TextField()
    reviews = models.ManyToManyField(Review, null=None, blank=None)

    def __str__(self):
        return self.name


class Basket(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    purchases = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.name}`s Basket'

