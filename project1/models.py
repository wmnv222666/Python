from django.db import models


class Department(models.Model):
    # id = models.BigIntegerField(verbose_nam="Id",primary_key=True)//default 1
    # id = models.AutoFied(verbose_nam="Id",primary_key=True)//default 2
    title = models.CharField(verbose_name="Title", max_length=32)

    def __str__(self):
        return self.title


class UserInfoForm(models.Model):

    name = models.CharField(verbose_name="name", max_length=16)
    password = models.CharField(verbose_name="password", max_length=64)
    age = models.IntegerField(verbose_name="age")
    account = models.DecimalField(
        verbose_name="Account balance", max_digits=10, decimal_places=2, default=0
    )
    create_time = models.DateTimeField(verbose_name="Time")

    depart = models.ForeignKey(
        verbose_name="Department",
        to="Department",
        to_field="id",
        on_delete=models.CASCADE,
    )

    gender_choices = (
        (1, "male"),
        (2, "female"),
    )
    gender = models.SmallIntegerField(verbose_name="Sex", choices=gender_choices)
