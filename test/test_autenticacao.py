"""
test_autenticacao_luan.py
====================
Testes automatizados para o módulo auth.autenticacao.

Funções testadas:
    - autenticar(login, senha) → "admin" | "funcionario" | None
    - login_existe(login)      → bool

Como executar:
    python test/test_autenticacao.py
    # ou com pytest a partir da raiz:
    pytest test/test_autenticacao.py -v
"""

import sys
import os
import unittest

# Garante que a raiz do projeto está no path ao rodar direto da pasta test/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from auth.autenticacao import autenticar, login_existe, funcionarios


# Funcionário de exemplo reutilizado nos testes
FUNCIONARIO_EXEMPLO = {
    "nome": "Luan",
    "login": "luan",
    "senha": "456",
    "email": "luan@email.com",
    "telefone": "99999-0000",
    "salario": 3000.0,
    "cpf": "000.000.000-00",
}


class TestAutenticar(unittest.TestCase):
    """Testes para a função autenticar()."""

    def setUp(self):
        """Limpa a lista de funcionários antes de cada teste."""
        funcionarios.clear()

    def tearDown(self):
        """Garante limpeza mesmo se o teste falhar."""
        funcionarios.clear()

    def test_admin_credenciais_corretas(self):
        """Admin com login e senha corretos deve retornar 'admin'."""
        self.assertEqual(autenticar("adm", "123"), "admin")

    def test_admin_senha_errada(self):
        """Admin com senha errada deve retornar None."""
        self.assertIsNone(autenticar("adm", "errada"))

    def test_admin_login_errado(self):
        """Login errado com senha correta de admin deve retornar None."""
        self.assertIsNone(autenticar("outro", "123"))

    def test_credenciais_totalmente_invalidas(self):
        """Credenciais inexistentes devem retornar None."""
        self.assertIsNone(autenticar("ninguem", "nada"))

    def test_funcionario_autenticado(self):
        """Funcionário cadastrado com credenciais corretas deve retornar 'funcionario'."""
        funcionarios.append(FUNCIONARIO_EXEMPLO)
        self.assertEqual(autenticar("luan", "456"), "funcionario")

    def test_funcionario_senha_errada(self):
        """Funcionário com senha errada deve retornar None."""
        funcionarios.append(FUNCIONARIO_EXEMPLO)
        self.assertIsNone(autenticar("luan", "errada"))

    def test_lista_vazia_retorna_none(self):
        """Com lista vazia e credenciais não-admin, deve retornar None."""
        self.assertIsNone(autenticar("qualquer", "qualquer"))


class TestLoginExiste(unittest.TestCase):
    """Testes para a função login_existe()."""

    def setUp(self):
        """Limpa a lista de funcionários antes de cada teste."""
        funcionarios.clear()

    def tearDown(self):
        """Garante limpeza mesmo se o teste falhar."""
        funcionarios.clear()

    def test_login_nao_existe_em_lista_vazia(self):
        """Deve retornar False quando não há funcionários cadastrados."""
        self.assertFalse(login_existe("luan"))

    def test_login_existe(self):
        """Deve retornar True quando o login está cadastrado."""
        funcionarios.append(FUNCIONARIO_EXEMPLO)
        self.assertTrue(login_existe("luan"))

    def test_login_diferente_nao_encontrado(self):
        """Deve retornar False para login diferente do cadastrado."""
        funcionarios.append(FUNCIONARIO_EXEMPLO)
        self.assertFalse(login_existe("outro"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
