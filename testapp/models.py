from django.db import models

# Create your models here.

class Mensaje(models.Model):
    texto = models.CharField(max_length=100)

    def __str__(self):
        return self.texto
