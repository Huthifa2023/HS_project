from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def main(request):
    if 'id' in request.session:
        current_user = Client.objects.get(id = request.session['id'])
        context = {
            'all_services' : Service.objects.all(),
            'all_user_orders' : current_user.user_orders.all(),
            'current_user' : current_user,
        }
        return render(request, 'main.html', context)
    else:
        context = {
            'all_services' : Service.objects.all(),
        }
    return render(request, 'main.html', context)




def login(request):
    if 'id' in request.session:
        current_user = Client.objects.get(id = request.session['id'])
        context = {
        'all_user_orders' : current_user.user_orders.all(),
        'current_user' : current_user,  
        }
        return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')




def aboutus(request):
    if 'id' in request.session:
        current_user = Client.objects.get(id = request.session['id'])
        context = {
            'all_user_orders' : current_user.user_orders.all(),
            'current_user' : current_user,
        }
        return render(request, "aboutus.html", context)
    else:
        return render(request, "aboutus.html")





def contactus(request):
    if 'id' in request.session:
        current_user = Client.objects.get(id = request.session['id'])
        context = {
            'all_user_orders' : current_user.user_orders.all(),
            'current_user' : current_user
        }
        return render(request, "contactus.html", context)
    else:
        return render(request, "contactus.html")      





def view(request, prod_id):
    if 'id' in request.session:
        current_user = Client.objects.get(id = request.session['id'])
        context = {
            "product_to_view" : Product.objects.get(id = prod_id),
            'all_user_orders' : current_user.user_orders.all(),
            'current_user' : current_user,
        }
        return render(request, 'view.html', context)
    else:
        context = {
            "product_to_view" : Product.objects.get(id = prod_id),
        }
        return render(request, "view.html", context)      




def createEdit(request):
    return render(request, 'create_edit.html')

def products(request):
    if 'id' in request.session:
        current_user = Client.objects.get(id = request.session['id'])
        context = {
            'all_products' : Product.objects.all(),
            'all_user_orders' : current_user.user_orders.all(),
            'current_user' : current_user,
        }
        return render(request, 'products.html', context)    
    else:
        context = {
            'all_products' : Product.objects.all(),
        }
    return render(request, 'products.html', context)




def order_product(request, prod_id):
    current_user = Client.objects.get(id = request.session['id'])
    prod = Product.objects.get(id = prod_id)

    new_order = Order(
        client = current_user,
    )
    new_order.save()
    new_order.product.add(prod)
    return redirect('/products')



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
    del request.session['id']
    return redirect('/login')

def checkout(request):
    if 'id' in request.session:
        current_user = Client.objects.get(id = request.session['id'])
        current_user.user_orders.all().delete()
        return redirect('/')
    else:
        return redirect('/login')