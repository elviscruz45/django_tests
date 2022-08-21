from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

def busqueda_productos(request):
    return render(request,"busqueda_productos.html")


def buscar(request):
#    mensaje="Articulo buscado: %r" %request.GET["prd"]
#    return HttpResponse(mensaje)    
    if request.GET["prd"]:
        #mensaje="Articulo buscado: %r" %request.GET["prd"]

        producto=request.GET["prd"]
        
        if len(producto) >20:
            mensaje="texto de busqueda demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request,"resultados.html",{"articulos":articulos,"query":producto})
        
    
    else:
        mensaje="No has introducido nada"
    return HttpResponse(mensaje)


def contacto(request):
    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            send_mail(infForm["asunto"],infForm["mensaje"],infForm.get("email",""),["elviscruz45@gmail.com"],)
            return render(request,"gracias.html")
    
    else:
        miFormulario=FormularioContacto()
    return render(request,"formulario_contacto.html",{"form":miFormulario})            

        #subject=request.POST["asunto"]
        #message=request.POST["mensaje"]+" "+ request.POST["email"]
        #email_from=settings.EMAIL_HOST_USER
        #recipient_list=["elviscruz45@gmail.com"]
        #send_mail(subject,message,email_from,recipient_list)
        #return render(request,"gracias.html")
       
    #return render(request,"contacto.html")

