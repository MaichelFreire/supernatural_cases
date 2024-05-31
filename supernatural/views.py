from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return HttpResponse('home')

def cases(response):
    return HttpResponse('cases')
