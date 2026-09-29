# Modelagem de Sistema Universitário — DER

Atividade acadêmica desenvolvida com o objetivo de aplicar conceitos de Modelagem de Dados na construção de um Diagrama Entidade-Relacionamento (DER) para um sistema de gestão universitária.

O modelo trabalha com estudantes, cursos, disciplinas e professores, incluindo relacionamentos de diferentes cardinalidades e uma entidade associativa para representar o histórico acadêmico dos alunos.

A atividade também propõe uma expansão do modelo para contemplar pré-requisitos entre disciplinas, departamentos e bolsas.

## Objetivo

Os principais conceitos trabalhados foram:

- Identificação de entidades e atributos;
- Definição de chaves primárias;
- Relacionamentos `1:N` e `N:M`;
- Utilização de entidade associativa;
- Definição de regras e restrições de integridade;
- Autorrelacionamento;
- Expansão de um modelo de dados a partir de novos requisitos.

---

# Modelo inicial

O modelo acadêmico utiliza quatro entidades principais:

```text
ALUNO
CURSO
DISCIPLINA
PROFESSOR
```

Além delas, o relacionamento entre alunos e disciplinas exige uma entidade associativa:

```text
HISTÓRICO_MATRÍCULA
```

## ALUNO

Representa os estudantes da instituição.

Atributos documentados na atividade:

```text
ALUNO
├── RA (PK)
├── Nome
├── CPF
└── Data de Nascimento
```

O `RA` (Registro Acadêmico) foi escolhido como identificador do aluno.

## CURSO

Representa os cursos oferecidos pela instituição.

Atributos documentados:

```text
CURSO
├── Código do Curso
├── Nome do Curso
└── Carga Horária Total
```

O relatório acadêmico original apresenta esses atributos e registra, na seção de identificação das entidades, os três itens como chave primária.

Essa definição é preservada aqui como parte do registro da atividade original. Em uma implementação relacional posterior, a definição da chave pode ser refinada de acordo com as regras do modelo.

## DISCIPLINA

Representa as disciplinas pertencentes à estrutura acadêmica.

```text
DISCIPLINA
├── Código da Disciplina (PK)
├── Nome
├── Carga Horária
└── Período
```

O código da disciplina é utilizado como identificador.

## PROFESSOR

Representa os professores da instituição.

```text
PROFESSOR
├── Matrícula (PK)
├── Nome
└── Titulação
```

A matrícula foi definida como identificador do professor.

---

# Relacionamentos

O modelo estabelece os seguintes relacionamentos:

| Entidade | Relacionamento | Entidade | Cardinalidade |
|---|---|---|---|
| ALUNO | está matriculado em | CURSO | N:1 |
| CURSO | possui | DISCIPLINA | 1:N |
| ALUNO | cursa | DISCIPLINA | N:M |
| PROFESSOR | leciona | DISCIPLINA | 1:N |

De forma simplificada:

```text
ALUNO ───── N:1 ───── CURSO
                       │
                       │ 1:N
                       ▼
                   DISCIPLINA
                       ▲
                       │
                  PROFESSOR
                      1:N
```

O relacionamento entre `ALUNO` e `DISCIPLINA` exige tratamento adicional porque possui cardinalidade `N:M`.

---

# Entidade associativa

Um aluno pode cursar diversas disciplinas e uma disciplina pode possuir diversos alunos.

Portanto:

```text
ALUNO N:M DISCIPLINA
```

Para representar esse relacionamento, foi criada a entidade:

```text
HISTÓRICO_MATRÍCULA
```

A atividade define os seguintes atributos para essa entidade:

```text
HISTÓRICO_MATRÍCULA
├── Nota Final
├── Frequência
└── Ano/Semestre
```

Conceitualmente, ela funciona como intermediária entre aluno e disciplina:

```text
ALUNO
   │
   │ 1:N
   ▼
HISTÓRICO_MATRÍCULA
   ▲
   │ N:1
   │
DISCIPLINA
```

Além de resolver o relacionamento muitos-para-muitos, essa entidade permite armazenar informações que pertencem especificamente à participação de determinado aluno em determinada disciplina.

---

# Decisões de modelagem

A atividade também documentou o propósito das principais entidades.

### ALUNO

Gerenciar o registro e o desempenho acadêmico dos estudantes.

### CURSO

Organizar a estrutura de formação oferecida pela instituição.

### DISCIPLINA

Controlar as matérias lecionadas e seus respectivos requisitos.

### PROFESSOR

