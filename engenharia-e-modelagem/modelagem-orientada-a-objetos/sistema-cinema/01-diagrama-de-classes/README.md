# Diagrama de Classes — Sistema de Cinema

Atividade acadêmica desenvolvida na disciplina de Análise Orientada a Objetos com o objetivo de modelar, utilizando UML, a estrutura de um sistema de cinema.

O trabalho parte de um cenário textual e transforma seus requisitos e regras de negócio em uma representação orientada a objetos, identificando as principais classes e os relacionamentos necessários para representar filmes, sessões, salas, ingressos e informações relacionadas ao elenco.

## Objetivo

Os principais objetivos da atividade foram:

- Interpretar os requisitos apresentados no cenário;
- Identificar as principais classes do sistema;
- Representar os relacionamentos entre os objetos;
- Trabalhar conceitos de multiplicidade e dependência;
- Aplicar a notação UML;
- Representar regras de negócio do sistema de cinema;
- Criar uma estrutura que pudesse servir como base para um futuro software.

---

# Ferramenta utilizada

O diagrama foi desenvolvido utilizando:

```text
Visual Paradigm
```

A ferramenta foi utilizada para representar graficamente as classes e seus relacionamentos utilizando a notação UML.

---

# Processo de modelagem

O desenvolvimento da atividade foi realizado a partir da análise dos requisitos do cenário proposto.

O processo envolveu:

1. Leitura e interpretação dos requisitos;
2. Separação entre dados e regras de negócio;
3. Identificação das principais classes;
4. Mapeamento dos objetos do domínio;
5. Representação dos relacionamentos utilizando UML;
6. Verificação das regras apresentadas no cenário.

Um dos pontos observados durante a análise foi a diferença entre informações propriamente ditas e regras do sistema.

Como exemplo:

```text
Dado:
nome do filme

Dado:
capacidade da sala

Regra:
um filme possui um gênero
```

---

# Estrutura do sistema

A modelagem trabalha elementos relacionados a:

```text
Gênero
Filme
Atuação
Elenco
Sessão
Sala
Ingresso
```

Esses elementos representam diferentes aspectos do funcionamento do cinema e se relacionam para formar a estrutura do sistema.

---

# Sessão como elemento central

Durante a elaboração do modelo, a `Sessão` foi considerada um dos elementos centrais da estrutura.

Ela conecta informações necessárias para que uma exibição possa acontecer.

De forma conceitual:

```text
Filme
  │
  ▼
Sessão
  ▲
  │
Sala
```

Sem uma sessão definida, não existe uma exibição específica disponível para a venda de ingressos.

Essa estrutura permite relacionar o conteúdo exibido com o local e o momento em que a exibição acontece.

---

# Filme e Gênero

O modelo também representa a classificação dos filmes por gênero.

Uma das regras consideradas na atividade é:

```text
um filme possui um gênero
```

O gênero permite organizar os filmes de acordo com sua classificação dentro do domínio modelado.

De maneira simplificada:

```text
Gênero
   │
   ▼
 Filme
```

---

# Filme e elenco

Além das informações básicas dos filmes, o cenário exige representar os profissionais envolvidos e os papéis interpretados.

Para isso, a modelagem utiliza o conceito de:

```text
Atuação
```

A estrutura permite associar a participação de um profissional ao filme correspondente e registrar o papel desempenhado naquela produção.

Isso evita misturar informações de participações realizadas em filmes diferentes.

---

# Sala

A sala representa o espaço físico em que determinada sessão acontece.

Uma informação relevante considerada no modelo é:

```text
capacidade da sala
```

Essa informação está relacionada às regras de ocupação e venda de ingressos.

---

# Ingresso

O ingresso representa o resultado da venda vinculada a uma sessão.

Uma regra importante apresentada na atividade é:

```text
o ingresso só existe se houver uma sessão vinculada
```

Assim, o ingresso não é tratado como um elemento isolado.

