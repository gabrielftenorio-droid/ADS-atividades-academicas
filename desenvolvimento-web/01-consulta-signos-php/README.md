# Consulta de Signos com PHP e XML

Atividade desenvolvida durante a graduação em Análise e Desenvolvimento de Sistemas com o objetivo de criar uma aplicação web capaz de identificar o signo de uma pessoa a partir da sua data de nascimento.

O projeto foi desenvolvido para execução em ambiente local utilizando XAMPP e reúne HTML, PHP, XML, CSS e Bootstrap.

## Objetivo da atividade

A proposta foi desenvolver uma página onde o usuário informa sua data de nascimento e recebe como resultado o signo correspondente.

Os dados dos signos são armazenados em um arquivo XML e consultados pelo PHP durante o processamento da data informada.

## Funcionamento

Na página inicial, o usuário informa sua data de nascimento por meio de um formulário.

Após o envio, o PHP:

1. recebe a data pelo método `POST`;
2. carrega os dados do arquivo `signos.xml`;
3. percorre os signos cadastrados;
4. compara a data informada com os períodos de cada signo;
5. apresenta o signo encontrado, seu símbolo e sua descrição.

Para trabalhar com as datas foi utilizada a classe `DateTime`.

Também foi necessário tratar separadamente o período de Capricórnio, pois ele começa em dezembro e termina em janeiro, atravessando a mudança de ano.

## Estrutura do projeto

```text
01-consulta-signos-php/
├── assets/
│   └── css/
│       └── style.css
├── layouts/
│   └── header.php
├── index.php
├── show_zodiac_sign.php
├── signos.xml
└── README.md
```

### `index.php`

Contém a página inicial e o formulário utilizado para receber a data de nascimento.

### `show_zodiac_sign.php`

Processa a data enviada pelo formulário, realiza a leitura do XML e identifica o signo correspondente.

### `signos.xml`

Armazena as informações dos 12 signos, incluindo nome, período e descrição.

### `layouts/header.php`

Contém elementos utilizados no cabeçalho da aplicação e o carregamento dos recursos de estilo.

### `assets/css/style.css`

Contém a estilização própria utilizada na interface.

## Tecnologias utilizadas

- HTML
- PHP
- XML
- CSS
- Bootstrap
- XAMPP

## Interface

A aplicação possui uma página inicial com um formulário para informar a data de nascimento.

Após a consulta, uma nova página apresenta o signo encontrado, seu símbolo e sua descrição, além da opção de realizar outra consulta.

A interface utiliza Bootstrap em conjunto com CSS próprio.

## Testes realizados

Durante a verificação da aplicação foram utilizadas datas pertencentes a diferentes períodos do calendário.

Entre os casos testados:

```text
15/04/2000 → Áries
15/06/2000 → Gêmeos
05/01/2000 → Capricórnio
```

O teste com Capricórnio também verifica o tratamento específico do intervalo que atravessa dezembro e janeiro.

## Como executar

Para executar o projeto localmente é necessário possuir um ambiente com PHP, como o XAMPP.

Com o Apache iniciado, coloque a pasta do projeto dentro de:

```text
C:\xampp\htdocs\
```

Depois acesse pelo navegador:

```text
http://localhost/nome-da-pasta/
```

## Aprendizados

Nesta atividade foram praticados conceitos como:

- criação e envio de formulários HTML;
- processamento de dados com PHP;
- método `POST`;
- leitura de arquivos XML;
- utilização de `SimpleXML`;
- manipulação e comparação de datas;
- uso da classe `DateTime`;
- estruturas condicionais;
- integração entre PHP e XML;
- organização básica de uma aplicação web;
- estilização com CSS e Bootstrap.

## Contexto acadêmico

Este projeto foi desenvolvido como atividade da graduação em Análise e Desenvolvimento de Sistemas.

O código desta pasta corresponde à implementação realizada para a atividade acadêmica e foi preservado no repositório como registro da minha evolução durante o curso.