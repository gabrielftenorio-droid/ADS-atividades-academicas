# Diagrama de Casos de Uso — Sistema Bancário

Atividade acadêmica desenvolvida na disciplina de Análise e Modelagem de Sistemas com o objetivo de elaborar um Diagrama de Casos de Uso UML para representar as principais interações existentes em um sistema bancário.

A modelagem permite visualizar os atores envolvidos, as funcionalidades oferecidas pelo sistema e como cada participante interage com essas funcionalidades.

## Objetivo

Os principais objetivos da atividade foram:

- Identificar os atores envolvidos no sistema;
- Levantar os casos de uso a partir dos requisitos apresentados;
- Definir as interações entre atores e funcionalidades;
- Representar graficamente o funcionamento do sistema utilizando UML;
- Compreender como diagramas de casos de uso auxiliam na análise de requisitos.

---

# Ferramenta utilizada

Para a construção do diagrama foi utilizado:

```text
Visual Paradigm Online
```

A ferramenta foi utilizada para representar graficamente os elementos da UML e organizar os atores, casos de uso e seus relacionamentos.

---

# Processo de desenvolvimento

A elaboração do diagrama foi realizada a partir das seguintes etapas:

1. Identificação dos atores envolvidos no sistema bancário;
2. Levantamento dos casos de uso presentes nos requisitos;
3. Definição dos relacionamentos entre atores e funcionalidades;
4. Representação gráfica utilizando a notação UML.

---

# Atores e participantes

O cenário analisado envolve:

```text
Cliente
Funcionário
Caixa Eletrônico
Sistema Bancário
```

Cada elemento participa de diferentes partes do funcionamento proposto.

## Cliente

O cliente realiza ou solicita as principais operações bancárias apresentadas na atividade.

Entre elas:

- Abertura de conta;
- Encerramento de conta;
- Depósito;
- Saque;
- Consulta de saldo;
- Emissão de extrato.

## Funcionário

O funcionário participa das operações que exigem atendimento dentro do banco.

No cenário proposto, o cliente depende do funcionário para:

```text
Abrir Conta
Encerrar Conta
```

## Caixa Eletrônico

O caixa eletrônico é utilizado pelo cliente para realizar operações como:

```text
Depositar Dinheiro
Sacar Dinheiro
Emitir Saldo
Emitir Extrato
```

## Sistema Bancário

O sistema é responsável pelo registro das movimentações realizadas durante as operações.

---

# Casos de uso identificados

Foram identificados sete casos de uso principais.

## 1. Abrir Conta

**Ator principal:** Cliente

Permite que o cliente solicite a abertura de uma conta bancária.

A atividade considera contas dos tipos:

```text
Especial
Poupança
```

A abertura é realizada com o auxílio de um funcionário do banco.

---

## 2. Encerrar Conta

**Ator principal:** Cliente

Permite solicitar o encerramento de uma conta bancária.

Uma regra apresentada no cenário é que:

```text
o saldo da conta deve estar zerado
```

A operação também é realizada junto a um funcionário.

---

## 3. Depositar Dinheiro

**Ator principal:** Cliente

Permite que o cliente realize depósitos em sua conta utilizando o caixa eletrônico.

---

## 4. Sacar Dinheiro

**Ator principal:** Cliente

Permite efetuar saques utilizando o caixa eletrônico.

---

## 5. Emitir Saldo

**Ator principal:** Cliente

Permite emitir um comprovante contendo o saldo da conta por meio do caixa eletrônico.

---

## 6. Emitir Extrato

**Ator principal:** Cliente

Permite obter um extrato contendo informações sobre transações recentes por meio do caixa eletrônico.

---

## 7. Registrar Movimentação

**Ator principal:** Sistema Bancário

O sistema registra automaticamente as movimentações realizadas.

Entre elas estão operações como:

```text
Depósitos
Saques
Demais movimentações
```

---

# Relacionamentos descritos na atividade

O relatório identifica as seguintes interações:

### Cliente → Funcionário

O cliente depende do funcionário para realizar a abertura e o encerramento de contas.

### Cliente → Caixa Eletrônico

O cliente utiliza o caixa eletrônico para:

```text
Depositar
Sacar
Emitir saldo
Emitir extrato
```

### Sistema Bancário → Cliente

O sistema registra as movimentações geradas pelas ações realizadas pelo cliente.

---

# Visão geral do cenário

De forma simplificada, as interações documentadas podem ser representadas como:

```text
                         SISTEMA BANCÁRIO
                                │
                                │
                    Registrar Movimentação
                                │
                                ▼

FUNCIONÁRIO ◄────────────── CLIENTE ──────────────► CAIXA ELETRÔNICO
     │                       │                            │
     │                       │                            ├── Depositar
     ├── Abrir Conta         │                            ├── Sacar
     │                       │                            ├── Emitir Saldo
     └── Encerrar Conta      │                            └── Emitir Extrato
```

Essa representação textual tem finalidade documental e não substitui o diagrama UML desenvolvido na atividade original.

---

# Conceitos trabalhados

## UML

A UML (Unified Modeling Language) fornece formas padronizadas de representar diferentes aspectos de um sistema de software.

Nesta atividade, foi utilizado o Diagrama de Casos de Uso.

## Caso de uso

Um caso de uso representa uma funcionalidade ou comportamento disponibilizado pelo sistema dentro do cenário analisado.

Exemplos da atividade:

```text
Abrir Conta
Sacar Dinheiro
Emitir Extrato
```

## Atores

Os atores representam elementos externos que participam ou interagem com as funcionalidades consideradas na modelagem.

A identificação dos atores ajuda a compreender quem participa de cada operação e quais funcionalidades são necessárias.

---

# Aprendizados

A atividade permitiu compreender como requisitos descritos textualmente podem ser transformados em uma representação visual das funcionalidades de um sistema.

A identificação dos atores e casos de uso facilita a compreensão do comportamento esperado antes da implementação do software.

O diagrama também fornece uma visão geral das operações bancárias consideradas no cenário e pode servir como base para etapas posteriores da análise e do desenvolvimento.

---

## Organização para o repositório

Esta documentação foi reorganizada a partir do relatório acadêmico original para facilitar sua apresentação e consulta no GitHub.

Os atores, casos de uso, regras e relacionamentos descritos neste `README` correspondem ao cenário trabalhado na atividade acadêmica.

A representação textual utilizada nesta documentação foi adicionada posteriormente para facilitar a leitura no repositório e não substitui o diagrama gráfico desenvolvido originalmente.

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Análise e Modelagem de Sistemas  
**Atividade:** Diagrama de Casos de Uso  
**Domínio:** Sistema Bancário  
**Modelagem:** UML  
**Ferramenta utilizada:** Visual Paradigm Online