De forma simplificada:

```text
Filme
   │
   ▼
Sessão ◄── Sala
   │
   ▼
Ingresso
```

---

# Regras consideradas na modelagem

Entre as regras analisadas durante a atividade estão:

```text
Um filme possui um gênero.

Uma sessão depende da existência de um filme e de uma sala.

Um ingresso deve estar vinculado a uma sessão.

A capacidade da sala precisa ser considerada na venda de ingressos.

A participação do elenco deve estar associada ao filme correspondente.

O tipo do ingresso pode diferenciar meia e inteira.
```

Essas regras ajudam a garantir coerência entre os objetos representados no modelo.

---

# Visão conceitual

De maneira resumida, parte da estrutura trabalhada pode ser compreendida como:

```text
GÊNERO
   │
   ▼
 FILME ───────── ATUAÇÃO / ELENCO
   │
   ▼
 SESSÃO ◄──────── SALA
   │
   ▼
INGRESSO
```

Essa representação textual serve apenas como apoio para a documentação.

Ela não substitui o Diagrama de Classes UML desenvolvido na atividade original.

---

# Conceitos trabalhados

## Classes

As classes representam elementos relevantes do domínio que possuem responsabilidades e informações próprias.

No cenário do cinema, diferentes conceitos do mundo real foram transformados em elementos do modelo.

## Relacionamentos

Os relacionamentos representam como os objetos se conectam dentro do sistema.

Por exemplo, uma sessão precisa estar relacionada às informações necessárias para representar uma exibição.

## Multiplicidade

A atividade também trabalhou o conceito de multiplicidade, utilizado para indicar quantas instâncias podem participar de determinado relacionamento.

## Regras de negócio

As regras de negócio estabelecem condições que precisam ser respeitadas pelo sistema.

Elas ajudam a evitar que a modelagem represente situações incompatíveis com o funcionamento esperado do domínio.

---

# Aprendizados

A atividade demonstrou a importância da modelagem antes da implementação de um software.

Ao transformar requisitos textuais em classes e relacionamentos, torna-se possível visualizar melhor como as informações do sistema estão organizadas e quais dependências precisam ser respeitadas.

O exercício também permitiu trabalhar conceitos importantes da orientação a objetos e da UML, principalmente:

- identificação de classes;
- relacionamentos;
- multiplicidade;
- dependência entre objetos;
- interpretação de requisitos;
- representação de regras de negócio.

A modelagem resultante serve como base conceitual para compreender como um sistema de cinema poderia ser estruturado antes da etapa de programação.

---

## Relação com as demais atividades

Esta atividade representa a **visão estrutural** do Sistema de Cinema.

Outras atividades acadêmicas posteriores utilizaram o mesmo domínio para explorar diferentes perspectivas da UML:

```text
Diagrama de Classes
        │
        │ estrutura do sistema
        ▼
Diagrama de Sequência
        │
        │ interação entre os objetos
        ▼
Máquina de Estados
        │
        │ comportamento durante a venda
        ▼
Fluxo completo de emissão do ingresso
```

Essas atividades estão organizadas conjuntamente no repositório para demonstrar diferentes perspectivas da modelagem do mesmo domínio.

---

## Organização para o repositório

Esta documentação foi reorganizada a partir da atividade acadêmica original para facilitar sua apresentação e consulta no GitHub.

As classes, conceitos e regras descritos neste `README` foram documentados a partir do cenário e dos resultados apresentados no relatório acadêmico.

As representações textuais foram adicionadas posteriormente apenas como apoio à documentação e não substituem o Diagrama de Classes UML desenvolvido originalmente.

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Análise Orientada a Objetos  
**Unidade:** Modelagem Essencial de Análise com UML  
**Aula:** Diagrama de Classes  
**Domínio:** Sistema de Cinema  
**Modelagem:** UML  
**Ferramenta utilizada:** Visual Paradigm