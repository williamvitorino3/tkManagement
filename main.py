# -*- coding: utf-8 -*-
"""Script de inicialização do projeto."""

from tkinter import Tk
from view.tela import Janela
from defaults import FRAME


root = Tk()
root.configure(**FRAME)
root.title("tkMeanagement")
root.resizable(False, False)
root.geometry("+0+0")
# root.geometry("1366x768+0+0")
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
tela = Janela(root)
root.mainloop()
