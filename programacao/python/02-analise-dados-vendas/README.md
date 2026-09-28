# Análise de Dados de Vendas com Python

Atividade acadêmica desenvolvida em Python com o objetivo de praticar a criação, consulta, tratamento, análise e visualização de dados de vendas.

O projeto utiliza SQLite para armazenamento dos dados, Pandas para manipulação e análise e Matplotlib e Seaborn para geração das visualizações.

## Funcionalidades

O programa realiza as seguintes etapas:

- Criação de um banco de dados SQLite;
- Criação da tabela de vendas;
- Inserção de dados de vendas;
- Consulta dos registros armazenados no banco;
- Carregamento dos dados em um DataFrame;
- Conversão e tratamento da coluna de datas;
- Agrupamento das vendas por categoria;
- Agrupamento das vendas por mês;
- Cálculo do valor total de vendas;
- Geração de gráfico de barras por categoria;
- Geração de gráfico de linha com as vendas ao longo do ano.

## Tecnologias utilizadas

- Python
- SQLite
- Pandas
- Matplotlib
- Seaborn

## Estrutura dos dados

O banco de dados utiliza a tabela `vendas1`, composta pelos seguintes campos:

| Campo | Descrição |
| --- | --- |
| `id_venda` | Identificador da venda |
| `data_venda` | Data em que a venda foi realizada |
| `produto` | Produto vendido |
| `categoria` | Categoria do produto |
| `valor_venda` | Valor da venda |

A atividade utiliza 14 registros de exemplo distribuídos ao longo do ano de 2023.

## Análise dos dados

Após a consulta ao banco SQLite, os registros são carregados em um DataFrame do Pandas.

A coluna `data_venda` é convertida para o formato de data utilizando `pd.to_datetime()`.

Em seguida, são realizadas duas análises principais.

### Vendas por categoria

Os valores das vendas são agrupados pela coluna `categoria` e somados para identificar o total vendido em cada categoria.

As categorias presentes na base são:

- Eletrônicos;
- Roupas;
- Livros.

Os resultados são apresentados em um gráfico de barras.

### Vendas por mês

O mês é extraído da coluna `data_venda` e utilizado para agrupar os valores das vendas.

O resultado permite visualizar a variação do total de vendas ao longo dos 12 meses do ano e é apresentado em um gráfico de linha.

## Visualizações

O projeto gera duas visualizações:

1. **Total de Vendas por Categoria** — gráfico de barras criado com Seaborn e Matplotlib.
2. **Vendas Totais ao Longo do Ano** — gráfico de linha representando os valores de vendas por mês.

## Estrutura do projeto

```text
02-analise-dados-vendas/
├── analise_vendas.py
└── README.md
```

O arquivo `dados_vendas.db` é criado localmente durante a execução do programa e não é versionado no repositório.

## Como executar

É necessário possuir o Python instalado.

Instale as bibliotecas utilizadas pelo projeto:

```bash
python -m pip install pandas matplotlib seaborn
```

Depois execute:

```bash
python analise_vendas.py
```

Durante a execução, o programa cria o banco de dados quando necessário, realiza as análises e apresenta os gráficos.

## Ajuste realizado

A versão acadêmica original realizava a inserção dos registros sempre que o código era executado.

Durante a organização da atividade para este repositório, a inicialização do banco foi ajustada para verificar se a tabela já possui registros antes de inserir os dados de exemplo.

Esse ajuste evita a duplicação dos registros em execuções posteriores, preservando a estrutura e a proposta original da atividade.

## Contexto acadêmico

Este projeto foi desenvolvido como atividade acadêmica durante a graduação em Análise e Desenvolvimento de Sistemas.

A atividade teve como objetivo aplicar conceitos relacionados a banco de dados, manipulação e análise de dados com Python e representação gráfica dos resultados.