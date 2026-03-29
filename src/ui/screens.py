from src.ui.banner import show_banner
from src.ui.menu import menu_login, menu_principal
from src.services.auth_service import login, register
from src.utils.helpers import clear_screen, check_exit
import sys


def tela_login():
    clear_screen()
    show_banner()
    menu_login()

    op = input("\n➤ Escolha: ").strip()
    check_exit(op)

    if op == "1":
        print("\n🔐 LOGIN\n")

        user = input("Usuário: ").strip()
        check_exit(user)

        senha = input("Senha: ").strip()
        check_exit(senha)

        user_id = login(user, senha)

        if user_id:
            return user_id

        input("\nPressione ENTER...")

    elif op == "2":
        print("\n📝 CADASTRO\n")

        user = input("Novo usuário: ").strip()
        check_exit(user)

        senha = input("Senha: ").strip()
        check_exit(senha)

        register(user, senha)

        input("\nPressione ENTER...")

    elif op == "3":
        print("\nEncerrando o sistema...")
        sys.exit(0)

    return None


def tela_principal(user_id):
    while True:
        clear_screen()
        show_banner()
        menu_principal()

        op = input("\n➤ Escolha: ").strip()
        check_exit(op)

        if op == "5":
            print("\nEncerrando o sistema...")
            break