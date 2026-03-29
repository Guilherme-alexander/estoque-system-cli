from src.database.connection import get_connection


def realizar_venda(produto_id, user_id, quantidade):
    if not produto_id or not user_id:
        print("❌ Dados inválidos.")
        return False

    if quantidade is None or quantidade <= 0:
        print("❌ Quantidade inválida.")
        return False

    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return False

    cursor = conn.cursor()

    # buscar produto
    cursor.execute(
        "SELECT preco, quantidade FROM produtos WHERE id=%s",
        (produto_id,)
    )
    produto = cursor.fetchone()

    if not produto:
        print("❌ Produto não encontrado.")
        cursor.close()
        conn.close()
        return False

    preco, estoque = produto

    if estoque < quantidade:
        print("❌ Estoque insuficiente.")
        cursor.close()
        conn.close()
        return False

    total = preco * quantidade

    # atualizar estoque
    cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade - %s,
            vendidos = vendidos + %s
        WHERE id=%s
    """, (quantidade, quantidade, produto_id))

    # registrar venda
    cursor.execute("""
        INSERT INTO vendas (produto_id, user_id, quantidade, valor_total)
        VALUES (%s, %s, %s, %s)
    """, (produto_id, user_id, quantidade, total))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Venda realizada! Total: R$ {total}")
    return True


def lucro_mes():
    conn = get_connection()

    if not conn:
        print("❌ Banco indisponível.")
        return 0

    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(valor_total)
        FROM vendas
        WHERE MONTH(created_at) = MONTH(CURRENT_DATE())
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total or 0