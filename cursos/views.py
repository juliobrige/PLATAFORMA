from django.shortcuts import render, get_object_or_404
from .models import Curso, Aula

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aulas = Aula.objects.filter(curso=curso)
    return render(request, 'cursos/detalhes_curso.html', {'curso': curso, 'aulas': aulas})