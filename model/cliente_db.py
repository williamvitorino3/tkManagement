# -*- coding: utf-8 -*-
# http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html


import sqlite3
from datetime import datetime


def criar_banco():
    """Cria o banco de dados."""
    with sqlite3.connect('clientes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                data_atendimento varchar(15) NOT NULL,
                data_nascimento varchar(15) NOT NULL,
                tipo_atendimento varchar(50) NULL
        );
        """)


def _now_(formato="%d/%m/%Y"):
    return datetime.today().strftime(formato)


def inserir(nome="None", data_nascimento="None", tipo_atendimento="None"):
    """Insere dados no banco."""
    with sqlite3.connect('clientes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO clientes
                    (data_atendimento, nome, data_nascimento, tipo_atendimento)
        VALUES (?, ?, ?, ?)
        """, (_now_(), nome, data_nascimento, tipo_atendimento))

        conn.commit()
        conn.close()


def buscar_all():
    """Busca dados no banco."""
    resultado = None
    with sqlite3.connect('clientes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM clientes ORDER BY nome""")
        resultado = cursor.fetchall()
    return resultado


def buscar(nome):
    """Busca dados no banco."""
    with sqlite3.connect('clientes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM clientes
        WHERE nome like ?
        ORDER BY nome
        """, ('%' + nome + '%', ))
        resultado = cursor.fetchall()
    return resultado


def remover(id_cliente):
    """Remove do banco o cliente com o ID recebido."""
    with sqlite3.connect('clientes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM clientes WHERE id = ?""", (id_cliente,))
        conn.commit()


def atualizar(id_cliente, nome, data_nascimento, tipo_atendimento):
    """Atualiza no banco os dados do cliente com o ID recebido."""
    with sqlite3.connect('clientes.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE clientes
        SET data_atendimento = ?, nome = ?,
            data_nascimento = ?, tipo_atendimento = ?
        WHERE id = ?
        """, (_now_(), nome, data_nascimento, tipo_atendimento, id_cliente))
        conn.commit()


def add_clientes_teste():
    """Adiciona a lista de clientes no banco."""
    with open("clientes_falsos.txt", 'r') as arquivo:
        for line in arquivo.readlines():
            inserir(*line.rstrip().split(','))


if __name__ == '__main__':
    criar_banco()