Administrar informações do corpo docente e suas atribuições de ensino.

---

# Escolha de identificadores

## ALUNO

Chave escolhida:

```text
RA
```

O relatório justifica a escolha por se tratar de um código interno capaz de identificar individualmente cada estudante.

## PROFESSOR

Chave escolhida:

```text
Matrícula
```

A matrícula funciona como identificador do professor dentro da instituição.

---

# Regras e restrições

A atividade também estabelece algumas regras para o sistema.

Entre as suposições documentadas estão:

- Um aluno pode possuir apenas uma matrícula ativa por vez em cada curso;
- Uma disciplina somente pode ser ofertada quando existir professor vinculado;
- O sistema de notas é numérico e fechado por semestre.

Entre as restrições de integridade:

- Uma disciplina com alunos matriculados não deve ser excluída;
- A nota final deve estar entre `0` e `10`;
- Chaves estrangeiras não devem ser nulas em relacionamentos obrigatórios.

Essas regras são importantes porque mostram que a modelagem não representa apenas tabelas e atributos, mas também regras existentes no domínio da aplicação.

---

# Expansão do modelo

Após a construção inicial, a atividade propõe novos requisitos.

## Pré-requisitos entre disciplinas

Uma disciplina pode exigir outra disciplina como pré-requisito.

A solução adotada na atividade foi um:

```text
autorrelacionamento em DISCIPLINA
```

Conceitualmente:

```text
DISCIPLINA
    │
    └──── possui pré-requisito ────► DISCIPLINA
```

Isso permite representar relações entre registros pertencentes à própria entidade.

---

# Departamentos

A expansão adiciona a entidade:

```text
DEPARTAMENTO
```

com os atributos:

```text
DEPARTAMENTO
├── Código_Departamento (PK)
├── Nome_Departamento
└── Sigla
```

A relação documentada com `PROFESSOR` é:

```text
DEPARTAMENTO 1:N PROFESSOR
```

Um departamento pode possuir diversos professores, enquanto cada professor pertence a um departamento principal.

---

# Bolsas

Também foi proposta a entidade:

```text
BOLSA
```

com os atributos:

```text
BOLSA
├── ID_Bolsa
├── Tipo
└── Valor
```

A entidade é relacionada a `ALUNO`, permitindo representar informações sobre bolsas vinculadas aos estudantes.

---

# Visão conceitual expandida

De maneira simplificada, a expansão do modelo passa a envolver:

```text
                 DEPARTAMENTO
                       │
                      1:N
                       │
                       ▼
                  PROFESSOR
                       │
                      1:N
                       │
                       ▼
ALUNO ──► HISTÓRICO_MATRÍCULA ◄── DISCIPLINA
  │                                  │
  │                                  └──► pré-requisito
  │                                        DISCIPLINA
  │
  └──► BOLSA

ALUNO ── N:1 ──► CURSO ── 1:N ──► DISCIPLINA
```

Esse desenho textual tem finalidade apenas documental e não substitui o DER gráfico produzido durante a atividade acadêmica.

---

# Aprendizados

Esta atividade permitiu avançar além da identificação básica de entidades e atributos.

Foram trabalhados conceitos como:

- Relacionamentos de diferentes cardinalidades;
- Resolução de relacionamento `N:M`;
- Entidades associativas;
- Regras de integridade;
- Autorrelacionamentos;
- Expansão de modelos;
- Representação de requisitos de negócio através da estrutura dos dados.

O uso de `HISTÓRICO_MATRÍCULA` demonstra como um relacionamento muitos-para-muitos pode ser transformado em uma estrutura capaz de armazenar informações próprias da relação, como nota, frequência e período acadêmico.

---

# Evolução para o portfólio

O modelo conceitual desenvolvido nesta atividade servirá como base para uma implementação relacional em SQL adicionada posteriormente a este projeto.

Essa implementação será apresentada como uma evolução para o portfólio e não como parte do trabalho acadêmico original.

A evolução permitirá aplicar conceitos como:

```text
CREATE TABLE
PRIMARY KEY
FOREIGN KEY
NOT NULL
CHECK
UNIQUE
```

e transformar as regras conceituais do DER em restrições implementadas diretamente no banco de dados.

---

## Contexto acadêmico

Este projeto teve origem em uma atividade da disciplina de Modelagem de Dados durante a graduação em Análise e Desenvolvimento de Sistemas.

O trabalho original teve como foco a construção e expansão de um Diagrama Entidade-Relacionamento para um sistema universitário.