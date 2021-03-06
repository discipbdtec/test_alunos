# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. Primeira mensagem do arquivo views.py.")

from .models import Noticia


def index(request):
    latest_question_list = Noticia.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'noticias/index.html', context)

def mapa(request):
    latest_question_list = Noticia.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'noticias/mapa.html', context)
