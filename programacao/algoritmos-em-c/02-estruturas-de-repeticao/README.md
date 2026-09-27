# Estruturas de Repetição em C

Atividade acadêmica desenvolvida na disciplina de **Algoritmos e Programação Estruturada**, com foco na utilização de estruturas de repetição na linguagem C.

## Objetivo

Desenvolver um programa capaz de receber números inteiros sucessivamente, acumulando seus valores até que o usuário informe `0` para encerrar a execução.

## Conceitos praticados

- Estrutura de repetição `while`
- Condição de parada
- Valor sentinela
- Variável acumuladora
- Entrada de dados com `scanf()`
- Saída de dados com `printf()`
- Operadores de comparação
- Atualização de variáveis durante uma repetição

## Funcionamento

O programa:

1. Solicita um número inteiro ao usuário.
2. Verifica se o número informado é diferente de `0`.
3. Enquanto essa condição for verdadeira, adiciona o número à soma acumulada.
4. Solicita um novo número.
5. Repete o processo enquanto o usuário não informar `0`.
6. Ao receber `0`, encerra o laço.
7. Exibe a soma total dos valores informados.

## Estrutura de repetição

A principal estrutura utilizada é o `while`:

```c
while (numero != 0) {
    soma_total = soma_total + numero;

    printf("Digite outro numero inteiro (0 para encerrar): ");
    scanf("%d", &numero);
}
```

Nesse caso, o valor `0` funciona como **sentinela**, indicando quando a repetição deve terminar.

O zero não é acrescentado à soma, pois a condição do `while` deixa de ser verdadeira assim que esse valor é informado.

## Exemplo de execução

Entrada:

```text
10
5
20
-3
0
```

Resultado:

```text
Programa encerrado.
Soma total: 32
```

O resultado pode ser verificado pela soma:

```text
10 + 5 + 20 - 3 = 32
```

## Contexto acadêmico

Esta atividade faz parte dos meus estudos iniciais de programação estruturada em C durante a graduação em Análise e Desenvolvimento de Sistemas.

O exercício introduz o uso de estruturas de repetição controladas por condição e demonstra como um valor sentinela pode ser utilizado para determinar o encerramento de um processamento.

O código disponível neste diretório foi reconstruído a partir da lógica e dos requisitos documentados no relatório acadêmico original.