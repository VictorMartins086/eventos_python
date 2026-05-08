---
tags: [modulo, autenticacao, funcionarios, produtos]
date: 2026-05-08
---

# Módulo — autenticacao.py

> Voltar para [[00-indice]] | Ver testes em [[04-testes]]

**Localização:** `auth/autenticacao.py`

## Responsabilidade

Centraliza toda a lógica de:
- Autenticação de admin e funcionários
- CRUD de funcionários
- CRUD de produtos
- Menus interativos (admin e funcionário)

## Dados em Memória

```python
funcionarios = []  # lista de dicts
produtos     = []  # lista de dicts
```

> Não há persistência em banco ou arquivo — os dados vivem apenas em tempo de execução.

## Credenciais de Admin

| Campo | Valor |
|---|---|
| Login | `adm` |
| Senha | `123` |

---

## Funções

### `autenticar(login, senha) → str | None`

Verifica se as credenciais correspondem ao admin ou a algum funcionário.

| Retorno | Condição |
|---|---|
| `"admin"` | Login e senha batem com o admin |
| `"funcionario"` | Login e senha batem com algum funcionário |
| `None` | Credenciais inválidas |

---

### `login_existe(login) → bool`

Retorna `True` se já existe um funcionário com aquele login na lista.

---

### `cadastrar_funcionario()`

Lê os dados do funcionário via `input()` e adiciona à lista. Campos:
`nome`, `login`, `senha`, `email`, `telefone`, `salario`, `cpf`

- Limite de 30 funcionários
- Bloqueia login duplicado (usa [[#login_existe]])

---

### `atualizar_funcionario(login_usuario)`

Atualiza `email`, `telefone` e `salario` do funcionário com o login informado.

---

### `listar_funcionarios()`

Imprime todos os funcionários cadastrados.

---

### `cadastrar_produto()`

Lê código, descrição e preço via `input()`. Bloqueia código duplicado.

---

### `listar_produtos()` / `buscar_produto()`

Lista todos os produtos ou busca por código.

---

### `menu_admin()` / `menu_funcionario(login)`

Loops interativos com as opções disponíveis para cada perfil.

---

## Guard `__main__`

```python
# Luan corrigiu: sem esse guard, o bloco de login executava automaticamente ao importar o módulo em app.py
if __name__ == "__main__":
    ...
```

Sem esse guard, o bloco de login era executado ao importar o módulo em `app.py`.
Ver [[05-historico-de-alteracoes]].
