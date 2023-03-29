from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home_view(request):
    if request.method == 'POST':
        user_id = request.POST['email_user']
        user_passwd = request.POST['passwd_user']
        user = authenticate(request, username=user_id, password=user_passwd)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.warning(request, "Email or Password is not correct! Try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})  

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out!")
    return redirect('home')