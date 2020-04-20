from django.db import models


class ShopDetails(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)


class Articles(models.Model):
    name = models.CharField(max_length=250)
    shop_id = models.ForeignKey(ShopDetails, on_delete=models.CASCADE)


class Users(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
