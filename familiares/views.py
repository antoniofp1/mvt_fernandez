from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import per_familia

def probar_template(request):
    queryset = per_familia.objects.all()
    diccionario = {'familiares': queryset}
    plantilla = loader.get_template( 'familiares_list.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)
