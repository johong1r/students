from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if not username:
            messages.error(request, "Имя пользователя не может быть пустым")
            return redirect('register')

        if password != password2:
            messages.error(request, "Пароли не совпадают")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким именем уже существует")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        messages.success(request, "Регистрация успешна! Теперь войдите в систему.")
        return redirect('login')

    return render(request, "accounts/register.html")


def login_custom(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("login")  
        else:
            messages.error(request, "Неверное имя пользователя или пароль")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из системы")
    return redirect("login")

