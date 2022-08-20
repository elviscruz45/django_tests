from multiprocessing.reduction import ACKNOWLEDGE
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render

def saludo(request):
    nombre="Elvis"
#   doc_externo=open("/Users/elviscruz45/Desktop/django_tests/Proyecto1/Proyecto1/plantillas/miplantilla.html")
#   plt=Template(doc_externo.read())
#   doc_externo.close()
#   ctx=Context({"lista":["hola","como","estas","muchacha"]})
#   documento=plt.render(ctx)
#   return HttpResponse(documento)
    return render(request,"miplantilla.html",{"nombre":nombre})


def dameFecha(request):
    fecha=datetime.datetime.now()
    
    doc="<h2> La fecha es %s </h2>" %fecha
    
    return HttpResponse(doc)

def edad(request,agno):
    agno=agno
    act=2000+agno
    doc="en el %s tendras %s agnos" %(agno,act)
    
    return HttpResponse(doc)

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"CursoC.html",{"dameFecha": fecha_actual})


def cursoCss(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"Cursocss.html",{"dameFecha": fecha_actual})