from django.urls import path
from app1.views import index, empt_page,contact

urlpatterns = [
    path('', index),
    path('app1/', empt_page),
    path('contact/', contact),
]