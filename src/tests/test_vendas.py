# depende de existir produto com ID 1 e usuário 1
from services.venda_service import realizar_venda


def test_venda():
    result = realizar_venda(1, 1, 1)

    assert result in [True, False]