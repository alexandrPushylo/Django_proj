from django.shortcuts import render, redirect
#from django.contrib.admin import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def index(request):
    return render(request, "app1/homePage.html")

def signup(request):
        return render(request,"app1/signup.html")

def signin(request):
        return render(request,"app1/signin.html")

def sucsignup(request):
        return render(request,"app1/ssign.html")

@login_required
def myaccount(request):
      
       # uname=models.User.objects.get(username=USER)
        uname=request.user
        
        
        return render(request,"app1/myaccount.html",{'UserName':uname})

def reg_user(request):
    if request.method=="POST":
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
                reg_form.save()
                return HttpResponse("app1/homePage.html")
    else: 
        reg_form = UserCreationForm()
    return render(request,'app1/signup.html',{'reg_form':reg_form})
        

def user_logout(request):
        logout(request)
        return redirect('/')














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