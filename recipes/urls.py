from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
