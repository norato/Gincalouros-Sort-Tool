#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from should_dsl import should
from gincalouros import Calouro, Grupo
from xlwt   import Workbook
import xlwt

class TestGincalouros(unittest.TestCase):

    calouro_1 = Calouro('11', 'Joao Felipe','123', '0000', 'otal')
    calouro_2 = Calouro('1','Gabriel Campista','432', '1111', 'otal')
    calouro_3 = Calouro('2','Rodrigo Otal','243', '2222', 'otal')


    def test_conferir_cadastro(self):
        self.calouro_1.nome |should| equal_to('Joao Felipe')
        self.calouro_2.numero |should| equal_to('1')
        self.calouro_3.pasta |should| equal_to('243')

    grupo1 = Grupo()
    grupo2 = Grupo()
    grupo3 = Grupo()

    grupo1.adicionar(calouro_1)
    grupo1.adicionar(calouro_2)
    grupo2.adicionar(calouro_3)

    def test_adicionar_calouro_em_grupo(self):
        self.grupo1.nomes() |should| equal_to(['Joao Felipe', 'Gabriel Campista'])
        self.grupo2.nomes() |should| equal_to(['Rodrigo Otal'])
        self.grupo3.nomes() |should| equal_to([])


if __name__ == "__main__":
    unittest.main
