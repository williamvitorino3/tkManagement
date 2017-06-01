# -*- coding: utf-8 -*-

u"""
Widget de lista com multiplas colunas.

Implementação de uma tabela.
"""

import tkinter as tk
from tkinter import ttk


class Coluna(object):
    u"""Abstração de uma coluna da tabela."""

    def __init__(self, master, text, width):
        """Construtor da classe."""
        self.janela = tk.Frame(master)
        self._cabecalho_ = tk.Label(self.janela, text=text)
        self.lista = tk.Listbox(self.janela, bd=2, width=width)
        self.rolagem = ttk.Scrollbar(self.janela, orient=tk.HORIZONTAL,
                                     command=self.lista.xview)
        self._cabecalho_.configure(width=width, bd=2, relief=tk.GROOVE)
        self.lista.configure(xscrollcommand=self.rolagem.set)

    def pack(self, **kwargs):
        """Empacota os Widgets na tela."""
        self.janela.pack(**kwargs)
        self.rolagem.pack(side=tk.BOTTOM, fill=tk.X)
        self._cabecalho_.pack()
        self.lista.pack(side=tk.LEFT)


class Tabela(object):
    u"""Implementação de uma tabela."""

    def __init__(self, master):
        """Construtor da classe."""
        self.frame = tk.Frame(master)
        self.rolagem = ttk.Scrollbar(self.frame, orient=tk.VERTICAL,
                                     command=self.mover)
        self.colunas = {}

    def mover(self, *args):
        """Move as Listbox no eixo Y."""
        for coluna in self.colunas:
            self.colunas[coluna].lista.yview(*args)

    def add_colunm(self, text="", width=20):
        """Adiciona uma coluna na tabela."""
        self.colunas[text] = (Coluna(self.frame, text, width))
        self.colunas[text].lista.configure(yscrollcommand=self.rolagem.set)
        self.colunas[text].pack(side=tk.LEFT)

    def pack(self, **kwargs):
        """Empacota os Widgets na tela."""
        self.rolagem.pack(side=tk.RIGHT, fill=tk.Y)
        self.frame.pack(**kwargs)

    def size(self):
        """Retorna a quantidade de itens no Widget."""
        temp = 0
        for coluna in self.colunas:
            temp = self.colunas[coluna].lista.size()
        return temp

    def insert(self, coluna="", arg=""):
        """Inseri dados na coluna especificada."""
        self.colunas[coluna].lista.insert(-1, arg)

    def curselection(self):
        u"""Devolve as posições selecionadas."""
        for coluna in self.colunas:
            if self.colunas[coluna].lista.curselection():
                return self.colunas[coluna].lista.curselection()

    def delete(self, *args):
        """Deleta os itens da lista."""
        for coluna in self.colunas:
            self.colunas[coluna].lista.delete(*args)


def exemplo():
    u"""Função de exemplo do componente."""
    janela = tk.Tk()
    table = Tabela(janela)
    table.pack()
    table.add_colunm("Nome")
    table.add_colunm("Data Nascimento")
    table.add_colunm("Plano")
    for i in range(3000000000000000000000000, 3000000000000000000000050):
        for line in table.colunas:
            table.colunas[line].lista.insert(tk.END, i)
    janela.mainloop()


if __name__ == '__main__':
    exemplo()
