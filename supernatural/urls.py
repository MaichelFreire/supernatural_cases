from django.urls import path
from django.http import HttpResponse
from .views import home, cases

urlpatterns = [
    path('', home),
    path('cases/', cases)
]