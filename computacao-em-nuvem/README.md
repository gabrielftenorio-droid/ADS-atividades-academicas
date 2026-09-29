# Computação em Nuvem

Este diretório reúne atividades práticas selecionadas desenvolvidas na disciplina de **Computação em Nuvem** durante a graduação em Análise e Desenvolvimento de Sistemas.

As atividades abordam diferentes etapas do estudo de ambientes e serviços em nuvem, passando pela simulação de infraestrutura, utilização de banco de dados em servidor remoto, aplicações no modelo SaaS e conceitos relacionados à segurança de aplicações web.

## Atividades

### 01 — Simulação com CloudSim

Prática introdutória utilizando **Java** e o framework **CloudSim** para execução de uma simulação de computação em nuvem.

Durante a atividade foram trabalhados:

- configuração do ambiente Java;
- utilização do Apache NetBeans;
- integração de biblioteca externa;
- execução de uma simulação com CloudSim;
- observação de máquinas virtuais, datacenter e Cloudlets;
- análise do resultado da simulação.

O exemplo `CloudSimExample1` utilizado durante a prática pertence ao próprio CloudSim e foi executado sem alterações em sua lógica original.

📁 [`01-simulacao-cloudsim`](./01-simulacao-cloudsim/)

---

### 02 — Banco de Dados em Nuvem

Prática de criação e administração de um banco de dados **MySQL** em um ambiente de hospedagem remoto.

Foram utilizados recursos de gerenciamento através do **phpMyAdmin**, incluindo execução de comandos SQL para criação de tabelas, inserção de registros e definição de relacionamentos.

A estrutura resultante possuía sete tabelas:

```text
categoria
cliente
fornecedor
itempedido
marca
pedido
produtos
```

Entre os conceitos trabalhados estão:

- bancos de dados relacionais;
- MySQL;
- phpMyAdmin;
- `CREATE TABLE`;
- `INSERT INTO`;
- chaves primárias;
- chaves estrangeiras;
- relacionamentos entre tabelas.

📁 [`02-banco-de-dados-em-nuvem`](./02-banco-de-dados-em-nuvem/)

---

### 03 — SaaS e Colaboração

Atividade voltada à utilização prática de aplicações disponibilizadas através do modelo **Software as a Service (SaaS)**.

Foram utilizados serviços integrados ao Google Drive:

```text
Google Drive
├── Google Docs
├── Google Sheets
└── Google Forms
```

A prática envolveu:

- armazenamento em nuvem;
- organização de arquivos;
- compartilhamento;
- controle de permissões;
- edição colaborativa;
- histórico de versões;
- utilização de fórmulas em planilhas;
- criação de formulários;
- coleta de respostas;
- integração entre Forms e Sheets.

📁 [`03-saas-e-colaboracao`](./03-saas-e-colaboracao/)

---

### 04 — Segurança e HTTPS

Prática relacionada à segurança de uma aplicação hospedada na internet, utilizando conceitos de **SSL/TLS**, certificados digitais e **HTTPS**.

A atividade incluiu:

- criação de hospedagem;
- publicação de uma página HTML;
- verificação de certificado digital;
- análise de informações do certificado;
- comparação entre HTTP e HTTPS;
- configuração de `.htaccess`;
- redirecionamento de HTTP para HTTPS;
- validação da conexão através do navegador.

Durante a execução, foi identificado que o serviço de hospedagem já disponibilizava SSL para o subdomínio utilizado. O procedimento foi então adaptado para validar o certificado existente e configurar o redirecionamento para HTTPS.

📁 [`04-seguranca-e-https`](./04-seguranca-e-https/)

---

## Progressão das atividades

As práticas foram organizadas neste repositório de forma a representar diferentes aspectos estudados na disciplina:

```text
Fundamentos de Computação em Nuvem
              │
              ▼
      Simulação com CloudSim
              │
              ▼
    Banco de Dados em Nuvem
              │
              ▼
       SaaS e Colaboração
              │
              ▼
       Segurança e HTTPS
```

Essa sequência reúne experiências relacionadas tanto à utilização de recursos computacionais em nuvem quanto à administração de serviços, colaboração online e segurança de aplicações.

## Tecnologias e ferramentas

| Tecnologia / Ferramenta | Utilização nas atividades |
|---|---|
| Java | Execução da simulação com CloudSim |
| CloudSim | Simulação de recursos de computação em nuvem |
| Apache NetBeans | Ambiente utilizado na atividade com Java |
| MySQL | Banco de dados relacional em ambiente remoto |
| phpMyAdmin | Administração do banco de dados |
| SQL | Criação de estruturas e inserção de registros |
| Google Drive | Armazenamento e organização em nuvem |
| Google Docs | Edição colaborativa de documentos |
| Google Sheets | Planilhas e colaboração |
| Google Forms | Formulários e coleta de dados |
| HTML | Página publicada na hospedagem |
| SSL/TLS | Proteção da comunicação |
| HTTPS | Comunicação segura com a aplicação |
| `.htaccess` | Configuração do redirecionamento para HTTPS |

## Organização

```text
computacao-em-nuvem/
│
├── README.md
│
├── 01-simulacao-cloudsim/
│   └── README.md
│
├── 02-banco-de-dados-em-nuvem/
│   └── README.md
│
├── 03-saas-e-colaboracao/
│   └── README.md
│
└── 04-seguranca-e-https/
    └── README.md
```

Cada diretório contém a documentação da respectiva atividade, incluindo objetivos, procedimentos realizados, conceitos trabalhados e resultados observados.

## Contexto acadêmico

As atividades foram desenvolvidas em **2026** na disciplina de **Computação em Nuvem**, como parte da graduação em **Análise e Desenvolvimento de Sistemas**.

A organização apresentada neste repositório foi realizada posteriormente com o objetivo de preservar e documentar as práticas acadêmicas de forma adequada para consulta e portfólio.