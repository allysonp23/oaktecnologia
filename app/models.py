from django.db import models

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Nome'
    )
    description = models.TextField(
        verbose_name="Descrição do Produto"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço"
        )
    available = models.BooleanField(
        default=True,
        verbose_name="Disponível em Estoque"
        )

    def __str__(self):
        return self.name
