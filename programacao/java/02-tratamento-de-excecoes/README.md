# Tratamento de Exceções em Java

Atividade acadêmica desenvolvida em Java com o objetivo de aplicar conceitos de Programação Orientada a Objetos, com foco em abstração, herança, sobrescrita de métodos e tratamento de exceções.

O projeto implementa uma estrutura simples de operações matemáticas utilizando uma classe abstrata como base para diferentes operações. Além disso, utiliza uma exceção personalizada para tratar tentativas de divisão por zero de forma controlada.

## Objetivo

A atividade tem como principais objetivos:

- Utilizar classes abstratas em Java;
- Aplicar herança entre classes;
- Implementar e sobrescrever métodos com `@Override`;
- Criar uma exceção personalizada;
- Utilizar `throw` para lançar uma exceção;
- Utilizar `throws` para declarar a possibilidade de uma exceção;
- Aplicar `try-catch` para tratamento de erros;
- Evitar que situações inválidas encerrem a aplicação de maneira inesperada.

## Estrutura das classes

O projeto é composto pelas seguintes classes:

### `OperacaoMatematica`

Classe abstrata que representa uma operação matemática de forma genérica.

Ela declara o método:

```java
public abstract double calcular(double a, double b) throws DivisaoPorZeroException;
```

As subclasses são responsáveis por fornecer a implementação específica desse método.

### `Soma`

A classe `Soma` herda de `OperacaoMatematica` e sobrescreve o método `calcular()`:

```java
@Override
public double calcular(double a, double b) {
    return a + b;
}
```

Nesse caso, o método simplesmente retorna a soma dos dois valores recebidos.

### `Divisao`

A classe `Divisao` também herda de `OperacaoMatematica`, mas realiza uma validação antes de executar o cálculo.

```java
@Override
public double calcular(double a, double b) throws DivisaoPorZeroException {
    if (b == 0) {
        throw new DivisaoPorZeroException();
    }

    return a / b;
}
```

Caso o divisor seja igual a zero, uma exceção personalizada é lançada em vez de realizar a operação.

### `DivisaoPorZeroException`

Exceção personalizada criada especificamente para representar uma tentativa de divisão por zero.

```java
public class DivisaoPorZeroException extends Exception {
    public DivisaoPorZeroException() {
        super("Não é possível dividir por zero.");
    }
}
```

Por herdar de `Exception`, trata-se de uma exceção verificada (*checked exception*), que precisa ser declarada ou tratada pelo programa.

### `Principal`

A classe `Principal` contém o método `main()` e realiza os testes das operações.

São executados três casos:

1. Soma de `10 + 5`;
2. Divisão de `10 / 2`;
3. Tentativa de divisão de `10 / 0`.

O tratamento da exceção é realizado com um bloco `try-catch`:

```java
try {
    // execução das operações
} catch (DivisaoPorZeroException e) {
    System.out.println("Erro capturado: " + e.getMessage());
}
```

Dessa forma, uma tentativa de divisão por zero é tratada de maneira controlada.

## Conceitos aplicados

### Abstração

A classe `OperacaoMatematica` define uma estrutura comum para diferentes tipos de operações sem determinar diretamente como cada cálculo deve ser realizado.

### Herança

As classes `Soma` e `Divisao` utilizam:

```java
extends OperacaoMatematica
```

permitindo que ambas compartilhem a estrutura definida pela classe abstrata.

### Sobrescrita

Cada operação fornece sua própria implementação do método `calcular()`, utilizando a anotação:

```java
@Override
```

### Exceção personalizada

A classe `DivisaoPorZeroException` representa especificamente uma situação inválida dentro da aplicação.

Quando o divisor é zero, a classe `Divisao` utiliza:

```java
throw new DivisaoPorZeroException();
```

para interromper o fluxo normal da operação e sinalizar o problema.

### Tratamento com `try-catch`

A classe `Principal` captura a exceção e apresenta uma mensagem adequada ao usuário, evitando que a situação seja tratada como uma falha não controlada da aplicação.

## Resultado da execução

A execução do programa apresenta:

```text
Soma de 10 + 5:
15.0
Divisão de 10 / 2:
5.0
Tentativa de divisão de 10 / 0:
Erro capturado: Não é possível dividir por zero.
```

O resultado demonstra que as operações válidas são realizadas normalmente e que a tentativa de divisão por zero é interceptada pela exceção personalizada.

## Estrutura do projeto

```text
02-tratamento-de-excecoes/
├── Divisao.java
├── DivisaoPorZeroException.java
├── OperacaoMatematica.java
├── Principal.java
├── Soma.java
└── README.md
```

Os arquivos `.class` gerados durante a compilação são ignorados pelo Git e não são versionados no repositório.

## Como compilar

Com o JDK instalado, execute na pasta da atividade:

```bash
javac *.java
```

## Como executar

Após a compilação:

```bash
java Principal
```

## Organização para o repositório

Esta atividade foi organizada para o repositório a partir dos conceitos, estrutura e resultados registrados no relatório acadêmico original.

Durante a reconstrução do código, foi necessário garantir que a assinatura do método abstrato `calcular()` fosse compatível com a exceção verificada `DivisaoPorZeroException` utilizada pela implementação da classe `Divisao`.

Por esse motivo, a classe abstrata declara:

```java
throws DivisaoPorZeroException
```

permitindo que a implementação de `Divisao` lance a exceção personalizada de forma compatível com as regras de sobrescrita de métodos em Java.

Essa adequação mantém o comportamento e os conceitos propostos na atividade, ao mesmo tempo em que permite a compilação correta da implementação organizada neste repositório.

## Contexto acadêmico

Este projeto foi desenvolvido como atividade acadêmica da disciplina de Linguagem Orientada a Objetos durante a graduação em Análise e Desenvolvimento de Sistemas.

A atividade teve como foco a aplicação prática de classes abstratas, herança, sobrescrita de métodos e tratamento de exceções em Java.