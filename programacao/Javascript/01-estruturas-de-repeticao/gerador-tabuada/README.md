# Gerador de Tabuada Interativo

## Sobre o projeto

Atividade prática desenvolvida durante os estudos de JavaScript, com foco em estruturas de repetição. O projeto consiste em uma página web que gera a tabuada de um número inteiro entre 1 e 10, exibindo os resultados dinamicamente na tela.

## Funcionalidades

- Receber um número informado pelo usuário.
- Gerar a tabuada do número selecionado, de 1 a 10.
- Validar a entrada para aceitar apenas números inteiros entre 1 e 10.
- Exibir uma mensagem de erro quando o valor informado for inválido.
- Atualizar os resultados na página sem precisar recarregá-la.

## Tecnologias utilizadas

- **HTML5:** estrutura da página.
- **CSS3:** estilização e apresentação visual.
- **JavaScript:** validação da entrada, cálculo da tabuada e atualização dos elementos da página.

## Estrutura dos arquivos

- `index.html`: estrutura da aplicação.
- `style.css`: estilos da página.
- `script.js`: lógica de geração da tabuada e validação dos dados.

## Como executar

1. Abra o arquivo `index.html` em um navegador.
2. Digite um número inteiro entre 1 e 10.
3. Clique em **Gerar tabuada**.
4. Confira os resultados exibidos na página.

## Conceitos praticados

- Declaração de variáveis com `const` e `let`.
- Conversão e validação de valores numéricos.
- Estrutura condicional `if`.
- Laço de repetição `for`.
- Manipulação do DOM.
- Eventos de clique com `addEventListener`.
- Criação e inserção de elementos HTML com JavaScript.

## Validação e testes

Foram realizados testes com valores válidos e inválidos:

- **Valores válidos:** números inteiros de 1 a 10, com geração da tabuada correspondente.
- **Valores inválidos:** valores como `0` e `11`, que exibem uma mensagem de validação.
