from src.database.connection import get_connection


def criar_produto(nome, preco, quantidade):
    if not nome:
        print("❌ Nome do produto é obrigatório.")
        return False

    if preco is None or preco <= 0:
        print("❌ Preço inválido.")
        return False

    if quantidade is None or quantidade < 0:
        print("❌ Quantidade inválida.")
        return False

    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return False

    cursor = conn.cursor()

    sql = """
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (nome, preco, quantidade))

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Produto criado com sucesso!")
    return True


def listar_produtos():
    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    cursor.close()
    conn.close()

    return produtos


def atualizar_estoque(produto_id, nova_qtd):
    if not produto_id:
        print("❌ ID inválido.")
        return False

    if nova_qtd is None or nova_qtd < 0:
        print("❌ Quantidade inválida.")
        return False

    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return False

    cursor = conn.cursor()

    sql = "UPDATE produtos SET quantidade=%s WHERE id=%s"
    cursor.execute(sql, (nova_qtd, produto_id))

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Estoque atualizado!")
    return True


def remover_produto(produto_id):
    if not produto_id:
        print("❌ ID inválido.")
        return False

    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return False

    cursor = conn.cursor()

    cursor.execute("DELETE FROM produtos WHERE id=%s", (produto_id,))

    conn.commit()
    cursor.close()
    conn.close()

    print("🗑️ Produto removido!")
    return True