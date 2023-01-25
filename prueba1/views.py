from django.http import HttpResponse
from datetime import date, time, datetime
from django.template import Template, Context
from App1.models import *
def saludo(request):
	return HttpResponse("Hola Django - Coder")

def quien_soy(request):
    return HttpResponse("Mi nombre es Mariana, tengo 34 años, tengo dos hijos y un marido hermoso")
def diadehoy(request):
    dia= date.today()
    documentoDeTexto= f" Hoy es día: <br>{dia}"
    return HttpResponse(documentoDeTexto)
def nombredeltipo(self, nombre):
    docdetexto= f"Mi nombre es <br> <br> {nombre}"
    return HttpResponse(docdetexto)
def pruebaTemplate(request):
    nom= "Pedrito"
    ap= "Urzua"
    diaDeFabr= datetime.today
    diccionario= {"nombre":nom, "apellido": ap, "dia":diaDeFabr}
    
    miHtml= open("H:/Mi unidad/data/python/dj_proy_1/prueba1/plantillas/template1.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto= Context(diccionario)
    documento=plantilla.render(miContexto)
    return HttpResponse(documento)

def curso1(request):
    curso1= curso(nombre="SQL",comision=1)
    curso1.save()
    documentoDeTexto= f"----> Curso: {curso1.nombre} Comision: {curso1.comision}"
    return HttpResponse(documentoDeTexto)
def alumnos1(request):
    alumnos1= estudiantes(nombre="Pedro", apellido= "urzua", email= 'pedro@gmail.com')
    alumnos1.save()
    diccionario= {"nombre":alumnos1.nombre, "apellido":alumnos1.apellido, "Correo":alumnos1.email}
    miHtml= open("H:/Mi unidad/data/python/dj_proy_1/prueba1/plantillas/template2.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto= Context(diccionario)    
    documento=plantilla.render(miContexto)
    return HttpResponse(documento)
def entregable1(request):
    entregable1= entregable(nombre= "pedrourzua", fechaDeEntrega="2023-01-23", entregado= False)
    entregable1.save()
    docdetext= f"El alumno {entregable1.nombre} entrego la prueba: {entregable1.entregado} el dia:{entregable1.fechaDeEntrega}" 
    return HttpResponse(docdetext)