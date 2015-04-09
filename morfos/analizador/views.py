from django.shortcuts import get_object_or_404, render
from analizador.forms import FormaEntrada
from analizador.decodificador import decodificador
from django.template import RequestContext
import json
import os

wikicorpus = {}

# Carga del formulario y el wikicorpus
def index(request):
	# carga del wikicorpus
  jsonfile = open('morfos/wikicorpus.json', 'r')
  global wikicorpus
  wikicorpus = json.load(jsonfile)
  jsonfile.close()
  dicc = dict(form = FormaEntrada(), respuesta='')
  return render(request, 'analizador/index.html', dicc)

# Analisis morfologico y lema con wikicorpus
def analizar(request):
    # Procesamiento del formulario via POST
    if request.method == 'POST':
        # Se obtiene el texto y se valida
        forma = FormaEntrada(request.POST)
        # se valida el formulario
        if forma.is_valid():
            # Se analiza el texto utilizando freeling
            texto = forma.cleaned_data['contenido']
            textoFreeling = os.popen('echo "%s" | analyze -f es.cfg'%texto, 'r', 1)
            salida = ""

            for line in textoFreeling:
                if(len(line) != 1):   
                  # capturar cada palabra y buscar el lema en wiki
                  arreglo = line.split(" ")
                  if (len(arreglo) == 4):
                    forma, lema, tag, prob = arreglo
                  else: # si hay dos lemas con freeling
                    prob1 = arreglo[3]
                    prob2 = arreglo[-1]
                    if(prob1 >= prob2): # se escoge el de mayor probabilidad
                      forma, lema, tag, prob = arreglo[0:4]
                    else:
                      arreglo2 = arreglo
                      arreglo = arreglo2[4:]
                      arreglo.insert(0, arreglo2[0])
                      forma, lema, tag, prob = arreglo
                  # se obtiene el lema de wikicorpus, si no lo encuentra devuelve -1
                  global wikicorpus
                  infowiki = wikicorpus.get(forma.lower(), -1)
                  
                  if(infowiki != -1):
                    lemawiki = infowiki[0]
                    tagwiki = infowiki[1]
                    salida += "<span class='titulo'>F:</span> <span class='valores'>" + forma + "</span> <span class='titulo'>L(Wc):</span> <span class='valores'>" + lemawiki + "</span> <span class='titulo'>T:</span> <span class='valores'>" + tagwiki + "</span> <span class='titulo'>DT:</span> <span class='valores'>" + decodificador(tagwiki) +"</span>\n\n"
                  else:
                    salida += "<span class='titulo'>F:</span> <span class='valores'>" + forma + "</span> <span class='titulo'>L(Fl):</span> <span class='valores'>" + lema + "</span> <span class='titulo'>T:</span> <span class='valores'>" + tag + "</span> <span class='titulo'>DT:</span> <span class='valores'>" + decodificador(tag) + "</span>\n\n"
            # Se guarda el texto procesado y se muestra en la misma pagina
            dicc = dict(form = FormaEntrada(), texto = texto, respuesta = salida)
            return render(request, "analizador/index.html", dicc)
    
    # si la solicitud no es POST, no se realiza el analisis
    dicc = dict(form = FormaEntrada(), respuesta = '')
    return render(request, "analizador/index.html", dicc)