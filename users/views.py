from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.phonenumber import PhoneNumber

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("order:index"))

    if request.method == 'POST':
        try:
            phone = PhoneNumber.from_string(request.POST["phone"], region="IN")
            if phone.is_valid():
                try:
                    user = authenticate(request, username=phone.national_number, password=str(phone.national_number))
                except:
                    user = None
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse("order:index"))
                else:
                    return render(request, "users/login.html", {"message": "You are not registered."})
            else:
                return render(request, "users/login.html", {"message": "Enter a valid Indian phone number."})
        except:
            return render(request, "users/login.html", {"message": "Enter a valid Indian phone number."})
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("order:index"))

    if request.method == 'POST':
        try:
            phone = PhoneNumber.from_string(request.POST["phone"], region="IN")
            if not phone.is_valid():
                return render(request, "users/register.html", {"message": "Enter a valid Indian phone number."})
        except:
            return render(request, "users/register.html", {"message": "Enter a valid Indian phone number."})

        name = request.POST["name"]
        if not name:
            return render(request, "users/register.html", {"message": "Enter your name."})
        
        try:
            user = User.objects.get(username=phone.national_number)
        except:
            user = None

        if user is None:
            try:
                user = User.objects.create_user(username=phone.national_number, password=str(phone.national_number))
                user.first_name = name
                user.save()
            except:
                return render(request, "users/register.html", {"message": "Registration failed."})

            login(request, user)
            return HttpResponseRedirect(reverse("order:index"))
        else:
            return render(request, "users/register.html", {"message": "You are already registered."})   

    return render(request, "users/register.html")