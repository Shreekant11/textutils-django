# i have created this file shree
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
   return render(request, 'index.html')
    #return  HttpResponse("Home")

def removerpunc(request):
    return HttpResponse("removepunc")

def capitalfirst(request):
    return HttpResponse("capitalfirst")

def newlineremove(request):
    return HttpResponse("newlineremover")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")

