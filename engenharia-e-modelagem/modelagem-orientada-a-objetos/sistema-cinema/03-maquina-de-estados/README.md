# Diagrama de Máquina de Estados — Sistema de Cinema

Atividade acadêmica desenvolvida na disciplina de Análise Orientada a Objetos com o objetivo de representar, utilizando UML, os diferentes estados assumidos pelo sistema durante o processo de venda de ingressos de um cinema.

Enquanto o Diagrama de Classes representa a estrutura do sistema e o Diagrama de Sequência demonstra a interação entre os objetos, o Diagrama de Máquina de Estados permite visualizar como o sistema muda de estado em resposta às ações realizadas durante a operação.

## Objetivo

Os principais objetivos da atividade foram:

- Interpretar o fluxo de venda de ingressos;
- Identificar os estados relevantes do sistema;
- Representar as transições entre esses estados;
- Relacionar as transições às ações realizadas pelo funcionário;
- Representar o início e o encerramento do fluxo;
- Utilizar ações internas nos estados;
- Aplicar a notação UML de Máquina de Estados.

---

# Ferramenta utilizada

O diagrama foi desenvolvido utilizando:

```text
Visual Paradigm Community Edition
```

A ferramenta foi utilizada para representar graficamente os estados, transições, ações internas e os pontos inicial e final do fluxo.

---

# Cenário modelado

O cenário representa o comportamento do sistema durante o atendimento de um cliente no processo de venda de um ingresso.

O funcionário inicia a operação e o sistema passa por diferentes estados até que o ingresso seja emitido.

De maneira simplificada:

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

Essa representação textual serve apenas como apoio à documentação e não substitui o Diagrama de Máquina de Estados desenvolvido originalmente.

---

# Início da venda

O fluxo começa quando o funcionário inicia uma operação de venda.

A partir dessa ação, o sistema entra no primeiro estado principal:

```text
Apresentação de Sessões
```

---

# Estado — Apresentação de Sessões

Nesse estado, o sistema trabalha com as informações necessárias para apresentar ao funcionário as sessões disponíveis.

O processo descrito na atividade envolve:

```text
Consultar filmes disponíveis
Verificar salas
Filtrar sessões que não foram encerradas
Exibir sessões disponíveis
```

O objetivo é fornecer ao funcionário uma lista atualizada das opções que podem ser utilizadas na venda.

De forma conceitual:

```text
Apresentação de Sessões
        │
        ├── consultar informações
        ├── verificar disponibilidade
        └── exibir opções
```

O sistema permanece nesse contexto até que o funcionário escolha uma sessão.

---

# Transição — Seleção da sessão

Após analisar as opções apresentadas, o funcionário seleciona a sessão desejada pelo cliente.

Essa ação provoca a mudança para o próximo estado:

```text
Apresentação de Sessões
          │
          │ seleção da sessão
          ▼
Geração do Ingresso
```

---

# Estado — Geração do Ingresso

Após a seleção da sessão, o sistema entra no estado:

```text
Geração do Ingresso
```

Esse estado representa uma etapa de preparação da operação.

O sistema disponibiliza as opções necessárias para que o funcionário possa confirmar a venda.

O fluxo permanece nessa etapa até que ocorra a ação de confirmação.

---

# Transição — Confirmação

Quando o funcionário confirma a operação, o sistema realiza uma nova transição:

```text
Geração do Ingresso
        │
        │ confirmação
        ▼
Emissão de Ingressos
```

A confirmação permite que o fluxo avance para sua etapa final.

---

# Estado — Emissão de Ingressos

No último estado principal:

```text
Emissão de Ingressos
```

o ingresso é efetivamente gerado pelo sistema.

O relatório também considera que o bilhete pode ser:

```text
Impresso
ou
Enviado digitalmente
```

Após essa etapa, o processo de venda é encerrado.

---

# Estado final

Com a conclusão da emissão, o fluxo chega ao seu estado final.

Assim, a sequência principal pode ser compreendida como:

```text
●
│
▼
┌──────────────────────────┐
│ Apresentação de Sessões  │
└──────────────────────────┘
             │
             │ selecionar sessão
             ▼
┌──────────────────────────┐
│  Geração do Ingresso     │
└──────────────────────────┘
             │
             │ confirmar
             ▼
┌──────────────────────────┐
│  Emissão de Ingressos    │
└──────────────────────────┘
             │
             ▼
             ◎
```

