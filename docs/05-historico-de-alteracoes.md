---
tags: [historico, alteracoes, luan]
date: 2026-05-08
author: Luan
---

# Histórico de Alterações

> Voltar para [[00-indice]]

---

## 2026-05-08

### 1. Criação do `app.py` sem código duplicado

**Problema:** O código de login estava duplicado em `autenticacao.py` e precisava ser reutilizado.

**Solução:** `app.py` passa a importar `autenticar`, `menu_admin` e `menu_funcionario` de `autenticacao.py` e `Inscricao` de `inscricao.py`, sem copiar nenhuma lógica.

```python
from auth.autenticacao import autenticar, menu_admin, menu_funcionario
from auth.inscricao import Inscricao
```

---

### 2. Correção do guard `__main__` em `autenticacao.py`

**Problema:** O bloco de login estava solto no nível de módulo, executando automaticamente ao importar o arquivo.

**Solução:** Luan adicionou `if __name__ == "__main__":` com comentário explicativo.

```python
# Luan corrigiu: sem esse guard, o bloco de login executava automaticamente ao importar o módulo em app.py
if __name__ == "__main__":
    ...
```

**Arquivo afetado:** `auth/autenticacao.py`

---

### 3. Reorganização para pasta `auth/`

**Problema:** `autenticacao.py` e `inscricao.py` estavam soltos na raiz do projeto.

**Solução:** Movidos para `auth/`, e todos os imports atualizados.

**Arquivos afetados:**
- `app.py` → imports atualizados para `auth.autenticacao` e `auth.inscricao`
- `test/tests_inscricao.py` → import atualizado + `sys.path` corrigido
- `test/teste.py` → import atualizado + `sys.path` corrigido

---

### 4. Criação dos testes reais

**Problema:** `test/teste.py` usava apenas `print()`, sem nenhuma asserção. Ver [[04-testes#Crítica ao teste.py original]].

**Solução:** Criados dois arquivos de teste com `unittest`:

| Arquivo | Módulo testado | Testes |
|---|---|---|
| `test/tests_inscricao.py` | [[03-modulo-inscricao]] | 6 |
| `test/test_autenticacao.py` | [[02-modulo-autenticacao]] | 10 |

---

### 5. Documentação em `docs/`

**Adicionados:**
- [[00-indice]] — MOC do projeto
- [[01-estrutura-do-projeto]] — Árvore de pastas e responsabilidades
- [[02-modulo-autenticacao]] — Referência completa do módulo
- [[03-modulo-inscricao]] — Referência completa da classe `Inscricao`
- [[04-testes]] — Visão geral, crítica ao teste original e cobertura
- [[05-historico-de-alteracoes]] — Este arquivo
