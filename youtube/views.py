from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class you(TemplateView):
    template_name = 'first.html'

class tube(TemplateView):
    template_name = 'second.html'
