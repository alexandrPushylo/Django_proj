from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "app1/homePage.html")

def contact(request):
    return render(request,"app1/basic.html",{'values':[
        'Усли у вас остались вопросы, то задавайте их по телефону',
        '(025) 948-43-09',
        'aln@mail.com'
        ]})

def empt_page(request):# empty page for "app1"
    return HttpResponse('<H3>It is page "app1"</H3>')

