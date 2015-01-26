from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views import generic
from core import models
from core import forms


class PessoaList(generic.ListView):
    template_name = 'core/pessoa_list.html'
    model = models.Pessoa


class PessoaCreate(generic.CreateView):
    template_name = 'core/pessoa_form.html'
    model = models.Pessoa
    form_class = forms.PessoaModelForm
    success_url = reverse_lazy('pessoa:list')
