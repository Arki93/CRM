from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from .models import Record

def home(request):
    records = Record.objects.all()
    
    if request.method == "POST":
        username = request.POST["username"]
        passwd = request.POST["password"]
        user = authenticate(request, username=username, password=passwd)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("home")
        else:
            messages.warning(request, "Email or Password is not correct! Try again.")
            return redirect("home")
    else:
        return render(request, "home.html", {'records':records})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out!")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            passwd = form.cleaned_data["password1"]
            user = authenticate(username=username, password=passwd)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect("home")
    else:
        form = SignupForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})

def data_record(request, pk):
    if request.user.is_authenticated:
        rec_data = Record.objects.get(id=pk) 
        return render(request, "data_record.html", {"rec_data": rec_data})
    else:
        messages.warning(request, "You are not logged in!")
        return redirect("home")  
