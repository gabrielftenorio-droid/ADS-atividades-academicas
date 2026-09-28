# Construtores e Sobrecarga em Java

Atividade acadêmica desenvolvida em Java com o objetivo de aplicar conceitos fundamentais de Programação Orientada a Objetos, com foco em construtores, sobrecarga e membros estáticos.

O projeto implementa um sistema simples de cadastro de produtos, no qual diferentes objetos da classe `Produto` podem ser criados utilizando construtores distintos e uma variável compartilhada mantém o controle da quantidade total de produtos instanciados.

## Objetivo

A atividade tem como principais objetivos:

- Criar e instanciar objetos em Java;
- Utilizar atributos de instância;
- Implementar diferentes construtores;
- Aplicar sobrecarga de construtores;
- Utilizar o modificador `static`;
- Diferenciar membros de instância e membros pertencentes à classe;
- Criar métodos para exibição das informações dos objetos.

## Estrutura da classe Produto

A classe `Produto` possui os seguintes atributos:

```java
private String nome;
private double preco;
private static int quantidadeTotal = 0;
```

Os atributos `nome` e `preco` pertencem individualmente a cada objeto criado.

Já `quantidadeTotal` utiliza o modificador `static`, fazendo com que a variável seja compartilhada entre todas as instâncias da classe.

## Sobrecarga de construtores

A classe possui dois construtores.

### Construtor padrão

```java
public Produto()
```

Permite criar um produto sem informar seus atributos durante a instanciação.

### Construtor parametrizado

```java
public Produto(String nome, double preco)
```

Permite criar um produto informando nome e preço diretamente.

A existência de construtores com o mesmo nome e diferentes listas de parâmetros demonstra o conceito de sobrecarga.

Nos dois casos, a criação de um novo objeto incrementa a variável estática `quantidadeTotal`.

## Métodos

### `exibirDados()`

Apresenta o nome e o preço associados a uma determinada instância de `Produto`.

### `exibirQuantidadeTotal()`

Método estático utilizado para apresentar a quantidade total de objetos `Produto` criados durante a execução.

Por ser estático, pode ser chamado diretamente através da classe:

```java
Produto.exibirQuantidadeTotal();
```

## Classe Principal

A classe `Principal` contém o método `main()` responsável pela execução do programa.

Durante a execução são criados três objetos da classe `Produto`, utilizando tanto o construtor padrão quanto o construtor parametrizado.

Em seguida, os dados dos produtos são apresentados e o método estático da classe é utilizado para exibir a quantidade total de objetos criados.

## Exemplo de execução

```text
Nome: null
Preço: R$ 0.0
Nome: Notebook
Preço: R$ 3500.0
Nome: Mouse
Preço: R$ 120.0
Quantidade total de produtos: 3
```

O primeiro produto apresenta `null` para o nome e `0.0` para o preço porque foi criado utilizando o construtor sem parâmetros e esses atributos não receberam novos valores posteriormente.

## Estrutura do projeto

```text
01-construtores-e-sobrecarga/
├── Principal.java
├── Produto.java
└── README.md
```

Os arquivos `.class` gerados durante a compilação são ignorados pelo Git e não são versionados no repositório.

## Como compilar

Com o JDK instalado, execute na pasta da atividade:

```bash
javac Produto.java Principal.java
```

Após a compilação, serão gerados localmente os arquivos:

```text
Produto.class
Principal.class
```

## Como executar

Após a compilação:

```bash
java Principal
```

## Organização para o repositório

A atividade original foi desenvolvida durante a graduação utilizando a classe `Produto`, uma classe principal e o pacote `br.edu.produto`.

Durante a organização para este repositório, o código foi reconstruído a partir das informações e registros presentes no relatório acadêmico, preservando os conceitos, a estrutura e o comportamento documentados na atividade.

Para permitir uma execução direta e simplificada dentro da organização deste repositório, as classes foram mantidas no mesmo diretório, sem a declaração do pacote original.

Os valores utilizados nos produtos durante esta reconstrução servem para demonstrar o funcionamento documentado da atividade e não são apresentados como reprodução dos valores originais utilizados no trabalho acadêmico.

## Contexto acadêmico

Este projeto foi desenvolvido como atividade acadêmica da disciplina de Linguagem Orientada a Objetos durante a graduação em Análise e Desenvolvimento de Sistemas.

A atividade teve como foco a aplicação prática de construtores, sobrecarga, atributos de instância, atributos estáticos e métodos em Java.