A representação acima é apenas uma versão textual simplificada do comportamento documentado.

---

# Ações internas

Além dos estados e das transições, a atividade utilizou ações internas para detalhar comportamentos executados dentro de determinados estados.

Foram utilizados termos como:

```text
entry
do
```

Esses elementos permitem representar ações associadas ao comportamento interno de um estado.

## `entry`

Representa uma ação executada quando o sistema entra em determinado estado.

## `do`

Representa uma atividade realizada enquanto o sistema permanece naquele estado.

A utilização dessas ações permite detalhar melhor o comportamento do sistema sem transformar cada operação interna em um novo estado.

---

# Estados e transições

Um dos conceitos centrais da atividade é a diferença entre estado e transição.

## Estado

Representa uma situação em que o sistema se encontra em determinado momento.

Exemplos utilizados:

```text
Apresentação de Sessões
Geração do Ingresso
Emissão de Ingressos
```

## Transição

Representa a passagem de um estado para outro em resposta a determinada ação ou evento.

No cenário modelado:

```text
Selecionar sessão
        │
        ▼
mudança de estado

Confirmar operação
        │
        ▼
mudança de estado
```

---

# Relação com as outras perspectivas UML

A Máquina de Estados complementa as outras atividades desenvolvidas para o Sistema de Cinema.

## Diagrama de Classes

Responde principalmente:

```text
Quais elementos existem no sistema?
```

Representa sua estrutura.

## Diagrama de Sequência

Responde principalmente:

```text
Como os participantes interagem durante a venda?
```

Representa a ordem temporal das mensagens.

## Máquina de Estados

Responde principalmente:

```text
Em qual estado o sistema se encontra e como ele muda?
```

Representa a evolução do comportamento ao longo da operação.

Assim:

```text
DIAGRAMA DE CLASSES
        │
        │ estrutura
        ▼
DIAGRAMA DE SEQUÊNCIA
        │
        │ interação
        ▼
MÁQUINA DE ESTADOS
        │
        │ comportamento
        ▼
VISÕES COMPLEMENTARES DO SISTEMA
```

---

# Aprendizados

A atividade permitiu compreender que um sistema pode apresentar comportamentos diferentes dependendo do estado em que se encontra.

No processo de venda de ingressos, determinadas ações só fazem sentido depois que etapas anteriores foram concluídas.

Por exemplo:

```text
Primeiro:
apresentar as sessões

Depois:
selecionar uma sessão

Depois:
preparar e confirmar a venda

Por fim:
emitir o ingresso
```

A Máquina de Estados permite representar essa ordem de maneira visual e ajuda a compreender como ações do usuário provocam mudanças no comportamento do sistema.

O exercício também permitiu trabalhar conceitos como:

- estados;
- transições;
- eventos;
- estado inicial;
- estado final;
- ações internas;
- `entry`;
- `do`.

---

## Relação com o Sistema de Cinema

Esta atividade representa a terceira perspectiva UML organizada no estudo do Sistema de Cinema:

```text
01 — Diagrama de Classes
        │
        ▼
estrutura do sistema

02 — Diagrama de Sequência
        │
        ▼
interação entre os participantes

03 — Máquina de Estados
        │
        ▼
evolução do comportamento durante a venda
```

As três atividades foram desenvolvidas academicamente em etapas distintas e foram agrupadas posteriormente no repositório por utilizarem o mesmo domínio e apresentarem perspectivas complementares da modelagem UML.

---

## Organização para o repositório

Esta documentação foi reorganizada a partir da atividade acadêmica original para facilitar sua apresentação e consulta no GitHub.

Os estados, o fluxo e os conceitos apresentados neste `README` correspondem ao processo descrito no relatório acadêmico.

As representações textuais foram adicionadas posteriormente apenas como apoio à documentação e não substituem o Diagrama de Máquina de Estados desenvolvido originalmente.

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Análise Orientada a Objetos  
**Unidade:** Modelagem de caso com UML  
**Aula:** Modelagem complementar  
**Domínio:** Sistema de Cinema  
**Processo:** Venda de ingressos  
**Modelagem:** Diagrama de Máquina de Estados UML  
**Ferramenta utilizada:** Visual Paradigm Community Edition