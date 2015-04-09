# import csv
from glob import glob
from codecs import open, BOM_UTF8
import json

s = {"Acontecimientos":["acontecimientos","NP00000"],
	"Fallecimientos":["fallecimientos","NP00000"],
	"Nacimientos":["nacimientos","NP00000"],
	"¡":["¡","Faa"],
	"!":["!","Fat"],
	",":[",","Fc"],
	"[":["[","Fca"],
	"]":["]","Fct"],
	":":[":","Fd"],
	'"':['"',"Fe"],
	"-":["-","Fg"],
	"/":["/","Fh"],
	"¿":["¿","Fia"],
	"?":["?","Fit"],
	"{":["{","Fla"],
	"}":["}","Flt"],
	".":[".","Fp"],
	"(":["(","Fpa"],
	")":[")","Fpt"]}

archivos=0
excluir = ("<doc", "</doc>", "ENDOFARTICLE", "REDIRECT", "http",
		  "¡", "!", ",", "[", "]", ":", '"', "-", "/", "¿", "?",
		   "{", "}",  ".", "(", ")",
		  "Acontecimientos", "Fallecimientos", "Nacimientos")

for f in glob("tagged/*"):
	archivos += 1
	print(f)
	for line in open(f, encoding="latin-1"):
		if line == "\n" or line.startswith(excluir):
			continue
		w, lemma, tag, x = line.split(" ")
		w2 = s.get(w, "")
		if (w2 != ""):
			if (len(w2[0]) != len(lemma)):
				s[w.lower()] = [lemma.lower(), tag]
		else:
			s[w] = [lemma, tag]
# json
jsonfile = open('wikicorpus.json', 'w')
jsonfile.write(json.dumps(s, separators=(',',':')))
jsonfile.close()
print ("archivos recorridos %d" % archivos)
print ("tamaño del diccionaro %d" % len(s))
