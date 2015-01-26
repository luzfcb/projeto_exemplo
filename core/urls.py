# -*- coding: utf8 -*-
# __author__ = 'Fabio C. Barrionuevo da Luz'
from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
    url(r'^$', views.PessoaList.as_view(), name='list'),
    url(r'^create/', views.PessoaCreate.as_view(), name='create'),

)
