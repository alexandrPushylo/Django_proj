from django.urls import path
from app1 import views


urlpatterns = [
    path('',views.index),
    path('signup/', views.reg_user),
    path('signin/', views.signin),
    path('myaccount', views.myaccount),
    path('ssign', views.sucsignup),
    path('logout',views.user_logout),
    path('user_au/',views.user_au),

    
]