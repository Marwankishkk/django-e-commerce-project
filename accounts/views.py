from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(
                request, 'Invalid login credentials. Please try again.')
            return redirect('login')

    else:
        return render(request, "accounts/login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        Email = request.POST["email"]
        Password = request.POST["password"]
        user = User.objects.create_user(
            username=username, password=Password, email=Email)
        user.save()
        return redirect('/')
    else:
        return render(request, "accounts/register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
