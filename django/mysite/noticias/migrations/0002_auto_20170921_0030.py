# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commentario',
            new_name='Comentario',
        ),
        migrations.AddField(
            model_name='noticia',
            name='noticia_title',
            field=models.CharField(default='titulos iniciais', max_length=100),
        ),
    ]
