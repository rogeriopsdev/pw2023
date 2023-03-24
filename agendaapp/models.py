from django.db import models

# Create your models here.
class Servico(models.Model):
    nome_servico =models.CharField(max_length=50)

    def __str__(self):
        return self.nome_servico


class Agenda(models.Model):
    data_agenda =models.CharField(max_length=50)

    def __str__(self):
        return self.data_agenda
