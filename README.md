# Eventos Python

Sistema de gerenciamento de funcionários e produtos com controle de acesso por perfil, desenvolvido em Python puro (sem frameworks externos).

---

## Funcionalidades

### Perfil Administrador
- Cadastrar, atualizar e listar funcionários (limite de 30)
- Cadastrar, listar e buscar produtos
- Controle de login único por funcionário

### Perfil Funcionário
- Autenticação individual
- Atualização dos próprios dados (e-mail, telefone, salário)

### Módulo de Inscrição
- Classe `Inscricao` para vincular pessoas a eventos
- Serialização via `to_dict()`

---

## Estrutura do Projeto

```
eventos_python/
├── app.py                   # Ponto de entrada da aplicação
├── auth/
│   ├── autenticacao.py      # Lógica de autenticação, menus e CRUD de funcionários/produtos
│   └── inscricao.py         # Classe Inscricao
├── test/
│   ├── test_autenticacao.py # Testes unitários — autenticacao.py
│   ├── tests_inscricao.py   # Testes unitários — inscricao.py
│   └── teste.py             # Script exploratório (não automatizado)
└── docs/                    # Documentação adicional do projeto
```

---

## Requisitos

- Python 3.8+
- Sem dependências externas

---

## Como Executar

```bash
# Clone o repositório
git clone https://github.com/<seu-usuario>/eventos_python.git
cd eventos_python

# Execute a aplicação
python app.py
```

**Credenciais padrão do administrador:**

| Campo | Valor |
|-------|-------|
| Login | `adm` |
| Senha | `123` |

---

## Testes

Os testes utilizam `unittest` da biblioteca padrão e podem ser executados com `pytest` ou diretamente com o Python.

```bash
# Executar todos os testes com pytest (a partir da raiz)
pytest test/ -v

# Ou individualmente
python test/test_autenticacao.py
python test/tests_inscricao.py
```

---

## Documentação

A pasta [`docs/`](docs/) contém documentação detalhada sobre cada módulo:

- [Índice](docs/00-indice.md)
- [Estrutura do Projeto](docs/01-estrutura-do-projeto.md)
- [Módulo Autenticação](docs/02-modulo-autenticacao.md)
- [Módulo Inscrição](docs/03-modulo-inscricao.md)
- [Testes](docs/04-testes.md)
- [Histórico de Alterações](docs/05-historico-de-alteracoes.md)

---

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.