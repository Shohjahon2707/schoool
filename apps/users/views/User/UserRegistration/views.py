from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.users.models import User

def user_register_view(request):
    if request.method == 'GET':
        return render(request, 'users/registration.html')

    username = request.POST.get("username")
    password = request.POST.get("password")
    password2 = request.POST.get("password2")

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Bunday username allaqachon mavjud.')
        return redirect('register')

    if password != password2:
        messages.error(request, 'Parollar mos emas.')
        return redirect('register')

    user = User.objects.create_user(username=username, password=password)
    login(request, user)  # Автоматический вход
    messages.success(request, "Ro'yxatdan o'tdingiz va tizimga kirdingiz!")
    return redirect('home')
