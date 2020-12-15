from django.contrib import admin
from .models import Category, Book, Cart, CartItem

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Cart)
