from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html') 

def updateform(request):
    return render(request,'updateform.html')   



