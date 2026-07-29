# app-terminal

Mini app de terminal que consome a biblioteca Texto Mágico via submódulo Git.

## Estrutura

- `app/main.py`: aplicação de terminal.
- `texto_magico/`: biblioteca Texto Mágico adicionada como submódulo.

## Como executar

1. Entre na pasta do projeto:

```bash
cd /workspaces/app-terminal
```

2. Execute o app:

```bash
python3 app/main.py
```

3. Escolha uma opção no menu:

- `1` para inverter texto
- `2` para gritar texto
- `0` para sair

## Como adicionar o submódulo

```bash
git submodule add /workspaces/texto_magico texto_magico
```

## Biblioteca utilizada

Repositório da biblioteca: https://github.com/ph95583faculdade-maker/Texto_magico
