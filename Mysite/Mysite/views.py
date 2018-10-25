from django.http import HttpResponse


def empt_page(request):
    return HttpResponse('<H3>It is Home page</H3>')