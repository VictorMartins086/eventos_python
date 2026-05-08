# ====================================
# SISTEMA DE FUNCIONÁRIOS E PRODUTOS
# ====================================

funcionarios = []
produtos = []

# =========================
# ADMINISTRADOR
# =========================

ADMIN_LOGIN = "adm"
ADMIN_SENHA = "123"


# =========================
# LOGIN
# =========================

def autenticar(login, senha):

    if login == ADMIN_LOGIN and senha == ADMIN_SENHA:
        return "admin"

    for funcionario in funcionarios:
        if funcionario["login"] == login and funcionario["senha"] == senha:
            return "funcionario"

    return None


# =========================
# FUNCIONÁRIOS
# =========================

def login_existe(login):
    for funcionario in funcionarios:
        if funcionario["login"] == login:
            return True

    return False


def cadastrar_funcionario():

    if len(funcionarios) >= 30:
        print("\nLimite de funcionários atingido!")
        return

    login = input("Login: ")

    if login_existe(login):
        print("Login já cadastrado!")
        return

    funcionario = {
        "nome": input("Nome: "),
        "login": login,
        "senha": input("Senha: "),
        "email": input("Email: "),
        "telefone": input("Telefone: "),
        "salario": float(input("Salário: ")),
        "cpf": input("CPF: ")
    }

    funcionarios.append(funcionario)

    print("\nFuncionário cadastrado com sucesso!")


def atualizar_funcionario(login_usuario):

    for funcionario in funcionarios:

        if funcionario["login"] == login_usuario:

            print("\n=== ATUALIZAÇÃO ===")

            funcionario["email"] = input("Novo email: ")
            funcionario["telefone"] = input("Novo telefone: ")
            funcionario["salario"] = float(input("Novo salário: "))

            print("\nDados atualizados!")
            return

    print("\nFuncionário não encontrado!")


def listar_funcionarios():

    if not funcionarios:
        print("\nNenhum funcionário cadastrado!")
        return

    for funcionario in funcionarios:

        print("\n===================")
        print("Nome:", funcionario["nome"])
        print("Login:", funcionario["login"])
        print("Email:", funcionario["email"])
        print("Telefone:", funcionario["telefone"])
        print("Salário:", funcionario["salario"])
        print("CPF:", funcionario["cpf"])


# =========================
# PRODUTOS
# =========================

def codigo_existe(codigo):

    for produto in produtos:
        if produto["codigo"] == codigo:
            return True

    return False


def cadastrar_produto():

    codigo = int(input("Código do produto: "))

    if codigo_existe(codigo):
        print("\nCódigo já cadastrado!")
        return

    produto = {
        "codigo": codigo,
        "descricao": input("Descrição: "),
        "preco": float(input("Preço: "))
    }

    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")


def listar_produtos():

    if not produtos:
        print("\nNenhum produto cadastrado!")
        return

    for produto in produtos:

        print("\n===================")
        print("Código:", produto["codigo"])
        print("Descrição:", produto["descricao"])
        print("Preço:", produto["preco"])


def buscar_produto():

    codigo = int(input("Digite o código do produto: "))

    for produto in produtos:

        if produto["codigo"] == codigo:

            print("\n=== PRODUTO ENCONTRADO ===")
            print("Descrição:", produto["descricao"])
            print("Preço:", produto["preco"])
            return

    print("\nProduto não encontrado!")


# =========================
# MENU ADMIN
# =========================

def menu_admin():

    while True:

        print("\n========== MENU ADMIN ==========")
        print("1 - Cadastrar Funcionário")
        print("2 - Atualizar Funcionário")
        print("3 - Listar Funcionários")
        print("4 - Cadastrar Produto")
        print("5 - Listar Produtos")
        print("6 - Buscar Produto")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_funcionario()

        elif opcao == "2":
            login_func = input("Login do funcionário: ")
            atualizar_funcionario(login_func)

        elif opcao == "3":
            listar_funcionarios()

        elif opcao == "4":
            cadastrar_produto()

        elif opcao == "5":
            listar_produtos()

        elif opcao == "6":
            buscar_produto()

        elif opcao == "0":
            print("\nSistema encerrado!")
            break

        else:
            print("\nOpção inválida!")


# =========================
# MENU FUNCIONÁRIO
# =========================

def menu_funcionario(login_usuario):

    while True:

        print("\n====== MENU FUNCIONÁRIO ======")
        print("1 - Atualizar Meus Dados")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            atualizar_funcionario(login_usuario)

        elif opcao == "0":
            print("\nSaindo...")
            break

        else:
            print("\nOpção inválida!")


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