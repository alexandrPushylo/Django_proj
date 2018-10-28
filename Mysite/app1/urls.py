from django.urls import path
from app1 import views


urlpatterns = [
    path('',views.index),
    path('signup', views.signup),
    path('signin', views.signin),
    path('myaccount', views.myaccount),
    path('ssign', views.sucsignup),

    
]