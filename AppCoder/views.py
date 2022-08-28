from django.shortcuts import render
from .models import Familia
from django.http  import  HttpResponse
from django.template  import  Template,Context
import datetime

def Familia(request):
    carlos=Familia(nombre="Carlos", apellido="Fernandez",edad=50,nacimiento=2022-edad)
    maria=Familia(nombre="Maria", apellido="Ayala",edad=45,nacimiento=2022-edad)
    diego=Familia(nombre="Diego", apellido="Fernandez",edad=50,nacimiento=2022-edad)
    carlos.save()
    maria.save()
    diego.save()
    
    texto=f"Nombre {carlos.nombre}   apellido {carlos.apellido}     edad {carlos.edad}     fecha{carlos.nacimiento}  "
    texto2=f"Nombre {maria.nombre}   apellido {maria.apellido}     edad {maria.edad}     fecha{maria.nacimiento}  "
    texto3=f"Nombre {diego.nombre}   apellido {diego.apellido}     edad {diego.edad}     fecha{diego.nacimiento}  "
    
    return HttpResponse(texto,texto2,texto3)


def plantillahtml(request):
    archivo=open("C:/Users/Usuario/Desktop/entrega/proyecto/plantillas/template.html")
    contenido=archivo.read()
    archivo.close()
    plantilla=Template(contexto)
    contexto=Context()
    documento=plantilla.render(contexto)
    