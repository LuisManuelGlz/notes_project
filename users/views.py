from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationFormWithEmail, AuthenticationFormWithStyle

# Create your views here.
def signup_user(request):
    if request.method == 'POST':
        form = UserCreationFormWithEmail(request.POST)
        if form.is_valid():
            user = form.save()
            # user.set_password(user.password)
            # user.save()
            messages.success(request, f'You are registered')
            return redirect('login')
    else:
        form = UserCreationFormWithEmail()
    return render(request, 'users/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationFormWithStyle(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all-notes')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationFormWithStyle()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')