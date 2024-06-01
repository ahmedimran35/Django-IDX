from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect

def home (request):
    return render(request, 'website/index.html')

def about (request):
    return render(request, 'website/about.html')

def contact (request):
    return render(request, 'website/contact.html')
