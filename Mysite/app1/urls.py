from django.urls import path, re_path
from django.views.generic import TemplateView
from app1.views import LogoutView, UserRegistrationForm, LoginFormView, UserProfile


urlpatterns = [
    path('', TemplateView.as_view(template_name='app1/homePage.html')),
    path('logout', LogoutView.as_view()),
    path('signup/', UserRegistrationForm.as_view()),
    path('signin/', LoginFormView.as_view()),
    path('', TemplateView.as_view(template_name='app1/homePage.html')),
    re_path(r'^accounts/(?P<id>\d+)$', UserProfile),
    
 #   path('accounts/myaccount', UserProfile),
  #  path('', index),
 #   path('signup/', reg_user),
 #   path('signin/', signin),
    
 #   path('ssign', sucsignup),
 #   path('logout',user_logout),
    
 ##   path('user_au/',user_au),
 #  re_path(r'^accounts/(?P<id>\d+)$', views.UserProfile),
    
]