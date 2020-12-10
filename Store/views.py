from django.http import response
from django.shortcuts import render

# Create your views here.
from Store.models import Book


def home_page_view(request, *args, **kwargs):
    context = {}
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
    return render(request=request, template_name='ContactUs.html', context=context, content_type=None,
                  status=None,
                  using=None)


def payment_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='PaymentPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def payment_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='PaymentPage.html', context=context, content_type=None,
                  status=None,
                  using=None)
