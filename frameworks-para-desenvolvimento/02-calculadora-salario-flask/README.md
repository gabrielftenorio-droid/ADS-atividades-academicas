# Calculadora de Salário Líquido com Flask

Aplicação web desenvolvida como atividade prática da disciplina **Framework para Desenvolvimento de Software**, do curso de Análise e Desenvolvimento de Sistemas.

O projeto utiliza **Python e Flask** para receber dados por meio de um formulário HTML, realizar um cálculo simplificado de salário líquido no back-end e apresentar o resultado ao usuário.

## Objetivo

A atividade teve como objetivo aplicar conceitos introdutórios de desenvolvimento web com Flask, trabalhando a comunicação entre uma interface HTML e o processamento realizado no servidor.

Durante o desenvolvimento foram praticados:

- criação de uma aplicação Flask;
- definição de rotas;
- renderização de template HTML;
- envio de dados por formulário;
- utilização do método HTTP `POST`;
- acesso aos dados enviados pelo usuário;
- implementação de regras de cálculo;
- validação de entradas no back-end;
- tratamento de valores inválidos.

## Tecnologias utilizadas

- Python
- Flask
- HTML
- Jinja2
- ambiente virtual Python (`venv`)

## Estrutura da aplicação

O projeto possui uma estrutura simples:

```text
02-calculadora-salario-flask/
├── templates/
│   └── form.html
├── .gitignore
├── app.py
└── README.md
```

O ambiente virtual utilizado para executar o projeto não é versionado no repositório.

## Funcionamento

### Página inicial

A rota:

```text
/
```

renderiza o arquivo:

```text
templates/form.html
```

O formulário solicita:

- salário bruto;
- número de dependentes.

Ao selecionar **Calcular**, os dados são enviados utilizando o método `POST` para:

```text
/resultado
```

### Processamento

A rota `/resultado` recebe os valores enviados pelo formulário e realiza as validações e o cálculo no back-end.

O salário é convertido para `float` e o número de dependentes para `int`.

Caso os valores não possam ser convertidos, a aplicação retorna uma mensagem de erro.

## Regras utilizadas na atividade

Para fins didáticos, o exercício utiliza as seguintes regras simplificadas:

| Regra | Valor |
|---|---:|
| INSS | 8% do salário |
| IR | 15% para salário acima de R$ 2.500 |
| Valor por dependente | R$ 200 |

O cálculo implementado pode ser representado por:

```text
salário líquido = salário bruto - INSS - IR + valor dos dependentes
```

> **Importante:** essas regras fazem parte exclusivamente do exercício acadêmico e são simplificações utilizadas para praticar programação com Flask. O projeto não deve ser utilizado como calculadora trabalhista, previdenciária ou tributária real.

## Validações

A aplicação realiza validações no back-end antes de apresentar o resultado.

### Valores não numéricos

Caso os dados não possam ser convertidos para os tipos esperados, a aplicação retorna uma mensagem informando que devem ser inseridos valores válidos.

### Salário negativo

Valores de salário inferiores a zero são rejeitados.

### Número de dependentes negativo

A aplicação também impede a utilização de uma quantidade negativa de dependentes.

## Testes realizados

Durante a atividade acadêmica foram utilizados diferentes cenários para verificar o comportamento da aplicação.

| Salário bruto | Dependentes | Resultado esperado |
|---:|---:|---:|
| R$ 3.000,00 | 2 | R$ 2.710,00 |
| R$ 2.000,00 | 1 | R$ 2.040,00 |
| R$ 1.000,00 | 0 | R$ 920,00 |

Também foram considerados cenários inválidos:

| Entrada | Resultado |
|---|---|
| Salário `-500` | salário negativo rejeitado |
| Salário `abc` | valor inválido rejeitado |
| Dependentes `-1` | quantidade negativa rejeitada |

## Validação da implementação preservada

Após a recuperação da implementação acadêmica, o projeto foi executado novamente em ambiente virtual Python com Flask.

Foram verificados, entre outros, os seguintes casos:

```text
Salário bruto: 3000
Dependentes: 2
Resultado: R$ 2710,00
```

```text
Salário bruto: -500
Dependentes: 1
Resultado: salário negativo rejeitado
```

```text
Salário bruto: 2500
Dependentes: -1
Resultado: número de dependentes negativo rejeitado
```

Esses testes confirmaram o funcionamento da implementação preservada.

## Como executar

Com Python instalado, acesse a pasta do projeto e crie um ambiente virtual:

```bash
python -m venv .venv
```

### Windows PowerShell

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale o Flask:

```bash
python -m pip install Flask
```

Execute a aplicação:

```bash
python app.py
```

O servidor de desenvolvimento será iniciado localmente. A aplicação poderá então ser acessada pelo endereço exibido pelo Flask no terminal.

## Organização do código

### `app.py`

Contém:

- inicialização da aplicação Flask;
- rota da página inicial;
- rota responsável pelo processamento do formulário;
- conversão dos valores recebidos;
- validações;
- regras simplificadas de cálculo;
- retorno do resultado.

### `templates/form.html`

Contém o formulário HTML utilizado para informar o salário bruto e o número de dependentes.

## Contexto acadêmico

Projeto desenvolvido em **2026** como atividade prática da disciplina **Framework para Desenvolvimento de Software**, na unidade relacionada a frameworks destinados a servidores e desenvolvimento com Python.

A atividade teve como foco compreender o funcionamento básico de uma aplicação web utilizando Flask, incluindo rotas, formulários, requisições `POST`, processamento no back-end e validação de dados.

> Este diretório preserva a implementação realizada durante a atividade acadêmica. O ambiente virtual e outros arquivos locais necessários apenas ao ambiente de desenvolvimento não fazem parte do versionamento.