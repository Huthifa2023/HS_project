from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Specification)
admin.site.register(Order)
admin.site.register(Service)
