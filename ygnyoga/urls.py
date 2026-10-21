from django.urls import path
from .views import *

urlpatterns = [
    path('',welcome,name = 'yoga_welcome'),
    path('about/',about,name = 'yoga_about')
]