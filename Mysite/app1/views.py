from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.http.response import HttpResponse

def index(request):
    return render(request, "app1/homePage.html")

def signup(request):
        return render(request,"app1/signup.html")



def sucsignup(request):
        return render(request,"app1/ssign.html")

@login_required(login_url='/signin/')
def myaccount(request):
        uname=request.user
        
        return render(request,"app1/myaccount.html",{'UserName':uname})


def reg_user(request):
    if request.method == "POST":
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/')
    else: 
        reg_form = UserCreationForm()

    return render(request,'app1/signup.html',{'reg_form':reg_form})
        


def user_logout(request):
        logout(request)
        return redirect('/')

def user_au(request):
        render(request,"app1/signin.html")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                if user.is_active:
                        login(request, user)
                        return redirect('/myaccount')
                else:
                        return HttpResponse('<H3>Учетная запись отключена</H3>')
        else:
                return HttpResponse('<H3>Неверный логин или пороль</H3>')
        



def signin(request):
        return render(request,"app1/signin.html")
        









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