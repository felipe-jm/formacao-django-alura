# Generated by Django 3.0.3 on 2023-01-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('data_ida', models.DateField()),
                ('data_volta', models.DateField()),
                ('data_pesquisa', models.DateField()),
                ('informacoes', models.TextField(blank=True, max_length=200)),
                ('classe_viagem', models.CharField(choices=[('ECON', 'Econômica'), ('EXEC', 'Executiva'), ('PRIC', 'Primeira Classe')], default=0, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
