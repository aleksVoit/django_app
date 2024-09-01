from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup_user(request):
    if request.user.is_authenticated:
        return redirect(to='quoteapp:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'users/signup.html', context={'form': form})
    else:
        return render(request, 'users/signup.html', context={'form': RegisterForm()})


def login_user(request):
    if request.user.is_authenticated:
        return redirect(to='quoteapp:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])

        if user is None:
            messages.error(request, "Username or password don't match")
            return redirect(to='users:login')

        login(request, user)

        return redirect(to='quoteapp:main')

    return render(request, 'users/login.html', context={'form': LoginForm()})


@login_required()
def logout_user(request):
    logout(request)
    return redirect(to='quoteapp:main')
