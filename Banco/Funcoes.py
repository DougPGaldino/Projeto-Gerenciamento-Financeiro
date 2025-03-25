import sqlite3 as sqlite

def conectaDB():
        conexao = sqlite.connect('Financeiro.db')
        return conexao

def InserirUsuario(nm_Usuario, Senha):
        conexao = conectaDB
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Usuario (nm_Usuario,Senha) VALUES (?,?)",(nm_Usuario, Senha))
        conexao.commit()
        conexao.close   