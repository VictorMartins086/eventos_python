---
tags: [testes, unittest, qualidade]
date: 2026-05-08
---

# Testes Automatizados

> Voltar para [[00-indice]]

## Crítica ao `teste.py` original

O arquivo `test/teste.py` **não é um teste real**. Ele apenas imprime valores:

```python
print(insc.nome_pessoa)
print(insc.to_dict())
```

### Problemas

| # | Problema | Impacto |
|---|---|---|
| 1 | Nunca falha automaticamente | Exit code sempre `0`, mesmo com bug |
| 2 | Não verifica nada | Desenvolvedor precisa ler a saída manualmente |
| 3 | Não escala | Inviável em projetos maiores ou pipelines de CI/CD |

---

## Solução adotada — `unittest`

Os novos arquivos usam `unittest.TestCase`, que:
- Lança `AssertionError` automaticamente se um valor não bater
- Reporta quais testes passaram/falharam com mensagem clara
- Pode ser integrado a CI/CD

---

## Cobertura atual

| Arquivo de teste | Módulo testado | Testes |
|---|---|---|
| `test/tests_inscricao.py` | [[03-modulo-inscricao]] | 6 |
| `test/test_autenticacao.py` | [[02-modulo-autenticacao]] | 10 |

---

## Como executar

```bash
# Todos os testes a partir da raiz
pytest test/ -v

# Arquivo específico
python test/test_autenticacao.py
python test/tests_inscricao.py
```

---

## Detalhes — `tests_inscricao.py`

Classe: `TestInscricao`

| Teste | O que verifica |
|---|---|
| `test_atributo_id` | `id` armazenado corretamente |
| `test_atributo_nome_pessoa` | `nome_pessoa` armazenado corretamente |
| `test_atributo_evento_id` | `evento_id` armazenado corretamente |
| `test_to_dict_retorna_dict` | `to_dict()` retorna um `dict` |
| `test_to_dict_conteudo` | `to_dict()` retorna todos os campos corretos |
| `test_inscricao_diferentes_valores` | Instâncias distintas mantêm seus próprios valores |

---

## Detalhes — `test_autenticacao.py`

### `TestAutenticar`

| Teste | O que verifica |
|---|---|
| `test_admin_credenciais_corretas` | Admin com credenciais corretas retorna `"admin"` |
| `test_admin_senha_errada` | Admin com senha errada retorna `None` |
| `test_admin_login_errado` | Login errado retorna `None` |
| `test_credenciais_totalmente_invalidas` | Credenciais inexistentes retornam `None` |
| `test_funcionario_autenticado` | Funcionário cadastrado autentica como `"funcionario"` |
| `test_funcionario_senha_errada` | Funcionário com senha errada retorna `None` |
| `test_lista_vazia_retorna_none` | Lista vazia retorna `None` para qualquer credencial |

### `TestLoginExiste`

| Teste | O que verifica |
|---|---|
| `test_login_nao_existe_em_lista_vazia` | `False` quando lista está vazia |
| `test_login_existe` | `True` quando login está cadastrado |
| `test_login_diferente_nao_encontrado` | `False` para login diferente do cadastrado |

### Isolamento

`setUp` e `tearDown` limpam `funcionarios.clear()` antes e depois de cada teste, garantindo que um teste não interfira no outro.
