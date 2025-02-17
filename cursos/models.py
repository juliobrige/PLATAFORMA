from django.db import models
from usuarios.models import Usuario

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='cursos/')
    professor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

# models.py

class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)  # Arquivo de vídeo
    video_url = models.URLField(null=True, blank=True)
    duracao = models.IntegerField()  # Link externo (opcional)

    def __str__(self):
        return self.titulo

class Progresso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.titulo}"