class Produto:
    def __init__(
        self,
        id,
        nome,
        preco,
        quantidade,
        vendidos,
        reservados,
        encomendados,
        status,
        created_at,
    ):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.vendidos = vendidos
        self.reservados = reservados
        self.encomendados = encomendados
        self.status = status
        self.created_at = created_at

    def __repr__(self):
        return f"<Produto {self.nome} | R${self.preco} | QTD:{self.quantidade}>"