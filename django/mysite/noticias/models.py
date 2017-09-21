# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.

@python_2_unicode_compatible
class Noticia(models.Model):
    noticia_title = models.CharField(max_length=100,default='titulos iniciais')
    noticia_text = models.CharField(max_length=200)
    latitude = models.FloatField(default=-20.297618)
    longitude = models.FloatField(default=-40.295777)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return (self.noticia_title)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    comentario_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.comentario_text
# adicione linha no mysite/settings.py => 'noticias.apps.NoticiasConfig',        
#apos conclusao do modulo execute: python manage.py makemigrations noticias
#execute: python manage.py sqlmigrate noticias 0001
#execute: python manage.py migrate
#no noticias/admin.py inclua a linha: admin.site.register(Noticia)
#execute: python manage.py runserver