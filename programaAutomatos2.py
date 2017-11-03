#coding: utf-8

class Grafo:
    def __init__(self):
        self.lista_vizinhos = {}
        self.lista_vertices = {}
    
    def add_vertice(self, vertice):
        self.lista_vertices[vertice] = True
    
    def add_aresta(self, qa, qb, palavra):
    	#se nao existe estado qa nao add
        if not qa in self.lista_vizinhos:
            self.lista_vizinhos[qa] = []
        #add qb e w como uma transicao de qa
        self.lista_vizinhos[qa].append([palavra,qb])
    
    def transicoes(self, qa):
        if qa in self.lista_vizinhos:
        	#retorna as transicoes de um estado qa
            return self.lista_vizinhos[qa]
        else:
            return []
    
    def estados(self):
        return self.lista_vertices.keys()

    def deleta_aresta(self, vertice, outro_vertice):
        self.vizinhos(vertice).remove(outro_vertice)
    
    def deleta_vertice(self, vertice):
        for outro_vertice in self.lista_vizinhos[vertice]:
            self.deleta_aresta(vertice, outro_vertice)
        del self.lista_vizinhos[vertice]
        del self.lista_vertices[vertice]

file = open("programa2.txt", "r")
words = []
transitions = []
#Leitura do arquivo
for i in file:
    for word in i.split():
        words.append(word)

#Organização do arquivo
AFND = words[0]
AFND = AFND.split(";")
estados = AFND[1].split(',')
palavras = AFND[2].split(',')
estadoI = AFND[3]
estadoF = AFND[4].split(',')

for i in range (2, len(words)):
    transitions.append(words [i])


G = Grafo()

#adiciona os estados no grafo
for i in range (0, len(estados)):
	G.add_vertice(estados[i])

#add transicoes no grafo (qa -> qb)
for i in range (0, len(transitions)):
	#quebra a string -> aux[0] = (qa,w) e aux[1] = qb
	aux = transitions[i].split("=")
	#retira parenteses
	aux[0] = aux[0][1:]
	aux[0] = aux[0][:-1]
	#quebra a string em qa e w
	aux[0] = aux[0].split(",")
	#add transicao
	G.add_aresta(aux[0][0],aux[1],aux[0][1])

print ("AFND: ",AFND)
print ("Estados: ",estados)
print ("Palvras: ",palavras)
print ("Estado inicial: ",estadoI)
print ("Estado final: ",estadoF)
print ("Transicoes:",transitions)
print ("")
print ("")

print (G.estados())
print ('transicoes',G.transicoes('p'))



#AFD
print()
print()
print ('---- TESTE 2 -----------------------------')
afd2 = {}
afd2[estadoI] = True
n = len(afd2.keys())
i = 0

G_AFD = Grafo()
novos_estados_finais = []

#problema ---> len(afd2.keyd()) não ta atualizando quando adiciona um novo estado em afd2
while(i < n):
    if (i >= len(afd2.keys())): break;
    estadosAFD = list(afd2.keys())
    estadoAux = estadosAFD[i].split(",") #quebra o estado em virgulas
    for l in range(0, len(estadoAux)):
        transicoes = G.transicoes(estadoAux[l])
        print("estados ", estadosAFD)
        print("transicoes ", transicoes)
        for j in range(0, len(palavras)):
            new_estado = ""
            for k in range(0, len(transicoes)):
                if (palavras[j] == transicoes[k][0]):
                    new_estado += transicoes[k][1] + ","
            if (new_estado != ""):
                new_estado = new_estado[:-1] #retira a ultima virgula
                afd2[new_estado] = True #adiciona o novo estado no afd2
                n += 1
                #add no grafo (new_estado)
                G_AFD.add_vertice(estadosAFD[i])


                #MERDA DOS ESTADOS FINAIS 
                for e in estadoF:
                    aux233 = estadosAFD[i].split(",")
                    for m in range(0, len(aux233)):
                        print e, '////', aux233
                        if e in aux233[m]:
                            novos_estados_finais.append(estadosAFD[i])

                #add aresta (estadosAFD[i]  ==palavras[j]==>  new_estado)
                G_AFD.add_aresta(estadosAFD[i], new_estado, palavras[j])
    i += 1
               
print('NOVO GRAFO')
print (novos_estados_finais)
print(G_AFD.estados())
print ('q0:', G_AFD.transicoes('q0'))
print ('q1q2:',G_AFD.transicoes('q1,q2'))
print ('q2q3:',G_AFD.transicoes('q2,q3'))
print ('q1q3:',G_AFD.transicoes('q1,q3'))
print ('q4:',G_AFD.transicoes('q4'))

#print(afd2.keys())



a = 'PpqmF'
estadoAtual = estadoI
resp = True

for i in a:
    proximo_estado = False

    t = G_AFD.transicoes(estadoAtual)
    for j in G_AFD.transicoes(estadoAtual):
        print(i,'//',j[0])
        if i == j[0]:
            proximo_estado = True
            estadoAtual = j[1]
    if proximo_estado == False:
        resp = False

for e in novos_estados_finais:
    if e != estadoAtual:
        resp = False 
    

        
print(resp)