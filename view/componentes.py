"""Pacote com componentes customizados."""
# -*- coding: utf-8 -*-


from tkinter import ttk
from view.table import Tabela
import tkinter as tk
from platform import system as so
if so().lower() == "windows":
    import defaults_win as style
else:
    import defaults as style


class CustomCombobox(object):
    """Combobox customizado."""
    def __init__(self, tela, range_limite, text):
        self.frame = tk.Frame(tela)
        self._label = tk.Label(self.frame, text=text)
        self._var = tk.StringVar()
        self._widget = ttk.Combobox(self.frame, textvariable=self._var)
        self._configure_(range_limite)

    def _configure_(self, range_limite):
        self.frame.configure(**style.FRAME)
        self._widget['values'] = [str(i) for i in range(range_limite, 0, -1)]
        self._widget.configure(**style.COMBOBOX)

    def configure(self, **kwargs):
        """Atalho para o método configure."""
        self._widget.configure(**kwargs)

    def pack(self, **kwargs):
        """Atalho para o gerênciador de geometria."""
        self.frame.pack(**kwargs)
        self._label.pack()
        self._widget.pack()

    def get(self):
        """Getter do objeto."""
        return self._var.get()

    def set(self, valor):
        """Eetter do objeto."""
        self._var.set(valor)

