from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .forms import UserLoginForm, UserRegisterForm, UserProfileForm, CartForm

from main.models import Product, Basket



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'title': 'Store',
    }
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:bardStore'))
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'title': 'Store-Login'
    }

    return render(request, 'users/login.html', context)



@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:bardStore'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
        'title': 'Store-profile',
    }
    return render(request, 'users/profile.html', context)


@login_required
def cart(request):
    baskets = Basket.objects.filter(user=request.user)
    total_sum_products = sum(basket.sum() for basket in baskets)
    discount_total_sum = sum(basket.discount_sum() for basket in baskets)
    if discount_total_sum == 0:
        total_sum = 0
    else:
        total_sum = discount_total_sum + 200
    context = {
        'baskets': baskets,
        'total_sum_products': total_sum_products,
        'discount_total_sum': discount_total_sum,
        'total_sum': total_sum,
    }

    return render(request, 'users/cart.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            size = form.cleaned_data['size']
            quantity = form.cleaned_data['quantity']
            baskets = Basket.objects.filter(user=request.user, product=product, size=size)

            if baskets.exists():
                basket = baskets.first()
                basket.quantity += quantity
                basket.save()
            else:
                Basket.objects.create(user=request.user, product=product, size=size, quantity=quantity)

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = CartForm()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])