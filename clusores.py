"""Biblioteca de clusores."""
# -*- coding: utf-8 -*-

from tkinter import messagebox as msg


def valida_insercao(func):
    """Clusore de validação."""
    def valida_campos_vazios(self):
        """Valida os campos de texto."""
        if not self.nome.entry.get():
            msg.showerror("Erro de validação", "Campo \"Nome\" em vazio.")
            return
        if self.data_nasc.get() == "//":
            msg.showerror("Erro de validação", "Campo \"Data de nascimento\" em vazio.")
            return
        try:
            self.atendimento.get()
        except IndexError:
            msg.showerror("Erro de validação", "Campo \"Tipo de Atendimento\" não seleionado.")
            return
        func(self)
    return valida_campos_vazios
