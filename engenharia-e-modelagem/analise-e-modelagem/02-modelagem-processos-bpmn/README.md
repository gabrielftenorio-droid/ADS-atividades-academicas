# Modelagem de Processos com BPMN — Processo de Compras

Atividade acadêmica desenvolvida com o objetivo de aplicar a notação BPMN (Business Process Model and Notation) na representação de um processo de Solicitação e Compra de Material ou Insumo.

O processo modelado envolve diferentes participantes, atividades, eventos e pontos de decisão, permitindo representar visualmente o fluxo desde a solicitação inicial até o recebimento do material e a programação do pagamento ao fornecedor.

## Objetivo

Os principais objetivos da atividade foram:

- Compreender os fundamentos da modelagem de processos de negócio;
- Utilizar a notação BPMN para representar um processo organizacional;
- Identificar participantes e suas responsabilidades;
- Organizar atividades em raias (Lanes);
- Representar a sequência das atividades;
- Utilizar eventos e pontos de decisão;
- Aplicar um Gateway Exclusivo para representar caminhos alternativos no processo.

---

# Ferramenta utilizada

O diagrama foi desenvolvido utilizando:

```text
bpmn.io
```

A ferramenta foi utilizada para criação, visualização e edição do diagrama BPMN.

---

# Processo modelado

O cenário da atividade representa o processo de:

```text
Solicitação e Compra de Material ou Insumo
```

O fluxo envolve desde a identificação da necessidade de compra até o recebimento do material e a programação do pagamento ao fornecedor.

---

# Participantes

O processo foi organizado envolvendo os seguintes participantes:

```text
Solicitante
Setor de Compras
Fornecedor
Setor de Recepção
Setor Financeiro
```

Cada participante possui responsabilidades específicas dentro do fluxo.

---

# Fluxo do processo

## 1. Solicitação Interna de Compra

O processo começa quando o solicitante realiza:

```text
Fazer Solicitação Interna de Compra (SIC)
```

A SIC inicia formalmente o processo de aquisição do material ou insumo.

---

## 2. Realização de orçamentos

Após a solicitação, o Setor de Compras realiza orçamentos com:

```text
pelo menos três fornecedores
```

Essa etapa permite comparar diferentes possibilidades de fornecimento.

---

## 3. Seleção do fornecedor

Após os orçamentos, é selecionado o fornecedor que apresenta as melhores condições comerciais.

Os critérios considerados na atividade incluem:

```text
Preço
Prazo de entrega
```

---

## 4. Elaboração da Ordem de Compra

Após a seleção do fornecedor, é elaborada uma:

```text
Ordem de Compra (OC)
```

A Ordem de Compra formaliza a aquisição do material.

---

## 5. Envio ao fornecedor

A Ordem de Compra é enviada ao fornecedor selecionado.

A partir desse ponto, o fornecedor participa do fluxo relacionado ao fornecimento e entrega do material.

---

## 6. Recebimento da mercadoria

O Setor de Recepção recebe:

```text
Mercadoria
Fatura
```

Após o recebimento, é realizada a conferência da mercadoria de acordo com a fatura.

---

# Gateway de decisão

Após a conferência, o processo chega a um ponto de decisão representado por um:

```text
Gateway Exclusivo
```

A decisão determina o caminho que o processo seguirá de acordo com o resultado da conferência.

De forma simplificada:

```text
                    Conferência
                        │
                        ▼
                 Material correto?
                    /          \
                  Sim          Não
                  /              \
                 ▼                ▼
        Continuar processo    Recusar entrega
```

---

# Caminho positivo — Material correto

Quando a mercadoria está correta, o Setor de Recepção realiza duas ações:

```text
Material → Solicitante

Fatura → Setor Financeiro
```

O material é encaminhado ao solicitante e a fatura segue para o setor responsável pelo pagamento.

---

# Caminho negativo — Erro na entrega

Caso exista algum erro na mercadoria ou na fatura:

