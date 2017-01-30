# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod


class Imposto(object):
    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    @abstractmethod
    def calcular(self, orcamento):
        pass

    def calcular_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        return self.__outro_imposto.calcular(orcamento)


class Template_de_imposto_condicional(Imposto):
    __metaclass__ = ABCMeta

    def calcular(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calcular_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calcular_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


def IPVX(metodo_ou_funcao):
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50.0
    return wrapper


class ISS(Imposto):
    @IPVX
    def calcular(self, orcamento):
        return orcamento.valor * 0.1 + self.calcular_outro_imposto(orcamento)


class ICMS(Imposto):
    def calcular(self, orcamento):
        return orcamento.valor * 0.06 + self.calcular_outro_imposto(orcamento)


class ICPP(Template_de_imposto_condicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.03


class IKCV(Template_de_imposto_condicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_cem_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.04

    def __tem_item_maior_que_cem_reais(self, orcamento):
        for item in orcamento.obter_itens:
            if item.valor > 100:
                return True
        return False
