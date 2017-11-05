# Trabalho Final - Linguagens Formais e Autômatos
Requisitos: Python 3.6

Este programa realiza a conversão de um Autômato finito não determinístico(AFND) para um Autômato finito determinístico(AFD). Além disso,
ele reconhece as palavras aceitas pela linguagem do Autômato.

Para a executação correta do programa, edite o arquivo programa.txt de acordo com o exemplo:

-Automato M=;estados do automato;simbolos aceitos;estado inicial;estado final

  -ex: M=;q0,q1,q2,q3,q4;P,p,q,m,F;q0;q0

-Transição (estado atual, simbolo lido)=proximo estado

  -ex: (q0,P)=q1

Após editar o programa, excecute com python 3.6 o programaAutomatos.py na mesma pasta que estiver o arquivo programa.txt. Ao executá-lo
ele irá imprimir a equivalência entre os autômatos e pedirá a inserção de palavras para testar a validade de tal.

Para sair do programa, basta clicar exit.
