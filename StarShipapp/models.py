from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

# class Funcao(models.Model):
#     capitao = 'cp'
#     primeiroOficial = 'po'
#     engenheiroChefe = 'ec'
#     oficialTatico = 'of'
#     oficalMedico = 'md'
#     oficialCiencias = 'oc'
#     oficialOperacao = 'op'
#     crewman = 'cw'
#     CHOICES_FUNCOES = ((capitao, 'Capitão'),
#                        (primeiroOficial, 'Primeiro Oficial'),
#                        (engenheiroChefe, 'Engenheiro Chefe'),
#                        (oficialTatico, 'Oficial Tatico'),
#                        (oficalMedico, 'Oficial Medico'),
#                        (oficialCiencias, 'Oficial Ciencias'),
#                        (oficialOperacao, 'Oficial Operações'),
#                        (crewman, 'Crewman'),
#                        )
#
#     funcaoNaNave = models.CharField(max_length=2, choices=CHOICES_FUNCOES, default=crewman)
#
#     def is_upperclass(self):
#         return self.funcaoNaNave in (self.capitao, self.oficialTatico)
#

class Usuario(models.Model):
    capitao = 'cp'
    primeiroOficial = 'po'
    engenheiroChefe = 'ec'
    oficialTatico = 'of'
    oficalMedico = 'md'
    oficialCiencias = 'oc'
    oficialOperacao = 'op'
    crewman = 'cw'
    CHOICES_FUNCOES = ((capitao, 'Capitão'),
                       (primeiroOficial, 'Primeiro Oficial'),
                       (engenheiroChefe, 'Engenheiro Chefe'),
                       (oficialTatico, 'Oficial Tatico'),
                       (oficalMedico, 'Oficial Medico'),
                       (oficialCiencias, 'Oficial Ciencias'),
                       (oficialOperacao, 'Oficial Operações'),
                       (crewman, 'Crewman'),
                       )

    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    bio = models.TextField(max_length=60, blank=True)
    tel = models.CharField(max_length=13, blank=True)
    datanascimento = models.DateField(blank=True,null=True)
    foto_de_Perfil = models.ImageField(upload_to='perfil', null=True, blank=True)


    #funcao = models.ForeignKey(Funcao.is_upperclass, on_delete=models.CASCADE, )
    funcao = models.CharField(choices=CHOICES_FUNCOES,max_length=2,null=True,default=crewman)



    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.user.username


class Nave(models.Model):
    nome = models.CharField(max_length=45, null=True, blank=False)
    nRegistro = models.CharField(max_length=8, null=True, blank=False, unique=True,verbose_name='nº-Registro')
    modelo = models.CharField(max_length=45, null=True, blank=False)
    marca = models.CharField(max_length=45, null=True, blank=False)
    capacidadeTripulantes = models.PositiveIntegerField(blank=False)
    capacidadeCargaMax = models.PositiveIntegerField()
    range = models.FloatField(validators=[MinValueValidator(0)], blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crewmans')

    crewman = models.ManyToManyField(User, blank=True, verbose_name='Tripulação')

    foto_de_nave = models.ImageField(upload_to='perfil', null=True, blank=True)

    def __str__(self):
        return self.nome



class Corveta(Nave):
    CHOICES_TIPO = (('p', 'Pessoal'),
                    ('g', 'Combate'),
                    ('t', 'Transporte'),
                    ('e', 'Exploração'),
                    )

    shuttle = models.BooleanField(default=False)
    shuttleqtd = models.IntegerField(blank=False)
    tipo = models.CharField(max_length=5, null=False, choices=CHOICES_TIPO)

    class Meta:
        verbose_name_plural = "Corvetas"

    def __str__(self):
        return self.nome


class Cargo(Nave):
    CHOICES_TIPO = (('md', 'Materias Diversos'),
                    ('m', 'Minerio'),
                    ('a', 'Alimento'),
                    ('p', 'Materiais Perigosos'),
                    ('sm', 'Suprimentos Medicos'),
                    )

    shuttle = models.BooleanField(default=False)
    shuttleqtd = models.IntegerField(blank=False)
    tipo = models.CharField(max_length=5, null=False, choices=CHOICES_TIPO)

    class Meta:
        verbose_name_plural = "Cargo"

    def __str__(self):
        return self.nome


class StarFight(Nave):
    CHOICES_TIPO = (('p', 'Pessoal'),
                    ('g', 'Combate'),
                    ('x', 'Transporte'),
                    ('e', 'Exploração'),
                    )


    tipo = models.CharField(max_length=5, null=False, choices=CHOICES_TIPO)

    class Meta:
        verbose_name_plural = "Star Fighers"

    def __str__(self):
        return self.nome
