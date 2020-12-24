from .views import *
from django.urls import path, include

urlpatterns = [
    path('', home_page_view, name='HomePage'),
    path('books', all_books_page_view, name='AllBooksPage'),
    path('books/<str:book_id>', detail_books_page_view, name='DetailBookPage'),
    path('books/add/<int:book_id>', add_to_cart_view, name='AddToCart'),
    path('about', contact_us_page_view, name='ContactUsPage'),
    path('payment', payment_page_view, name='PaymentPage'),
    path('serch', search_view, name='SearchingPage'),

]
