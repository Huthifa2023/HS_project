from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('login', views.login),
    path('aboutus', views.aboutus),
    path('contactus', views.contactus),
    path('view', views.view),
    path('create/edit', views.createEdit),


    path('register', views.register),
    path('login_request', views.login_request),
    path('logout', views.logout),
]
