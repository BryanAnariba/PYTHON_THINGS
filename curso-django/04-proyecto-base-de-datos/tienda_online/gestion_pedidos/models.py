from django.db import models

class Client(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Article(models.Model):
    articleName = models.CharField(max_length=60)
    articleSection = models.CharField(max_length=40)
    articlePrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "articleName: {}, articleSection: {}, articlePrice: {}".format(self.articleName, self.articleSection, self.articlePrice)


class Order(models.Model):
    orderNumber = models.IntegerField()
    orderDate = models.DateField()
    orderDelivered = models.BooleanField()