# cursos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/detalhes_curso/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
]