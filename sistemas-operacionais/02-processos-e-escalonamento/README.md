# Processos, Escalonamento e Uso da CPU com SOsim

Atividade prática desenvolvida na disciplina de Sistemas Operacionais utilizando o simulador **SOsim** para observar o funcionamento do gerenciamento de processos.

Durante os experimentos foram analisados processos CPU-bound e I/O-bound, estados de execução, escalonamento circular, fatia de tempo (quantum), troca de contexto, estatísticas do sistema e concorrência pelo processador.

## Objetivos

Os principais objetivos da atividade foram:

- compreender o ciclo de vida de um processo;
- observar os estados Pronto, Execução e Bloqueado;
- comparar processos CPU-bound e I/O-bound;
- analisar o funcionamento do escalonamento;
- compreender o impacto da fatia de tempo (quantum);
- observar mudanças de contexto;
- analisar estatísticas de execução;
- acompanhar transições de estado através dos logs do SOsim.

---

# Conceitos fundamentais

Um processo pode assumir diferentes estados durante sua execução.

```text
          ┌──────────┐
          │  Pronto  │
          └────┬─────┘
               │
               ▼
        ┌─────────────┐
        │  Execução   │
        └──────┬──────┘
               │
        ┌──────┴───────┐
        │              │
        ▼              ▼
     Pronto        Bloqueado
                       │
                       ▼
                    Pronto
```

### Pronto

O processo está preparado para executar, mas aguarda disponibilidade da CPU.

### Execução

O processo está utilizando o processador.

### Bloqueado

O processo está aguardando algum evento ou operação, como uma entrada ou saída de dados.

---

# CPU-bound e I/O-bound

Dois tipos de processos foram utilizados nos experimentos.

## CPU-bound

Processo caracterizado pelo uso intensivo do processador.

Durante a atividade, foi observado que esse tipo de processo tentava permanecer o máximo possível utilizando a CPU e alternava principalmente entre os estados:

```text
Pronto ⇄ Execução
```

## I/O-bound

Processo dependente de operações de entrada e saída.

Nesse caso, foi observada maior ocorrência do estado:

```text
Bloqueado
```

porque o processo precisava aguardar operações externas antes de continuar sua execução.

---

# Atividade 1 — Conhecendo o SOsim

Inicialmente, o ambiente do simulador foi preparado para permitir a observação dos componentes do sistema.

Foram ativadas sete janelas:

```text
Console SOsim
Gerência de Processos
Gerência do Processador
Gerência de Memória
Arquivo de Paginação
Estatísticas
Log
```

Essa configuração permitiu acompanhar diferentes aspectos do funcionamento dos processos durante os experimentos.

---

# Atividade 2 — Criação de Processos

Foram criados dois processos com características diferentes:

```text
Processo 1 → CPU-bound
Processo 2 → I/O-bound
```

A observação mostrou comportamentos distintos.

### CPU-bound

O processo alternava principalmente entre:

```text
Pronto → Execução → Pronto
```

Como utiliza intensivamente o processador, sua mudança de contexto ocorria principalmente quando sua fatia de tempo terminava.

### I/O-bound

O processo apresentava frequentemente o comportamento:

```text
Execução → Bloqueado
```

Isso acontecia quando solicitava uma operação de entrada/saída.

Enquanto aguardava a conclusão dessa operação, a CPU podia ser utilizada por outro processo.

## Tempo de processador

Também foi comparado o crescimento do tempo de processador.

O processo CPU-bound apresentou crescimento mais rápido porque permanecia utilizando a CPU por períodos maiores.

O processo I/O-bound acumulava menos tempo de processador porque permanecia parte significativa do tempo aguardando operações de entrada/saída.

---

# Atividade 3 — Análise da Fatia de Tempo

Nesta etapa foi utilizado o **Escalonamento Circular**.

Foram criados novamente:

```text
1 processo CPU-bound
1 processo I/O-bound
```

ambos com a mesma prioridade.

## Primeira observação

Os processos foram observados durante aproximadamente dois minutos.

Os tempos registrados foram:

| Processo | Tempo de processador |
|---|---:|
| CPU-bound | 80 s |
| I/O-bound | 14 s |

O processo CPU-bound acumulou muito mais tempo de CPU, enquanto o I/O-bound permaneceu frequentemente aguardando operações de entrada/saída.

---

## Alteração do quantum

Em seguida, os processos foram suspensos e a **fatia de tempo foi aumentada** na Gerência do Processador.

Depois de retomar a execução e realizar uma nova observação de aproximadamente dois minutos, foram registrados:

| Processo | Tempo de processador |
|---|---:|
| CPU-bound | 194 s |
| I/O-bound | 15 s |

## Comparação

```text
                  Primeira       Após alteração
CPU-bound            80 s             194 s
I/O-bound            14 s              15 s
```

