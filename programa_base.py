#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import nltk

import test

reload(sys)  
sys.setdefaultencoding('utf8')

#Lectura del fichero de texto
f = open ('texto_test.txt')
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
dict['al']='PREP'
dict['ante']='PREP'
dict['con']='PREP'
dict['de']='PREP'
dict['del']='PREP'
dict['desde']='PREP'
dict['durante']='PREP'
dict['en']='PREP'
dict['entre']='PREP'
dict['excepto']='PREP'
dict['hacia']='PREP'
dict['hasta']='PREP'
dict['mediante']='PREP'
dict['para']='PREP'
dict['por']='PREP'
dict['salvo']='PREP'
dict['según']='PREP'
dict['sin']='PREP'
dict['sobre']='PREP'
dict['tras']='PREP'

#Conjunciones

dict['que']='CONJ'
dict['y']='CONJ'
dict['o']='CONJ'
dict['pero']='CONJ'
dict['e']='CONJ'
dict['u']='CONJ'
dict['porque']='CONJ'
dict['sino']='CONJ'
dict['si']='CONJ'
dict['aunque']='CONJ'
dict['ni']='CONJ'
dict['mientras']='CONJ'
dict['incluso']='CONJ'
dict['pues']='CONJ'

#Adjetivos

dict['su']='ADJ'
dict['sus']='ADJ'
dict['binario']='ADJ'
dict['binarios']='ADJ'
dict['binaria']='ADJ'
dict['binarias']='ADJ'
dict['multinúcleo']='ADJ'
dict['bajo']='ADJ' #Mejor que la preposición
dict['baja']='ADJ'
dict['mismo']='ADJ'
dict['misma']='ADJ'
dict['semiconductor']='ADJ' #Es más común el nombre en plural y el adjetivo en singular
dict['duro']='ADJ'

#Verbos

dict['es']='VIP3S0'
dict['está']='VIP3S0'
dict['son']='VIP3P0'
dict['ha']='VAIP3S0'
dict['ejecuta']='VIP3S0'

#Pronombres

dict['se']='PRON'
dict['le']='PRON'
dict['lo']='PRON' #Mejor que el artículo

#Nombres

dict['informática']='NCFS' #El término masculino parece ser más común como adjetivo (y el femenino plural)
dict['programa']='NCMS'
dict['programas']='NCMP'
dict['programadores']='NCMP'
dict['procesadores']='NCMP'
dict['microprocesadores']='NCMP'
dict['sistema']='NCMS'
dict['sistemas']='NCMP'
dict['componente']='NCMS'
dict['componentes']='NCMP' #Para compensar la regexp que coge -es como plural femenino.
dict['circuito']='NCMS'
dict['circuitos']='NCMP'
dict['unidad']='NCFS'
dict['soporte']='NCMS'
dict['cliente']='NCMS'
dict['clientes']='NCMP'
dict['fuente']='NCFS'
dict['periférico']='NCMS'
dict['periféricos']='NCMP'
dict['lenguaje']='NCMS'
dict['intérprete']='NCMS'
dict['archivo']='NCMS'
dict['archivos']='NCMP'
dict['interfaz']='NCFS'
dict['semiconductores']='NCMP'
dict['paradigma']='NCMS'
dict['paradigmas']='NCMP'
dict['entrada']='NCFS' #Evitar que los seleccione como adjetivos
dict['entradas']='NCFP'
dict['salida']='NCFS'
dict['salidas']='NCFP'
dict['entrada/salida']='NCFS'
dict['dispositivo']='NCMS'
dict['dispositivos']='NCMP'
dict['encendido']='NCMS'
dict['estado']='NCMS'
dict['estados']='NCMP'

#Numerales

dict['uno']='NUM'
dict['dos']='NUM'
dict['tres']='NUM'
dict['cuatro']='NUM'
dict['cinco']='NUM'
dict['seis']='NUM'
dict['siete']='NUM'
dict['ocho']='NUM'
dict['nueve']='NUM'
dict['diez']='NUM'
dict['primer']='NUM'
dict['primero']='NUM'
dict['primera']='NUM'
dict['primeros']='NUM'
dict['segundo']='NUM'
dict['segunda']='NUM'
dict['segundos']='NUM'
dict['tercero']='NUM'
dict['tercera']='NUM'
dict['terceros']='NUM'

