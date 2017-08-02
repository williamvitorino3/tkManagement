# -*- coding: utf-8 -*-

u"""Implementação da tela principal do projeto."""

from model import cliente_db as db
from platform import system as SO
from datetime import datetime
from tkinter import ttk
import view.componentes as wid
import clusores as validacao
import tkinter as tk
if SO().lower() == "windows":
    import defaults_win as style
else:
    import defaults as style

# TODO: Resolver imcompatibilidade do tamanho dos widgets do windows.
# TODO: Mudar "Cadastrado a" para "Atendido a".
# TODO: Alterar a cor dos botões.

class Janela(object):
    u"""Implementação da janela."""

    def __init__(self, root):
        """Construtor da classe."""
        self.janela = tk.Frame(root, **style.BORDA)
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        # Frame paraa manipulação dos dados.
        self.frame_management = tk.Frame(self.janela, **style.BORDA)
        # Frame para a saída de dados.
        self.frame_output = tk.Frame(self.janela, **style.BORDA)

        self.frame_dados_cliente = tk.Frame(self.frame_management, **style.BORDA)
        self.frame_botoes_acao = tk.Frame(self.frame_management, **style.BORDA)

        # Gerência de dados.
        self.nome = wid.TextBox(self.frame_dados_cliente, text="Nome")
        self.data_nasc = wid.TextBox(self.frame_dados_cliente, text="Data Nascimento")
        self.data_nasc.entry.configure(width=int(self.data_nasc.entry["width"]*0.4))
        self.atendimento = wid.ChooseMenu(self.frame_dados_cliente, text="Atendimento")
        self.botoes = wid.FrameButtons(self.frame_botoes_acao)

        # Saída dedados.
        self.pesquisa = wid.SearchBox(self.frame_output, text="Pesquisa")
        self.lista_clientes = wid.Lista(self.frame_output)
        self.clientes = []
        self._lest_id_ = 0
        self._main_()

    def add_collunms(self):
        """Adiciona as colunas na tabela."""
        self.lista_clientes.list.add_colunm("Último Atendimento", width=style.WIDTH_COLUNM)
        self.lista_clientes.list.add_colunm("Nome", width=style.WIDTH_COLUNM)
        self.lista_clientes.list.add_colunm("Data Nascimento", width=style.WIDTH_COLUNM)
        self.lista_clientes.list.add_colunm("Tipo de Atendimento", width=style.WIDTH_COLUNM)
        self.lista_clientes.list.add_colunm("Atendido há", width=style.WIDTH_COLUNM)

    def configure_buttons(self):
        """Configura os botões."""
        self.botoes.add_button.configure(command=self.adicionar)
        self.botoes.remove_button.configure(command=self.remover)
        self.botoes.edit_button.configure(command=self.editar)
        self.pesquisa.button.configure(command=self.pesquisar)
        self.pesquisa.entry.bind("<Return>", self.pesquisar)

    def _main_(self):
        u"""Método principal da Classe."""
        self.add_collunms()
        self.configure_buttons()
        self.pack(padx=7)
        self.atualizar()

    def pack(self, **kwargs):
        """Plota os componentes na tela."""
        self.janela.pack(**kwargs)
        self.frame_management.pack(side=tk.TOP)
        self.frame_output.pack(side=tk.TOP)
        self.frame_dados_cliente.pack(side=tk.RIGHT)
        self.frame_botoes_acao.pack(side=tk.LEFT)
        self.botoes.pack(side=tk.TOP)
        self.nome.pack(side=tk.TOP, pady=16)
        self.data_nasc.pack(side=tk.LEFT, pady=16)
        self.atendimento.pack(side=tk.LEFT, pady=16)
        self.pesquisa.pack(side=tk.TOP)
        self.lista_clientes.pack(side=tk.TOP)

    def set_clientes(self):
        """Adiciona os dados na lista de clientes."""
        for cliente in self.clientes[::-1]:
            self.lista_clientes.insert("Nome", cliente[1])
            self.lista_clientes.insert("Último Atendimento", cliente[2])
            self.lista_clientes.insert("Data Nascimento", self._formata_data_(cliente[3]))
            self.lista_clientes.insert("Tipo de Atendimento", cliente[4])
            self.lista_clientes.insert("Atendido há", self._ultima_consulta_(cliente))

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
