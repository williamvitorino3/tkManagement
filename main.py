# -*- coding: utf-8 -*-
"""Script de inicialização do projeto."""

from tkinter import Tk
from view.tela import Janela


root = Tk()
root.title("tkMeanagement")
root.resizable(False, False)
root.geometry("1366x768+0+0")
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
tela = Janela(root)
root.mainloop()
