"""Biblioteca de clusores."""
# -*- coding: utf-8 -*-

from tkinter import messagebox as msg

def remocao(func):
    """Valida a remoção de um cliente."""
    def questionar(self):
        """Pergunta se deve remover."""
        if msg.askyesno("Remover paciente", "Deseja remover o paciente?"):
            func(self)
    return questionar

def insercao(func):
    """Clusore de validação."""
    def campos_vazios(self):
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
    return campos_vazios

def successful(func):
    """Exibe mensagem de sucesso após a operação."""
    def callback(*args):
        """Chama a função"""
        func(*args)
        msg.showinfo("Sucesso", "Operação realizada com sucesso.")
    return callback
