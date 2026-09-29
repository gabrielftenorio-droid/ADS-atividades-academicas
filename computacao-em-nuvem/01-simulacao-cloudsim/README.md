# Simulação de Computação em Nuvem com CloudSim

Atividade prática desenvolvida na disciplina de **Computação em Nuvem**, durante a graduação em Análise e Desenvolvimento de Sistemas.

A prática teve como objetivo configurar um ambiente de simulação utilizando **Java**, **Apache NetBeans** e **CloudSim**, permitindo executar e observar um exemplo básico de infraestrutura de computação em nuvem.

## Objetivo

Preparar um ambiente Java capaz de executar uma simulação utilizando o CloudSim, trabalhando com:

- instalação e verificação do JDK;
- configuração do Apache NetBeans;
- organização dos arquivos do CloudSim;
- utilização de uma biblioteca externa em formato JAR;
- execução de uma simulação;
- observação de elementos como datacenter, máquina virtual e tarefa computacional.

## Tecnologias e ferramentas utilizadas

| Tecnologia / Ferramenta | Utilização |
|---|---|
| Java | Linguagem utilizada pelo CloudSim |
| JDK | Compilação e execução da aplicação Java |
| Apache NetBeans | Ambiente de desenvolvimento |
| CloudSim | Framework utilizado para simulação |
| `cloudsim-3.0.3.jar` | Biblioteca adicionada ao projeto |

## Preparação do ambiente

Inicialmente, foi instalado e verificado o **Java Development Kit (JDK)**.

A disponibilidade do ambiente Java e do compilador foi conferida pelo Prompt de Comando utilizando:

```bash
java -version
javac -version
```

Após essa verificação, foi instalado o **Apache NetBeans**, utilizado para organizar e executar o projeto Java.

## Configuração do CloudSim

Os arquivos do CloudSim foram baixados e extraídos em uma pasta local.

Dentro da estrutura disponibilizada pelo framework foi localizado o arquivo:

```text
CloudSimExample1.java
```

Esse arquivo corresponde a um exemplo básico fornecido pelo próprio CloudSim e foi utilizado na atividade sem alteração de sua lógica original.

## Criação do projeto

No Apache NetBeans foi criado um projeto Java denominado:

```text
Redes
```

Foi utilizada uma estrutura de projeto **Java com Ant**.

Dentro do projeto foi criado o pacote:

```text
org.cloudbus.cloudsim.examples
```

O arquivo `CloudSimExample1.java` foi então incluído nesse pacote.

## Configuração da biblioteca

Para que as classes utilizadas pelo exemplo fossem reconhecidas, a biblioteca:

```text
cloudsim-3.0.3.jar
```

foi adicionada à seção de bibliotecas do projeto.

Após essa configuração, as dependências utilizadas pelo exemplo passaram a ser reconhecidas corretamente pelo ambiente de desenvolvimento.

## Execução da simulação

Com o ambiente configurado, o `CloudSimExample1.java` foi executado pelo Apache NetBeans.

A saída da execução permitiu observar o processamento de um **Cloudlet** dentro do ambiente simulado.

Entre os resultados apresentados estavam:

```text
SUCCESS
CloudSimExample1 finished!
BUILD SUCCESSFUL
```

O status `SUCCESS` indicou que a tarefa simulada foi processada corretamente.

A execução também apresentou a associação do Cloudlet a elementos da simulação, incluindo um **datacenter** e uma **máquina virtual**.

## Conceitos trabalhados

Durante a atividade foram explorados conceitos relacionados a:

```text
Computação em Nuvem
│
├── Simulação de infraestrutura
│
├── Datacenter
│
├── Máquina Virtual
│
├── Cloudlet
│
├── Java
│   └── Bibliotecas externas
│
└── CloudSim
    └── Execução de cenários simulados
```

Além dos conceitos relacionados à nuvem, a prática também envolveu configuração de dependências Java e utilização de uma biblioteca externa em um ambiente de desenvolvimento.

## Resultado

A configuração do ambiente foi concluída com sucesso.

Após a inclusão da biblioteca `cloudsim-3.0.3.jar`, o NetBeans reconheceu as classes necessárias e o exemplo pôde ser executado.

A simulação terminou com o Cloudlet apresentando status `SUCCESS` e com a indicação `BUILD SUCCESSFUL`, confirmando a execução do exemplo sem erros.

## Sobre o código utilizado

O arquivo `CloudSimExample1.java` utilizado nesta atividade faz parte dos exemplos disponibilizados pelo **CloudSim**.

Durante a atividade acadêmica, esse exemplo foi utilizado sem alterações em sua lógica original.

Por esse motivo, o código-fonte do exemplo não é apresentado neste diretório como uma implementação autoral. O foco deste registro de portfólio está na **configuração do ambiente, integração da biblioteca, execução da simulação e compreensão dos conceitos envolvidos**.

## Contexto acadêmico

Atividade desenvolvida em 2026 na disciplina de **Computação em Nuvem**, na unidade de Fundamentos de Computação em Nuvem.

O trabalho original abordou **Modelos de Implantação em Computação em Nuvem** e utilizou o CloudSim como ferramenta prática para relacionar os conceitos estudados com a simulação de recursos computacionais.