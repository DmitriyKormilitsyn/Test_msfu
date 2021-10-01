from django.shortcuts import render
from django.views.generic import ListView

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def HomeView(request):
    return render(request, "templates/home.html") 
 
#class HomeView(ListView):
#    template_name = 'home.html'