# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Noticia,Comentario
# Register your models here.
admin.site.register(Noticia)
admin.site.register(Comentario)
