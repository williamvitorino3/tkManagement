"""Biblioteca de clusores."""
# -*- coding: utf-8 -*-
from datetime import date
from tkinter import messagebox as msg


def successful(func):
    """Exibe mensagem de sucesso após a operação."""
    def callback(*args):
        """Chama a função e mostra a mensagem de sucesso."""
        try:
            func(*args)
            msg.showinfo("Sucesso", "Operação realizada com sucesso.")
        except Exception:
            msg.showinfo("Falha", "Operação realizada com falhas.")
    return callback

def remocao(func):
    """Valida a remoção de um cliente."""
    def questionar(self):
        """Pergunta se deve remover."""
        if msg.askyesno("Remover paciente", "Deseja remover o paciente?"):
            func(self)
            msg.showinfo("Sucesso", "Operação realizada com sucesso.")
        else:
            msg.showinfo("Falha", "Operação não realizada.")
    return questionar

def insercao(func):
    """Clusore de validação."""
    def campos_vazios(self):
        """Valida os campos de texto."""
        if not self.nome.entry.get():
            msg.showerror("Erro de validação", "Campo \"Nome\" em vazio.")
            return
        try:
            if len(self.data_nasc.get().split("/")[-1]) != 4:
                raise AssertionError
            date(*[int(i) for i in self.data_nasc.get().split("/")[::-1]])
        except ValueError:
            msg.showerror("Erro de validação", "Campo \"Data de nascimento\" em inválido.")
            return
        except AssertionError:
            msg.showerror("Erro de validação", "Ano deve ter 4 digitos.")
            return
        try:
            if not self.atendimento.get():
                raise IndexError
        except IndexError:
            msg.showerror("Erro de validação", "Campo \"Tipo de Atendimento\" não seleionado.")
            return
        func(self)
        msg.showinfo("Sucesso", "Operação realizada com sucesso.")
    return campos_vazios
