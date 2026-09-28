# Classificação de Espécies Iris com Machine Learning

Atividade acadêmica desenvolvida em Python com o objetivo de aplicar conceitos introdutórios de Machine Learning e redes neurais em um problema de classificação.

O projeto utiliza o conjunto de dados Iris, disponibilizado pelo Scikit-learn, para treinar uma rede neural capaz de classificar flores entre três espécies: setosa, versicolor e virginica.

A atividade foi originalmente desenvolvida no Google Colab e posteriormente organizada e testada em ambiente local para este repositório.

## Objetivo

O objetivo da atividade é percorrer etapas fundamentais de um projeto de aprendizado de máquina:

- Carregamento de um conjunto de dados;
- Separação entre dados de treino e teste;
- Normalização das características;
- Construção de uma rede neural;
- Treinamento do modelo;
- Avaliação do desempenho;
- Realização de previsões.

## Tecnologias utilizadas

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn

## Conjunto de dados

O projeto utiliza o dataset Iris disponível no Scikit-learn.

O conjunto de dados contém informações sobre flores de três espécies:

- setosa;
- versicolor;
- virginica.

Cada amostra possui quatro características utilizadas pelo modelo para realizar a classificação.

## Pré-processamento

Os dados são divididos entre treino e teste utilizando `train_test_split`.

A configuração utilizada na atividade é:

```python
test_size=0.3
random_state=42
stratify=y
```

Dessa forma, 70% dos dados são utilizados para treinamento e 30% para teste.

Em seguida, as características são normalizadas utilizando `StandardScaler`.

O ajuste do normalizador é realizado somente sobre os dados de treinamento, enquanto os dados de teste são transformados utilizando os parâmetros obtidos durante o treinamento.

## Modelo de rede neural

O modelo foi construído utilizando TensorFlow/Keras com a seguinte arquitetura:

```text
Entrada: 4 características

Camada oculta:
10 neurônios
Ativação ReLU

Camada oculta:
8 neurônios
Ativação ReLU

Camada de saída:
3 neurônios
Ativação Softmax
```

A camada de saída possui três neurônios, correspondentes às três espécies presentes no conjunto de dados.

## Compilação do modelo

O modelo utiliza:

- Otimizador: Adam;
- Função de perda: `sparse_categorical_crossentropy`;
- Métrica de avaliação: `accuracy`.

## Treinamento

O treinamento é realizado utilizando:

```text
Épocas: 50
Batch size: 8
```

Durante o treinamento, os dados de teste também são utilizados como conjunto de validação para acompanhar a evolução da perda e da acurácia.

## Avaliação

Após o treinamento, o modelo é avaliado utilizando o conjunto de teste.

Em uma das execuções realizadas durante a organização da atividade em ambiente local, foi obtido o seguinte resultado:

```text
Loss (Erro): 0.3509
Acurácia: 84.44%
```

Os resultados podem apresentar variações entre execuções devido ao processo de treinamento da rede neural.

## Previsões

Após a avaliação, o modelo realiza previsões sobre os dados de teste.

A saída da rede neural contém as probabilidades associadas às três classes. A função `argmax` do NumPy é utilizada para identificar a classe com maior probabilidade.

O programa apresenta as primeiras classes previstas e seus respectivos valores reais.

Também são exibidos exemplos utilizando os nomes das espécies, permitindo comparar diretamente a previsão do modelo com a classificação correta.

## Estrutura do projeto

```text
03-classificacao-iris-machine-learning/
├── classificacao_iris.py
└── README.md
```

O ambiente virtual utilizado para execução local não é versionado no repositório.

## Como executar

Para reproduzir a execução local, é recomendado utilizar um ambiente virtual com uma versão do Python compatível com o TensorFlow.

Crie e ative o ambiente virtual e instale as dependências:

```bash
python -m pip install tensorflow pandas numpy scikit-learn
```

Depois execute:

```bash
python classificacao_iris.py
```

O programa irá carregar o dataset Iris, preparar os dados, treinar a rede neural durante 50 épocas, avaliar o modelo e apresentar exemplos de previsões.

## Organização para o repositório

A atividade foi originalmente desenvolvida e executada no Google Colab.

Durante a organização para este repositório, o código foi recuperado a partir do trabalho acadêmico e preparado para execução local, preservando a estrutura, a arquitetura da rede neural e os principais parâmetros utilizados na atividade original.

Para a execução local, foi utilizado um ambiente virtual com Python 3.13 e as dependências necessárias ao projeto.

## Contexto acadêmico

Este projeto foi desenvolvido como atividade acadêmica durante a graduação em Análise e Desenvolvimento de Sistemas.

A proposta foi aplicar conceitos introdutórios de Machine Learning, passando pelas etapas de preparação dos dados, construção de uma rede neural, treinamento, avaliação e realização de previsões.