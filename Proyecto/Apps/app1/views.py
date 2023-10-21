from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required

def salir(request):
    logout(request)
    return redirect('/')

def home(request): 
    return render(request, 'home.html')

from .models import Fact 
# Create your views here. 


#p17, borrar pa abajo

from django.http import HttpResponse 
from .models import Fact 