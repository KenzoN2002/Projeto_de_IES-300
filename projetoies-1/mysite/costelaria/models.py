from django.db import models
from django.urls import reverse 

class Prato(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome 
    
    def get_absolute_url(self):
        return reverse('prato-detail', args=[str(self.id)])

class Bebida(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("bebida-detail", kwargs={"pk": self.pk})
 
class Sobremesa(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("sobremesa-detail", kwargs={"pk": self.pk})
    

class Comanda(models.Model):
    mesa = models.IntegerField(max_length=100, help_text='Digite o número da mesa')
    prato = models.ManyToManyField(Prato, help_text='Selecione o prato')
    bebida = models.ManyToManyField(Bebida, help_text='Selecione a bebida')
    sobremesa = models.ManyToManyField(Sobremesa, help_text='selecione a sobremesa')

    def __str__(self):
        return self.mesa
    
    def get_absolute_url(self):
        return reverse("comanda-detail", kwargs={"pk": self.pk})
