# Sistemas Operacionais

Esta seção reúne atividades práticas desenvolvidas na disciplina de **Sistemas Operacionais** durante a graduação em Análise e Desenvolvimento de Sistemas.

As atividades foram organizadas de forma progressiva, partindo dos fundamentos dos sistemas operacionais e da comparação entre Windows e Linux, passando pelo gerenciamento de processos e sistemas de arquivos, até chegar aos conceitos de memória virtual e paginação.

## Conteúdos desenvolvidos

### 1. Windows, Linux, Kernel e Shell

Estudo introdutório sobre o funcionamento dos sistemas operacionais Windows e Linux.

Foram explorados conceitos relacionados a:

- Kernel e Shell;
- processos em execução;
- comandos no PowerShell e terminal Linux;
- permissões de arquivos;
- estrutura de diretórios;
- diferenças entre Windows e Linux.

📁 [`01-windows-linux-kernel-shell`](./01-windows-linux-kernel-shell/)

---

### 2. Processos e Escalonamento

Atividade prática utilizando o **SOsim** para visualizar o gerenciamento de processos pelo sistema operacional.

Foram analisados:

- estados Pronto, Execução e Bloqueado;
- processos CPU-bound e I/O-bound;
- escalonamento circular;
- fatia de tempo (quantum);
- troca de contexto;
- concorrência pelo processador;
- estatísticas de execução;
- transições de estados através dos logs.

Também foram realizados experimentos alterando a fatia de tempo para observar mudanças no comportamento dos processos.

📁 [`02-processos-e-escalonamento`](./02-processos-e-escalonamento/)

---

### 3. Sistemas de Arquivos

Estudo sobre arquivos, metadados e formas de acesso aos dados.

A atividade utilizou o **PowerShell** para analisar propriedades de diferentes tipos de arquivos e trabalhou conceitos como:

- sistemas de arquivos;
- metadados;
- atributos;
- tamanho de arquivos;
- datas de criação e modificação;
- extensões;
- permissões;
- acesso sequencial;
- consulta a informações específicas.

📁 [`03-sistemas-de-arquivos`](./03-sistemas-de-arquivos/)

---

### 4. Gerenciamento de Memória

Atividade prática utilizando novamente o **SOsim**, desta vez com foco no gerenciamento de memória.

Foram estudados e observados:

- memória virtual;
- memória física;
- paginação;
- Tabela de Páginas;
- Bit de Validade (Bit V);
- arquivo de paginação;
- busca de páginas antecipada;
- relação entre processos e memória.

A utilização do simulador permitiu visualizar a Tabela de Páginas de um processo e acompanhar a presença ou ausência de páginas na memória física.

📁 [`04-gerenciamento-de-memoria`](./04-gerenciamento-de-memoria/)

---

## Progressão dos estudos

As atividades foram organizadas para representar a progressão dos conteúdos estudados na disciplina:

```text
Fundamentos de Sistemas Operacionais
                │
                ▼
       Windows e Linux
                │
                ▼
      Processos e CPU
                │
                ▼
     Sistemas de Arquivos
                │
                ▼
   Gerenciamento de Memória
                │
                ▼
     Memória Virtual e Paginação
```

Essa sequência permitiu relacionar diferentes responsabilidades de um sistema operacional e compreender como processos, arquivos, CPU e memória são administrados.

## Ferramentas e ambientes utilizados

| Ferramenta / Ambiente | Aplicação |
|---|---|
| Windows | Exploração do sistema e gerenciamento de arquivos |
| Linux | Terminal, processos, permissões e diretórios |
| PowerShell | Consulta de processos e propriedades de arquivos |
| SOsim | Simulação de processos, escalonamento e memória |

## Conceitos trabalhados

Ao longo das atividades foram abordados conceitos como:

```text
Sistemas Operacionais
├── Kernel e Shell
├── Processos
│   ├── CPU-bound
│   ├── I/O-bound
│   ├── Estados
│   ├── Escalonamento
│   └── Troca de contexto
├── Sistemas de Arquivos
│   ├── Metadados
│   ├── Permissões
│   └── Acesso aos dados
└── Gerenciamento de Memória
    ├── Memória Virtual
    ├── Paginação
    ├── Tabela de Páginas
    └── Bit de Validade
```

## Organização

```text
sistemas-operacionais/
├── README.md
├── 01-windows-linux-kernel-shell/
│   └── README.md
├── 02-processos-e-escalonamento/
│   └── README.md
├── 03-sistemas-de-arquivos/
│   └── README.md
└── 04-gerenciamento-de-memoria/
    └── README.md
```

Cada diretório contém a documentação de uma atividade ou conjunto de experimentos realizados durante a disciplina.

## Contexto acadêmico

As atividades foram desenvolvidas durante a graduação em **Análise e Desenvolvimento de Sistemas**, em 2026.

A documentação apresentada neste repositório reorganiza os trabalhos acadêmicos para fins de estudo e portfólio, preservando os conceitos, procedimentos e experimentos registrados nas atividades originais.