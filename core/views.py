from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def login(request):
    return render(request, template_name='login.html')


def register(request):
    return render(request, template_name='register.html')


def negotiate(request):
    return render(request, template_name='negotiate.html')
