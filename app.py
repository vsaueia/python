# -*- coding: UTF-8 -*-
def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def imprimir(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def menu():
    nomes = []
    opcao = '';
    while (opcao != '0'):
        print 'Digite 1 para cadastrar, 2 para mostrar nomes, 0 para terminar'
        opcao = raw_input()
        if(opcao == '1'):
            cadastrar(nomes)
        if(opcao == '2'):
            imprimir(nomes)
menu()
