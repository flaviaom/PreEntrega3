from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("curso/", crear_curso, name ='Nuevo Curso'),
    path("estudiantes/", crear_estudiante, name = 'Nuevo Estudiante'),
    path("ver_cursos", ver_cursos, name = 'Courses'),
    path("ver_estudiantes", ver_estudiantes, name = 'Estudiantes'),
    path("ver_profes", ver_profesores, name = 'Profesores'),
    path("ver_entregas", ver_entregables, name = 'Entregables'),
    path("", inicio, name = 'Home'),

]