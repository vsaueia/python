# -*- coding: UTF-8 -*-
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):
    def calcular(self, orcamento):
        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(Sem_desconto())).aplicar(orcamento)
        return desconto

if __name__ == '__main__':
    from orcamento import Orcamento, Item
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 100))
    
    calculador = Calculador_de_descontos()
    desconto_calculado = calculador.calcular(orcamento)
    print 'Desconto calculado = %s' % (desconto_calculado)
