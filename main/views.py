from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return render(requests, 'main/index.html')

def contact(requests):
    return render(requests, 'main/contact.html')

def blog(requests):
    return render(requests, 'main/blog.html')

def portfolio(requests):
    return render(requests, 'main/portfolio.html')

def services(requests):
    return render(requests, 'main/services.html')
