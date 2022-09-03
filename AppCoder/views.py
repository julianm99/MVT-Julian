from django.shortcuts import render
from .models import Familia
from django.http  import  HttpResponse
from django.template  import  Template,Context,loader
import datetime

def familiares(request):
    carlos=Familia(nombre="Carlos", apellido="Fernandez",edad=50,fecha="1972-02-03")
    maria=Familia(nombre="Maria", apellido="Ayala",edad=45,fecha="1977-02-04")
    diego=Familia(nombre="Diego", apellido="Fernandez",edad=20,fecha="2002-10-05")
    carlos.save()
    maria.save()
    diego.save()

    
    texto= f"NOMBRE:  {carlos.nombre}  APELLIDO: {carlos.apellido}  EDAD: {carlos.edad}  FECHA: {carlos.fecha}      NOMBRE:  {maria.nombre}  APELLIDO: {maria.apellido}  EDAD: {maria.edad}  FECHA: {maria.fecha}    NOMBRE:  {diego.nombre}  APELLIDO: {diego.apellido}  EDAD: {diego.edad}  FECHA: {diego.fecha} "

 
    return HttpResponse(texto)

def probandotemplate(request):
    html=open("C:/Users/Usuario/Desktop/entrega/proyecto/proyecto/plantillas/template.html")
    plantilla=Template(html.read())
    html.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)