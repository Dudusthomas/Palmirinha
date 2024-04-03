from django.db import models
 
class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome
 
class Receita(models.Model):

    DIFICULDADE = [
        ("facil", "FÁCIL"),
        ("moderado", "MODERADO"),
        ("dificil", "DÍFICIL")    
    ]
 
    nome = models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=2000)
    modo_de_preparo = models.TextField(max_length=8000)
    grau_de_dificuldade = models.CharField(max_length=10, blank=True, null=True, choices=DIFICULDADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nome