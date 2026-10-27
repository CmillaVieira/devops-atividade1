
# Atividade 1 - DevOps

## Objetivo

Este projeto foi desenvolvido para praticar conceitos de DevOps,
controle de versão com Git e testes automatizados com Python.

## Tecnologias utilizadas

- Python
- Git
- pytest
- GitHub Actions (integração contínua)

## Funcionalidade

O projeto possui uma função que calcula o valor total de um pedido
com base no preço e na quantidade de cada item.

## Como preparar o ambiente

1. Instale o Python.
2. Abra o terminal na pasta do projeto.
3. Instale as dependências:

   python -m pip install -r requirements.txt

## Como executar os testes

Execute o comando:

python -m pytest -v

## Estrutura do projeto

- src/: código da aplicação.
- tests/: testes automatizados.
- .github/workflows/: configuração do pipeline de CI.

## Controle de versão

O projeto utiliza Git para registrar alterações e a convenção
Conventional Commits para padronizar as mensagens dos commits.

## Exemplo de uso

A função `processar_pedido` recebe uma lista de itens
e retorna a quantidade total de unidades e o valor do pedido.