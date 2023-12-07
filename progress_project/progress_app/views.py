from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    return render(request, "contactus.html")        

def view(request, prod_id):
    context = {
        "product_to_view" : Product.objects.get(id = prod_id),
    }

    return render(request, 'view.html', context)

def createEdit(request):
    return render(request, 'create_edit.html')

def products(request):
    context = {
        'all_products' : Product.objects.all(),
    }
    return render(request, 'products.html', context)

def register(request):
    errors = Client.objects.validator(request.POST)
    if len(errors) > 0:
        for k , v in errors.items():
            messages.error(request, v)
        return redirect('/login')
    else:
        Client.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode(),
        )
        messages.success(request, 'New user added successfully, please login!')
        return redirect('/login')


def login_request(request):
    client = Client.objects.filter(email = request.POST['email'])
    if client:
        client = client[0]
        if bcrypt.checkpw(request.POST['password'].encode(), client.password.encode()):
            request.session['id'] = client.id
            return redirect('/')
        else:
            messages.error(request, 'Wrong Email or Passowrd')
            return redirect('/login')
    else:
        messages.error(request, 'Wrong Email or Passowrd')
        return redirect('/login')
    
def logout(request):
    request.session.flush()
    return redirect('/login')