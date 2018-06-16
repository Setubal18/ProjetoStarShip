from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    bio = models.TextField(max_length=60, blank=True)
    tel = models.CharField(max_length=13, blank=True)

    datanascimento = models.DateField()
    foto_de_Perfil = models.ImageField(upload_to='perfil', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Funcao(models.Model):
    CHOICES_Fucoes= (('im','Imediato'),
                     ('ec', 'Engenheiro Chefe'),
                     ('of', 'Oficial Tatico'),
                     ('cm', 'Comunicação'),
                     ('md', 'Oficial Medico'),
                     ('cw', 'Crewman'),
                     )



class Nave(models.Model):
    nome = models.CharField(max_length=45, null=True, blank=False)
    nRegistro = models.CharField(max_length=8, null=True, blank=False, unique=True)
    modelo = models.CharField(max_length=45, null=True, blank=False)
    marca = models.CharField(max_length=45, null=True, blank=False)
    capacidadeTripulantes = models.PositiveIntegerField(blank=False)
    capacidadeCargaMax = models.PositiveIntegerField()
    range = models.FloatField(validators=[MinValueValidator(0)], blank=False)

    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='crewmans')

    def is_CapOrCrewman(self,user):
        if user:
            dono = user
        else:
            crewman = models.CharField(user,blank=True,verbose_name='Tripulação')
            funcao = models.OneToOneField(Funcao,blank=True,verbose_name='Função')





class Corveta_Nave(Nave):
    CHOICES_TIPO = (('p', 'Pessoal'),
                    ('g', 'Combate'),
                    ('t', 'Transporte'),
                    ('e', 'Exploração'),
                    )

    corveta = models.ForeignKey(Nave, on_delete=models.CASCADE, related_name='Corveta')
    shuttle = models.BooleanField(default=False)
    shuttleqtd = models.IntegerField(blank=False)
    tipo = models.CharField(max_length=5, null=False, choices=CHOICES_TIPO)


class Cargo_Nave(Nave):
    CHOICES_TIPO = (('md', 'Materias Diversos'),
                    ('m', 'Minerio'),
                    ('a', 'Alimento'),
                    ('p', 'Materiais Perigosos'),
                    ('sm', 'Suprimentos Medicos'),
                    )

    cargo = models.ForeignKey(Nave, on_delete=models.CASCADE,  related_name='Cargo')
    shuttle = models.BooleanField(default=False)
    shuttleqtd = models.IntegerField(blank=False)
    tipo = models.CharField(max_length=5, null=False, choices=CHOICES_TIPO)


class StarFight_Nave(Nave):
    CHOICES_TIPO = (('p', 'Pessoal'),
                    ('g', 'Combate'),
                    ('x', 'Transporte'),
                    ('e', 'Exploração'),
                    )

    starFight = models.ForeignKey(Nave, on_delete=models.CASCADE, related_name='StarFight')

    tipo = models.CharField(max_length=5, null=False, choices=CHOICES_TIPO)