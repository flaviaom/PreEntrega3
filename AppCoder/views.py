from django.shortcuts import render
from django.http import	HttpResponse
from AppCoder.models import Curso, Estudiantes

# Create your views here.

def ver_estudiantes (request):
    return render(request,'ver_estudiantes.html')

def inicio(request):
    return render(request, "inicio.html")

def ver_cursos(request):
    return render(request, "ver_cursos.html")

def ver_profesores(request):
    return render(request, "ver_profes.html")

def ver_entregables(request):
    return render(request, "ver_entregables.html")

def crear_curso(request):

    curso_1= Curso(nombre='desarrollo movil', comision=5555)
    curso_1.save() #guardarlo en su respectiva tabla

    curso_2= Curso(nombre='desarrollo estudiantil', comision=5355)
    curso_2.save() #guardarlo en su respectiva tabla

    return HttpResponse(f'Hemos creado un curso llamado {curso_1.nombre}!')

def crear_estudiante(request):
    est_1 = Estudiantes(nombre= "Flavia", apellido='Ochoa', email='flavia@gmail.com', edad=15)
    est_2 = Estudiantes(nombre= "Sofia", apellido='Ochoa', email='sofia@gmail.com', edad=16)

    est_1.save()
    est_2.save()

    info = {'nombre1':est_1.nombre, 'nombre2':est_2.nombre}

    return render(request,'ver_estudiantes.html',info)