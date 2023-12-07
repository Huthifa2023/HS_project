from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('login', views.login),
    path('aboutus', views.aboutus),
    path('contactus', views.contactus),


    path('view/<int:prod_id>', views.view),


    path('products', views.products),
    path('create/edit', views.createEdit),


    path('register', views.register),
    path('login_request', views.login_request),
    path('logout', views.logout),


    path('order_product/<int:prod_id>', views.order_product),
]
