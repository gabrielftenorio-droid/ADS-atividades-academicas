# Gerenciamento de Memória e Paginação com SOsim

Atividade prática desenvolvida na disciplina de Sistemas Operacionais utilizando o simulador **SOsim** para observar conceitos relacionados ao gerenciamento de memória.

O experimento teve como foco a **paginação**, a utilização da **memória virtual**, a **Tabela de Páginas** e o **Bit de Validade (Bit V)**.

## Objetivos

Os principais objetivos da atividade foram:

- compreender o funcionamento básico da paginação;
- observar a relação entre memória virtual e memória física;
- analisar a Tabela de Páginas de um processo;
- compreender o significado do Bit de Validade;
- configurar uma política de busca de páginas no SOsim;
- visualizar o gerenciamento de memória por meio de uma simulação.

---

# Paginação

A paginação é um mecanismo utilizado para organizar a memória de um processo em blocos.

Na atividade, esse conceito foi relacionado à memória virtual.

De forma simplificada:

```text
Processo
   │
   ▼
Memória Virtual
   │
   ▼
┌─────────┐
│ Página 0│
├─────────┤
│ Página 1│
├─────────┤
│ Página 2│
├─────────┤
│   ...   │
└─────────┘
```

Essas páginas podem ser mapeadas para diferentes regiões da memória física.

O gerenciamento desse mapeamento é realizado com auxílio da **Tabela de Páginas**.

---

# Tabela de Páginas

Durante a atividade, a Tabela de Páginas foi utilizada para observar informações relacionadas às páginas pertencentes ao processo criado.

Ela funciona como uma estrutura de mapeamento utilizada pelo sistema operacional para acompanhar as páginas de memória do processo.

Um dos elementos analisados no experimento foi o:

```text
Bit de Validade (Bit V)
```

---

# Bit de Validade

No experimento realizado no SOsim, o Bit V indicava se determinada página estava presente na memória física.

A interpretação utilizada na atividade foi:

```text
Bit V = 0
     │
     ▼
Página não está
na memória física
```

e:

```text
Bit V = 1
     │
     ▼
Página presente
na memória RAM
```

Essa informação foi acompanhada diretamente na Tabela de Páginas do processo.

---

# Busca de Páginas Antecipada

A política utilizada no experimento foi:

```text
Busca de Páginas Antecipada
```

Na abordagem estudada, essa política procura carregar antecipadamente páginas que poderão ser necessárias ao processo.

O relatório também diferencia essa estratégia da busca por demanda, na qual a página é trazida quando é solicitada.

---

# Atividade prática

## 1. Preparação do ambiente

Inicialmente, o SOsim foi configurado através de:

```text
Console SOsim
      │
      ▼
Opções
      │
      ▼
Parâmetros do Sistema
```

Na guia relacionada ao processador, foi selecionado:

```text
Escalonamento Circular
```

Na configuração de memória, foi selecionada:

```text
Busca de Páginas Antecipada
```

Assim, o ambiente ficou preparado para a realização do experimento.

---

# 2. Criação do processo

Após configurar o simulador, foi aberta a janela:

```text
Gerência de Processos
```

Em seguida:

```text
Gerência de Processos
        │
        ▼
      Criar
        │
        ▼
    CPU-bound
```

Foi criado um processo do tipo **CPU-bound** para realizar a observação.

---

# 3. Observação da paginação

Depois da criação do processo, foi aberta a opção:

```text
Janelas
   │
   ▼
Arquivos de Paginação
```

O objetivo foi visualizar o arquivo de paginação utilizado pelo simulador.

Em seguida, foi acessado o contexto do processo.

O relatório registra duas formas de chegar a essa área:

```text
Botão direito sobre o processo
```

ou:

```text
Gerência de Processos → PCB
```

Dentro do contexto do processo foi acessada a guia:

```text
Tab. de Pag.
```

A partir dela foi possível acompanhar a **Tabela de Páginas**.

---

# Observação do Bit V

Durante a análise, a atenção foi direcionada principalmente para a coluna correspondente ao **Bit de Validade**.

```text
             Tabela de Páginas
                    │
                    ▼
                 Bit V
              ┌─────┴─────┐
              │           │
              ▼           ▼
              0           1
              │           │
              ▼           ▼
        Não presente    Presente
        na memória      na RAM
        física
```

Essa observação permitiu relacionar visualmente a teoria de paginação com o comportamento apresentado pelo simulador.

---

# Fluxo do experimento

```text
Inicialização do SOsim
          │
          ▼
Parâmetros do Sistema
          │
          ├── Escalonamento Circular
          │
          └── Busca de Páginas Antecipada
                         │
                         ▼
               Criação do processo
                    CPU-bound
                         │
                         ▼
                Arquivo de Paginação
                         │
                         ▼
                 Contexto do Processo
                         │
                         ▼
                  Tabela de Páginas
                         │
                         ▼
                 Observação do Bit V
```

---

# Conceitos trabalhados

Durante a atividade foram abordados conceitos relacionados a:

- gerenciamento de memória;
- memória virtual;
- memória física;
- paginação;
- páginas;
- Tabela de Páginas;
- Bit de Validade;
- arquivo de paginação;
- política de busca antecipada;
- processo CPU-bound;
- escalonamento circular.

---

# Principais aprendizados

A utilização do SOsim permitiu visualizar conceitos de gerenciamento de memória que normalmente são apresentados de maneira abstrata.

A observação da Tabela de Páginas ajudou a compreender como o sistema operacional acompanha a situação das páginas associadas a um processo.

O Bit de Validade permitiu identificar, dentro da simulação, se determinada página estava ou não presente na memória física.

A atividade também permitiu relacionar conceitos de memória virtual, paginação e gerenciamento de processos em um mesmo ambiente de simulação.

---

## Ferramenta utilizada

**SOsim — Simulador de Sistemas Operacionais**

O simulador foi utilizado para visualizar o comportamento do gerenciamento de memória e da paginação.

---

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Sistemas Operacionais  
**Unidade:** Gerenciamento de Dispositivos  
**Aula:** Gerenciamento de Memória  
**Ferramenta:** SOsim  
**Processo utilizado:** CPU-bound  
**Política de memória:** Busca de Páginas Antecipada  
**Escalonamento:** Circular  
**Ano:** 2026

---

## Organização para o repositório

Este `README` reorganiza para fins de portfólio a atividade documentada no relatório acadêmico original.

Os procedimentos, configurações e observações apresentados correspondem ao experimento registrado no trabalho. A documentação foi reorganizada posteriormente para facilitar sua consulta no GitHub.