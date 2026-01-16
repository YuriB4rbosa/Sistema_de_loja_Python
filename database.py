import sqlite3

def abrir_conexao():
    
    return sqlite3.connect("lojinha_perifericos.db")

def inicializar_sistema_database():
    
    query = """
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        valor REAL NOT NULL,
        data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    with abrir_conexao() as conn:
        conn.execute(query)

def registrar_venda(item, valor):
    
    try:
        with abrir_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vendas (item, valor) VALUES (?, ?)", (item, valor))
            conn.commit()
            return True
    except sqlite3.Error as erro:
        print(f"Erro Crítico de Banco de Dados: {erro}")
        return False

def relatorio_vendas():
    
    with abrir_conexao() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vendas ORDER BY data_venda DESC")
        return cursor.fetchall()
