from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField()
    image = models.TextField() 
    datasheet = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Specification(models.Model):
    width = models.IntegerField()
    height = models.IntegerField() 
    voltage = models.IntegerField() 
    indoor_outdoor = models.CharField(max_length=45)
    product = models.OneToOneField(Product, related_name="specification",on_delete=models.CASCADE) 

class Order(models.Model):
    product = models.ManyToManyField(Product, related_name="order_product")
    client = models.ForeignKey(Client, related_name="user_orders", on_delete=models.CASCADE) 


class Service(models.Model):
    name = models.CharField(max_length=45) 
    description = models.TextField()
    image = models.TextField()
    client = models.OneToOneField(Client, related_name="client_service", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     
      