from auth.autenticacao import (
    autenticar,
    menu_admin,
    menu_funcionario,
)
from auth.inscricao import Inscricao

# =========================
# PROGRAMA PRINCIPAL
# =========================

print("======= LOGIN =======")

login = input("Login: ")
senha = input("Senha: ")

tipo = autenticar(login, senha)

if tipo == "admin":
    menu_admin()
elif tipo == "funcionario":
    menu_funcionario(login)
else:
    print("\nAcesso negado!")
