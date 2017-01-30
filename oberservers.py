# -*- coding: UTF-8 -*-
def imprimir(nota_fiscal):
    print 'Imprimindo nota fiscal %s' % (nota_fiscal.cnpj)

def enviar_por_email(nota_fiscal):
    print 'Enviando nota fiscal %s por email' % (nota_fiscal.cnpj)

def persistir(nota_fiscal):
    print 'Persistindo nota fiscal %s no banco de dados' % (nota_fiscal.cnpj)