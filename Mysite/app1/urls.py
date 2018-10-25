from django.urls import path
from app1.views import hello

urlpatterns = [
    path('', hello),
    
]