"""Pacote com componentes customizados."""
# -*- coding: utf-8 -*-


import tkinter as tk
import dafaults as tema
from table import Tabela


class ChooseMenu(object):
    u"""Implementação de menu de opções."""

    def __init__(self, tela, text):
        """Construtor da classe."""
        self.frame_bd = tk.Frame(tela)
        self.frame = tk.Frame(self.frame_bd)
        self.opcao = tk.StringVar()
        self.label = tk.Label(self.frame, text=text)
        self.escolha = tk.StringVar()
        self.entry = tk.Listbox(self.frame, listvariable=self.escolha)
        self.opcoes = tk.Menubutton(self.frame, text="Escolher")
        self._configure_()

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self.frame_bd.configure(bd=2, bg=tema.bg_borda)
        self.frame.configure(bd=10, bg=tema.bg_widget)
        self.label.configure(tema.CHOOSE_LISTBOX)
        self.entry.configure(width=135, bg=tema.bg_widget,
                             fg=tema.fg_widget, height=1, bd=2)
        self.opcoes.configure(width=12, **tema.CHOOSE_BUTTONS)
        self.opcoes.menu = tk.Menu(self.opcoes, tearoff=0)
        self.opcoes['menu'] = self.opcoes.menu
        for atendimento in tema.ATENDIMENTOS:
            self.insert_option(atendimento)
        self.opcoes.menu.configure(**tema.CHOOSE_BUTTONS)

    def set(self, item):
        """Setter da classe."""
        self.escolha.set(item[0])

    def pack(self, **kwargs):
        u"""Substituição do método pack()."""
        self.frame_bd.pack(**kwargs)
        self.frame.pack()
        self.label.pack(side=tk.LEFT)
        self.opcoes.pack(side=tk.RIGHT)
        self.entry.pack(side=tk.LEFT)

    def get(self):
        """Devolve o valor da escolha."""
        return self.escolha.get()

    def insert_option(self, label):
        u"""Substituição do método insert()."""
        self.opcoes.menu.add_radiobutton(label=label, variable=self.escolha)


class TextBox(object):
    u"""Implementação de um box com Label e Enty."""

    def __init__(self, tela, text):
        """Construtor da classe."""
        self.frame_bd = tk.Frame(tela)
        self.frame = tk.Frame(self.frame_bd)
        # self.frame = tk.Frame(tela, bd=10)
        self.length_line = tela.winfo_screenwidth()
        self.label = tk.Label(self.frame, text=text)
        self.entry = tk.Entry(self.frame)
        self._configure_()

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self.frame_bd.configure(bd=2, bg=tema.bg_borda)
        self.frame.configure(bd=10, bg=tema.bg_widget)
        self.label.configure(bg=tema.bg_widget, fg=tema.fg_widget, width=20)
        self.entry.configure(**tema.ENTRY_TEXT)

    def pack(self, side=tk.TOP):
        u"""Substituição do método pack()."""
        self.frame_bd.pack(side=side)
        self.frame.pack()
        self.label.pack(side=tk.LEFT)
        self.entry.pack(side=tk.RIGHT)

    def insert(self, *args):
        """Substituição do método insert()."""
        self.entry.insert(0, args)


class SearchBox(object):
    u"""Implementação de um box com Label e Enty."""

    def __init__(self, tela, text):
        """Construtor da classe."""
        self.frame_bd = tk.Frame(tela)
        self.frame = tk.Frame(self.frame_bd)
        # self.frame = tk.Frame(tela, bd=10)
        self.length_line = tela.winfo_screenwidth()
        self.label = tk.Label(self.frame, text=text)
        self.entry = tk.Entry(self.frame)
        self.button = tk.Button(self.frame)
        self._configure_()

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self.frame_bd.configure(**tema.BORDA)
        self.frame.configure(bd=10, bg=tema.bg_widget)
        self.label.configure(bg=tema.bg_widget, fg=tema.fg_widget, width=20)
        self.entry.configure(justify=tk.LEFT, width=135, bg=tema.bg_widget,
                             fg=tema.fg_widget,
                             insertbackground=tema.insert_bg)
        self.button.configure(text="Pesquisar", width=10, bg=tema.bg_widget,
                              fg=tema.fg_widget)

    def pack(self, **kwargs):
        """Substituição do método pack()."""
        self.frame_bd.pack(**kwargs)
        self.frame.pack()
        self.label.pack(side=tk.LEFT)
        self.button.pack(side=tk.RIGHT)
        self.entry.pack(side=tk.RIGHT)


class Lista(object):
    """Implementa uma lista de atributos."""

    def __init__(self, tela):
        """Construtor da classe."""
        self.frame_bd = tk.Frame(tela)
        self.frame_buttons = tk.Frame(self.frame_bd)
        self.label = tk.Label(self.frame_buttons)
        self.add_button = tk.Button(self.frame_buttons)
        self.remove_button = tk.Button(self.frame_buttons)
        self.edit_button = tk.Button(self.frame_buttons)
        self.frame = tk.Frame(self.frame_bd)
        self.list = Tabela(self.frame)

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self.frame_bd.configure(bd=2, bg=tema.bg_borda)
        self.frame_buttons.configure(bg=tema.bg_widget)
        self.label.configure(width=170, text="Clientes", bg=tema.bg_widget,
                             fg=tema.fg_widget)
        self.add_button.configure(text="Cadastrar", bg=tema.bg_widget,
                                  fg=tema.fg_widget)
        self.remove_button.configure(text="Remover", bg=tema.bg_widget,
                                     fg=tema.fg_widget)
        self.edit_button.configure(text="Editar", bg=tema.bg_widget,
                                   fg=tema.fg_widget)
        self.frame.configure(bd=10, bg=tema.bg_widget)
        for item in self.list.colunas:
            self.list.colunas[item].lista.configure(justify=tema.justify_text,
                                                    bg=tema.bg_widget, bd=2,
                                                    selectmode=tk.EXTENDED,
                                                    fg=tema.fg_widget)

    def pack(self, **kwargs):
        u"""Substituição do método pack()."""
        self._configure_()
        self.frame_bd.pack(**kwargs)
        self.label.pack()
        self.frame_buttons.pack()
        self.add_button.pack(side=tk.LEFT)
        self.edit_button.pack(side=tk.LEFT)
        self.remove_button.pack(side=tk.RIGHT)
        self.list.pack(side=tk.RIGHT, fill=tk.Y)
        self.frame.pack()

    def insert(self, *args):
        u"""Substituição do método insert()."""
        self.list.insert(*args)

    def reset(self):
        u"""Apaga todas as posições da."""
        _itens_ = self.list.size()
        if _itens_ > 0:
            print("Deletando")
            self.list.delete(0, _itens_-1)
        return []
