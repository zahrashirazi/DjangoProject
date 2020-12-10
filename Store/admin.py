from django.contrib import admin
from .models import Category, Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