class ChooseData(object):
    """Componente para a escolha de datas"""
    def __init__(self, tela, text):
        self._frame_bd = tk.Frame(tela, **style.BORDA)
        self._frame = tk.Frame(self._frame_bd)
        self._label = tk.Label(self._frame, text=text, **style.LABEL)
        self._dia = CustomCombobox(self._frame, 31, "Dia")
        self._mes = CustomCombobox(self._frame, 12, "Mês")
        self._ano = CustomCombobox(self._frame, 2017, "Ano")

    def configure(self, width=15):
        """implementação do método de configuração."""
        self._dia.configure(width=int(width//3))
        self._mes.configure(width=int(width//3))
        self._ano.configure(width=int(width//3))

    def pack(self, **kwargs):
        """Atalho para o gerênciador de geometria."""
        self._frame_bd.pack(**kwargs)
        self._frame.pack()
        self._label.pack(side=tk.LEFT)
        self._dia.pack(side=tk.LEFT)
        self._mes.pack(side=tk.LEFT)
        self._ano.pack(side=tk.LEFT)

    def get(self):
        """Getter do objeto."""
        return "{dia}/{mes}/{ano}".format(dia=self._dia.get(), mes=self._mes.get(),
                                          ano=self._ano.get())

    def set(self, data="//"):
        """Setter do objeto."""
        dia, mes, ano = data.split("/")
        self._dia.set(dia)
        self._mes.set(mes)
        self._ano.set(ano)


class ChooseMenu(object):
    u"""Implementação de menu de opções."""

    def __init__(self, tela, text):
        """Construtor da classe."""
        self._frame_bd = tk.Frame(tela)
        self.frame = tk.Frame(self._frame_bd)
        self.opcao = tk.StringVar()
        self.label = tk.Label(self.frame, text=text)
        self.escolha = tk.StringVar()
        self.entry = ttk.Combobox(self.frame, textvariable=self.escolha)
        self._configure_()

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self._frame_bd.configure(**style.BORDA)
        self.frame.configure(**style.FRAME)
        self.label.configure(**style.LABEL)
        self.entry["values"] = style.ATENDIMENTOS
        self.entry.configure(**style.CHOOSE_COMBOBOX)

    def set(self, item):
        """Setter da classe."""
        self.escolha.set(item)

    def pack(self, **kwargs):
        u"""Substituição do método pack()."""
        self._frame_bd.pack(**kwargs)
        self.frame.pack(padx=2)
        self.label.pack(side=tk.LEFT, pady=9)
        self.entry.pack(side=tk.LEFT)

    def get(self):
        """Devolve o valor da escolha."""
        return self.escolha.get()


class TextBox(object):
    u"""Implementação de um box com Label e Enty."""

    def __init__(self, tela, text):
        """Construtor da classe."""
        self._frame_bd = tk.Frame(tela)
        self.frame = tk.Frame(self._frame_bd)
        # self.frame = tk.Frame(tela, bd=10)
        self.label = tk.Label(self.frame, text=text)
        self.entry = ttk.Entry(self.frame)
        self._configure_()

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self._frame_bd.configure(**style.BORDA)
        self.frame.configure(**style.FRAME)
        self.label.configure(**style.LABEL)
        self.entry.configure(**style.ENTRY_TEXT)

    def pack(self, **kargs):
        u"""Substituição do método pack()."""
        self._frame_bd.pack(**kargs)
        self.frame.pack()
        self.label.pack(side=tk.LEFT, pady=9)
        self.entry.pack(side=tk.RIGHT)

    def insert(self, *args):
        """Substituição do método insert()."""
        self.entry.insert(0, args)

    def get(self):
        """Substituição do método get()."""
        return self.entry.get()


class SearchBox(object):
    u"""Implementação de um box com Label e Enty."""

    def __init__(self, tela, text):
        """Construtor da classe."""
        self._frame_bd = tk.Frame(tela)
        self.frame = tk.Frame(self._frame_bd)
        self.label = tk.Label(self.frame, text=text)
        self.entry = ttk.Entry(self.frame)
        self.button = ttk.Button(self.frame)
        self._configure_()

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self._frame_bd.configure(**style.BORDA)
        self.frame.configure(**style.FRAME)
        self.label.configure(**style.LABEL)
        self.entry.configure(**style.ENTRY_TEXT)
        self.button.configure(text="Pesquisar", **style.BUTTON)
        self.entry.configure(width=(style.ENTRY_TEXT["width"]-14))

    def pack(self, **kwargs):
        """Substituição do método pack()."""
        self._frame_bd.pack(**kwargs)
        self.frame.pack()
        self.label.pack(side=tk.LEFT)
        self.button.pack(side=tk.RIGHT)
        self.entry.pack(side=tk.RIGHT, padx=2)

class FrameButtons(object):
    """Implementa uma lista de botões."""

    def __init__(self, tela):
        """Construtor da classe."""
        self._frame_bd = tk.Frame(tela, **style.BORDA)
        self.frame = tk.Frame(self._frame_bd, **style.FRAME)
        self.label = tk.Label(self.frame, **style.LABEL)
        self.add_button = ttk.Button(self.frame)
        self.edit_button = ttk.Button(self.frame)
        self.remove_button = ttk.Button(self.frame)

    def _configure_(self):
        self.label.configure(width=200)
        self.add_button.configure(text="Cadastrar", **style.BUTTON)
        self.remove_button.configure(text="Remover", **style.BUTTON)
        self.edit_button.configure(text="Editar", **style.BUTTON)

    def pack(self, **kwargs):
        """Atalho para o gerênciador de geometria Pack."""
        self._configure_()
        self._frame_bd.pack(**kwargs)
        self.frame.pack()
        self.label.pack(padx=3)
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.edit_button.pack(side=tk.LEFT, padx=5)
        self.remove_button.pack(side=tk.RIGHT, padx=5)

class Lista(object):
    """Implementa uma lista de atributos."""

    def __init__(self, tela):
        """Construtor da classe."""
        self._frame_bd = tk.Frame(tela, **style.BORDA)
        self.frame_buttons = tk.Frame(self._frame_bd)
        self.frame = tk.Frame(self._frame_bd)
        self.list = Tabela(self.frame)

    def _configure_(self):
        """Configura os Widgets do Componente."""
        self._frame_bd.configure()
        self.frame_buttons.configure(bg=style.bg_widget)
        self.frame.configure(**style.FRAME)
        for item in self.list.colunas:
            self.list.colunas[item].lista.configure(**style.COLUN_LIST)

    def pack(self, **kwargs):
        u"""Substituição do método pack()."""
        self._configure_()
        self._frame_bd.pack(**kwargs)
        self.frame_buttons.pack(padx=2)
        self.list.pack(side=tk.RIGHT, fill=tk.Y, padx=2)
        self.frame.pack()

    def insert(self, *args):
        u"""Substituição do método insert()."""
        self.list.insert(*args)

    def reset(self):
        u"""Apaga todas as posições da lista."""
        self.list.delete(0, self.list.size()-1)
