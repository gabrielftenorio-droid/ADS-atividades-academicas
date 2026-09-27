# Vetores em C

Atividade acadêmica desenvolvida na disciplina de **Algoritmos e Programação Estruturada**, com foco na declaração, preenchimento e manipulação de vetores na linguagem C.

## Objetivo

Desenvolver um programa que simule o registro das vendas diárias de uma pequena loja.

O programa recebe cinco valores inteiros, armazena os dados em um vetor e posteriormente percorre seus elementos para exibir as vendas registradas e calcular o total do período.

## Conceitos praticados

- Declaração de vetores
- Indexação de elementos
- Estrutura de repetição `for`
- Entrada de dados com `scanf()`
- Saída de dados com `printf()`
- Variável acumuladora
- Percorrimento de arrays
- Operador de atribuição `+=`

## Funcionamento

O programa:

1. Declara um vetor de inteiros com cinco posições.
2. Utiliza um laço `for` para solicitar as vendas de cinco dias.
3. Armazena cada valor em uma posição do vetor.
4. Utiliza um segundo laço `for` para percorrer os valores armazenados.
5. Exibe a venda correspondente a cada dia.
6. Soma os elementos do vetor.
7. Apresenta o total de vendas do período.

## Utilização do vetor

Os valores são armazenados em:

```c
int vendas_diarias[5];
```

O vetor possui cinco posições, que em C são identificadas pelos índices de `0` a `4`.

O primeiro laço percorre essas posições para realizar a entrada dos dados:

```c
for (i = 0; i < 5; i++) {
    printf("Digite o valor das vendas do dia %d: ", i + 1);
    scanf("%d", &vendas_diarias[i]);
}
```

Posteriormente, outro laço percorre os valores armazenados e realiza a soma:

```c
for (i = 0; i < 5; i++) {
    printf("Dia %d: %d\n", i + 1, vendas_diarias[i]);
    soma_total += vendas_diarias[i];
}
```

## Exemplo de execução

Entrada:

```text
10
15
17
5
10
```

Resultado:

```text
Dia 1: 10
Dia 2: 15
Dia 3: 17
Dia 4: 5
Dia 5: 10

Total de vendas no periodo: 57
```

O resultado corresponde à soma:

```text
10 + 15 + 17 + 5 + 10 = 57
```

## Contexto acadêmico

Esta atividade faz parte dos meus estudos iniciais de programação estruturada em C durante a graduação em Análise e Desenvolvimento de Sistemas.

O exercício demonstra a utilização de vetores para armazenar vários valores relacionados em uma única estrutura e o uso de estruturas de repetição para percorrer e processar esses dados.

O código disponível neste diretório foi reconstruído a partir da lógica e dos requisitos documentados no relatório acadêmico original.