# Create your views here.
from django.http import HttpResponse

def home(request):
    text =   "<h1>Pages#home</h1>"
    text +=  "<p>Find me in Mostly_static_pages.Practica5.views.home</p>"
    
    return HttpResponse(text)

def contact(request):
    text =   "<h1>Pages#contact</h1>"
    text +=  "<p>Find me in Mostly_static_pages.Practica5.views.contact</p>"
    
    return HttpResponse(text)

def about(request):
    text =   "<h1>Pages#about</h1>"
    text +=  "<p>Find me in Mostly_static_pages.Practica5.views.about</p>"
    
    return HttpResponse(text)