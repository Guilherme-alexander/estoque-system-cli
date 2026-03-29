from src.ui.screens import tela_login, tela_principal
from src.utils.helpers import clear_screen, pause


def start():
    try:
        while True:
            clear_screen()

            user_id = tela_login()

            if user_id:
                clear_screen()
                tela_principal(user_id)
            else:
                pause()

    except KeyboardInterrupt:
        print("\n\nEncerrado pelo usuário (Ctrl+C)")