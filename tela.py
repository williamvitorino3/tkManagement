# -*- coding: utf-8 -*-

u"""Implementação da tela principal do projeto."""

import tkinter as tk
import componentes as wid
import cliente_db as db
# TODO: Adicionar confirmação da remoção.
# TODO: Quantos dias a pessoas esta cadastrada.
# TODO: Tempo do último atendimento.
# TODO: Implementar um componente de data.


class Janela(object):
    u"""Implementação da janela."""

    def __init__(self, root):
        """Construtor da classe."""
        self.janela = tk.Frame(root)
        self.nome = wid.TextBox(self.janela, text="Nome")
        self.data_nasc = wid.TextBox(self.janela, text="Data Nascimento")
        self.atendimento = wid.ChooseMenu(self.janela,
                                          text="Tipo de Atendimento")
        self.pesquisa = wid.SearchBox(self.janela, text="Pesquisa")
        self.lista_clientes = wid.Lista(self.janela)
        self.clientes = []
        self._lest_id_ = 0
        self._main_()

    def _main_(self):
        u"""Método principal da Classe."""
        self.lista_clientes.list.add_colunm("Data do Atendimento", width=32)
        self.lista_clientes.list.add_colunm("Nome", width=32)
        self.lista_clientes.list.add_colunm("Data Nascimento", width=32)
        self.lista_clientes.list.add_colunm("Tipo de Atendimento", width=32)
        self.lista_clientes.list.add_colunm("Cadastrado à", width=32)
        self.lista_clientes.add_button.configure(command=self.adicionar)
        self.lista_clientes.remove_button.configure(command=self.remover)
        self.lista_clientes.edit_button.configure(command=self.editar)
        self.pesquisa.button.configure(command=self.pesquisar)
        self.janela.pack()
        self.nome.pack(side=tk.TOP)
        self.data_nasc.pack(side=tk.TOP)
        self.atendimento.pack(side=tk.TOP)
        self.pesquisa.pack(side=tk.TOP)
        self.lista_clientes.pack()
        self.atualizar()

    def set_clientes(self):
        """Adiciona os dados na lista de clientes."""
        for cliente in self.clientes:
            self.lista_clientes.insert("Nome", cliente[1])
            self.lista_clientes.insert("Data do Atendimento", cliente[2])
            self.lista_clientes.insert("Data Nascimento", cliente[3])
            self.lista_clientes.insert("Tipo de Atendimento", cliente[4])

    def _pesquisa_init_(self):
        """Pesquisa inicial da tela."""
        self.clientes = db.buscar_all()
        self.set_clientes()

    def adicionar(self):
        """Adiciona os dados dos campon no banco."""
        db.inserir(self.nome.entry.get(), self.data_nasc.entry.get(),
                   self.atendimento.get())
        self._limpar_entradas_()
        self.atualizar()

    def remover(self):
        """Deleta os itens selecionados."""
        pos = 0
        for i in self.lista_clientes.list.curselection():
            item_pos = int(i) - pos
            item = self.clientes[item_pos][0]
            db.remover(item)
            self.lista_clientes.list.delete(item_pos, item_pos)
            pos = pos + 1

    def atualizar(self):
        """Atualiza os dados da tabela."""
        self.lista = self.lista_clientes.reset()
        self.pesquisa.entry.focus_force()
        self._pesquisa_init_()

    def _limpar_entradas_(self):
        """Limpa os campos de preenchimento."""
        self.nome.entry.delete(0, tk.END)
        self.data_nasc.entry.delete(0, tk.END)
        self.atendimento.entry.delete(0, tk.END)

    def _edicao_(self):
        if self.lista_clientes.add_button["text"] == "Cadastrar":
            self.lista_clientes.add_button.configure(text="Atualizar",
                                                     command=self.update)
        elif self.lista_clientes.add_button["text"] == "Atualizar":
            self.lista_clientes.add_button.configure(text="Adicionar",
                                                     command=self.adicionar)

    def pesquisar(self):
        """Pesquisa clientes no banco."""
        # TODO: Encontrar um modo melhor de fazer isso.
        print(__name__)
        self.lista = self.lista_clientes.reset()
        self.clientes = db.buscar(self.pesquisa.entry.get())
        self.set_clientes()
        self.pesquisa.entry.delete(0, tk.END)

    def update(self):
        """Atualiza os dados do cliente no Banco de Dados."""
        db.atualizar(self._lest_id_, self.nome.entry.get(),
                     self.data_nasc.entry.get(), self.atendimento.get())
        self._edicao_()
        self._limpar_entradas_()
        self.atualizar()

    def editar(self):
        u"""Habilita para edição o cliente selecionado."""
        self._limpar_entradas_()
        self._edicao_()
        for i in self.lista_clientes.list.curselection():
            pos = int(i)
            self._lest_id_ = self.clientes[pos][0]
            self.nome.entry.insert(0, self.clientes[pos][1])
            self.data_nasc.entry.insert(0, self.clientes[pos][3])
            self.atendimento.entry.insert(0, self.clientes[pos][4])
