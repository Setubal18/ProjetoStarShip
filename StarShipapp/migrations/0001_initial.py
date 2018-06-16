# Generated by Django 2.0.6 on 2018-06-16 19:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Nave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45, null=True)),
                ('nRegistro', models.CharField(max_length=8, null=True, unique=True)),
                ('modelo', models.CharField(max_length=45, null=True)),
                ('marca', models.CharField(max_length=45, null=True)),
                ('capacidadeTripulantes', models.PositiveIntegerField()),
                ('capacidadeCargaMax', models.PositiveIntegerField()),
                ('range', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=60)),
                ('tel', models.CharField(blank=True, max_length=13)),
                ('datanascimento', models.DateTimeField()),
                ('foto_de_Perfil', models.ImageField(blank=True, null=True, upload_to='perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo_Nave',
            fields=[
                ('nave_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='StarShipapp.Nave')),
                ('shuttle', models.BooleanField(default=False)),
                ('shuttleqtd', models.IntegerField()),
                ('tipo', models.CharField(choices=[('md', 'Materias Diversos'), ('m', 'Minerio'), ('a', 'Alimento'), ('p', 'Materiais Perigosos'), ('sm', 'Suprimentos Medicos')], max_length=5)),
            ],
            bases=('StarShipapp.nave',),
        ),
        migrations.CreateModel(
            name='Corveta_Nave',
            fields=[
                ('nave_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='StarShipapp.Nave')),
                ('shuttle', models.BooleanField(default=False)),
                ('shuttleqtd', models.IntegerField()),
                ('tipo', models.CharField(choices=[('p', 'Pessoal'), ('g', 'Combate'), ('t', 'Transporte'), ('e', 'Exploração')], max_length=5)),
            ],
            bases=('StarShipapp.nave',),
        ),
        migrations.CreateModel(
            name='StarFight_Nave',
            fields=[
                ('nave_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='StarShipapp.Nave')),
                ('tipo', models.CharField(choices=[('p', 'Pessoal'), ('g', 'Combate'), ('x', 'Transporte'), ('e', 'Exploração')], max_length=5)),
            ],
            bases=('StarShipapp.nave',),
        ),
        migrations.AddField(
            model_name='nave',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crewmans', to='StarShipapp.Usuario'),
        ),
        migrations.AddField(
            model_name='starfight_nave',
            name='starFight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StarFight', to='StarShipapp.Nave'),
        ),
        migrations.AddField(
            model_name='corveta_nave',
            name='corveta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Corveta', to='StarShipapp.Nave'),
        ),
        migrations.AddField(
            model_name='cargo_nave',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cargo', to='StarShipapp.Nave'),
        ),
    ]