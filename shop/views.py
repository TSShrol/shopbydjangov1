from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def list_product(request,name):
    return HttpResponse(f"<h1>Інформація за переданим аргументом {name} </h1>")

def computer(request):
    return HttpResponse("<h1>Інформація про computer</h1>")

def smartphon(request):
    return HttpResponse("<h1>Інформація про smartphon</h1>")