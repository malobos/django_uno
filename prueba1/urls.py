
from django.contrib import admin
from django.urls import path
from prueba1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('presentacion/', quien_soy),
    path( 'diadehoy/', diadehoy),
    path( 'holaminombre/<nombre>', nombredeltipo),
    path( 'template/', pruebaTemplate),
    path( 'curso/', curso1),
    path('alumno/', alumnos1),
    path('entregas/', entregable1),
]
