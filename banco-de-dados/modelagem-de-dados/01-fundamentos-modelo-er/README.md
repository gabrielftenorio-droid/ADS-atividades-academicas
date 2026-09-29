# Fundamentos de Modelagem Entidade-Relacionamento

Atividade acadêmica desenvolvida com o objetivo de aplicar os fundamentos da modelagem de dados por meio do Modelo Entidade-Relacionamento (MER).

O trabalho aborda a identificação de entidades, atributos, chaves primárias e estrangeiras e relacionamentos entre entidades, utilizando diferentes cenários para representar estruturas de dados de forma conceitual.

## Objetivo

A atividade teve como principais objetivos:

- Compreender os fundamentos do Modelo Entidade-Relacionamento;
- Identificar entidades e seus respectivos atributos;
- Definir chaves primárias;
- Utilizar chaves estrangeiras para representar relacionamentos;
- Compreender diferentes cardinalidades;
- Trabalhar com atributos simples, compostos e multivalorados;
- Representar regras de negócio por meio da modelagem de dados.

---

# Cenário 1 — Sistema de Biblioteca

O primeiro cenário representa um sistema destinado ao gerenciamento de uma biblioteca.

Foram consideradas três entidades principais:

- `LIVRO`
- `LEITOR`
- `EMPRÉSTIMO`

## Entidade LIVRO

Representa os livros disponíveis na biblioteca.

Entre as informações associadas a um livro podem estar dados utilizados para sua identificação e descrição dentro do sistema.

Cada livro possui uma identificação própria, permitindo que seja diferenciado dos demais registros.

## Entidade LEITOR

Representa as pessoas cadastradas para utilizar os serviços da biblioteca.

Cada leitor possui uma identificação própria e informações necessárias para seu cadastro.

## Entidade EMPRÉSTIMO

Representa a operação realizada quando um leitor retira um livro da biblioteca.

Essa entidade permite relacionar os registros de livros e leitores, armazenando as informações necessárias sobre cada empréstimo.

O relacionamento utiliza chaves estrangeiras para associar o empréstimo às entidades correspondentes.

## Relacionamentos

O modelo permite representar situações em que um leitor pode realizar diferentes empréstimos ao longo do tempo e um livro pode participar de diferentes operações de empréstimo.

A entidade `EMPRÉSTIMO` funciona como elemento de ligação entre os dados de leitores e livros.

De forma simplificada:

```text
LEITOR
   │
   │
   └──── EMPRÉSTIMO ──── LIVRO
```

A estrutura demonstra como relacionamentos entre entidades podem ser representados utilizando identificadores e referências entre registros.

---

# Cenário 2 — Sistema de Clínica

Outro cenário utilizado na atividade representa informações relacionadas ao funcionamento de uma clínica.

As principais entidades consideradas são:

- `PACIENTE`
- `MÉDICO`
- `CONSULTA`

## Entidade PACIENTE

Representa os pacientes cadastrados no sistema.

A entidade reúne informações necessárias para identificar e registrar cada paciente.

Durante a modelagem também são considerados diferentes tipos de atributos, incluindo situações em que uma informação pode ser composta por outras partes.

## Entidade MÉDICO

Representa os profissionais responsáveis pelos atendimentos.

Cada médico possui informações próprias que permitem sua identificação dentro do sistema.

## Entidade CONSULTA

Representa o atendimento realizado entre um médico e um paciente.

Essa entidade estabelece a associação entre os participantes da consulta e permite armazenar informações relacionadas ao atendimento.

De forma simplificada:

```text
PACIENTE
    │
    │
    └──── CONSULTA ──── MÉDICO
```

---

# Conceitos trabalhados

## Entidades

Uma entidade representa um elemento relevante do domínio que precisa ter suas informações armazenadas.

Exemplos utilizados na atividade:

```text
LIVRO
LEITOR
EMPRÉSTIMO
PACIENTE
MÉDICO
CONSULTA
```

## Atributos

Os atributos representam características ou informações associadas às entidades.

Eles permitem descrever os dados que deverão ser armazenados para cada registro.

Durante a atividade foram trabalhados diferentes tipos de atributos, incluindo atributos simples, compostos e multivalorados.

## Chave primária

A chave primária (`Primary Key`) é utilizada para identificar de maneira única cada registro de uma entidade.

De forma conceitual:

```text
ENTIDADE
├── id_entidade (PK)
└── demais atributos
```

## Chave estrangeira

A chave estrangeira (`Foreign Key`) permite estabelecer uma referência entre registros pertencentes a entidades diferentes.

No cenário da biblioteca, por exemplo, a entidade responsável pelo empréstimo precisa estabelecer relações com o leitor e com o livro envolvidos na operação.

De forma simplificada:

```text
EMPRÉSTIMO
├── id_emprestimo (PK)
├── id_leitor (FK)
└── id_livro (FK)
```

## Cardinalidade

A cardinalidade determina a quantidade de ocorrências de uma entidade que pode estar associada às ocorrências de outra entidade.

Entre as possibilidades estudadas estão:

```text
1:1  → um para um
1:N  → um para muitos
N:M  → muitos para muitos
```

A definição correta da cardinalidade é importante para representar as regras existentes no domínio modelado.

## Atributos compostos

Um atributo composto pode ser dividido em informações menores.

Um exemplo conceitual é um endereço:

```text
ENDEREÇO
├── rua
├── número
├── cidade
└── CEP
```

## Atributos multivalorados

Um atributo multivalorado pode possuir mais de um valor associado à mesma entidade.

Um exemplo conceitual seria uma pessoa possuir mais de um telefone.

```text
PESSOA
└── telefone
    ├── telefone 1
    └── telefone 2
```

---

# Aprendizados

A atividade permitiu compreender como requisitos de um domínio podem ser transformados em uma representação estruturada dos dados.

A identificação correta de entidades, atributos, relacionamentos e cardinalidades constitui uma etapa importante no desenvolvimento de bancos de dados, pois fornece uma base conceitual para etapas posteriores de construção do modelo lógico e implementação do banco.

Também foi possível observar que diferentes cenários podem utilizar os mesmos princípios de modelagem, mesmo quando representam domínios distintos.

---

## Organização para o repositório

Esta atividade foi reorganizada para apresentação neste repositório acadêmico.

A documentação preserva os principais conceitos e cenários trabalhados na atividade original, apresentando-os em uma estrutura mais adequada para consulta pelo GitHub.

Os diagramas textuais utilizados neste `README` têm finalidade de documentação e representação simplificada dos relacionamentos e não substituem os diagramas desenvolvidos durante a atividade acadêmica.

## Contexto acadêmico

Este trabalho foi desenvolvido durante a graduação em Análise e Desenvolvimento de Sistemas, na disciplina de Modelagem de Dados.

A atividade teve como foco a introdução aos fundamentos do Modelo Entidade-Relacionamento e à representação estruturada de entidades, atributos e relacionamentos.