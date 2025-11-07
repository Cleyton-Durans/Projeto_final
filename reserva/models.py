from django.db import models
from django.contrib.auth.models import User

class Mesa(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Ocupada', 'Ocupada'),
    ]
    numero = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Disponível')
   
    # 🔹 Vínculo direto com a reserva (pode ser nulo)
    reserva = models.ForeignKey(
        'Reserva',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='mesas'
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cliente = self.reserva.nome if self.reserva else "Sem cliente"
        return f"Mesa {self.numero} - {self.status} ({cliente})"
    
class Reserva(models.Model):
    STATUS_CHOICES = [
        ('Em espera', 'Em espera'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data = models.DateField()
    hora = models.TimeField()
    quantidade_pessoas = models.PositiveIntegerField()
    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservas')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Em espera')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.data} ({self.status})"
