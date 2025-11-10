from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import SignUpForm, SignInForm

# Create your views here.

def users_list(request):
    users = CustomUser.objects.all()
    print(users)
    return render(request, 'users_list.html', {'users': users})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if CustomUser.objects.filter(username = username):
                pass
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form':form})

def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_profile.html', {'user': user})

def delete_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('users:users_list')

def signout(request):
    ...