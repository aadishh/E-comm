from django.contrib import messages
from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User


def home(request):
    return render(request, 'app/home.html')


def product_detail(request):
    return render(request, 'app/productdetail.html')


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request):
    return render(request, 'app/mobile.html')


def login(request):
    return render(request, 'app/login.html')


def customerregistration(request):
    return render(request, 'app/customerregistration.html')


def checkout(request):
    return render(request, 'app/checkout.html')


def sign(request):
    if request.method == "POST":
        inputEmail4 = request.POST.get('inputEmail4')
        inputPassword1 = request.POST.get('inputPassword1')
        inputPassword2 = request.POST.get('inputPassword2')
        if inputPassword1 != inputPassword2:
            return HttpResponse("password is not same")
        my_user = User.objects.create_user(
            inputEmail4, inputPassword1,inputPassword2)
        my_user.save()
        messages.success(request, 'User has been created..')
        return render(request, 'app/login.html')
    else:
        return render(request, 'app/customerregistration.html')
