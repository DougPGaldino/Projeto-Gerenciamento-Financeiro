import sqlite3 as sqlite

conexao = sqlite.connect("Financeiro.db")

cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS CategoriaMovimentacao(
            ID_CategoriaMovimentacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ds_CategoriaMovimentacao TEXT NOT NULL
        );
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Usuarios(
            ID_Usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nm_Usuario TEXT NOT NULL,
            Senha TEXT NOT NULL,
            Dt_Criacao TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS FormaPagamento(
            ID_Pagamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ds_Pagamento TEXT NOT NULL
        );
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Movimentacoes(
            ID_Movimentacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ID_Usuario INTEGER NOT NULL,
            Descricao TEXT NOT NULL,
            Categoria INTEGER NOT NULL,
            Valor INTEGER NOT NULL,
            FormaPagamento INTEGER NOT NULL,
            Dt_Movimentacao TEXT NOT NULL,
            FOREIGN KEY (Categoria) REFERENCES CategoriaMovimentacao(ID_CategoriaMovimentacao),
            FOREIGN KEY (FormaPagamento) REFERENCES FormaPagamento(ID_Pagamento),
            FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
        );
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Recorrencia (
            ID_Recorrencia INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ID_Movimentacao INTEGER NOT NULL,
            Periodicidade TEXT NOT NULL,  -- 'Diário', 'Semanal', 'Mensal', 'Anual'
            Data_Fim TEXT,  -- Opcional, se houver data para encerrar a recorrência
            FOREIGN KEY (ID_Movimentacao) REFERENCES Movimentacoes(ID)
       );
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Orcamento (
            ID_Orcamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ID_Usuario INTEGER NOT NULL,
            ID_CategoriaMovimentacao INTEGER NOT NULL,
            Valor_Limite INTEGER NOT NULL,  -- Valor máximo para a categoria
            Periodo TEXT NOT NULL,  -- 'Mensal', 'Anual', etc.
            FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
            FOREIGN KEY (ID_CategoriaMovimentacao) REFERENCES CategoriaMovimentacao(ID_CategoriaMovimentacao)
        );
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Parcelamentos (
            ID_Parcela INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ID_Movimentacao INTEGER NOT NULL,
            Numero_Parcela INTEGER NOT NULL,
            Total_Parcelas INTEGER NOT NULL,
            Valor_Parcela INTEGER NOT NULL,
            Dt_Vencimento TEXT NOT NULL,
            FOREIGN KEY (ID_Movimentacao) REFERENCES Movimentacoes(ID)
        );
    """
)



cursor.close()

print('Tabela criada com sucesso')