# Frameworks para Desenvolvimento de Software

Este diretório reúne atividades práticas desenvolvidas na disciplina **Framework para Desenvolvimento de Software**, do curso de **Análise e Desenvolvimento de Sistemas**.

As atividades selecionadas exploram aplicações de frameworks e ferramentas em diferentes contextos de desenvolvimento, incluindo uma aplicação mobile Android com persistência local e uma aplicação web utilizando Flask no back-end.

## Atividades

### 01 — Cadastro de Produtos Android

Aplicação Android para cadastro e armazenamento local de produtos, desenvolvida com **Java** e **SQLite**.

Principais conceitos trabalhados:

- desenvolvimento de aplicações Android;
- construção de interface utilizando XML;
- programação em Java;
- persistência local com SQLite;
- utilização de `SQLiteOpenHelper`;
- inserção e consulta de registros;
- validação de dados;
- exibição de registros utilizando `ListView`;
- organização de um projeto Android com Gradle.

A aplicação permite cadastrar produtos informando nome e preço, validar os valores recebidos e armazenar os registros localmente.

A persistência foi verificada reiniciando a aplicação e confirmando que os produtos cadastrados anteriormente continuavam disponíveis.

A implementação acadêmica preservada também foi posteriormente compilada novamente com sucesso.

📁 [`01-android-cadastro-produtos`](./01-android-cadastro-produtos/)

---

### 02 — Calculadora de Salário Líquido com Flask

Aplicação web desenvolvida com **Python e Flask** para demonstrar processamento de formulários e execução de regras no back-end.

Principais conceitos trabalhados:

- criação de aplicações Flask;
- definição de rotas;
- renderização de templates HTML;
- formulários web;
- requisições HTTP `POST`;
- processamento de dados no servidor;
- conversão e validação de entradas;
- tratamento de valores inválidos;
- aplicação de regras de negócio simplificadas.

O formulário recebe salário bruto e número de dependentes. O servidor processa os valores utilizando regras definidas especificamente para o exercício e retorna o resultado calculado.

> As regras de INSS, IR e dependentes utilizadas nessa atividade são simplificações acadêmicas e não representam uma calculadora trabalhista, previdenciária ou tributária real.

A implementação acadêmica preservada foi posteriormente executada novamente e seus principais comportamentos foram validados.

📁 [`02-calculadora-salario-flask`](./02-calculadora-salario-flask/)

## Tecnologias utilizadas

Ao longo das atividades deste diretório foram utilizadas:

- Java;
- Python;
- Flask;
- HTML;
- Android Studio;
- Android SDK;
- SQLite;
- SQLiteOpenHelper;
- Gradle.

## Conceitos praticados

As atividades permitiram aplicar conceitos relacionados a:

- desenvolvimento mobile;
- desenvolvimento web;
- back-end;
- persistência de dados;
- formulários e requisições;
- validação de entradas;
- organização de aplicações;
- utilização de frameworks e ferramentas de desenvolvimento.

## Estrutura

```text
frameworks-para-desenvolvimento/
├── 01-android-cadastro-produtos/
│   ├── app/
│   ├── gradle/
│   ├── README.md
│   └── ...
│
├── 02-calculadora-salario-flask/
│   ├── templates/
│   │   └── form.html
│   ├── app.py
│   └── README.md
│
└── README.md
```

Cada atividade possui seu próprio `README.md`, contendo informações específicas sobre objetivo, implementação, funcionamento, testes e instruções de execução.

## Contexto acadêmico

As atividades foram desenvolvidas em **2026** durante a graduação em **Análise e Desenvolvimento de Sistemas**.

Este diretório faz parte da organização das atividades acadêmicas selecionadas para o portfólio, preservando as implementações realizadas durante a disciplina e documentando os conceitos praticados em cada atividade.