from django.shortcuts import render


# Create your views here.
def login_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='LoginPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def signup_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='SignUpPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def payment_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='PaymentPage.html', context=context, content_type=None,
                  status=None,
                  using=None)


def user_panel_main_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='UserPanelMainPage.html', context=context, content_type=None,
                  status=None,
                  using=None)
