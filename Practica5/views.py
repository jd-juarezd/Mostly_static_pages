# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.http import HttpResponse

def home(request):
    
    return render_to_response('home.html')
    
def contact(request):
    
    return render_to_response('contact.html')

def about(request):
    
    return render_to_response('about.html')