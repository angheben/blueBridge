from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def login(request):
    return render(request, template_name='login.html')


def signup(request):
    return render(request, template_name='signup.html')


def negotiate(request):
    return render(request, template_name='negotiate.html')
