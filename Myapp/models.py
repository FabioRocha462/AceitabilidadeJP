from django.db import models
import uuid
from users.models import User
# Create your models here.

class School(models.Model):
     choices = (
        ("04 de Outubro","04 de Outubro"),
        ("Pequeno Mário","Pequeno Mário"),
        ("Ariamiro","Ariamiro"),
        ("Maria Dália","Maria Dália"),
        ("Baixa do Fogo","Baixa do Fogo"),
        ("Serra","Serra"),
        ("Angicos","Angicos"),
        ("Jerimum","Jerimum"),
        ("Ema","Ema"),
        ("Carnaubinha","Carnaubinha")
        )
     uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
     name = models.CharField(max_length=255, choices=choices)
     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now = True)

     def __str__(self):
        return self.name

class Classroom(models.Model):

    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null= True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.name

class Food(models.Model):
    choices = (
        ("BISCOITO ROSQUINHA COM SUCO VITAMINA DE GOIABA E FRUTA", "BISCOITO ROSQUINHA COM SUCO VITAMINA DE GOIABA E FRUTA"),
        ("BISCOITO MARIA OU CREAM CRACKER COM SUCO", "BISCOITO MARIA OU CREAM CRACKER COM SUCO"),
        ("ARROZ COM FEIJÃO E FRANGO GUISADO","ARROZ COM FEIJÃO E FRANGO GUISADO"),
        ("SOPA DE FRANGO COM ESPAGUETE E LEGUMES","SOPA DE FRANGO COM ESPAGUETE E LEGUMES"),
        ("BEIJU COM MARGARINA E CAFÉ COM LEITE", "BEIJU COM MARGARINA E CAFÉ COM LEITE"),
        ("CUSCUZ RECHEADO COM OVOS MEXIDOS E SUCO","CUSCUZ RECHEADO COM OVOS MEXIDOS E SUCO"),
        ("BAIÃO DE 2 COM MACAXEIRA, CARNE BOVINA E SUCO","BAIÃO DE 2 COM MACAXEIRA, CARNE BOVINA E SUCO"),
        ("TAPIOCA COM QUEIJO COALHO E VITAMINA DE DE GOIABA", "TAPIOCA COM QUEIJO COALHO E VITAMINA DE GOIABA"),
        ("ARROZ DE LEITE COM PAÇOCA DE CARNES DE SOL","ARROZ DE LETE COM PAÇOCA DE CARNE DE SOL"),
        ("CUSCUZ RECHEADO COM CARNE MOÍDA E SUCO","CUSCUZ RECHEADO COM CARNE MOÍDA"),
        ("CACHORRO QUENTE COM MOLHO DE CARNE MOÍDA DE SUCO","CACHORRO QUENTE COM MOLHO DE CARNE MOÍDA E SUCO"),
        ("RISOTO DE FRANGO COM LEGUMES", "RISOTO DE FRANGO COM LEGUMES"),
        ("BOLO DE CACO E CAFÉ COM LEITE", "BOLO DE CACO E CAFÉ COM LEITE"),
        ("TAPIOCA RECHEADA COM OVOS MEXIDOS E SUCO DE POLPA", "TAPIOCA RECHEADA COM OVOS MEXIDOS E SUCO DE POLPA"),
        ("MUNGUNZÁ COM FRANGO AO MOLHO BRANCO","MUNGUNZÁ COM FRANGO AO MOLHO BRANCO"),
        ("SOPA DE CARNE BOVINA COM MACARRÃO E LEGUMES", "SOPA DE CARNE BOVINA COM MACARRÃO E LEGUMES"),
        ("MACARRONADA DE FRANGO", "MACARRONADA DE FRANGO"),
        ("BOLO SIMPLES COM VITAMINA DE BANANA E AVEIA", "BOLO SIMPLES COM VITAMINA DE BANANA E AVEIA"),
        ("CANJA DE FRANGO COM BATATA INGLESA E CENOURA", "CANJA DE FRANGO COM BATATA INGLESA E CENOURA"),
        ("BAIÃO DE 2 COM CARNE BOVINA E VINAGRETE", "BAIÃO DE 2 COM CARNE BOVINA E VINAGRETE"),
        ("MACARRONADA DE CARNE MOÍDA","MACARRONADA DE CARNE MOÍDA")
    )
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255, choices=choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.name

class Classroom_Food(models.Model):

    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)
    liked  = models.IntegerField()
    disliked = models.IntegerField()

    def __str__(self):

        return self.food.name



