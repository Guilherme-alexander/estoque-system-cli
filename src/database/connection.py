import mysql.connector
from mysql.connector import Error
from src.config.settings import settings


def get_connection():
    try:
        conn = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME,
        )

        if conn.is_connected():
            return conn

    except Error as e:
        print("""
┌──────────────────────────────────────────────┐
│         ERRO DE CONEXÃO COM O BANCO          │
├──────────────────────────────────────────────┤
│  [*] Verifique:                              │
│  [!] MySQL está rodando                      │
│  [!] Porta 3306                              │
│  [!] Credenciais (.env)                      │
└──────────────────────────────────────────────┘
""")
        print(f"[Detalhes técnicos]: {e}\n")

    return None