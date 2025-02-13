from django.core.mail import send_mail
from django.conf import settings

def enviar_email_boas_vindas(email):
    assunto = 'Bem-vindo à Plataforma de Cursos!'
    mensagem = '''
    Olá,

    Obrigado por se registrar na nossa plataforma. Seu cadastro está aguardando aprovação do administrador.

    Atenciosamente,
    Equipe Plataforma de Cursos
    '''
    remetente = settings.EMAIL_HOST_USER
    destinatario = [email]

    send_mail(assunto, mensagem, remetente, destinatario, fail_silently=False)