#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryFile
from random import choice
from xlwt import Workbook
import xlrd

calouros =[]
grupos =[]

class Calouro():

    def __init__(self, numero, nome, pasta, telefone, gremista):

        self.numero = numero
        self.nome = nome
        self.pasta = pasta
        self.telefone = telefone
        self.gremista = gremista


class Grupo():

    def __init__(self):
        self.lista =[]

    def adicionar(self, calouro):
        self.lista.append(calouro)

    def nomes(self):
        retorno =[]
        for calouros in range(len(self.lista)):
             retorno.append(self.lista[calouros].nome)
        return retorno

    def pastas(self):
        retorno =[]
        for calouros in range(len(self.lista)):
             retorno.append(self.lista[calouros].pasta)
        return retorno

def capturar(arq_xls):
    def xlread(arq_xls):
        xls = xlrd.open_workbook(arq_xls)
        plan = xls.sheets()[0]

        for i in xrange(2,plan.nrows):
            yield plan.row_values(i)
    for linha in xlread(arq_xls):
        if linha[1]:
           calouros.append(Calouro(*linha))
    return calouros

def criar_grupos(quantidade):
    for i in range(quantidade):
        grupos.append(Grupo())
    return grupos

def sorteio(calouros, grupos):
    i = 0
    while calouros:
        if len(grupos) <= i:
            i = 0
        grupos[i].adicionar(pop(calouros))
        i += 1

out = Workbook()

def exportar(nome_planilha, grupo_nome, grupo_pasta):
    planilha = out.add_sheet(nome_planilha)
    planilha.write(0,0,nome_planilha)
    planilha.write(1,0,'Nome')
    planilha.write(1,1,'Pasta')
    planilha.col(0).width = 10000
    for i in range(len(grupo_nome)):
        planilha.write(2+i,0,grupo_nome[i])
    for i in range(len(grupo_pasta)):
        planilha.write(2+i,1,grupo_pasta[i])

def salvar(out_xls):
    out.save(out_xls)
    out.save(TemporaryFile())