No experimento realizado, o aumento da fatia de tempo foi acompanhado por um crescimento expressivo do tempo acumulado pelo processo CPU-bound, enquanto o valor do I/O-bound apresentou pouca variação.

A análise registrada no relatório relacionou esse comportamento à redução da frequência de interrupções do CPU-bound e ao fato de o I/O-bound interromper sua própria execução quando necessita aguardar operações de entrada/saída.

---

# Quantum e Troca de Contexto

A fatia de tempo, também chamada de **quantum**, determina por quanto tempo um processo pode permanecer utilizando a CPU antes que o escalonador permita a execução de outro processo.

De forma simplificada:

```text
Quantum menor
      │
      ├── mais alternância entre processos
      └── mais trocas de contexto

Quantum maior
      │
      ├── períodos maiores de execução
      └── menos alternância
```

Durante a atividade, essa diferença pôde ser observada diretamente no simulador.

---

# Atividade 4 — Observação das Estatísticas

A janela de **Estatísticas** do SOsim foi utilizada para acompanhar indicadores relacionados à execução dos processos.

Foram observados:

- número de processos ativos;
- estados dos processos;
- quantidade de processos em Pronto;
- processos em Execução;
- processos Bloqueados;
- frequência de escalonamento.

Novamente foram utilizados processos CPU-bound e I/O-bound para observar como os indicadores se comportavam.

## Pronto x Execução

Durante a observação, foram registrados momentos em que havia processos no estado **Pronto**, mas nenhum processo aparecia como **Execução**.

No relatório, esse comportamento foi associado ao intervalo necessário para a realização de uma troca de contexto.

Durante essa operação, o sistema precisa salvar informações do processo que deixa a CPU e preparar o próximo processo que será executado.

---

# Atividade 5 — Mudanças de Estado

Na última etapa foi utilizada a janela de **Log**.

Foram criados:

```text
2 processos CPU-bound
```

com o objetivo de fazê-los competir diretamente pelo processador.

O Log permitiu acompanhar transições como:

```text
Pronto → Execução
Execução → Pronto
```

Quando a fatia de tempo de um processo terminava, ele retornava para a fila de processos prontos e outro processo podia utilizar a CPU.

---

# Comparação entre diferentes fatias de tempo

O experimento também comparou o comportamento dos dois processos CPU-bound utilizando valores diferentes de quantum.

## Fatia de tempo menor

Foi observada maior frequência de alternância entre os processos.

```text
Processo A → CPU
Processo B → CPU
Processo A → CPU
Processo B → CPU
...
```

Isso aumenta a quantidade de trocas de contexto.

## Fatia de tempo maior

Cada processo permanece mais tempo utilizando a CPU antes de ser interrompido.

```text
Processo A ─────────→ CPU
Processo B ─────────→ CPU
```

Consequentemente, o outro processo pode permanecer mais tempo aguardando no estado Pronto.

---

# Fluxo observado no experimento

```text
              ┌───────────────┐
              │ Processo novo │
              └───────┬───────┘
                      │
                      ▼
                 ┌────────┐
                 │ Pronto │◄─────────────┐
                 └───┬────┘              │
                     │                   │
                     ▼                   │
                ┌─────────┐              │
                │ Execução│──────────────┘
                └────┬────┘   fim do quantum
                     │
                     │ operação de E/S
                     ▼
                ┌───────────┐
                │ Bloqueado │
                └─────┬─────┘
                      │
                      │ fim da espera
                      └──────────► Pronto
```

---

# Principais aprendizados

A utilização do SOsim permitiu visualizar conceitos que normalmente são apresentados de maneira abstrata na teoria de Sistemas Operacionais.

Entre os principais pontos observados durante a atividade estão:

- ciclo de vida dos processos;
- estados Pronto, Execução e Bloqueado;
- diferença de comportamento entre CPU-bound e I/O-bound;
- concorrência pelo processador;
- escalonamento circular;
- fatia de tempo;
- troca de contexto;
- acompanhamento de estatísticas;
- transições de estado através de logs.

Os experimentos mostraram que alterações nos parâmetros de escalonamento modificam o comportamento observado na execução e na alternância entre os processos.

---

## Ferramenta utilizada

**SOsim — Simulador de Sistemas Operacionais**

O simulador foi utilizado para acompanhar visualmente o gerenciamento de processos e diferentes componentes relacionados ao funcionamento de um sistema operacional.

---

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Sistemas Operacionais  
**Unidade:** Processos e Threads  
**Aula:** Processos — Conceito e Gerenciamento  
**Ferramenta:** SOsim  
**Ano:** 2026

---

## Organização para o repositório

Este `README` reorganiza para fins de portfólio os experimentos documentados no relatório acadêmico original.

Os procedimentos, valores observados e análises experimentais foram mantidos de acordo com o trabalho realizado. A estrutura da documentação foi reorganizada posteriormente para tornar o conteúdo mais adequado para consulta no GitHub.