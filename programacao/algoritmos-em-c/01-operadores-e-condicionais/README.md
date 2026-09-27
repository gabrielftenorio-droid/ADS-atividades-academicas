# Operadores e Condicionais em C

Atividade acadêmica desenvolvida na disciplina de **Algoritmos e Programação Estruturada**, com o objetivo de praticar conceitos fundamentais da linguagem C.

## Objetivo

Desenvolver um programa capaz de receber três números inteiros e realizar operações aritméticas, comparações e verificações lógicas.

## Conceitos praticados

- Entrada e saída de dados com `scanf()` e `printf()`
- Operadores aritméticos
- Operadores relacionais
- Operadores lógicos
- Estruturas condicionais `if/else`
- Operador módulo `%`
- Conversão de tipos para operações de divisão
- Validação para evitar divisão por zero

## Funcionamento

O programa:

1. Solicita três números inteiros ao usuário.
2. Realiza operações aritméticas utilizando os valores informados.
3. Verifica se é possível realizar a divisão sem divisão por zero.
4. Compara se o primeiro número é maior que o segundo.
5. Compara se o segundo número é menor que o terceiro.
6. Verifica se o primeiro número é positivo e se o segundo número é par.
7. Apresenta os resultados das verificações como verdadeiro ou falso.

## Conceitos utilizados

### Operadores aritméticos

O programa utiliza operações de:

- adição (`+`);
- subtração (`-`);
- multiplicação (`*`);
- divisão (`/`).

Antes da divisão, os valores são verificados para evitar uma operação com divisor igual a zero.

### Operadores relacionais

São realizadas comparações utilizando os operadores:

```c
num1 > num2
```

e:

```c
num2 < num3
```

Essas expressões permitem verificar relações entre os números fornecidos pelo usuário.

### Operadores lógicos

O programa também combina duas condições utilizando o operador lógico AND (`&&`):

```c
num1 > 0 && num2 % 2 == 0
```

A expressão verifica simultaneamente se:

- o primeiro número é positivo;
- o segundo número é par.

O operador módulo (`%`) é utilizado para verificar o resto da divisão por 2.

## Contexto acadêmico

Esta atividade faz parte dos meus estudos iniciais de programação estruturada em C durante a graduação em Análise e Desenvolvimento de Sistemas.

O código disponível neste diretório foi reconstruído a partir da lógica e dos requisitos documentados no relatório acadêmico original.