WIDTH = 46


def linha_top():
    print("┌" + "─" * WIDTH + "┐")


def linha_mid():
    print("├" + "─" * WIDTH + "┤")


def linha_bottom():
    print("└" + "─" * WIDTH + "┘")


def titulo(texto):
    linha_top()
    print(f"│{texto.center(WIDTH)}│")
    linha_mid()


def opcao(num, texto):
    print(f"│  [{num}] {texto.ljust(WIDTH - 6)}│")


def menu_login():
    titulo("LOGIN")
    opcao(1, "Entrar")
    opcao(2, "Criar conta")
    opcao(3, "Sair")
    linha_bottom()


def menu_principal():
    titulo("MENU PRINCIPAL")
    opcao(1, "Cadastrar produto")
    opcao(2, "Listar produtos")
    opcao(3, "Realizar venda")
    opcao(4, "Relatório do mês")
    opcao(5, "Sair")
    linha_bottom()