# Diagrama de Sequência — Venda de Ingressos

Atividade acadêmica desenvolvida na disciplina de Análise Orientada a Objetos com o objetivo de representar, utilizando UML, a sequência de interações envolvidas no processo de venda de ingressos de um sistema de cinema.

Enquanto o Diagrama de Classes apresenta a estrutura estática do sistema, o Diagrama de Sequência permite observar como os participantes e objetos colaboram ao longo do tempo para executar uma operação.

Neste caso, o processo analisado é a venda e emissão de um ingresso.

## Objetivo

Os principais objetivos da atividade foram:

- Representar dinamicamente o processo de venda de ingressos;
- Identificar os participantes envolvidos na operação;
- Organizar as interações em ordem temporal;
- Representar chamadas e retornos entre os objetos;
- Utilizar lifelines e barras de ativação;
- Aplicar um fragmento combinado de repetição;
- Representar a criação do objeto `Ingresso`;
- Relacionar o comportamento do sistema à estrutura definida anteriormente no Diagrama de Classes.

---

# Ferramenta utilizada

O diagrama foi desenvolvido utilizando:

```text
Visual Paradigm
```

A ferramenta foi utilizada para representar as lifelines, mensagens, ativações, fragmentos combinados e demais elementos do Diagrama de Sequência UML.

---

# Cenário modelado

O cenário representa o atendimento realizado por um funcionário durante a venda de um ingresso.

O fluxo começa quando o funcionário inicia uma venda na interface do sistema.

De forma geral:

```text
Funcionário
     │
     ▼
Interface do Cinema
     │
     ▼
Controlador
     │
     ├── Sessão
     ├── Sala
     └── Filme
     │
     ▼
Seleção da sessão
     │
     ▼
Confirmação
     │
     ▼
Criação do Ingresso
```

Essa representação textual serve apenas como apoio à documentação e não substitui o Diagrama de Sequência UML original.

---

# Participantes da interação

O fluxo documentado envolve elementos como:

```text
Funcionário
Interface do Cinema
Controlador
Sessão
Sala
Filme
Ingresso
```

Cada participante possui uma função diferente durante a execução da operação.

---

# Funcionário

O funcionário representa o ator que inicia e conduz a operação de venda.

A interação começa quando ele solicita a abertura do processo de venda por meio da interface do sistema.

---

# Interface do Cinema

A Interface do Cinema representa o ponto de interação entre o funcionário e o sistema.

Ela recebe a solicitação inicial e encaminha a operação para o componente responsável pela lógica do processo.

Em vez de acessar diretamente as entidades do sistema, a interface utiliza o Controlador.

---

# Controlador

O Controlador coordena as operações necessárias para realizar a venda.

Durante o fluxo, ele gerencia solicitações relacionadas às entidades:

```text
Sessão
Sala
Filme
```

A utilização do Controlador permite separar a interface da lógica necessária para consultar e organizar os dados do sistema.

---

# Consulta das sessões

Após o início da venda, o sistema precisa recuperar as sessões disponíveis.

O Controlador coordena as consultas necessárias para obter informações que serão apresentadas ao funcionário.

Entre as informações envolvidas estão dados relacionados a:

```text
Sessões
Filmes
Salas
```

Esses dados permitem montar a lista de opções disponíveis para a venda.

---

# Fragmento combinado LOOP

Durante a recuperação das informações das sessões, foi utilizado um fragmento combinado:

```text
[LOOP]
```

O `LOOP` representa uma repetição dentro do Diagrama de Sequência.

Na atividade, ele foi utilizado para representar a iteração necessária durante a coleta de informações de múltiplas sessões.

Conceitualmente:

```text
┌──────────────────────── LOOP ────────────────────────┐
│                                                     │
│  Consultar sessão                                   │
│        │                                            │
│        ├── obter informações do filme               │
│        └── obter informações da sala                │
│                                                     │
└─────────────────────────────────────────────────────┘
```

Essa representação textual é apenas explicativa.

---

# Apresentação das opções

Após a recuperação das informações necessárias, os dados retornam para que a interface possa apresentar as sessões disponíveis ao funcionário.

Informações como:

```text
Título do filme
Número da sala
```

ajudam a compor a lista de escolha apresentada durante o atendimento.

---

# Seleção da sessão

O funcionário analisa as opções disponíveis e seleciona a sessão desejada.

A sessão escolhida passa a ser utilizada nas etapas seguintes da venda.

O fluxo garante que a emissão do ingresso esteja associada a uma sessão válida.

---

# Confirmação da operação

Após a escolha da sessão, o fluxo prossegue para a confirmação da venda.

Somente depois da validação da sessão e da confirmação da operação ocorre a criação do ingresso.

