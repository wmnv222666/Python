# Generated by Django 5.0.2 on 2024-02-26 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("title", models.CharField(max_length=32, verbose_name="Title")),
            ],
        ),
        migrations.CreateModel(
            name="UserInfoForm",
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
                ("name", models.CharField(max_length=16, verbose_name="name")),
                ("password", models.CharField(max_length=64, verbose_name="password")),
                ("age", models.IntegerField(verbose_name="age")),
                (
                    "account",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Account balance",
                    ),
                ),
                ("create_time", models.DateTimeField(verbose_name="Time")),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(1, "male"), (2, "female")], verbose_name="Sex"
                    ),
                ),
                (
                    "depart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project1.department",
                        verbose_name="Department",
                    ),
                ),
            ],
        ),
    ]