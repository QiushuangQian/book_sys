from django.urls import path
from . import views

urls_patterns = [
    path('',views.index,name='index')
]