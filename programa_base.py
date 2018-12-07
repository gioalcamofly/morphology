#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import nltk

import test

reload(sys)  
sys.setdefaultencoding('utf8')

#Lectura del fichero de texto
f = open ('texto.txt')
freqdist = nltk.FreqDist()
words=nltk.word_tokenize(f.read())
fd = nltk.FreqDist(word.lower() for word in words)
fdf= fd.most_common(50)

print('Palabras del texto ordenadas por frecuencia')
t=''
for w in fdf:
    t+='('+w[0]+','+str(w[1])+') '
print(t)

dict ={}

#Preposiciones

dict['a']='PREP'
dict['para']='PREP'
dict['en']='PREP'
dict['de']='PREP'
dict['con']='PREP'
dict['por']='PREP'
dict['desde']='PREP'
dict['entre']='PREP'
dict['sobre']='PREP'
dict['al']='PREP'
dict['del']='PREP'

#Conjunciones

dict['que']='CONJ'
dict['y']='CONJ'
dict['o']='CONJ'
dict['pero']='CONJ'
dict['e']='CONJ'
dict['u']='CONJ'

#Adjetivos

dict['su']='ADJ'
dict['sus']='ADJ'
dict['integrado']='ADJ'
dict['compilado']='ADJ'
dict['compilados']='ADJ'
dict['operativo']='ADJ'

#Verbos

dict['es']='VAP3PS'

#Pronombres

dict['se']='PRON'
dict['le']='PRON'

#Nombres

dict['programa']='NCMS'
dict['programas']='NCMP'
dict['sistema']='NCMS'
dict['sistemas']='NCMP'
dict['componente']='NCMS'
dict['componentes']='NCMP' #Para compensar la regexp que coge -es como plural femenino.
dict['circuito']='NCMS'
dict['circuitos']='NCMP'
dict['unidad']='NCFS'
dict['soporte']='NCMS'
dict['fuente']='NCFS'
dict['periférico']='NCMS'
dict['periféricos']='NCMP'

#Numerales

dict['primero']='NUM'
dict['primeros']='NUM'
dict['segundo']='NUM'
dict['segundos']='NUM'
dict['tercero']='NUM'
dict['terceros']='NUM'

#Adverbios

dict['como']='ADV'
dict['más']='ADV'
dict['así']='ADV'
dict['mediante']='ADV'

#Abreviaturas

dict['cpu']='ABRV'
dict['etc']='ABRV'

#Aquí hay se añaden las palabras del diccionario y sus etiquetas

p=[
    (r'^[Cc]ual(quiera?)?$', 'PRON'),
    (r'^[Ee]st(e|a|o|os|as)$', 'PRON'),
    (r'^[Aa]lg[uú]n(o|a|os|al)?$', 'PRON'),
    (r'^[Oo]tr(o|a|os|as)$', 'DET'),
    (r'^[Uu]n(a|os|as)?$', 'DET'),
    (r'^[.,\(\);:]$', 'PUNT'),
    (r'^([Ee]l|[Ll](a|o|os|as))$', 'ART'),
    (r'^[0-9]+(.[0-9]+)?$', 'NUM'),
    (r'.+mente$', 'ADV'), #Se usa '+' para evitar que trate el nombre 'mente' como adverbio.
    (r'.*ware$','NCMS'),
    (r'.*amos$','VIP1S'),
    (r'.*imos$','VIP1S'),
    (r'.*rlos?$', 'VERBO'), #CAMBIAR A FORMA REAL
    (r'.*(icos?|icas?)$', 'ADJ'),
    (r'.*(ados|idos)$', 'VMP00PM'), #en singular podría ser también un verbo
    (r'.*(adas|idas)$', 'VMP00PF'),
    (r'.*bles?$', 'ADJ'),
    (r'.*(ado|ido)$', 'VMP00SM'),
    (r'.*(ada|ida)$', 'VMP00SF'),
    (r'.*ndo$', 'VERBO'),   #CAMBIAR FORMA A GERUNDIA
    (r'.*ble$', 'ADJ'),
    (r'.*ión$','NCFS'),
    (r'.*it[oa]$', 'ADJ'),
    (r'.*(ar|er|ir)$', 'VN'),
    (r'.*al$', 'ADJ'), #En este contexto, parece más probable que palabras acabadas en -al sean adjetivos a nombres
    (r'.*(as|es)$', 'NCFP'), #Parece más probable encontrar plurales femeninos acabados en -es que masculinos
    (r'.*os$', 'NCMP'),
    (r'.*(en|an)$', 'VERBO'),
    (r'.*e$', 'VERBO'), #VALE LA PENA INCLUIR PALABRAS QUE ROMPAN ESTO EN DICCIONARIO PORQUE LOS VERBOS SON MAYORIA
    (r'.*a$','NCFS'),
    (r'.*$','NCMS'),
    #Aquí hay se añaden los patrones necesarios
    ]




rt=nltk.RegexpTagger(p)
taggedText=rt.tag(words)
prueba={}
count = 0
for item in taggedText:
    if dict.has_key(item[0].lower()):
        #print(item[0] + ' ' + dict[item[0].lower()])
        prueba[count]=(item[0], dict[item[0].lower()])
    else:
        #print(item[0] + ' ' + item[1])
        prueba[count]=(item[0], item[1])
    count+=1

print('Eficiencia: {}'.format(test.efficiency(prueba)))

sys.exit()
