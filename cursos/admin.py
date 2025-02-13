from django.contrib import admin
from .models import Curso, Aula, Progresso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco')

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso')

@admin.register(Progresso)
class ProgressoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'concluido')