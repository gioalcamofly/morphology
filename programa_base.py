#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from collections import Counter
import nltk
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

print 'Palabras del texto ordenadas por frecuencia'
t=''
for w in fdf:
    t+='('+w[0]+','+str(w[1])+') '
print t


dict ={}
dict['.']='PUNT'
dict['la']='DET'
dict['a']='PREP'
dict['para']='PREP'
dict['que']='CONJ'
dict['en']='PREP'
dict['el']='DET'
#Aquí hay se añaden las palabras del diccionario y sus etiquetas




p=[
    (r'.*amos$','VIP1S'),
    (r'.*imos$','VIP1S'),
    (r'.*a$','NCFS'),
    (r'.*$','NCMS'),
    #Aquí hay se añaden los patrones necesarios
    ]



rt=nltk.RegexpTagger(p)
taggedText=rt.tag(words)
for item in taggedText:
    if dict.has_key(item[0]):
        print item[0]+' '+dict[item[0]]
    else:
        print item[0]+' '+item[1]
    


sys.exit()
