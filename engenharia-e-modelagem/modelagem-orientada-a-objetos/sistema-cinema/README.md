# Sistema de Cinema — Modelagem Orientada a Objetos com UML

Estudo acadêmico de modelagem orientada a objetos aplicado ao domínio de um **Sistema de Cinema**, desenvolvido durante a graduação em Análise e Desenvolvimento de Sistemas.

O conjunto reúne três atividades relacionadas, utilizando diferentes diagramas UML para representar perspectivas complementares do mesmo domínio:

- estrutura do sistema;
- interação entre os participantes;
- comportamento durante o processo de venda de ingressos.

> As atividades foram desenvolvidas academicamente em etapas distintas e posteriormente organizadas em conjunto neste repositório por utilizarem o mesmo domínio e apresentarem uma evolução natural dos conceitos de modelagem UML.

---

## Visão geral

Um sistema de software pode ser analisado a partir de diferentes perspectivas.

Neste estudo, três tipos de diagramas UML foram utilizados:

```text
DIAGRAMA DE CLASSES
        │
        │ estrutura
        ▼
Quais elementos existem
e como se relacionam?
        │
        ▼
DIAGRAMA DE SEQUÊNCIA
        │
        │ interação
        ▼
Como os participantes
colaboram durante a venda?
        │
        ▼
MÁQUINA DE ESTADOS
        │
        │ comportamento
        ▼
Como o sistema muda de estado
durante o processo?
```

Dessa forma, as atividades permitem observar o mesmo domínio sob diferentes perspectivas.

---

## 01 — Diagrama de Classes

📁 [`01-diagrama-de-classes`](./01-diagrama-de-classes/)

Representa a **estrutura estática** do Sistema de Cinema.

A atividade parte da análise dos requisitos do domínio para identificar elementos e relacionamentos relacionados a conceitos como:

```text
Gênero
Filme
Atuação / Elenco
Sessão
Sala
Ingresso
```

A `Sessão` possui papel importante na modelagem por conectar informações necessárias para representar uma exibição e permitir a associação com a venda de ingressos.

Entre os conceitos trabalhados estão:

- identificação de classes;
- relacionamentos;
- multiplicidade;
- dependências;
- interpretação de requisitos;
- regras de negócio.

➡️ [Ver documentação do Diagrama de Classes](./01-diagrama-de-classes/README.md)

---

## 02 — Diagrama de Sequência

📁 [`02-diagrama-de-sequencia`](./02-diagrama-de-sequencia/)

Representa a **interação entre os participantes ao longo do tempo** durante o processo de venda de um ingresso.

O fluxo envolve elementos como:

```text
Funcionário
Interface do Cinema
Controlador
Sessão
Sala
Filme
Ingresso
```

A atividade permite observar como uma operação passa pela interface, é coordenada pelo controlador e utiliza elementos do domínio até chegar à criação do ingresso.

Entre os conceitos trabalhados estão:

- lifelines;
- mensagens síncronas;
- mensagens de retorno;
- barras de ativação;
- fragmento combinado `[LOOP]`;
- criação de objetos;
- separação de responsabilidades.

➡️ [Ver documentação do Diagrama de Sequência](./02-diagrama-de-sequencia/README.md)

---

## 03 — Máquina de Estados

📁 [`03-maquina-de-estados`](./03-maquina-de-estados/)

Representa a **evolução do comportamento do sistema** durante o processo de venda de ingressos.

O fluxo principal pode ser compreendido como:

```text
Início
  │
  ▼
Apresentação de Sessões
  │
  ▼
Geração do Ingresso
  │
  ▼
Emissão de Ingressos
  │
  ▼
Fim
```

A atividade demonstra como ações realizadas durante a operação provocam mudanças no estado do sistema.

Entre os conceitos trabalhados estão:

- estados;
- transições;
- eventos;
- estado inicial;
- estado final;
- ações internas;
- `entry`;
- `do`.

➡️ [Ver documentação da Máquina de Estados](./03-maquina-de-estados/README.md)

---

## Relação entre os diagramas

Os três diagramas não representam exatamente a mesma informação.

Cada um responde a um tipo diferente de pergunta sobre o sistema.

| Diagrama | Perspectiva | Principal questão |
|---|---|---|
| Diagrama de Classes | Estrutural | Quais elementos existem e como se relacionam? |
| Diagrama de Sequência | Interação | Como os participantes colaboram durante uma operação? |
| Máquina de Estados | Comportamental | Como o sistema muda de estado durante o processo? |

Juntos, eles permitem observar diferentes aspectos da modelagem do Sistema de Cinema.

---

## Evolução da modelagem

A organização das atividades também permite visualizar uma progressão conceitual:

```text
REQUISITOS DO DOMÍNIO
        │
        ▼
IDENTIFICAÇÃO DOS ELEMENTOS
        │
        ▼
DIAGRAMA DE CLASSES
        │
        ▼
INTERAÇÃO ENTRE OBJETOS
        │
        ▼
DIAGRAMA DE SEQUÊNCIA
        │
        ▼
ESTADOS E TRANSIÇÕES
        │
        ▼
MÁQUINA DE ESTADOS
```

Primeiro é analisada a estrutura do domínio.

Depois, os elementos identificados são observados durante uma operação.

Por fim, é representada a mudança de comportamento do sistema ao longo desse processo.

---

## Tecnologias e conceitos

**Modelagem**

```text
UML — Unified Modeling Language
```

**Ferramenta**

```text
Visual Paradigm
Visual Paradigm Community Edition
```

**Área**

```text
Análise e Modelagem Orientada a Objetos
```

**Domínio**

```text
Sistema de Cinema
Venda de Ingressos
```

---

## Estrutura do diretório

```text
sistema-cinema/
│
├── README.md
│
├── 01-diagrama-de-classes/
│   └── README.md
│
├── 02-diagrama-de-sequencia/
│   └── README.md
│
└── 03-maquina-de-estados/
    └── README.md
```

Cada diretório contém a documentação correspondente à respectiva atividade acadêmica.

---

## Contexto acadêmico

As atividades foram desenvolvidas durante a graduação em **Análise e Desenvolvimento de Sistemas**, na disciplina de **Análise Orientada a Objetos**.

Os trabalhos foram realizados em momentos distintos da disciplina e exploraram diferentes recursos da UML aplicados ao mesmo domínio.

Para apresentação no GitHub, as atividades foram posteriormente agrupadas em um único estudo de caso, preservando a natureza acadêmica de cada trabalho.

---

## Sobre esta versão

Este diretório tem como objetivo organizar e documentar atividades acadêmicas selecionadas para composição de portfólio.

Os conteúdos foram estruturados para facilitar a navegação e a compreensão dos conceitos trabalhados durante a graduação.

As representações textuais presentes nos arquivos `README.md` foram adicionadas posteriormente como apoio à documentação e não substituem os diagramas UML originalmente desenvolvidos nas atividades.