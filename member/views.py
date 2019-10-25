from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import LoginForm

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'user/login.html', {'error': 'email or password is not correct'})
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], 
                password = request.POST['password1'],
                email = request.POST['email']
            )
            user.save()
            auth.login(request, user)
            return redirect('login')
        return render(request, 'user/signup.html', {})
    return render(request, 'user/signup.html', {})
# Create your views here.
