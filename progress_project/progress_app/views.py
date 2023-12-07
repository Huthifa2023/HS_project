from django.shortcuts import render, redirect

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    return render(request, "contactus.html")        

def view(request):
    return render(request, 'view.html')

def createEdit(request):
    return render(request, 'create_edit.html')