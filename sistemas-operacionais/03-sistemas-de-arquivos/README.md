# Arquivos e Sistemas de Arquivos

Atividade prática desenvolvida na disciplina de Sistemas Operacionais com foco na organização e no gerenciamento de arquivos.

A prática utilizou ferramentas de linha de comando para analisar propriedades de arquivos e comparar diferentes formas de acesso aos dados.

## Objetivos

Os principais objetivos foram:

- compreender o papel do sistema de arquivos;
- analisar metadados e atributos de arquivos;
- utilizar o PowerShell para inspecionar arquivos;
- identificar informações como nome, tamanho e datas;
- compreender os conceitos de acesso sequencial e acesso direto apresentados na atividade;
- comparar o comportamento dos dois métodos em consultas aos dados.

---

# Metadados de arquivos

Além de seu conteúdo, um arquivo possui informações utilizadas pelo sistema operacional para identificá-lo e gerenciá-lo.

Essas informações são chamadas de **metadados** ou **atributos**.

Durante a atividade foram observados atributos como:

| Atributo | Informação observada |
|---|---|
| `Name` | Nome completo e extensão do arquivo |
| `Length` | Tamanho do arquivo em bytes |
| `CreationTime` | Data e horário de criação |
| `LastWriteTime` | Data da última alteração do conteúdo |

Essas propriedades permitem ao sistema operacional manter informações sobre os arquivos armazenados.

---

# Atividade 1 — Identificação e análise de atributos

A primeira atividade utilizou o **PowerShell do Windows** para analisar arquivos presentes no computador.

Foram selecionados três formatos diferentes:

```text
Documento → .docx
Imagem    → .jpg
Executável → .exe
```

O objetivo foi observar como arquivos de diferentes tipos possuem propriedades que podem ser consultadas pelo sistema operacional.

## Consulta das propriedades

O relatório registra o uso do `Get-Item` em conjunto com `Select-Object *` para visualizar as propriedades dos arquivos.

A estrutura utilizada foi:

```powershell
Get-Item <nome_do_arquivo> | Select-Object *
```

A consulta permitiu analisar informações como:

```text
Arquivo
   │
   ├── Name
   ├── Length
   ├── CreationTime
   ├── LastWriteTime
   ├── atributos
   └── outras propriedades
```

---

# Atributos analisados

## Nome

O atributo `Name` identifica o nome e a extensão do arquivo.

Exemplos dos formatos analisados:

```text
arquivo.docx
imagem.jpg
programa.exe
```

A extensão auxilia na identificação do tipo de arquivo e de aplicações associadas a ele.

---

## Tamanho

O atributo:

```text
Length
```

representa o tamanho do arquivo em bytes.

Essa informação permite verificar quanto espaço o arquivo ocupa.

---

## Data de criação

O atributo:

```text
CreationTime
```

registra a data e o horário associados à criação do arquivo.

---

## Última modificação

O atributo:

```text
LastWriteTime
```

indica quando o conteúdo do arquivo foi alterado pela última vez.

Essas informações podem ser úteis para organização, buscas, backups e acompanhamento de alterações.

---

## Permissões e atributos

A atividade também abordou a importância das permissões no controle de acesso aos arquivos.

Esses mecanismos ajudam a determinar quais operações podem ser realizadas sobre determinados recursos, contribuindo para a proteção e a integridade dos dados.

---

# Atividade 2 — Acesso Sequencial e Acesso Direto

Na segunda atividade foi criado um arquivo de texto contendo várias linhas de dados.

O arquivo foi utilizado para comparar dois métodos apresentados no roteiro:

```text
Acesso Sequencial
        vs.
Acesso Direto
```

---

# Acesso Sequencial

No primeiro teste, o arquivo foi percorrido linha por linha.

O procedimento utilizou o comando `for /f` para realizar a leitura do arquivo `dados.txt`.

De maneira simplificada, o comportamento observado foi:

```text
Linha 1
   ↓
Linha 2
   ↓
Linha 3
   ↓
Linha 4
   ↓
...
   ↓
Fim do arquivo
```

Nesse experimento, todas as informações armazenadas eram exibidas em sequência.

Esse método foi utilizado para representar situações em que existe interesse em processar todo o conteúdo do arquivo.

---

# Acesso Direto

No segundo teste, o usuário informava o número da linha que desejava consultar.

O script então localizava a linha correspondente e exibia apenas a informação escolhida.

No experimento registrado no relatório foi escolhida:

```text
Linha 03
```

O comportamento pode ser representado como:

```text
Usuário informa
      │
      ▼
   Linha 03
      │
      ▼
Script localiza
a linha correspondente
      │
      ▼
Informação exibida
```

Na atividade, esse procedimento foi denominado **acesso direto** por permitir solicitar uma informação específica sem exibir todo o conteúdo do arquivo.

---

# Comparação realizada

Durante os testes, foram observadas diferenças entre os dois procedimentos.

| Característica | Sequencial | “Direto” no experimento |
|---|---|---|
| Objetivo | Percorrer o conteúdo | Localizar uma informação específica |
| Exibição | Todas as linhas | Linha escolhida |
| Exemplo utilizado | Leitura completa | Linha 03 |
| Uso observado | Processamento de todos os dados | Consulta específica |

O relatório registra que, durante o experimento, a consulta específica apresentou resposta mais rápida para localizar a informação desejada, enquanto a leitura sequencial percorreu todas as linhas.

Não foram registradas medições numéricas de tempo de execução.

---

# Fluxo geral da atividade

```text
                 SISTEMA DE ARQUIVOS
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
         Metadados              Acesso aos dados
             │                       │
     ┌───────┼────────┐        ┌─────┴─────┐
     │       │        │        │           │
    Name   Length   Datas   Sequencial   “Direto”
```

---

# Ferramentas e recursos utilizados

Durante as atividades foram utilizados:

- Windows;
- PowerShell;
- linha de comando;
- arquivos `.docx`, `.jpg` e `.exe`;
- arquivo de texto para os testes de leitura.

---

# Principais aprendizados

A atividade permitiu observar na prática que arquivos possuem informações adicionais além de seu conteúdo.

Entre os conceitos trabalhados estão:

- sistemas de arquivos;
- arquivos e metadados;
- atributos;
- tamanho de arquivos;
- datas de criação e modificação;
- permissões;
- extensões de arquivos;
- PowerShell;
- leitura sequencial;
- consulta a uma informação específica.

A prática também mostrou como ferramentas de linha de comando podem ser utilizadas para investigar propriedades que normalmente ficam menos visíveis durante o uso cotidiano da interface gráfica.

---

## Contexto acadêmico

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas.

**Disciplina:** Sistemas Operacionais  
**Unidade:** Sistema de Arquivos  
**Aula:** Arquivos e Sistemas de Arquivos  
**Ambiente:** Windows  
**Ferramenta:** PowerShell  
**Ano:** 2026

---

## Organização para o repositório

Este `README` reorganiza para fins de portfólio as práticas documentadas no relatório acadêmico original.

A documentação mantém os procedimentos, conceitos e resultados registrados no trabalho, reorganizando sua apresentação para facilitar a consulta no GitHub.