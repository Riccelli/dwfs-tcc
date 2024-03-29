# Generated by Django 4.2.6 on 2023-10-16 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cpf", models.CharField(max_length=11)),
                ("nome", models.CharField(max_length=200)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Indice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sigla", models.CharField(max_length=10)),
                (
                    "descricao",
                    models.CharField(max_length=100, verbose_name="Descrição"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Modalidade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sigla", models.CharField(max_length=10)),
                (
                    "descricao",
                    models.CharField(max_length=100, verbose_name="Descrição"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Programa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "descricao",
                    models.CharField(max_length=100, verbose_name="Descrição"),
                ),
                (
                    "indice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="tcc.indice",
                        verbose_name="Índice",
                    ),
                ),
                (
                    "modalidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="tcc.modalidade",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Telefone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ddd", models.IntegerField()),
                ("numero", models.CharField(max_length=9, verbose_name="Número")),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tcc.cliente"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Proposta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contrato", models.CharField(max_length=20)),
                ("data_criacao", models.DateField(verbose_name="Data de Criação")),
                (
                    "valor_principal",
                    models.DecimalField(decimal_places=2, max_digits=18),
                ),
                (
                    "numero_de_parcelas",
                    models.IntegerField(verbose_name="Número de Parcelas"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("N", "Nova"), ("A", "Aprovada"), ("R", "Rejeitada")],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="tcc.cliente"
                    ),
                ),
                (
                    "programa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="tcc.programa"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Parcela",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.IntegerField(verbose_name="Número")),
                ("vencimento", models.DateField(verbose_name="Data de Vencimento")),
                ("valor", models.DecimalField(decimal_places=2, max_digits=18)),
                (
                    "proposta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tcc.proposta"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pagamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_pagamento", models.DateField(verbose_name="Data de Pagamento")),
                ("valor", models.DecimalField(decimal_places=2, max_digits=18)),
                (
                    "parcela",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tcc.parcela"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Aliquota",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vigencia", models.DateField(verbose_name="Data Inicial de Vigência")),
                (
                    "aliquota",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Taxa % a.a."
                    ),
                ),
                (
                    "indice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tcc.indice",
                        verbose_name="Índice",
                    ),
                ),
            ],
        ),
    ]