#Adverbios

dict['como']='ADV'
dict['más']='ADV'
dict['así']='ADV'
dict['mediante']='ADV'
dict['solo']='ADV'
dict['sólo']='ADV'
dict['no']='ADV'
dict['sí']='ADV'

#Abreviaturas

dict['cpu']='ABRV'
dict['etc']='ABRV'
dict['bios']='ABRV'
dict['ram']='ABRV'
dict['rom']='ABRV'
dict['ci']='ABRV'


#Aquí hay se añaden las palabras del diccionario y sus etiquetas

p=[
    (r'^[Cc]uy(o|a|os|as)$', 'PRON'),
    (r'^[Mm]uch(o|a|os|as)$', 'ADJ'),
    (r'^[Tt]od(o|a|os|as)$', 'ADJ'),
    (r'^[Cc]ual(quiera?)?$', 'PRON'),
    (r'^[Ee]st(e|a|o|os|as)$', 'PRON'),
    (r'^[Aa]lg(u|ú)n(o|a|os|as)?$', 'PRON'),
    (r'^[Oo]tr(o|a|os|as)$', 'DET'),
    (r'^[Uu]n(a|os|as)?$', 'DET'),
    (r'^[.,\(\);:\"\']$', 'PUNT'),
    (r'^([Ee]l|[Ll](a|os|as))$', 'ART'),
    (r'^[0-9]+(.[0-9]+)?$', 'NUM'),
    (r'.+mente$', 'ADV'), #Se usa '+' para evitar que trate el nombre 'mente' como adverbio.
    (r'.*ware$','NCMS'),
    (r'.*(aron|eron)$', 'VIS3P0'),
    (r'.*amos$','VIP1S'),
    (r'.*imos$','VIP1S'),
    (r'.*rl(o|a)s?$', 'VN'), #La terminación es un pronombre, que en este caso no se trata
    (r'.*aban$', 'VII3P0'),
    (r'.*ían$', 'VII3P0'),
    (r'.*(icos?|icas?)$', 'ADJ'),
    (r'.*(ados|idos)$', 'VP00PM'),
    (r'.*(adas|idas)$', 'VP00PF'),
    (r'.*bles?$', 'ADJ'),
    (r'.*ivos?$','ADJ'),
    (r'.*aba$', 'VII3S0'),
    (r'.*dad$', 'NCFS'),
    (r'.*(ado|ido)$', 'VP00SM'),
    (r'.*(ada|ida)$', 'VP00SF'),
    (r'.*ndo$', 'VG'),
    (r'.*ble$', 'ADJ'),
    (r'.*ión$','NCFS'),
    (r'.*rse$', 'VN'), #La terminación -se es un pronombre
    (r'.*it[oa]$', 'ADJ'),
    (r'.*(ar|er|ir)$', 'VN'),
    (r'.*ía$', 'VII3S0'),
    (r'.*ez$', 'NCMS'),
    (r'.*al$', 'ADJ'), #En este contexto, parece más probable que palabras acabadas en -al sean adjetivos a nombres
    (r'.*(as|es)$', 'NCFP'), #Parece más probable encontrar plurales femeninos acabados en -es que masculinos
    (r'.*os$', 'NCMP'),
    (r'.*(en|an)$', 'VIP3P0'),
    (r'.*e$', 'VIP3S0'), #Vale la pena incluir palabras que no cumplan esto en el diccionario porque los verbos son mayoría
    (r'.*a$','NCFS'),
    (r'.*ó$', 'VIS3S0'),
    (r'.*$','NCMS'),
    #Aquí hay se añaden los patrones necesarios
    ]




rt=nltk.RegexpTagger(p)
taggedText=rt.tag(words)
prueba={}
count = 0
for item in taggedText:
    if dict.has_key(item[0].lower()):
        print(item[0] + ' ' + dict[item[0].lower()])
        prueba[count]=(item[0], dict[item[0].lower()])
    else:
        print(item[0] + ' ' + item[1])
        prueba[count]=(item[0], item[1])
    count+=1

#print('Eficiencia: {}'.format(test.efficiency(prueba)))

sys.exit()
