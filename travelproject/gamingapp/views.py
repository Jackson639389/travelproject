from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Place, team


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid login")
            return redirect('gaming:login')

    return render(request, 'login.html')


def web(request):
    obj = Place.objects.all()
    obj1 = team.objects.all()
    return render(request, "index.html", {'output': obj, 'result': obj1})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('gaming:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('gaming:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)

                user.save()
                return redirect('gaming:login')

        else:
            print("password did not matched")
            return redirect('gaming:register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
