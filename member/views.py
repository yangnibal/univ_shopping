from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import LoginForm

def login(request):
    if request.method == "POST":
        login = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'error': 'error'})
    else:
        login = LoginForm()
    return render(request, 'user/login.html', {'login': login})

def logout(request):
    auth.logout(request)

    return redirect('home')

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
        else:
            return render(request, 'user/signuperror.html', {'error', '비밀번호가 일치하지 않습니다.'})
        return render(request, 'user/signup.html', {})
    return render(request, 'user/signup.html', {})


# Create your views here.
