from django.shortcuts import render, get_object_or_404
from .models import Curso, Aula
from pagamentos.models import MpesaPayment
from django.contrib.auth.decorators import login_required


@login_required
def lista_cursos(request):
    cursos = Curso.objects.all()
    cursos_pagos = MpesaPayment.objects.filter(usuario=request.user, status='aprovado').values_list('curso_id', flat=True)
    
    context = {
        'cursos': cursos,
        'cursos_pagos': cursos_pagos,
    }
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})
    
def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aulas = Aula.objects.filter(curso=curso)
    return render(request, 'cursos/detalhes_curso.html', {'curso': curso, 'aulas': aulas})

