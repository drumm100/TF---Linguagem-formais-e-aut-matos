# coding: utf-8
from tkinter import *

#1==========Criação do Grafo=======================
class Grafo:
    def __init__(self):
        self.lista_vizinhos = {}
        self.lista_vertices = {}

    def add_vertice(self, vertice):
        self.lista_vertices[vertice] = True

    def add_aresta(self, qa, qb, palavra):
        # se nao existe estado qa nao add
        if not qa in self.lista_vizinhos:
            self.lista_vizinhos[qa] = []
        # add qb e w como uma transicao de qa
        self.lista_vizinhos[qa].append([palavra, qb])

    def transicoes(self, qa):
        if qa in self.lista_vizinhos:
            # retorna as transicoes de um estado qa
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


# 2============Leitura do arquivo================
file = open("programa.txt", "r")
words = []
transitions = []

for i in file:
    for word in i.split():
        words.append(word)

# Organização do arquivo
AFND = words[0]
AFND = AFND.split(";")
estados = AFND[1].split(',')
palavras = AFND[2].split(',')
estadoI = AFND[3]
estadoF = AFND[4].split(',')

for i in range(2, len(words)):
    transitions.append(words[i])

# 3============Criando AFND=======================
G = Grafo()  # Instanciando o AFND

for i in range(0, len(estados)):  # adiciona os estados no grafo
    G.add_vertice(estados[i])

for i in range(0, len(transitions)):  # add transicoes no grafo (qa -> qb)

    aux = transitions[i].split("=")  # quebra a string -> aux[0] = (qa,w) e aux[1] = qb
    aux[0] = aux[0][1:]  # retira parenteses
    aux[0] = aux[0][:-1]  # quebra a string em qa e w
    aux[0] = aux[0].split(",")
    G.add_aresta(aux[0][0], aux[1], aux[0][1])  # add transicao

# 4==========Criando AFD============================
afd2 = {}
afd2[estadoI] = True
n = len(afd2.keys())
i = 0

G_AFD = Grafo()  # instancia um novo grafo AFD
G_AFD.add_vertice(estadoI)  # add o estado inicial no novo grafo AFD
novos_estados_finais = []  # lista de estados finais do AFD

while (i < n and n < 30):  # Converte AFND para AFD enquanto já cria o novo grafo AFD
    if (i >= len(afd2.keys())): break;
    estadosAFD = list(afd2.keys())
    estadoAux = estadosAFD[i].split(",")  # quebra o estado em virgulas
    for j in range(0, len(palavras)):
        new_estado = ""
        for l in range(0, len(estadoAux)):
            transicoes = G.transicoes(estadoAux[l])
            for k in range(0, len(transicoes)):
                if (palavras[j] == transicoes[k][0]) and (transicoes[k][1] not in new_estado):
                    new_estado += transicoes[k][1] + ","

        if (new_estado != ""):
            new_estado = new_estado[:-1]  # retira a ultima virgula
            afd2[new_estado] = True  # adiciona o novo estado no afd2
            n += 1
            G_AFD.add_vertice(new_estado)  # add no grafo (new_estado)

            for e in estadoF:  # Cria os estados fianais
                aux233 = new_estado.split(",")
                for m in range(0, len(aux233)):
                    if (e in aux233[m]) and (new_estado not in novos_estados_finais):
                        novos_estados_finais.append(new_estado)

            G_AFD.add_aresta(estadosAFD[i], new_estado, palavras[j])
            # DEBUG MANUAL
            # print("estado criado ",estadosAFD[i], palavras[j], new_estado)
            # print("transicoes ", transicoes)
            # print("-------------------------")
    i += 1

# 5===============Verificacao da palavra===================================

def lerPalavra(x):
    a = str(x)
    estadoAtual = estadoI
    resp = True
    for i in a:
        proximo_estado = False

        t = G_AFD.transicoes(estadoAtual)
        for j in G_AFD.transicoes(estadoAtual):
            ##print(i,'//',j[0])   #Debug para conferir estados
            if i == j[0]:
                proximo_estado = True
                estadoAtual = j[1]
        if proximo_estado == False:
            resp = False

    for e in novos_estados_finais:
        if e != estadoAtual:
            resp = False
    print('Válida: ', resp)


# 6==========Print==============================
print('==========================================')
print('AFND')
print(AFND)
print('Prog')
for m in G.estados():
    print(m, ': ', G.transicoes(m))

print('==========================================')

print('AFD')
print(G_AFD.estados())
# print(novos_estados_finais)
print("Prog")
for m in G_AFD.estados():
    print(m, ": ", G_AFD.transicoes(m))





#7=============GUI=================================
def show_entry_fields():

   print("Palavra: %s" % (e1.get()))
   lerPalavra(e1.get())
   e1.delete(0, END)


#create the window
root = Tk()
root.title('Conversao AFND para AFD')
root.geometry('300x100')
Label(root, text = 'Digite a palavra:').grid(row=0)
e1 = Entry(root)
#e1.insert(10,"Teste")
e1.grid(row=0, column=1)
Button(root, text='Executar', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=3)
Button(root, text='Quit', command=root.quit).grid(row=3, column=1, sticky=W, pady=3)

root.mainloop()

