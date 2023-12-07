from django.db import models
import re


class ClientManager(models.Manager):
    def validator(self,POST_data):
        errors = {}
        if len(POST_data['first_name']) < 4:                                        #first name length
            errors['first_name'] = 'your first name should be at least 4 characters'

        if len(POST_data['last_name']) < 4:                                         #last name length
            errors['last_name'] = 'your last name should be at least 4 characters'

        if Client.objects.filter(email = POST_data['email']):                         #account already exists? unique email
            errors['account_exsits'] = 'email address used for another account!'

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  #email syntax valid?
        if not email_regex.match(POST_data['email']):
            errors['vaild_email'] = "Invalid email address!"

        if len(POST_data['password']) < 8:                                          #password length 8
            errors['password_len'] = 'your password should be at least 8 characters'

        if POST_data['password'] != POST_data['password2']:                        #password confirmation
            errors['password_confirm'] = 'password and password confirmation does not match!'
        return errors

class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()
    #user_orders
    def __str__(self):
        return self.first_name
# ########################################################


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField()
    image = models.TextField() 
    datasheet = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #order_product = 
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
    # client = models.OneToOneField(Client, related_name="client_service", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     
