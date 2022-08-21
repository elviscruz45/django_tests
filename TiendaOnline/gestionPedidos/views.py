from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *
from django.core.mail import send_mail
from django.conf import settings

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
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+ request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["elviscruz45@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"gracias.html")
       
    return render(request,"contacto.html")
