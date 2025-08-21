from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.users.models import User

def user_register_view(request):
    if request.method == 'GET':
        return render(request, 'users/registration.html')

    # Обязательные поля
    username = request.POST.get("username")
    password = request.POST.get("password")
    password2 = request.POST.get("password2")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    phone_number = request.POST.get("phone_number")

    # Необязательные поля
    gender = request.POST.get("gender")
    shift = request.POST.get("shift")
    study_lang = request.POST.get("study_lang")
    address = request.POST.get("address")
    blood_group = request.POST.get("blood_group")
    bio = request.POST.get("bio")

    # Проверка обязательных полей
    if not all([username, password, password2, first_name, last_name, phone_number]):
        messages.error(request, 'Iltimos, barcha majburiy maydonlarni to‘ldiring.')
        return redirect('register')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Bunday username allaqachon mavjud.')
        return redirect('register')

    if password != password2:
        messages.error(request, 'Parollar mos emas.')
        return redirect('register')

    # Создание пользователя
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        gender=gender,
        shift=shift,
        study_lang=study_lang,
        address=address,
        blood_group=blood_group,
        bio=bio
    )

    login(request, user)
    messages.success(request, "Ro'yxatdan o'tdingiz va tizimga kirdingiz!")
    return redirect('login')
