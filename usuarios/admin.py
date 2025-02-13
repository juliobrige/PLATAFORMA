from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'genero', 'telefone', 'aprovado')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('foto_perfil', 'genero', 'telefone', 'aprovado')}),
    )

admin.site.register(Usuario, UsuarioAdmin)
