# Estudo - Lembrete de Atividades Diárias

Este repositório contém um pequeno programa em Python que exibe lembretes de atividades diárias com base em um arquivo `atividades.json`.

## Como usar

1. Instale as dependências necessárias:

```bash
pip install schedule
```

2. Edite o arquivo `atividades.json` para incluir suas atividades e horários no formato `HH:MM`.

3. Execute o programa:

```bash
python remind.py
```

O script permanecerá em execução e exibirá mensagens no terminal nos horários configurados.

## Exemplo de `atividades.json`

```json
[
    {"hora": "09:00", "atividade": "Tomar café da manhã"},
    {"hora": "12:00", "atividade": "Almoçar"},
    {"hora": "18:00", "atividade": "Jantar"}
]
```

