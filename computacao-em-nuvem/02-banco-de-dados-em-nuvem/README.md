# Banco de Dados em Nuvem com MySQL e phpMyAdmin

Atividade prática desenvolvida na disciplina de **Computação em Nuvem**, durante a graduação em Análise e Desenvolvimento de Sistemas.

A prática teve como objetivo configurar um banco de dados MySQL em um ambiente de hospedagem online, utilizando o **phpMyAdmin** para executar um script SQL responsável pela criação das tabelas, inserção de registros e definição de relacionamentos.

## Objetivo

Acompanhar o processo de criação de um banco de dados em um servidor remoto, desde a preparação da hospedagem até a execução e verificação da estrutura criada.

Durante a atividade foram trabalhados:

- hospedagem em ambiente remoto;
- criação de banco de dados MySQL;
- administração pelo phpMyAdmin;
- execução de scripts SQL;
- criação de tabelas;
- inserção de registros;
- chaves primárias;
- chaves estrangeiras;
- relacionamentos entre tabelas.

## Ambiente utilizado

A atividade foi realizada em uma plataforma de hospedagem online.

Foi criada uma hospedagem gratuita vinculada a um subdomínio específico para a prática. A partir do painel de gerenciamento da hospedagem, foi possível acessar os recursos relacionados ao banco de dados.

O banco utilizado na atividade recebeu o nome:

```text
atividade_ads
```

A própria plataforma acrescentou um prefixo relacionado à conta de hospedagem ao nome apresentado no ambiente.

## Criação do banco MySQL

Após a configuração da hospedagem, foi acessada a área destinada ao gerenciamento de bancos **MySQL**.

O banco `atividade_ads` foi criado e posteriormente aberto através do **phpMyAdmin**.

No primeiro acesso, o banco ainda não possuía tabelas, pois sua estrutura seria construída através da execução do script SQL utilizado na atividade.

## Execução do script SQL

Na área SQL do phpMyAdmin foi inserido o script responsável pela criação da estrutura do banco.

O script utilizava comandos como:

```sql
CREATE TABLE
```

para criação das tabelas e definição de suas estruturas, e:

```sql
INSERT INTO
```

para inserção dos registros previstos no exercício.

Também foram definidos relacionamentos entre algumas das tabelas utilizando **chaves estrangeiras**.

Após a execução, o phpMyAdmin apresentou confirmações indicando que os comandos haviam sido processados corretamente.

## Estrutura resultante

Ao final da execução foram identificadas sete tabelas:

```text
atividade_ads
│
├── categoria
├── cliente
├── fornecedor
├── itempedido
├── marca
├── pedido
└── produtos
```

Essas estruturas representavam diferentes informações relacionadas ao domínio utilizado no exercício.

Os relacionamentos definidos pelo script permitiram estabelecer referências entre registros de diferentes tabelas, incluindo informações relacionadas a pedidos, clientes e produtos.

## Conceitos de banco de dados trabalhados

A atividade permitiu aplicar conceitos fundamentais de bancos de dados relacionais:

```text
Banco de Dados Relacional
│
├── Tabelas
│   ├── Colunas
│   └── Registros
│
├── SQL
│   ├── CREATE TABLE
│   └── INSERT INTO
│
├── Chaves
│   ├── Chave Primária
│   └── Chave Estrangeira
│
└── Relacionamentos
    └── Referências entre tabelas
```

A utilização de chaves estrangeiras permitiu relacionar informações distribuídas em estruturas diferentes sem concentrar todos os dados em uma única tabela.

## Gerenciamento pelo phpMyAdmin

O **phpMyAdmin** foi utilizado como interface web para administração do banco.

Por meio dele foi possível:

- acessar o banco criado;
- executar o script SQL;
- acompanhar o processamento dos comandos;
- visualizar as tabelas;
- verificar os registros inseridos;
- conferir a estrutura final do banco.

Após a execução do script, a área de estrutura confirmou a existência das sete tabelas e dos registros adicionados durante a atividade.

## Resultado

A prática foi concluída com a criação do banco de dados e das sete tabelas previstas no exercício.

O script foi executado sem falhas registradas no relatório, e o phpMyAdmin confirmou o processamento dos comandos de criação e inserção.

A atividade permitiu observar como um banco relacional pode ser administrado em um servidor remoto através de uma interface web, diferenciando essa experiência da utilização de um banco restrito ao ambiente local.

## Sobre o script SQL

O trabalho acadêmico registra a utilização de um script SQL contendo comandos para criação das tabelas, inserção dos registros e definição de relacionamentos.

Entretanto, o código completo desse script não é reproduzido neste diretório, pois o relatório disponível documenta sua execução e seus resultados, mas não apresenta integralmente o conteúdo textual do arquivo SQL utilizado.

Por esse motivo, nenhum script foi reconstruído ou apresentado como se fosse o código original da atividade.

## Contexto acadêmico

Atividade desenvolvida em 2026 na disciplina de **Computação em Nuvem**.

O trabalho pertence à unidade **Ofertas de Serviço em Computação em Nuvem**, na aula **Gerenciamento de Dados em Nuvem**.

A prática relacionou conceitos de computação em nuvem e bancos de dados através da configuração de um banco MySQL em um ambiente remoto, administração pelo phpMyAdmin e execução de comandos SQL.