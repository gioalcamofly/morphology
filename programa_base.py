#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from collections import Counter


import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

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
dict['.']='PUNT'
dict['lo']='DET'
dict['la']='DET'
dict['los']='DET'
dict['las']='DET'
dict['a']='PREP'
dict['para']='PREP'
dict['que']='CONJ'
dict['en']='PREP'
dict['el']='DET'
dict['de']='PREP'
dict[',']='PUNT'
dict['(']='PUNT'
dict[')']='PUNT'
dict['un']='DET'
dict['una']='DET'
dict['unos']='DET'
dict['unas']='DET'

#Aquí hay se añaden las palabras del diccionario y sus etiquetas




p=[
    (r'.$ware$','NCMS'),
    (r'.*amos$','VIP1S'),
    (r'.*imos$','VIP1S'),
    (r'.*it[oa]$', 'ADJ'),
    (r'.*(ar|er|ir)$', 'VN'),
    (r'.*as$', 'NCFP'),
    (r'.*os$', 'NCMP'),
    (r'.*a$','NCFS'),
    (r'.*$','NCMS'),
    #Aquí hay se añaden los patrones necesarios
    ]



rt=nltk.RegexpTagger(p)
taggedText=rt.tag(words)
for item in taggedText:
    if dict.has_key(item[0].lower()):
        print(item[0] + ' ' + dict[item[0].lower()])
    else:
        print(item[0] + ' ' + item[1])


sys.exit()
