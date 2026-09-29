# Windows e Linux — Kernel, Shell, Permissões e Diretórios

Atividade prática desenvolvida na disciplina de Sistemas Operacionais com o objetivo de compreender e comparar características fundamentais dos ambientes Windows e Linux.

O trabalho explorou, por meio de comandos e operações práticas, conceitos relacionados ao Kernel, Shell, gerenciamento de processos, permissões de arquivos e organização da estrutura de diretórios.

## Objetivos

Os principais objetivos da atividade foram:

- compreender o papel do Kernel e do Shell;
- observar processos em execução no Windows e no Linux;
- utilizar ferramentas de linha de comando;
- trabalhar com permissões de arquivos;
- comparar a estrutura de diretórios dos dois sistemas operacionais;
- relacionar os conceitos teóricos da disciplina com operações realizadas em ambientes reais.

---

## Conceitos fundamentais

O sistema operacional atua como uma camada intermediária entre o hardware e o usuário.

Dois componentes importantes estudados durante a atividade foram:

### Kernel

O Kernel representa o núcleo do sistema operacional e é responsável pelo gerenciamento de recursos como:

```text
CPU
Memória
Dispositivos de entrada e saída
Processos
```

### Shell

O Shell permite que o usuário interaja com o sistema operacional por meio de comandos.

Durante a atividade foram utilizados ambientes de linha de comando tanto no Windows quanto no Linux.

---

# Atividade 1 — Explorando Kernel e Shell

A primeira etapa consistiu em observar como Windows e Linux permitem consultar informações relacionadas ao sistema e aos processos em execução.

## Linux

No Linux, foi utilizado o comando:

```bash
uname -r
```

para identificar a versão do Kernel.

Para visualizar os processos em execução, foi utilizado:

```bash
ps -e
```

A consulta permitiu observar os processos ativos sendo gerenciados pelo sistema operacional.

## Windows

No Windows, foi utilizado o PowerShell.

Para listar os processos ativos:

```powershell
Get-Process
```

O comando permite visualizar processos e serviços que estão sendo gerenciados pelo sistema.

Também foi utilizado:

```text
winver
```

para identificar a versão instalada do Windows.

### Comparação

Apesar das diferenças entre comandos e interfaces, os dois ambientes permitem consultar informações relacionadas aos processos e ao próprio sistema operacional.

```text
Linux                         Windows

uname -r                      winver
   │                             │
   ▼                             ▼
Versão do Kernel             Versão do Windows


ps -e                         Get-Process
   │                             │
   ▼                             ▼
Processos ativos             Processos ativos
```

---

# Atividade 2 — Gerenciamento de Arquivos e Permissões

A segunda etapa foi dedicada ao gerenciamento de permissões de arquivos.

O objetivo foi observar como Windows e Linux permitem controlar quais usuários podem acessar ou modificar determinados recursos.

## Linux

Foi criado o diretório:

```bash
test_dir
```

e, dentro dele, o arquivo:

```bash
test_file.txt
```

Em seguida, foram definidas permissões utilizando:

```bash
chmod 600 test_file.txt
```

A configuração `600` concede ao proprietário:

```text
Leitura  → permitida
Escrita  → permitida
Execução → não permitida
```

e remove essas permissões dos demais usuários.

A configuração foi verificada com:

```bash
ls -l
```

O resultado permitiu confirmar as permissões atribuídas ao arquivo.

## Windows

No Windows, foi criada a pasta:

```text
TestFolder
```

contendo:

```text
TestFile.txt
```

As permissões foram alteradas para restringir o acesso ao proprietário.

Na atividade, esse procedimento foi realizado pela interface gráfica do Windows, com a desativação da herança de permissões.

O roteiro também apresentava como alternativa o comando:

```cmd
icacls TestFile.txt /grant %username%:F
```

O exercício demonstrou que os dois sistemas possuem mecanismos de controle de acesso, embora utilizem formas diferentes de configuração e representação.

---

# Atividade 3 — Comparação das Estruturas de Diretórios

A última etapa analisou como Windows e Linux organizam arquivos e diretórios.

