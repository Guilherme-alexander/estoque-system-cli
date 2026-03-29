import os
import sys


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPressione ENTER para continuar...")


def input_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print("Valor inválido")
        return None


def input_float(msg):
    try:
        return float(input(msg))
    except ValueError:
        print("Valor inválido")
        return None


# 🔥 NOVO
def check_exit(value: str):
    comandos_saida = ["exit", "end", "close", "quit"]

    if value.lower() in comandos_saida:
        print("\nEncerrando o sistema...")
        sys.exit(0)