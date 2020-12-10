from django.shortcuts import render


# Create your views here.
def user_panel_main_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='HomePage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def all_books_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='AllBooksPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def detail_books_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='DetailBookPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


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
