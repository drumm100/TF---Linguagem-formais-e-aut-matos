#coding: utf-8

file = open("/home/16105077/Downloads/programa.txt", "r")
words = []
transitions = []
#Leitura do arquivo
for i in file:
    for word in i.split():
        words.append(word)

#Organização do arquivo
AFND = words[0]
AFND = AFND.split(";")
estados = AFND[1]
palavras = AFND[2]
estadoI = AFND[3]
estadoF = AFND[4]

for i in range (2, len(words)):
    transitions.append(words [i])



print "AFND: ",AFND
print "Estados: ",estados
print "Palvras: ",palavras
print "Estado inicial: ",estadoI
print "Estado final: ",estadoF
print "Transicoes:",transitions


#percorrer Transicoes com regras, procruar primeiro estado
#depois do '(', procurar parametor depois da ',', procurar estado
#direcional depois do '='.

