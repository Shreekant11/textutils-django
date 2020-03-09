# i have created this file shree
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
   return render(request, 'index.html')
    #return  HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc' , 'off')
    print(removepunc)
    print(djtext)
    analyze = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyze = ""
    for char in  djtext:
        if char not in punctuations:
            analyze = analyze+char
    params = {'purpose':'Removed Punctuations','analyzed_text':analyze}
    return render(request,'analyze.html', params)
    #analyze the text


#def capitalfirst(request):
 #   return HttpResponse("capitalfirst")

#def newlineremove(request):
 #   return HttpResponse("newlineremover")

#def spaceremove(request):
 #   return HttpResponse("spaceremove")

#def charcount(request):
 #   return HttpResponse("charcount")

