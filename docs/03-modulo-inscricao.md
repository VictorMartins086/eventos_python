---
tags: [modulo, inscricao, classe]
date: 2026-05-08
---

# Módulo — inscricao.py

> Voltar para [[00-indice]] | Ver testes em [[04-testes]]

**Localização:** `auth/inscricao.py`

## Responsabilidade

Define o modelo de dados de uma inscrição em evento.

## Classe `Inscricao`

### Atributos

| Atributo | Tipo | Descrição |
|---|---|---|
| `id` | `int` | Identificador único da inscrição |
| `nome_pessoa` | `str` | Nome da pessoa inscrita |
| `evento_id` | `int` | Identificador do evento |

### Métodos

#### `__init__(id, nome_pessoa, evento_id)`

Construtor — inicializa os três atributos.

```python
insc = Inscricao(1, "drey", 10)
```

---

#### `to_dict() → dict`

Serializa a inscrição como dicionário.

```python
insc.to_dict()
# {"id": 1, "nome_pessoa": "drey", "evento_id": 10}
```

---

## Exemplo de Uso

```python
from auth.inscricao import Inscricao

insc = Inscricao(1, "drey", 10)
print(insc.nome_pessoa)   # drey
print(insc.to_dict())     # {"id": 1, "nome_pessoa": "drey", "evento_id": 10}
```