```text
Entrega não é aceita
        │
        ▼
Fornecedor recolhe o material
```

Esse caminho é encerrado após a recusa da entrega e o recolhimento do material pelo fornecedor.

---

# Programação do pagamento

No fluxo principal, após receber a fatura, o Setor Financeiro realiza:

```text
Programação do pagamento ao fornecedor
```

Essa atividade representa a última etapa do fluxo principal documentado.

---

# Encerramento do processo

O processo é encerrado após a programação do pagamento pelo Setor Financeiro.

De maneira resumida:

```text
Solicitação Interna de Compra
            │
            ▼
Realização de orçamentos
            │
            ▼
Seleção do fornecedor
            │
            ▼
Elaboração da Ordem de Compra
            │
            ▼
Envio ao fornecedor
            │
            ▼
Recebimento da mercadoria e fatura
            │
            ▼
Conferência
            │
            ▼
      Material correto?
        /          \
      Sim          Não
       │             │
       ▼             ▼
Material para     Recusar
solicitante       entrega
       │             │
Fatura para       Fornecedor
Financeiro        recolhe material
       │             │
       ▼             ▼
Programar          Fim
pagamento
       │
       ▼
      Fim
```

Essa representação textual possui finalidade documental e não substitui o diagrama BPMN desenvolvido originalmente.

---

# Elementos BPMN trabalhados

## Raias — Lanes

As raias foram utilizadas para separar as responsabilidades dos participantes envolvidos no processo.

Isso permite visualizar quem é responsável por cada atividade.

## Atividades — Tasks

As atividades representam ações executadas durante o processo.

Exemplos presentes na atividade:

```text
Fazer Solicitação Interna de Compra
Realizar orçamentos
Selecionar fornecedor
Elaborar Ordem de Compra
Realizar conferência
Programar pagamento
```

## Eventos — Events

Os eventos permitem representar pontos relevantes do processo, incluindo seu início e encerramento.

## Gateway

O Gateway representa um ponto em que o fluxo precisa tomar uma decisão.

Nesta atividade foi utilizado um:

```text
Gateway Exclusivo
```

para decidir o caminho seguido após a conferência da mercadoria e da fatura.

---

# Aprendizados

A atividade permitiu compreender como um processo organizacional pode ser transformado em uma representação visual estruturada.

A utilização de participantes, raias, atividades, eventos e gateways facilita a identificação das responsabilidades de cada setor e permite visualizar o fluxo completo do processo.

O Gateway Exclusivo também demonstrou como diferentes caminhos podem ser representados a partir de uma condição de negócio, como a aprovação ou rejeição de uma entrega.

A modelagem BPMN pode auxiliar na análise de processos antes de sua implementação ou automatização, tornando mais claras as etapas, responsabilidades e decisões existentes no fluxo.

---

## Organização para o repositório

Esta documentação foi reorganizada a partir do relatório acadêmico original para facilitar sua apresentação e consulta no GitHub.

O processo, os participantes, as atividades e o ponto de decisão apresentados neste `README` correspondem ao fluxo documentado na atividade acadêmica.

A representação textual do processo foi adicionada posteriormente para facilitar a visualização no repositório e não substitui o diagrama BPMN desenvolvido originalmente.

## Observação sobre o relatório original

O relatório acadêmico original apresenta, em sua seção de conclusão, um texto relacionado a tabelas-verdade, conectivos lógicos e Leis de De Morgan.

Como esse conteúdo não corresponde à atividade de modelagem BPMN desenvolvida no restante do relatório, ele não foi reproduzido nesta documentação.

O `README` foi organizado com base no processo BPMN efetivamente descrito e desenvolvido na atividade.

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Área:** Análise e Modelagem de Sistemas  
**Atividade:** Modelagem de Processo de Negócio  
**Processo:** Solicitação e Compra de Material ou Insumo  
**Notação:** BPMN  
**Ferramenta utilizada:** bpmn.io