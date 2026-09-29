# Normalização de Dados — 3FN e 4FN

Atividade acadêmica desenvolvida na disciplina de Modelagem de Dados com foco na aplicação da Terceira Forma Normal (3FN) e da Quarta Forma Normal (4FN).

O trabalho analisa estruturas que apresentam redundância e dependências inadequadas e demonstra como a decomposição em tabelas menores pode melhorar a organização e a integridade dos dados.

## Objetivos

A atividade teve como principais objetivos:

- Identificar dependências funcionais;
- Identificar dependências transitivas;
- Reconhecer problemas de redundância;
- Compreender anomalias de inserção e atualização;
- Aplicar a Terceira Forma Normal (3FN);
- Identificar dependências multivaloradas;
- Aplicar a Quarta Forma Normal (4FN);
- Decompor estruturas problemáticas em tabelas normalizadas.

---

# Atividade 1 — Normalização de PEDIDO

O primeiro caso analisa uma tabela de pedidos contendo, na mesma estrutura, informações do pedido e do cliente.

A estrutura possui dados como:

```text
PEDIDO
├── num_pedido (PK)
├── data
├── CPF_cliente
├── nome_cliente
├── cidade_cliente
└── estado_cliente
```

## Dependências funcionais

Foram identificadas as seguintes dependências:

```text
num_pedido → data, CPF_cliente

CPF_cliente → nome_cliente, cidade_cliente, estado_cliente
```

Isso significa que as informações do cliente não dependem diretamente do número do pedido.

Existe, portanto, uma dependência transitiva:

```text
num_pedido
     ↓
CPF_cliente
     ↓
dados do cliente
```

Um exemplo identificado na atividade foi:

```text
num_pedido → CPF_cliente → cidade_cliente
```

## Problemas identificados

A estrutura pode provocar:

- Redundância dos dados do cliente em diferentes pedidos;
- Anomalia de inserção;
- Anomalia de atualização.

Por exemplo, quando um mesmo cliente realiza diversos pedidos, seus dados precisam ser repetidos em várias linhas.

## Transformação para 3FN

A solução proposta foi separar as informações em duas tabelas.

### PEDIDO

```text
PEDIDO
├── num_pedido (PK)
├── data
└── CPF_cliente (FK)
```

### CLIENTE

```text
CLIENTE
├── CPF_cliente (PK)
├── nome_cliente
├── cidade_cliente
└── estado_cliente
```

O relacionamento passa a ser:

```text
CLIENTE 1 ───────── N PEDIDO
```

Dessa forma, os dados do cliente ficam armazenados apenas em `CLIENTE`, enquanto `PEDIDO` mantém uma referência ao cliente correspondente.

---

# Atividade 2 — Normalização de FUNCIONÁRIO

O segundo caso trabalha com uma tabela contendo informações de funcionários, departamentos e projetos.

A estrutura original analisada possuía:

```text
FUNCIONÁRIO
├── CPF (PK)
├── nome
├── cod_depto
├── nome_depto
├── local_depto
├── salário
└── cod_projeto
```

## Dependências funcionais

Foram identificadas:

```text
CPF → nome, salário, cod_depto, cod_projeto

cod_depto → nome_depto, local_depto
```

Na tabela analisada, `cod_projeto` não possuía outro atributo dependente.

## Dependências transitivas

O problema ocorre porque:

```text
CPF
 ↓
cod_depto
 ↓
nome_depto
local_depto
```

`nome_depto` e `local_depto` dependem de `cod_depto`, e não diretamente da chave primária da tabela de funcionários.

## Transformação para 3FN

A decomposição realizada na atividade resultou em três tabelas.

### FUNCIONÁRIO

```text
FUNCIONÁRIO
├── CPF (PK)
├── nome
├── salário
├── cod_depto (FK)
└── cod_projeto (FK)
```

### DEPARTAMENTO

```text
DEPARTAMENTO
├── cod_depto (PK)
├── nome_depto
└── local_depto
```

### PROJETO

```text
PROJETO
└── cod_projeto (PK)
```

Com essa decomposição, os dados referentes aos departamentos deixam de ser repetidos para cada funcionário.

A tabela `PROJETO` também passa a representar os códigos de projeto como uma estrutura independente.

De forma simplificada:

```text
DEPARTAMENTO
      │
      │ 1:N
      ▼
 FUNCIONÁRIO
      │
      │ N:1
      ▼
   PROJETO
```

