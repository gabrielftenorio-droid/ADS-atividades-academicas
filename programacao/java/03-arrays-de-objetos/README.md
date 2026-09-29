# Arrays de Objetos em Java

Atividade acadêmica desenvolvida em Java com o objetivo de aplicar conceitos de Programação Orientada a Objetos utilizando arrays de objetos, estruturas de repetição e pesquisa de texto com o método `contains()`.

O projeto implementa um pequeno catálogo de livros. Cada livro é representado por um objeto contendo título, autor e ano de publicação.

Durante a organização da atividade para este repositório, a busca originalmente fixa pela palavra `"Java"` foi evoluída para permitir que o usuário informe uma palavra a ser pesquisada nos títulos.

## Objetivo

A atividade tem como principais objetivos:

- Criar uma classe para representar objetos do tipo `Livro`;
- Utilizar construtores para inicializar objetos;
- Criar e manipular arrays de objetos;
- Percorrer um array utilizando uma estrutura de repetição;
- Utilizar o método `contains()` para pesquisar textos;
- Exibir informações dos objetos encontrados;
- Aplicar conceitos básicos de Programação Orientada a Objetos em Java.

## Classe Livro

A classe `Livro` representa os livros armazenados no catálogo.

Cada objeto possui:

```java
String titulo;
String autor;
int ano;
```

O construtor recebe essas informações no momento da criação do objeto:

```java
public Livro(String titulo, String autor, int ano) {
    this.titulo = titulo;
    this.autor = autor;
    this.ano = ano;
}
```

A classe também possui o método `exibirInformacoes()`, responsável por apresentar os dados do livro no console.

## Array de objetos

Na classe `Principal`, é criado um array capaz de armazenar cinco objetos do tipo `Livro`:

```java
Livro[] livros = new Livro[5];
```

Os livros utilizados nesta versão são:

- Dom Casmurro — Machado de Assis;
- O Alquimista — Paulo Coelho;
- Grande Sertão: Veredas — João Guimarães Rosa;
- Ensaio Sobre a Cegueira — José Saramago;
- Vidas Secas — Graciliano Ramos.

Cada posição do array armazena uma referência para um objeto `Livro`.

## Percorrendo o array

Para percorrer os objetos armazenados, é utilizado um `for-each`:

```java
for (Livro livro : livros) {
    // processamento de cada livro
}
```

A cada repetição, a variável `livro` representa um dos objetos presentes no array.

## Busca por título

Na atividade acadêmica original, o método `contains()` foi utilizado para identificar livros que possuíam a palavra `"Java"` no título.

Nesta versão organizada para o repositório, esse conceito foi mantido e a busca foi tornada interativa.

O usuário informa uma palavra:

```java
System.out.print("Digite uma palavra para buscar no título: ");
String busca = scanner.nextLine();
```

Em seguida, cada título é verificado:

```java
if (livro.titulo.toLowerCase().contains(busca.toLowerCase())) {
    livro.exibirInformacoes();
}
```

O uso de `toLowerCase()` permite que diferenças entre letras maiúsculas e minúsculas não interfiram na pesquisa.

Por exemplo, as buscas:

```text
dom
Dom
DOM
```

podem localizar o título:

```text
Dom Casmurro
```

## Tratamento de busca sem resultado

Uma variável booleana é utilizada para registrar se algum livro foi encontrado:

```java
boolean encontrado = false;
```

Quando existe uma correspondência, seu valor é alterado para `true`.

Caso nenhum título corresponda à pesquisa, o programa apresenta:

```text
Nenhum livro encontrado.
```

## Exemplo de execução

Pesquisa:

```text
Digite uma palavra para buscar no título: dom
```

Resultado:

```text
Resultado da busca:
-------------------------
Título: Dom Casmurro
Autor: Machado de Assis
Ano: 1899
-------------------------
```

Também foi testada uma pesquisa sem correspondência:

```text
Digite uma palavra para buscar no título: java

Resultado da busca:
Nenhum livro encontrado.
```

## Estrutura do projeto

```text
03-arrays-de-objetos/
├── Livro.java
├── Principal.java
└── README.md
```

Os arquivos `.class` gerados durante a compilação são ignorados pelo Git e não são versionados no repositório.

## Como compilar

Com o JDK instalado, execute na pasta da atividade:

```bash
javac Livro.java Principal.java
```

## Como executar

Após a compilação:

```bash
java Principal
```

O programa solicitará uma palavra para realizar a pesquisa nos títulos cadastrados.

## Organização para o repositório

A atividade acadêmica original utilizava um catálogo com cinco livros e realizava uma busca fixa pela palavra `"Java"` utilizando o método `contains()`.

O relatório registra que três dos cinco títulos utilizados originalmente atendiam a essa condição.

Durante a organização para este repositório, os livros cadastrados foram substituídos e a busca foi transformada em uma entrada interativa utilizando `Scanner`.

Também foi adicionada uma verificação para informar quando nenhum livro corresponde à pesquisa.

Essas alterações preservam os principais conceitos trabalhados na atividade — objetos, arrays, estruturas de repetição e `contains()` — ao mesmo tempo em que tornam o programa mais interativo.

## Contexto acadêmico

Este projeto teve origem em uma atividade acadêmica da disciplina de Linguagem Orientada a Objetos durante a graduação em Análise e Desenvolvimento de Sistemas.

A atividade original teve como foco a criação e manipulação de arrays de objetos em Java e a utilização do método `contains()` para realizar buscas em textos.