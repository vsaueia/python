# -*- coding: UTF-8 -*-
from datetime import date
from oberservers import imprimir, enviar_por_email, persistir

class Item(object):
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal(object):
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observers=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota nao pode ter mais que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

        for observer in observers:
            observer(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':
    from oberservers import imprimir, enviar_por_email, persistir

    itens = [Item('Item A', 10.0), Item('Item B', 20.0)]
    observers=[imprimir, enviar_por_email, persistir]
    nota_fiscal = Nota_fiscal(razao_social='VSA Ltda',
                    cnpj='123123123',itens=itens, observers=observers)
    print nota_fiscal.cnpj
