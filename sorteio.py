#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gincalouros import *
from string import join

calouros = capturar('gincalouros.xls')

numero = input('Entre com a quantidade de grupos: ')

grupos = criar_grupos(numero)

sorteio(calouros, grupos)

for total in range(len(grupos)):
    nome_planilha = ' '.join(['grupo', str(total+1)])
    grupo_nome = grupos[total].nomes()
    grupo_pasta = grupos[total].pastas()
    exportar(nome_planilha, grupo_nome, grupo_pasta)

out = raw_input('Entre com o nome do novo arquivo: ')

out_xls = '.'.join([out,'xls'])

salvar(out_xls)
