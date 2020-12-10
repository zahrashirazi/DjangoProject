from django.shortcuts import render


# Create your views here.
def user_panel_main_page_view(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='HomePage.html', context=context, content_type=None,
                  status=None,
                  using=None)
