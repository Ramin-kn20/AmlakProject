from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('AMLAKAPP:list')
    else:
        form = UserCreationForm()
    return render(request, 'user/user_register.html', {'FORM': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('AMLAKAPP:list')
    else:
        form = AuthenticationForm()
    return render(request, 'user/user_login.html', {'FORM': form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('AMLAKAPP:list')