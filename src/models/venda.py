class Venda:
    def __init__(
        self,
        id,
        produto_id,
        user_id,
        quantidade,
        valor_total,
        created_at,
    ):
        self.id = id
        self.produto_id = produto_id
        self.user_id = user_id
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.created_at = created_at

    def __repr__(self):
        return f"<Venda Produto:{self.produto_id} QTD:{self.quantidade} Total:R${self.valor_total}>"