from .views import *
from django.urls import path, include

urlpatterns = [
    path('/login', login_page_view, name='LoginPage'),
    path('/logout', logout_page_view, name='LogoutPage'),
    path('/register', login_page_view, name='RegisterPage'),
    path('/payment', login_page_view, name='RegisterPage'),
    path('/panel', login_page_view, name='RegisterPage'),

]
