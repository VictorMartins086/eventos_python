---
tags: [estrutura, projeto]
date: 2026-05-08
---

# Estrutura do Projeto

> Voltar para [[00-indice]]

## Árvore de Pastas

```
eventos_python/
├── app.py               ← Ponto de entrada da aplicação
├── README.md
├── auth/
│   ├── autenticacao.py  ← Lógica de login, funcionários e produtos
│   └── inscricao.py     ← Classe Inscricao
├── test/
│   ├── teste.py             ← Teste original (apenas prints, sem asserts)
│   ├── tests_inscricao.py   ← Testes reais da classe Inscricao
│   ├── tests_luan.py        ← Versão anterior dos testes de inscrição
│   └── test_autenticacao.py ← Testes reais do módulo autenticacao
└── docs/                ← Esta pasta — documentação do projeto
```

## Responsabilidades

| Arquivo | Responsabilidade |
|---|---|
| `app.py` | Ponto de entrada — coleta login/senha e redireciona ao menu |
| `auth/autenticacao.py` | Admin, funcionários, produtos, menus |
| `auth/inscricao.py` | Modelo de dados de inscrição em eventos |
| `test/test_autenticacao.py` | Testes automatizados de autenticação |
| `test/tests_inscricao.py` | Testes automatizados de inscrição |

## Observações

- A pasta `auth/` agrupa os módulos de domínio para evitar imports soltos na raiz.
- Os arquivos em `test/` usam `sys.path.insert` para localizar a raiz do projeto independentemente de onde o teste é executado.
- Ver [[02-modulo-autenticacao]] e [[03-modulo-inscricao]] para detalhes dos módulos.
