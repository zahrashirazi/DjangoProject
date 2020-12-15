from .views import *
from django.urls import path, include

urlpatterns = [
    path('login', login_page_view, name='LoginPage'),
    path('logout', logout_page_view, name='LogoutPage'),
    path('register', signup_page_view, name='RegisterPage'),
    path('activate/<str:token>', signup_page_view, name='ActivatePage'),
    path('payment', payment_page_view, name='PaymentPage'),
    path('panel', user_panel_main_page_view, name='RegisterPage'),

]
