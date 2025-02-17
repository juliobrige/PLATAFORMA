from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistroForm
from .models import Usuario
from .email import enviar_email_boas_vindas
from pagamentos.models import MpesaPayment
from cursos.models import Curso




def registro(request):
    """Cadastro de novo usuário"""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.aprovado = True  # Novo usuário precisa ser aprovado pelo admin
            user.save()

            send_mail(
                'Bem-vindo à Plataforma de Cursos!',
                'Obrigado por se registrar. Seu cadastro está aguardando aprovação do administrador.',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            enviar_email_boas_vindas(user.email)

            return redirect('aguardando_aprovacao')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})


def aguardando_aprovacao(request):
    """Página de aviso para usuários que aguardam aprovação"""
    return render(request, 'usuarios/aguardando_aprovacao.html')


def user_login(request):
    """Login do usuário"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.aprovado:  # Verifica se o usuário foi aprovado pelo admin
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'usuarios/login.html', {'erro': 'Aguarde a aprovação do administrador.'})
        else:
            return render(request, 'usuarios/login.html', {'erro': 'Usuário ou senha inválidos.'})


    return render(request, 'usuarios/login.html')

@login_required
def dashboard(request):
    # Filtra os cursos pagos pelo usuário atual
    cursos_pagos_ids = MpesaPayment.objects.filter(usuario=request.user, status='aprovado').values_list('curso_id', flat=True)
    cursos_pagos = Curso.objects.filter(id__in=cursos_pagos_ids)

    context = {
        'cursos_pagos': cursos_pagos,  # Passa os cursos pagos para o template
    }
    return render(request, 'usuarios/dashboard.html', context)

@login_required
def user_logout(request):
    """Logout do usuário"""
    logout(request)
    return redirect('login')
