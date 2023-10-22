from django.db import models

# Create your models here.
from django.db import models  
class Funcionario(models.Model):  
    codigo = models.IntegerField()  
    nome = models.CharField(max_length=100)  
    email = models.EmailField()  
    contato = models.CharField(max_length=15)  

    class Meta:  
        db_table = "funcionario"