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

file = open("programa.txt", "r")
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
estadoF = AFND[4]

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
print (G.transicoes('q1'))
'''
#AFD
print ('TESTE-----------------------------')
states = list(G.estados())
new_state = ''
afd = {}
afd[estadoI] = True
aux2 = ''
        


for i in range(0,len(states)):
    aux = G.transicoes(states[i])
    print(aux)
    #print i, aux
    b = '->' #estados
    a = ''   #terminais

    for j in range(0,len(aux)):
        #print i,j
        aux2 = aux[j]
        #print aux2
        ##print (a, '/', aux2[0])
        if a == aux2[0]:
            a = aux2[0] + '/'
            b += aux2[1] + ','           
        else:
            a += aux2[0]
            b += '/' + aux2[1] + ',' 
        
        print (a + b)
    afd["q{0}".format(i)] = a + b[:-1]



print (afd)
'''

### Testes ipython
'''
afd = {'q0': 'P/->/q1q2', 'q1': 'Ip/->/q2q3', 'q2': 'Iq/->/q1q3', 'q3': 'M->/q4', 'q4': 'P/Pf->/q1q2/q0'}
state_A = afd['q0'][5:].split(',')
A = afd['q0'][5:] #precisa ser string
st_A = state_A[:-1]
b =''
final = {}
for s in st_A:
    a = afd[s] 
    b = b + a
    final[A] = b

In [106]: final
Out[106]: {'q1,q2,': 'Ip/->/q2,q3,Iq/->/q1,q3,Ip/->/q2,q3,Iq/->/q1,q3,'}
'''




#AFD
print()
print()
print ('---- TESTE 2 -----------------------------')
afd2 = {}
afd2[estadoI] = True
n = len(afd2.keys())

#problema ---> len(afd2.keyd()) não ta atualizando quando adiciona um novo estado em afd2
for i in range(0, n):
    estadosAFD = list(afd2.keys())
    transicoes = G.transicoes(estadosAFD[i])
    print("exemplo ", transicoes)
    for j in range(0, len(palavras)):
        new_estado = ""
        for k in range(0, len(transicoes)):
            if (palavras[j] == transicoes[k][0]):
                new_estado += transicoes[k][1] + ","
        if (new_estado != ""):
            new_estado = new_estado[:-1] #retira a ultima virgula
            afd2[new_estado] = True #adiciona o novo estado no afd2
            n = n+1


print(afd2.keys())