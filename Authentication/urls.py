from .views import *
from django.urls import path, include

urlpatterns = [
    path('login', login_page_view, name='LoginPage'),
    path('logout', logout_page_view, name='LogoutPage'),
    path('register', signup_page_view, name='RegisterPage'),
    path('activate/<str:token>', verification, name='ActivatePage'),
    path('payment', payment_page_view, name='PaymentPage'),
    path('panel', signup_page_view, name='UserPanel'),

]
