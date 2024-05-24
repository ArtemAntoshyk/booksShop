from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart
# from orders.models import Order, OrderItem

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        print(request.POST)  # Вивід вмісту POST-запиту для перевірки
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                session_key = request.session.session_key
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(client=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return redirect(redirect_page)

                return redirect('main:index')
            else:
                messages.error(request, "Неверное имя пользователя или пароль")
        else:
            print(form.errors)  # Вивід помилок форми для діагностики
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(client=user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    # orders = Order.objects.filter(user=request.user).prefetch_related(
    #     Prefetch(
    #         "orderitem_set",
    #         queryset=OrderItem.objects.select_related("product"),
    #     )
    # ).order_by("-id")

    context = {
        'title': 'Home - Кабинет',
        'form': form,
        # 'orders': orders,
    }
    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))