---

# Criação do objeto Ingresso

Um dos pontos importantes do diagrama é a representação explícita da criação de:

```text
Ingresso
```

Foi utilizada a notação de criação de objeto para indicar o momento em que o ingresso passa a existir no fluxo.

De forma conceitual:

```text
Sessão selecionada
        │
        ▼
     Validação
        │
        ▼
   Confirmação
        │
        ▼
  <<create>>
     Ingresso
```

Assim, a criação do ingresso ocorre somente depois das etapas necessárias da venda.

---

# Elementos UML trabalhados

## Lifelines

As lifelines representam os participantes existentes durante a interação.

Elas permitem visualizar a existência de cada participante ao longo do tempo.

## Mensagens síncronas

Foram utilizadas mensagens síncronas para representar chamadas realizadas entre os participantes.

Nesse tipo de interação, uma operação é solicitada e o fluxo aguarda sua execução antes de prosseguir.

## Mensagens de retorno

As mensagens de retorno representam os dados devolvidos após determinadas solicitações.

No cenário da atividade, retornos são importantes para fornecer à interface as informações necessárias sobre as sessões disponíveis.

## Barras de ativação

As barras de ativação representam períodos em que determinado participante está executando uma operação.

Elas ajudam a visualizar quando cada objeto participa ativamente do fluxo.

## Fragmentos combinados

O fragmento combinado `[LOOP]` foi utilizado para representar uma operação repetitiva durante a recuperação das informações de múltiplas sessões.

## Criação de objetos

A criação do objeto `Ingresso` foi representada explicitamente para demonstrar o momento em que o registro é gerado durante a venda.

---

# Separação de responsabilidades

Um aspecto observado durante a atividade é a utilização do Controlador entre a interface e as entidades do sistema.

De maneira simplificada:

```text
Funcionário
     │
     ▼
Interface
     │
     ▼
Controlador
     │
     ├────► Sessão
     ├────► Sala
     └────► Filme
```

A interface não precisa interagir diretamente com todas as entidades.

O Controlador coordena essas operações e devolve as informações necessárias para a interface.

---

# Relação com o Diagrama de Classes

O Diagrama de Classes representa os elementos existentes no sistema e seus relacionamentos.

O Diagrama de Sequência utiliza esses elementos para mostrar como eles colaboram durante uma operação.

Assim:

```text
DIAGRAMA DE CLASSES
        │
        │ estrutura
        ▼
Classes e relacionamentos
        │
        │ utilizados durante a operação
        ▼
DIAGRAMA DE SEQUÊNCIA
        │
        │ comportamento temporal
        ▼
Venda e criação do ingresso
```

A atividade demonstra como diferentes diagramas UML podem representar perspectivas complementares do mesmo sistema.

---

# Aprendizados

A atividade permitiu compreender que conhecer apenas a estrutura das classes não é suficiente para representar completamente o comportamento de um sistema.

O Diagrama de Sequência acrescenta a dimensão temporal, permitindo visualizar:

- quem inicia uma operação;
- quais objetos participam;
- em qual ordem as mensagens são enviadas;
- quais dados retornam;
- quando existe repetição;
- quando determinado objeto é criado.

O exercício também mostrou a importância da separação de responsabilidades entre interface, controle e entidades durante uma operação do sistema.

---

## Relação com o Sistema de Cinema

Esta é a segunda perspectiva UML organizada no estudo do Sistema de Cinema:

```text
01 — Diagrama de Classes
        │
        │ define a estrutura
        ▼
02 — Diagrama de Sequência
        │
        │ demonstra as interações
        ▼
03 — Máquina de Estados
        │
        │ demonstra a evolução dos estados
        ▼
Processo de venda de ingressos
```

Os três trabalhos foram desenvolvidos como atividades acadêmicas relacionadas ao mesmo domínio e foram agrupados posteriormente no repositório para facilitar a compreensão da evolução da modelagem.

---

## Organização para o repositório

Esta documentação foi reorganizada a partir da atividade acadêmica original para facilitar sua apresentação e consulta no GitHub.

Os participantes, interações e conceitos apresentados correspondem ao fluxo documentado no relatório da atividade.

As representações textuais presentes neste `README` foram adicionadas posteriormente apenas como apoio à documentação e não substituem o Diagrama de Sequência UML desenvolvido originalmente.

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Análise Orientada a Objetos  
**Unidade:** Modelagem Complementar de Análise com UML  
**Aula:** Diagrama de Sequências  
**Domínio:** Sistema de Cinema  
**Processo modelado:** Venda de ingressos  
**Modelagem:** UML  
**Ferramenta utilizada:** Visual Paradigm