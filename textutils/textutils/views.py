# i have created this file shree
from django.http import HttpResponse
def index(request):
    return  HttpResponse("<h2>Shree</h2>")

def about(request):
    return HttpResponse("About Shree bhai")