import random
import string

from django.shortcuts import render, redirect

# Create your views here.
from Authentication.models import Users, PhoneNumber
from Store.models import Cart
from Store.views import home_page_view
import requests
from django.contrib.auth import logout
from django.contrib.auth.models import User


def login_page_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number
        return redirect(home_page_view)
    else:
        if request.method == 'POST':
            number = request.POST.get('PhoneNumber')
            try:
                try:
                    number_instance = PhoneNumber.objects.get(Number=number)
                except PhoneNumber.DoesNotExist:
                    return render(request=request, template_name='LoginPage.html', context=context, content_type=None,
                                  status=None,
                                  using=None)
                user = Users.objects.get(Phone_number=number_instance).user
                password = request.POST.get('password')
                if user.check_password(raw_password=password):
                    slug = get_random_slug()
                    send_sms(number, request, slug)
                else:
                    return render(request=request, template_name='LoginPage.html', context=context, content_type=None,
                                  status=None,
                                  using=None)
            except Users.DoesNotExist:
                return render(request=request, template_name='LoginPage.html', context=context, content_type=None,
                              status=None,
                              using=None)

    return render(request=request, template_name='LoginPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def logout_page_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number
        try:
            logout(request)
        except:
            pass

    return redirect(home_page_view)


def signup_page_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number
    else:
        if request.method == "POST":
            username = request.POST.get('UserName', '')
            phone_number = request.POST.get('PhoneNumber', '')
            password = request.POST.get('Password', '')
            try:
                ins = PhoneNumber.objects.get(Number=phone_number)
                send_sms(number=phone_number, request=request, slug=ins.Token)
                return render(request=request, template_name='SignUpPage.html', context=context, content_type=None,
                              status=None,
                              using=None)
            except PhoneNumber.DoesNotExist:
                registration = Users.objects.create()
                user = User.objects.create_user(username=username, password=password)
                user.save()
                registration.user = user
                slug = get_random_slug()
                slug = send_sms(phone_number, request, slug)
                phone_number_instance = PhoneNumber.objects.create(Token=slug,
                                                                   Number=phone_number,
                                                                   user=user)
                phone_number_instance.save()
                registration.Phone_number = phone_number_instance
                registration.save()
                return redirect(login_page_view)

    return render(request=request, template_name='SignUpPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def user_panel_main_page_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number
    return render(request=request, template_name='UserPanelMainPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def get_random_slug():
    random_source = string.ascii_letters + string.digits
    slug = random.choice(string.ascii_lowercase)
    slug += random.choice(string.ascii_uppercase)
    slug += random.choice(string.digits)

    for i in range(6):
        slug += random.choice(random_source)

    password_list = list(slug)
    random.SystemRandom().shuffle(password_list)
    slug = ''.join(password_list)
    return slug


def send_sms(number, request, slug):
    data = {
        'username': '09020021211',
        'password': '1646',
        'to': str(number),
        'from': '30008666021211',
        'text': "Pleas Click The Link Below to Activate Your Login: \n {}".format(
            request.get_host() + '/user/activate/' + slug),
    }
    respond = requests.post(url='https://rest.payamak-panel.com/api/SendSMS/SendSMS', data=data).json()
    return slug


def verification(request, token, *args, **kwargs):
    context = {}
    if token:
        try:
            phone_number = PhoneNumber.objects.get(Token=token)
            phone_number.NumberOfSentNumbers = int(phone_number.NumberOfSentNumbers) + 1
            phone_number.Status = 'V'
            phone_number.save()
            return render(request=request, template_name='UserPanelMainPage.html', context=context, content_type=None,
                          status=None,
                          using=None)
        except PhoneNumber.DoesNotExist:
            return redirect(home_page_view)
