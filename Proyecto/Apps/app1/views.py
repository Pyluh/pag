from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required

def home(request): 
    return render(request, 'home.html')

from .models import Fact 
# Create your views here. 


def home(request): 
    lista = Fact.objects.all() 
    context = { 
        "listafacts" : lista 
} 
    return render(request, 'home.html',context)


#p17

from django.shortcuts import render 
from django.http import HttpResponse 
from .models import Fact 
from .services.getFact import get_fact 
 
# Create your views here. 
 
def home(request): 
    fact_data = get_fact()  # Obtener el diccionario con el hecho y la longitud 
    if fact_data: 
        new_fact = Fact.objects.create( 
            fact_text=fact_data['fact_text'], 
            length=fact_data['length'] 
        ) 
    new_fact.save() 
    lista = Fact.objects.all() 
    context = { 
        "listafacts" : lista 
    } 
    return render(request, 'home.html', context)

#paso 3 de borrar o editar
from django.shortcuts import redirect 
... 
def eliminarFact(request,fact_text): 
    fact=Fact.objects.get(fact_text=fact_text) 
    fact.delete() 
    return redirect('/') 
 
def edicionFact(request, fact_text): 
    fact = Fact.objects.get(fact_text=fact_text) 
    return render(request, 'edicionFact.html', {'fact_text': fact_text, 'fact': fact}) 
 
 
def editarFact(request, fact_text): 
    if request.method == 'POST': 
        fact_txt = request.POST['txtFact'] 
        fact = Fact.objects.get(fact_text=fact_text) 
        fact.fact_text = fact_txt 
        print(fact.fact_text) 
        fact.save() 
        return redirect('/') 
    else: 
        # Manejar el caso de solicitud no válida, si es necesario 
        pass