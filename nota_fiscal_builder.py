# -*- coding: UTF-8 -*-
from nota_fiscal import Nota_fiscal

class Nota_fiscal_builder(object):
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = ''

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes

    def construir(self):
        if self.__razao_social is None:
            raise Exception('Razao Social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('Cnpj deve ser preenchido')

        return Nota_fiscal(razao_social=self.__razao_social, cnpj=self.__cnpj,
                           data_de_emissao=self.__data_de_emissao, itens=self.__itens, detalhes=self.__detalhes)
