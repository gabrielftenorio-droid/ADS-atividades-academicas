# Estruturas de Repetição em C

Atividade acadêmica desenvolvida na disciplina de **Algoritmos e Programação Estruturada**, com foco na utilização da estrutura de repetição `while` na linguagem C.

## Objetivo

Desenvolver um programa capaz de receber uma quantidade indeterminada de números inteiros e calcular a soma dos valores informados pelo usuário.

O número `0` é utilizado como **valor sentinela**, indicando o encerramento da entrada de dados.

## Conceitos praticados

- Estrutura de repetição `while`
- Valor sentinela
- Variáveis acumuladoras
- Entrada de dados com `scanf()`
- Saída de dados com `printf()`
- Controle de fluxo
- Condições de repetição

## Funcionamento

O programa:

1. Solicita um número inteiro ao usuário.
2. Verifica se o valor informado é diferente de `0`.
3. Enquanto a condição for verdadeira, adiciona o número à soma acumulada.
4. Solicita um novo número.
5. Repete o processo até que o usuário informe `0`.
6. Encerra o laço e apresenta a soma total dos valores informados.

### Exemplo

Entrada:

```text
10
5
20
-3
0