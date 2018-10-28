from django.shortcuts import render
#from django.contrib.admin import models
from django.contrib.auth.models import User
#from django.http import HttpResponse

def index(request):
    return render(request, "app1/homePage.html")

def signup(request):
        return render(request,"app1/signup.html")

def signin(request):
        return render(request,"app1/signin.html")

def myaccount(request):
      
       # uname=models.User.objects.get(username=USER)
        uname=request.user
        fname=request
        
        return render(request,"app1/myaccount.html",{'UserName':uname,'fname':fname})

def sucsignup(request):
        return render(request,"app1/ssign.html")












def contact(request):
    return render(request,"app1/basic.html",{'values':[
        'Усли у вас остались вопросы, то задавайте их по телефону',
        '(025) 948-43-09',
        'aln@mail.com'
        ]})

'''
def empt_page(request):# empty page for "app1"
    return HttpResponse('<H3>It is page "app1"</H3>')
    '''