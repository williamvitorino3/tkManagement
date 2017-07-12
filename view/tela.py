# -*- coding: utf-8 -*-

u"""Implementação da tela principal do projeto."""

from datetime import datetime
from model import cliente_db as db
import view.componentes as wid
import clusores as validacao
import tkinter as tk
from tkinter import ttk
import defaults as style

# TODO: Resolver imcompatibilidade do tamanho dos widgets do windows.


class Janela(object):
    u"""Implementação da janela."""

    def __init__(self, root):
        """Construtor da classe."""
        self.janela = tk.Frame(root, **style.BORDA)
        self.frame_dados_cliente = tk.Frame(self.janela, **style.BORDA)
        self.nome = wid.TextBox(self.frame_dados_cliente, text="Nome")
        self.data_nasc = wid.TextBox(self.frame_dados_cliente, text="Data Nascimento")
        self.data_nasc.entry.configure(width=58)
        self.atendimento = wid.ChooseMenu(self.frame_dados_cliente, text="Atendimento")
        self.botoes = wid.FrameButtons(self.janela)
        self.pesquisa = wid.SearchBox(self.janela, text="Pesquisa")
        self.lista_clientes = wid.Lista(self.janela)
        self.clientes = []
        self._lest_id_ = 0
        self._main_()

    def _main_(self):
        u"""Método principal da Classe."""
        self.lista_clientes.list.add_colunm("Último Atendimento", width=31)
        self.lista_clientes.list.add_colunm("Nome", width=32)
        self.lista_clientes.list.add_colunm("Data Nascimento", width=31)
        self.lista_clientes.list.add_colunm("Tipo de Atendimento", width=32)
        self.lista_clientes.list.add_colunm("Cadastrado à", width=32)
        self.botoes.add_button.configure(command=self.adicionar)
        self.botoes.remove_button.configure(command=self.remover)
        self.botoes.edit_button.configure(command=self.editar)
        self.pesquisa.button.configure(command=self.pesquisar)
        self.pesquisa.entry.bind("<Return>", self.pesquisar)
        self.janela.pack()
        self.frame_dados_cliente.pack()
        self.nome.pack(side=tk.TOP)
        self.data_nasc.pack(side=tk.LEFT)
        self.atendimento.pack(side=tk.LEFT)
        self.botoes.pack(side=tk.TOP)
        self.pesquisa.pack(side=tk.TOP)
        self.lista_clientes.pack()
        self.atualizar()

    def set_clientes(self):
        """Adiciona os dados na lista de clientes."""
        for cliente in self.clientes[::-1]:
            self.lista_clientes.insert("Nome", cliente[1])
            self.lista_clientes.insert("Último Atendimento", cliente[2])
            self.lista_clientes.insert("Data Nascimento", self._formata_data_(cliente[3]))
            self.lista_clientes.insert("Tipo de Atendimento", cliente[4])
            self.lista_clientes.insert("Cadastrado à", self._ultima_consulta_(cliente))

    def _formata_data_(self, data):
        """Formata a data no formato dd/mm/yyy"""
        return "{0:02d}/{1:02d}/{2:04d}".format(*[int(i) for i in data.split('/')])

    def _pesquisa_init_(self):
        """Pesquisa inicial da tela."""
        self.clientes = db.buscar_all()
        self.set_clientes()

    @validacao.insercao
    def adicionar(self):
        """Adiciona os dados dos campon no banco."""
        db.inserir(self.nome.entry.get(), self.data_nasc.entry.get(),
                   self.atendimento.get())
        self._limpar_entradas_()
        self.atualizar()

    @validacao.remocao
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
        self.lista_clientes.reset()
        self.clientes.clear()
        self.pesquisa.entry.focus_force()
        self._pesquisa_init_()

    def _limpar_entradas_(self):
        """Limpa os campos de preenchimento."""
        self.nome.entry.delete(0, tk.END)
        self.data_nasc.entry.delete(0, tk.END)
        self.atendimento.set("")

    def _edicao_(self):
        """
        Faz a atualização da tela,  necesária para a edição
        de um paciente.
        """
        if self.botoes.add_button["text"] == "Cadastrar":
            self.botoes.add_button.configure(text="Atualizar", command=self.update)

    @validacao.successful
    def pesquisar(self, event=None):
        """Pesquisa clientes no banco."""
        self.lista_clientes.reset()
        self.clientes.clear()
        self.clientes = db.buscar(self.pesquisa.entry.get())
        self.set_clientes()
        self.pesquisa.entry.delete(0, tk.END)

    @validacao.insercao
    def update(self):
        """Atualiza os dados do cliente no Banco de Dados."""
        db.atualizar(self._lest_id_, self.nome.entry.get(),
                     self.data_nasc.entry.get(), self.atendimento.get())
        if self.botoes.add_button["text"] == "Atualizar":
            self.botoes.add_button.configure(text="Cadastrar", command=self.adicionar)
        self._limpar_entradas_()
        self.atualizar()

    def editar(self):
        u"""Habilita para edição o cliente selecionado."""
        try:
            self._limpar_entradas_()
            for i in self.lista_clientes.list.curselection():
                pos = int(i)
                self._lest_id_ = self.clientes[pos][0]
                self.nome.entry.insert(0, self.clientes[pos][1])
                self.data_nasc.entry.insert(0, self.clientes[pos][3])
                self.atendimento.set(self.clientes[pos][4])
            self._edicao_()
        except TypeError:
            pass

    def _ultima_consulta_(self, cliente):
        """
        Calcula a quantidade de dias do ultima
        consulta do cliente.
        """
        tempo = datetime.now() - datetime(*[int(i) for i in cliente[2].split('/')[::-1]])
        return "%d dia%s" %(tempo.days, "" if tempo.days == 1 else "s")
