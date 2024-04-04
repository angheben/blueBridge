from django.shortcuts import render
from django.views.generic import TemplateView


class ControlView(TemplateView):
    template_name = "control.html"


def login(request):
    return render(request, template_name='login.html')


def signup(request):
    return render(request, template_name='signup.html')



"""
def index(request):
    return render(request, template_name='index.html')


def negotiate(request):
    return render(request, template_name='negotiate.html')


def about(request):
    return render(request, template_name='about.html')
"""