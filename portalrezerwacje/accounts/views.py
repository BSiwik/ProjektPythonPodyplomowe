from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from rental.models import Rental


def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse_lazy('homepage'))
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form })

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse_lazy('homepage'))
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse_lazy('homepage'))

def user_rental_views(request):
    user = request.user
    userrentals = Rental.objects.filter(user=user).order_by('start_date')
    return render(request, 'accounts/user_rental.html', {
        'userrentals': userrentals,
    })