---

# Atividade 3 — Identificação de violação da 4FN

A terceira atividade analisa uma tabela de professores contendo disciplinas e telefones.

A estrutura utilizada foi:

```text
PROFESSOR
├── CRM
├── disciplina
└── telefone
```

No exemplo analisado, um professor poderia possuir simultaneamente:

```text
Disciplinas:
- Matemática
- Física

Telefones:
- 1111-1111
- 2222-2222
```

As disciplinas e os telefones são informações independentes entre si.

Entretanto, quando armazenados na mesma tabela, surge uma combinação entre todos os valores:

```text
Matemática + 1111-1111
Matemática + 2222-2222
Física      + 1111-1111
Física      + 2222-2222
```

São necessárias quatro linhas para representar duas disciplinas e dois telefones.

## Problema

Essa estrutura provoca uma combinação cartesiana desnecessária.

Além da redundância, surgem problemas como:

- Adicionar um telefone exige repeti-lo para todas as disciplinas;
- Adicionar uma disciplina exige repeti-la para todos os telefones.

Na análise realizada, a tabela atende à 3FN, mas não à 4FN.

## Transformação para 4FN

A solução foi separar as duas informações independentes.

### PROF_DISCIPLINA

```text
PROF_DISCIPLINA
├── CRM (PK composta)
└── disciplina (PK composta)
```

Chave primária:

```text
(CRM, disciplina)
```

### PROF_TELEFONE

```text
PROF_TELEFONE
├── CRM (PK composta)
└── telefone (PK composta)
```

Chave primária:

```text
(CRM, telefone)
```

Assim, disciplinas e telefones deixam de formar combinações desnecessárias.

---

# 3FN e 4FN

## Terceira Forma Normal — 3FN

Nos exemplos estudados, a 3FN está relacionada à eliminação de dependências transitivas.

Em termos práticos, buscamos evitar estruturas como:

```text
CHAVE PRIMÁRIA
      ↓
   atributo A
      ↓
   atributo B
```

quando `atributo B` deveria pertencer a outra entidade.

Foi o que ocorreu, por exemplo, com:

```text
num_pedido → CPF_cliente → dados do cliente
```

e:

```text
CPF → cod_depto → dados do departamento
```

## Quarta Forma Normal — 4FN

A 4FN aparece no trabalho quando uma mesma entidade possui conjuntos de informações independentes que geram combinações desnecessárias.

No exemplo:

```text
PROFESSOR
├── várias disciplinas
└── vários telefones
```

as disciplinas não dependem dos telefones e os telefones não dependem das disciplinas.

Separar essas informações elimina as combinações redundantes.

---

# Comparação das transformações

```text
PEDIDO + dados do cliente
          │
          ▼
     PEDIDO + CLIENTE
             3FN


FUNCIONÁRIO + dados do departamento + projeto
                    │
                    ▼
      FUNCIONÁRIO + DEPARTAMENTO + PROJETO
                    3FN


PROFESSOR + disciplina + telefone
                    │
                    ▼
       PROF_DISCIPLINA + PROF_TELEFONE
                    4FN
```

---

# Aprendizados

A atividade demonstrou que normalizar um banco de dados não consiste apenas em dividir tabelas.

É necessário compreender as dependências existentes entre os atributos e identificar quais informações realmente pertencem a cada entidade.

A aplicação da 3FN permitiu separar informações de clientes e pedidos, assim como funcionários e departamentos.

A análise da 4FN demonstrou que mesmo uma estrutura que atende à 3FN pode apresentar redundância quando possui informações multivaloradas independentes.

Esses conceitos contribuem para bancos de dados mais organizados e ajudam a reduzir inconsistências durante operações de inserção e atualização.

---

## Organização para o repositório

Esta documentação foi reorganizada a partir da atividade acadêmica original para facilitar sua apresentação e consulta no GitHub.

Os exemplos, dependências e decomposições apresentados correspondem aos exercícios desenvolvidos no relatório acadêmico.

A organização em Markdown foi realizada posteriormente para apresentação no repositório e não representa um novo trabalho acadêmico.

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas, na disciplina de Modelagem de Dados.

**Unidade:** Normalização de Dados  
**Seção:** Formas Normais II  
**Conteúdo principal:** Terceira Forma Normal (3FN) e Quarta Forma Normal (4FN)