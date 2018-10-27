from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "app1/homePage.html")


def empt_page(request):
    return HttpResponse('<H3>It is page "app1"</H3>')

