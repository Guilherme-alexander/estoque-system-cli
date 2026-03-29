from services.auth_service import hash_password


def test_hash():
    senha = "123456"
    hashed = hash_password(senha)

    assert hashed != senha
    assert len(hashed) > 0