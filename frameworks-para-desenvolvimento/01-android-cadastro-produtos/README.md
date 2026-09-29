# Cadastro de Produtos Android com SQLite

Aplicação Android desenvolvida como atividade prática da disciplina **Framework para Desenvolvimento de Software**, do curso de Análise e Desenvolvimento de Sistemas.

O projeto implementa um cadastro simples de produtos utilizando **Java** e persistência local com **SQLite**, permitindo inserir produtos, validar os dados informados e recuperar os registros armazenados mesmo após a reinicialização da aplicação.

## Objetivo

A atividade teve como objetivo aplicar conceitos de desenvolvimento Android e persistência local de dados, utilizando o `SQLiteOpenHelper` para criação e gerenciamento do banco de dados da aplicação.

Durante o desenvolvimento foram trabalhados:

- criação de uma aplicação Android;
- construção de uma interface para cadastro;
- modelagem de uma classe `Produto`;
- persistência local com SQLite;
- utilização de `SQLiteOpenHelper`;
- inserção e consulta de registros;
- validação de dados de entrada;
- exibição dos produtos cadastrados;
- testes funcionais;
- verificação da persistência dos dados.

## Tecnologias utilizadas

- Java
- Android Studio
- Android SDK
- SQLite
- SQLiteOpenHelper
- Gradle

## Estrutura principal

A implementação foi organizada em três classes Java principais:

### `Produto.java`

Representa os dados de um produto utilizados pela aplicação.

### `ProdutoDbHelper.java`

Responsável pelo gerenciamento do banco de dados SQLite, incluindo a criação da estrutura necessária para armazenamento e as operações utilizadas para inserir e recuperar produtos.

### `MainActivity.java`

Responsável pela interação com a interface da aplicação, leitura dos dados informados pelo usuário, validações, cadastro dos produtos e atualização da listagem apresentada na tela.

A interface principal está definida em:

```text
app/src/main/res/layout/activity_main.xml
```

## Funcionalidades

A aplicação permite:

- informar o nome de um produto;
- informar o preço;
- salvar o produto no banco de dados local;
- visualizar os produtos cadastrados;
- recuperar os registros armazenados;
- validar os dados antes da gravação.

## Validações

Foram aplicadas regras para impedir o armazenamento de dados inválidos.

### Nome

O nome do produto deve possuir pelo menos **3 caracteres**.

Caso contrário, a aplicação informa:

```text
Nome inválido. Mínimo de 3 caracteres.
```

### Preço

O preço deve ser um valor **maior que zero**.

Valores inválidos não são armazenados no banco de dados.

A aplicação informa:

```text
Preço inválido. Informe um valor maior que zero.
```

## Testes realizados

Durante a atividade foram utilizados produtos válidos para verificar o cadastro:

| Produto | Preço |
|---|---:|
| Caneta Azul | R$ 2,50 |
| Caderno Universitário | R$ 15,00 |
| Borracha | R$ 2,50 |
| Régua de 30 cm | R$ 3,00 |
| Marca-texto | R$ 4,50 |

Também foram realizados testes com entradas inválidas.

O nome `AB`, com apenas dois caracteres, foi rejeitado pela validação.

Também foi testado o produto `Lápis` com preço `-3,00`, que não foi armazenado por possuir valor inferior a zero.

Posteriormente, o nome `ABC` foi utilizado para confirmar que um nome com exatamente três caracteres era aceito pela aplicação.

## Persistência dos dados

Após os cadastros, a aplicação foi interrompida e executada novamente.

Os produtos cadastrados anteriormente continuaram disponíveis na listagem, confirmando que os registros estavam sendo armazenados no SQLite e não apenas mantidos temporariamente durante a execução da aplicação.

## Estrutura do projeto

```text
01-android-cadastro-produtos/
├── app/
│   ├── src/
│   │   ├── androidTest/
│   │   ├── main/
│   │   │   ├── java/com/example/cadastroprodutos/
│   │   │   │   ├── MainActivity.java
│   │   │   │   ├── Produto.java
│   │   │   │   └── ProdutoDbHelper.java
│   │   │   ├── res/
│   │   │   │   └── layout/
│   │   │   │       └── activity_main.xml
│   │   │   └── AndroidManifest.xml
│   │   └── test/
│   └── build.gradle.kts
├── gradle/
├── build.gradle.kts
├── gradle.properties
├── gradlew
├── gradlew.bat
└── settings.gradle.kts
```

## Como executar

1. Clone ou baixe o repositório.
2. Abra a pasta desta atividade no Android Studio.
3. Aguarde a sincronização das dependências do Gradle.
4. Configure um dispositivo virtual Android ou utilize um dispositivo compatível.
5. Execute a aplicação pelo Android Studio.
6. Preencha o nome e o preço de um produto.
7. Utilize o botão de salvamento para realizar o cadastro.
8. Verifique o produto na listagem apresentada pela aplicação.

## Contexto acadêmico

Projeto desenvolvido em **2026** como atividade prática da disciplina **Framework para Desenvolvimento de Software**, na unidade relacionada à aplicação de frameworks, desenvolvimento mobile e back-end.

A atividade teve como foco a implementação de uma aplicação Android funcional com armazenamento local, permitindo aplicar na prática conceitos de persistência, validação de entradas e manipulação de dados.

> Este diretório preserva a implementação realizada durante a atividade acadêmica. Arquivos locais, caches e artefatos gerados pelo ambiente de desenvolvimento e pelo processo de compilação não fazem parte do versionamento.