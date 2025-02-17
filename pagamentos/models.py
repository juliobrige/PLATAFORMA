from cursos.models import Curso
from usuarios.models import Usuario
from django.db import models


class MpesaPayment(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=50, unique=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('aprovado', 'Aprovado'), ('pendente', 'Pendente')])

    def __str__(self):
        return f"Pagamento de {self.amount} por {self.phone_number}"