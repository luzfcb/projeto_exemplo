# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ddd', models.CharField(max_length=255, null=True, blank=True)),
                ('cpf', models.CharField(max_length=14)),
                ('cep', models.CharField(max_length=9)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
