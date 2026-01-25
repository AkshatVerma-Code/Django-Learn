from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home/index.html')
    # return HttpResponse("Welcome to the Chai Aur Django Home Page!")

def about(request):
    return render(request,'about/about.html')

def contact(request):
    return HttpResponse("Contact Us at Chai Aur Django")

