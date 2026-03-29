from services.estoque_service import criar_produto, listar_produtos


def test_criar_produto():
    criar_produto("Produto Teste", 10.0, 5)

    produtos = listar_produtos()

    assert any(p[1] == "Produto Teste" for p in produtos)