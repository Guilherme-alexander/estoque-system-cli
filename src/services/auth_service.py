from src.database.connection import get_connection
from src.utils.hash import hash_password, verify_password


def register(username: str, password: str):
    if not username or not password:
        print("❌ Usuário e senha não podem ser vazios.")
        return False

    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return False

    cursor = conn.cursor()

    # verificar se já existe
    cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        print("❌ Usuário já existe.")
        cursor.close()
        conn.close()
        return False

    sql = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
    cursor.execute(sql, (username, hash_password(password)))

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Usuário criado com sucesso!")
    return True


def login(username: str, password: str):
    if not username or not password:
        print("❌ Preencha usuário e senha.")
        return None

    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return None

    cursor = conn.cursor()

    sql = "SELECT id, password_hash FROM users WHERE username=%s"
    cursor.execute(sql, (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        print("❌ Usuário não encontrado.")
        return None

    if not verify_password(password, user[1]):
        print("❌ Senha incorreta.")
        return None

    print("✅ Login realizado!")
    return user[0]