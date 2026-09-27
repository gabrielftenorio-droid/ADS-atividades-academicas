# Sistema de Gerenciamento de Livros

Atividade acadêmica desenvolvida em Python com o objetivo de praticar conceitos de programação por meio da criação de um sistema simples para gerenciamento de livros.

O programa permite cadastrar livros, visualizar os livros cadastrados, realizar buscas por título e gerar um gráfico com a quantidade de livros por gênero.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastro de livros com título, autor, gênero e quantidade disponível;
- Listagem dos livros cadastrados;
- Busca de livros pelo título;
- Exibição da quantidade de livros por gênero em um gráfico;
- Menu interativo executado pelo terminal.

## Conceitos praticados

Durante o desenvolvimento da atividade foram utilizados conceitos como:

- Classes e objetos;
- Funções;
- Listas;
- Dicionários;
- Estruturas condicionais;
- Estruturas de repetição;
- Entrada e saída de dados;
- Manipulação de strings;
- Organização do programa em funções;
- Utilização de biblioteca externa.

## Estrutura do programa

A classe `Livro` representa os livros cadastrados no sistema e armazena as seguintes informações:

- Título;
- Autor;
- Gênero;
- Quantidade disponível.

Os objetos criados são armazenados em uma lista e utilizados pelas funções responsáveis pelo cadastro, listagem, busca e geração do gráfico.

## Tecnologias utilizadas

- Python
- Matplotlib

## Como executar

É necessário possuir o Python instalado no computador.

Instale a biblioteca Matplotlib:

```bash
python -m pip install matplotlib
```

Depois, execute o programa:

```bash
python main.py
```

## Menu do sistema

Ao executar o programa, o seguinte menu é apresentado:

```text
--- Sistema de Gerenciamento de Livros ---
1. Cadastrar novo livro
2. Listar todos os livros
3. Buscar livro por título
4. Gerar gráfico de livros por gênero
5. Sair
```

O usuário pode escolher uma das opções para acessar as funcionalidades disponíveis.

## Exemplo de cadastro

```text
Escolha uma opção: 1
Digite o título do livro: Dom Quixote de La Mancha
Digite o autor do livro: Miguel de Cervantes
Digite o gênero do livro: Romance
Digite a quantidade disponível: 5
Livro 'Dom Quixote de La Mancha' cadastrado com sucesso!
```

## Gráfico por gênero

O sistema utiliza a biblioteca Matplotlib para gerar um gráfico de barras com a quantidade de livros disponíveis agrupada por gênero.

Os dados utilizados no gráfico são obtidos a partir dos livros cadastrados durante a execução do programa.

## Estrutura dos arquivos

```text
01-sistema-gerenciamento-livros/
├── main.py
└── README.md
```

## Contexto acadêmico

Este projeto foi desenvolvido como atividade acadêmica durante a graduação em Análise e Desenvolvimento de Sistemas.

A atividade teve como objetivo aplicar conceitos de programação em Python na implementação de um sistema de gerenciamento de livros, incluindo cadastro, consulta e representação gráfica dos dados.