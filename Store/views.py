from django.http import response
from django.shortcuts import render, redirect

# Create your views here.

from Store.models import Book, Cart, CartItem


def home_page_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number

    books_model = Book.objects.all()[:4]
    books = []
    for book in books_model:
        books.append(book)

    context['Books'] = books

    return render(request=request, template_name='HomePage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def all_books_page_view(request, *args, **kwargs):
    context = {}

    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number

    books_model = Book.objects.all()
    books = []
    for book in books_model:
        books.append(book)

    context['Books'] = books
    return render(request=request, template_name='AllBooksPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def detail_books_page_view(request, book_id, *args, **kwargs):
    context = {}

    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number

    try:
        book = Book.objects.get(pk=book_id)
        context['Book'] = book

        return render(request=request, template_name='DetailBookPage.html', context=context, content_type=None,
                      status=None,
                      using=None)
    except:
        response.status_code = 404
        return response


def contact_us_page_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        try:
            number = Cart.objects.get(user=request.user).number
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number

    return render(request=request, template_name='ContactUs.html', context=context, content_type=None,
                  status=None,
                  using=None)


def payment_page_view(request, *args, **kwargs):
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                cart = Cart.objects.get(user=request.user)
                cart.number = 0
                cart.Item.clear()
                cart.save()
                context['ALERT'] = 'Your payment paid successfully.'
            except:
                pass

        books = []
        try:
            number = Cart.objects.get(user=request.user).number
            items = Cart.objects.get(user=request.user).Item.all()
            for item in items:
                books.append(item)
        except Cart.DoesNotExist:
            number = 0
        context['Number'] = number
        context['Books'] = books

    return render(request=request, template_name='PaymentPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def add_to_cart_view(request, book_id, *args, **kwargs):
    context = {}
    if book_id:
        if request.user.is_authenticated:
            try:
                try:
                    cart = Cart.objects.get(user=request.user)
                except Cart.DoesNotExist:
                    cart = Cart.objects.create(user=request.user)
                book = Book.objects.get(pk=int(book_id))
                item, created = CartItem.objects.get_or_create(Book=book)
                item.Quantity += 1
                price = int(item.Quantity) * int(book.Price)
                item.Final_Price = str(price)
                item.save()
                cart.Item.add(item)
                cart.save()
                cart.number += 1
                cart.save()
                try:
                    number = Cart.objects.get(user=request.user).number
                except Cart.DoesNotExist:
                    number = 0
                context['Number'] = number
                return redirect(payment_page_view)
            except:
                raise
    try:
        number = Cart.objects.get(user=request.user).number
    except Cart.DoesNotExist:
        number = 0
    context['Number'] = number
    return redirect(home_page_view)


def search_view(request, *args, **kwargs):
    context = {}
    query = request.GET.get('query', '')
    if query != '':
        result = []
        for keyword in query.split(' '):
            result += list(Book.objects.filter(Title__icontains=keyword))
            result += list(Book.objects.filter(Summary__icontains=keyword))
        books = []
        for book in result:
            books.append(book)
        books = list(set(books))
        context['Books'] = books

    return render(request=request, template_name='SearchedBooksPage.html', context=context, content_type=None,
                  status=None,
                  using=None)