## Linux

A estrutura foi explorada a partir da raiz:

```text
/
```

utilizando:

```bash
ls /
```

Entre os diretórios analisados estavam:

### `/home`

Armazena os diretórios pessoais dos usuários.

```text
/home
├── usuario1
├── usuario2
└── ...
```

### `/etc`

Centraliza diversos arquivos de configuração do sistema e de aplicações instaladas.

### `/var`

Armazena dados que sofrem alterações frequentes durante o funcionamento do sistema, como logs e outros arquivos variáveis.

---

## Windows

No Windows, a exploração partiu da unidade:

```text
C:\
```

A navegação foi realizada utilizando o Explorador de Arquivos e o PowerShell.

Entre os principais diretórios analisados estavam:

### `C:\Users`

Armazena os diretórios e informações específicas dos perfis de usuários.

Possui função comparável, dentro da organização estudada, ao `/home` do Linux.

### `C:\Windows`

Contém arquivos importantes do sistema operacional e bibliotecas utilizadas pelo Windows.

### `C:\Program Files`

Diretório normalmente utilizado para instalação e organização de programas.

---

# Comparação das estruturas

Uma diferença observada durante a atividade foi a organização das estruturas de diretórios.

## Linux

O sistema utiliza uma única árvore iniciada na raiz:

```text
/
├── home
├── etc
├── var
└── ...
```

## Windows

A organização parte de unidades de armazenamento:

```text
C:\
├── Users
├── Windows
├── Program Files
└── ...
```

Essa diferença influencia a maneira como arquivos, configurações, aplicações e informações de usuários são organizados em cada ambiente.

---

# Comandos utilizados

| Ambiente | Comando | Finalidade |
|---|---|---|
| Linux | `uname -r` | Consultar a versão do Kernel |
| Linux | `ps -e` | Listar processos em execução |
| Linux | `chmod 600` | Alterar permissões de arquivo |
| Linux | `ls -l` | Visualizar informações e permissões |
| Linux | `ls /` | Visualizar a estrutura a partir da raiz |
| Windows | `Get-Process` | Listar processos ativos |
| Windows | `winver` | Consultar a versão do Windows |

O relatório também apresenta `icacls` como uma alternativa para alteração das permissões no Windows.

---

# Conceitos trabalhados

A atividade permitiu trabalhar conceitos fundamentais de Sistemas Operacionais:

```text
Sistema Operacional
        │
        ├── Kernel
        │    └── Gerenciamento de recursos
        │
        ├── Shell
        │    └── Interação por comandos
        │
        ├── Processos
        │    └── Programas em execução
        │
        ├── Sistema de Arquivos
        │    └── Organização dos dados
        │
        └── Permissões
             └── Controle de acesso
```

---

# Aprendizados

A prática permitiu observar que Windows e Linux apresentam diferenças importantes em seus comandos e na organização dos arquivos, mas ambos precisam resolver problemas fundamentais semelhantes de um sistema operacional.

Entre os principais aprendizados estiveram:

- utilização básica do terminal;
- consulta de processos;
- identificação de informações do sistema;
- gerenciamento de permissões;
- organização de arquivos e diretórios;
- diferenças entre as estruturas Windows e Linux;
- relação entre Shell, Kernel e recursos do sistema.

A atividade também mostrou a importância do conhecimento de linha de comando para administração e desenvolvimento de software, principalmente em ambientes nos quais é necessário trabalhar diretamente com arquivos, permissões, processos e configurações do sistema.

---

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Sistemas Operacionais  
**Unidade:** Introdução aos Sistemas Operacionais  
**Aula:** Características dos Sistemas Operacionais  
**Ambientes:** Windows e Linux  
**Ferramentas:** PowerShell e terminal Linux  
**Ano:** 2026

---

## Organização para o repositório

Este `README` reorganiza para fins de portfólio as práticas documentadas no relatório acadêmico original.

Os comandos, procedimentos e conceitos apresentados correspondem às atividades realizadas ou previstas no roteiro utilizado no trabalho. A documentação foi reorganizada posteriormente para facilitar sua consulta no GitHub.