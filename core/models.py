# -*- coding: utf-8 -*-
from django.db import models


class Pessoa(models.Model):
    ddd = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=14)
    cep = models.CharField(max_length=9)
