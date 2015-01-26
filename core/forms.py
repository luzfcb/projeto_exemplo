# -*- coding: utf8 -*-
# __author__ = 'Fabio C. Barrionuevo da Luz'
from django import forms
from core import models

from input_mask.widgets import InputMask
from input_mask.contrib.localflavor.br.widgets import BRCPFInput, BRZipCodeInput


class DDDFone(InputMask):
    mask = {'mask': '(99)9999-9999'}

class PessoaModelForm(forms.ModelForm):
    ddd = forms.CharField(widget=DDDFone)
    cep = forms.CharField(widget=BRZipCodeInput)

    class Meta:
        model = models.Pessoa
        fields = '__all__'
        widgets = {
            'cpf': BRCPFInput
        }
