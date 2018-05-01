'''
Created on May 1, 2018

@author: devals
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]