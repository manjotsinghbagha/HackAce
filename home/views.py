from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def uploadcat(request):
    return render(request, 'home/uploadcat.html')

def uploaddog(request):
    return render(request, 'home/uploaddog.html')

def about(request):
    return render(request, 'home/aboutus.html')

def dogdescription(request):
    return render(request, 'home/dogdescription.html')

def catdescription(request):
    return render(request, 'home/catdescription.html')    

