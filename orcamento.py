# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod


class EstadoDoOrcamento(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplicar_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprovar(self, orcamento):
        pass

    @abstractmethod
    def reprovar(self, orcamento):
        pass

    @abstractmethod
    def finalizar(self, orcamento):
        pass


class Em_aprovacao(EstadoDoOrcamento):
    def aplicar_desconto_extra(self, orcamento):
        orcamento.adicionar_desconto_extra(orcamento.valor * 0.02)

    def aprovar(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprovar(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finalizar(self, orcamento):
        raise Exception('Orcamento em aprovacao nao pode ser finalizado')


class Aprovado(EstadoDoOrcamento):
    def aplicar_desconto_extra(self, orcamento):
        orcamento.adicionar_desconto_extra(orcamento.valor * 0.05)

    def aprovar(self, orcamento):
        raise Exception('Orcamento ja aprovado')

    def reprovar(self, orcamento):
        raise Exception('Orcamento aprovado nao pode ser reprovado')

    def finalizar(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoDoOrcamento):
    def aplicar_desconto_extra(self, orcamento):
        raise Exception('Orcamentos reprovados nao recebem desconto extra')

    def aprovar(self, orcamento):
        raise Exception('Orcamento reprovado nao pode ser alterado')

    def reprovar(self, orcamento):
        raise Exception('Orcamento reprovado nao pode ser alterado')

    def finalizar(self, orcamento):
        raise Exception('Orcamento reprovado nao pode ser alterado')


class Finalizado(EstadoDoOrcamento):
    def aplicar_desconto_extra(self, orcamento):
        raise Exception('Orcamentos finalizados nao recebem desconto extra')

    def aprovar(self, orcamento):
        raise Exception('Orcamento finalizado nao pode ser alterado')

    def reprovar(self, orcamento):
        raise Exception('Orcamento finalizado nao pode ser alterado')

    def finalizar(self, orcamento):
        raise Exception('Orcamento finalizado nao pode ser alterado')


class Orcamento(object):
    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    def aplicar_desconto_extra(self):
        self.estado_atual.aplicar_desconto_extra(self)

    def adicionar_desconto_extra(self, desconto):
        self.__desconto_extra = desconto

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_de_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    def aprovar(self):
        self.estado_atual.aprovar(orcamento)

    def reprovar(self):
        self.estado_atual.reprovar(orcamento)

    def finalizar(self):
        self.estado_atual.finalizar(orcamento)


class Item(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 100))
    orcamento.adiciona_item(Item('Item 2', 50))
    orcamento.adiciona_item(Item('Item 3', 400))

    print orcamento.valor
    orcamento.aprovar()
    orcamento.aplicar_desconto_extra()
    orcamento.finalizar()

    print orcamento.valor
