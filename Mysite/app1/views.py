from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "base.html")





'''
# Create your views here.
def index1(request):
    return HttpResponse('<H3>Hello, world!</H3>')
'''