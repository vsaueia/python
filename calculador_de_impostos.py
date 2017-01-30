# -*- coding: UTF-8 -*-
from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):
    def realizar_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcular(orcamento)
        print imposto_calculado

if __name__ == '__main__':
    from orcamento import Orcamento, Item
    calculador = Calculador_de_impostos()
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 50))
    orcamento.adiciona_item(Item('Item 2', 20))
    orcamento.adiciona_item(Item('Item 3', 250))
    calculador.realizar_calculo(orcamento, ISS())
    calculador.realizar_calculo(orcamento, ICMS())
    calculador.realizar_calculo(orcamento, ICMS(ISS()))
    calculador.realizar_calculo(orcamento, ICPP())
    calculador.realizar_calculo(orcamento, IKCV())
    calculador.realizar_calculo(orcamento, IKCV(ICPP()))
