"""
tests_inscricao_luan.py
=============
Testes automatizados para o sistema de eventos.

Crítica ao teste.py original:
    O arquivo teste.py NÃO é um teste real. Ele apenas imprime valores com
    print(), o que significa que:

    1. Nunca falha automaticamente — mesmo que um valor esteja errado,
       o script termina com sucesso (exit code 0).

    2. Não verifica nada — o desenvolvedor precisa ler a saída manualmente
       para saber se o resultado está certo ou errado.

    3. Não escala — em projetos maiores, ler prints não é viável.

    Este arquivo corrige esses problemas usando unittest, que:
    - Lança AssertionError automaticamente se um valor não bater.
    - Reporta claramente quais testes passaram ou falharam.
    - Pode ser integrado a pipelines de CI/CD.

Módulos testados:
    - inscricao.Inscricao

Como executar:
    python tests_luan.py
    # ou com pytest:
    pytest tests_luan.py -v
"""

import sys
import os
import unittest

# Garante que a raiz do projeto está no path ao rodar direto da pasta test/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from auth.inscricao import Inscricao


class TestInscricao(unittest.TestCase):
    """Testes para a classe Inscricao."""

    def setUp(self):
        """Cria uma inscrição padrão reutilizada nos testes."""
        self.insc = Inscricao(1, "drey", 10)

    def test_atributo_id(self):
        """Verifica se o id é armazenado corretamente."""
        self.assertEqual(self.insc.id, 1)

    def test_atributo_nome_pessoa(self):
        """Verifica se o nome da pessoa é armazenado corretamente."""
        self.assertEqual(self.insc.nome_pessoa, "drey")

    def test_atributo_evento_id(self):
        """Verifica se o evento_id é armazenado corretamente."""
        self.assertEqual(self.insc.evento_id, 10)

    def test_to_dict_retorna_dict(self):
        """Verifica se to_dict retorna um dicionário."""
        self.assertIsInstance(self.insc.to_dict(), dict)

    def test_to_dict_conteudo(self):
        """Verifica se to_dict retorna todos os campos com os valores corretos."""
        esperado = {"id": 1, "nome_pessoa": "drey", "evento_id": 10}
        self.assertEqual(self.insc.to_dict(), esperado)

    def test_inscricao_diferentes_valores(self):
        """Verifica que diferentes instâncias mantêm seus próprios valores."""
        outra = Inscricao(99, "luan", 5)
        self.assertNotEqual(outra.id, self.insc.id)
        self.assertNotEqual(outra.nome_pessoa, self.insc.nome_pessoa)
        self.assertNotEqual(outra.evento_id, self.insc.evento_id)


if __name__ == "__main__":
    unittest.main(verbosity=2)
