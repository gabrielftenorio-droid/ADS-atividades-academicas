# Segurança em Nuvem com SSL/TLS e HTTPS

Atividade prática desenvolvida na disciplina de **Computação em Nuvem**, durante a graduação em Análise e Desenvolvimento de Sistemas.

A prática teve como objetivo aplicar conceitos relacionados à segurança de aplicações hospedadas em nuvem, utilizando uma hospedagem online para verificar o funcionamento de **SSL/TLS**, certificados digitais e **HTTPS**.

Também foi configurado um redirecionamento de HTTP para HTTPS e publicada uma página web para realização dos testes.

## Objetivo

Explorar mecanismos utilizados para proteger a comunicação entre o navegador e uma aplicação hospedada na internet.

Durante a atividade foram trabalhados:

- hospedagem de uma aplicação em ambiente de nuvem;
- criação e utilização de subdomínio;
- SSL/TLS;
- certificados digitais;
- HTTPS;
- validação do certificado pelo navegador;
- comparação entre HTTP e HTTPS;
- redirecionamento para HTTPS;
- configuração de `.htaccess`;
- publicação de uma página HTML.

## Ambiente de hospedagem

Para a realização da atividade foi criada uma hospedagem específica no **InfinityFree**.

O subdomínio utilizado durante a prática foi:

```text
segurancaads.lovestoblog.com
```

A hospedagem foi utilizada exclusivamente para os procedimentos relacionados à atividade de segurança e privacidade em nuvem.

## Verificação do SSL

O roteiro da atividade previa um processo de solicitação e instalação de um certificado SSL.

Entre as etapas previstas estavam:

```text
Solicitação do certificado
        │
        ▼
Validação por registros CNAME
        │
        ▼
Instalação do certificado
```

Entretanto, durante a execução da atividade foi encontrada uma diferença entre o procedimento apresentado no roteiro e o funcionamento da plataforma naquele momento.

Ao tentar solicitar um novo certificado, o InfinityFree informou que certificados SSL personalizados não eram mais suportados para aquele tipo de subdomínio gratuito porque o SSL já era disponibilizado por padrão.

Por esse motivo, não foi necessário realizar manualmente as etapas de solicitação, configuração de registros CNAME e instalação individual do certificado.

A atividade foi adaptada para verificar o certificado já disponibilizado pela plataforma.

## Validação do HTTPS

Após identificar a disponibilidade do SSL, o site foi acessado diretamente utilizando:

```text
HTTPS
```

A página foi carregada normalmente e as informações de segurança apresentadas pelo navegador foram utilizadas para verificar a conexão.

O navegador indicou que a conexão estava protegida e que o certificado apresentado pelo site era válido.

## Análise do certificado

Os detalhes do certificado também foram consultados através do navegador.

Durante a verificação foram observadas informações relacionadas a:

- domínio;
- autoridade certificadora;
- período de validade;
- chave pública;
- impressões digitais do certificado.

Na consulta realizada durante a atividade, o certificado apresentado para `lovestoblog.com` indicava como autoridade emissora:

```text
ZeroSSL ECC DV SSL CA 2
```

A verificação permitiu observar informações que normalmente não ficam visíveis durante uma navegação comum.

## HTTP e HTTPS

Durante os testes foi percebida uma diferença importante.

O fato de existir um certificado válido não significava, por si só, que todo acesso ao site seria iniciado automaticamente através de HTTPS.

Inicialmente, ao acessar o endereço utilizando HTTP, o navegador chegou a apresentar uma indicação de conexão não segura.

A atividade permitiu distinguir dois procedimentos:

```text
Certificado SSL/TLS
        │
        └── possibilita uma conexão protegida
                    │
                    ▼
                  HTTPS


Redirecionamento
        │
        └── direciona uma requisição HTTP
                    │
                    ▼
                  HTTPS
```

## Redirecionamento para HTTPS

Para direcionar acessos iniciados por HTTP para HTTPS, foi criado um arquivo:

```text
.htaccess
```

O arquivo foi armazenado no diretório:

```text
htdocs
```

Nele foram adicionadas regras de reescrita destinadas a redirecionar o acesso realizado por HTTP para a versão HTTPS do endereço.

O conteúdo textual completo do `.htaccess` utilizado não é reproduzido neste repositório, pois o relatório disponível documenta sua configuração e seu resultado, mas não fornece integralmente o arquivo original em formato de código.

## Publicação da página web

Além das configurações relacionadas à segurança, foi criado um arquivo:

```text
index.html
```

A página recebeu o título:

```text
Segurança e Privacidade em Nuvem
```

O conteúdo abordava temas relacionados a:

- hospedagem em nuvem;
- proteção através de HTTPS;
- utilização de SSL/TLS.

O arquivo foi publicado no diretório `htdocs` da hospedagem, substituindo a página padrão inicialmente disponibilizada pelo serviço.

O código HTML completo não é reproduzido neste diretório porque o relatório registra a criação e publicação da página, mas não apresenta integralmente o código-fonte original.

## Teste final

Após a publicação da página e a configuração do `.htaccess`, foi realizado um novo teste iniciando o acesso através de HTTP.

O comportamento observado foi:

```text
Requisição HTTP
      │
      ▼
Acesso inicial
      │
      ▼
Redirecionamento
      │
      ▼
Conexão HTTPS
```

Ao final do carregamento, a barra de endereços apresentava:

```text
https://segurancaads.lovestoblog.com
```

O teste permitiu comparar o comportamento observado antes e depois da configuração do redirecionamento.

## Resultados

Ao final da atividade foram obtidos os seguintes resultados:

- hospedagem criada para realização da prática;
- página HTML própria publicada;
- SSL disponível para o subdomínio;
- certificado reconhecido como válido pelo navegador;
- conexão HTTPS testada;
- informações do certificado analisadas;
- comportamento do acesso HTTP observado;
- `.htaccess` configurado para redirecionamento;
- teste final realizado utilizando HTTPS.

A atividade também demonstrou, na prática, que a disponibilidade de um certificado e o redirecionamento das requisições para HTTPS são procedimentos relacionados, mas distintos.

## Conceitos trabalhados

```text
Segurança em Aplicações na Nuvem
│
├── SSL/TLS
│   ├── Criptografia da comunicação
│   └── Certificado digital
│
├── HTTPS
│   └── Comunicação protegida
│
├── Certificado
│   ├── Domínio
│   ├── Autoridade certificadora
│   └── Validade
│
└── Redirecionamento
    │
    ├── HTTP
    │    │
    │    ▼
    └── HTTPS
         │
         └── .htaccess
```

## Adaptação do procedimento

Um aspecto relevante da atividade foi a necessidade de adaptar o procedimento originalmente previsto.

O roteiro apresentava etapas para solicitação e instalação manual de um certificado SSL. Durante a execução, entretanto, a plataforma utilizada informou que o SSL já era fornecido por padrão para o subdomínio gratuito.

Em vez de registrar como realizadas etapas que não eram mais necessárias, a prática prosseguiu através da validação do certificado existente, dos testes de HTTPS e da configuração do redirecionamento.

Essa diferença entre o roteiro e a execução efetiva foi registrada no relatório acadêmico.

## Sobre os arquivos da atividade

A atividade envolveu a criação de:

```text
htdocs/
├── index.html
└── .htaccess
```

O relatório acadêmico documenta a criação, configuração e utilização desses arquivos, porém não contém o código-fonte integral de ambos em formato textual.

Por esse motivo, eles não foram reconstruídos neste diretório como se fossem os arquivos originais.

Caso os arquivos originais sejam recuperados posteriormente, poderão ser incorporados ao repositório preservando a implementação realizada durante a atividade.

## Contexto acadêmico

Atividade desenvolvida em 2026 na disciplina de **Computação em Nuvem**.

O trabalho pertence à unidade **Arquitetura de Aplicação em Nuvem**, na aula **Segurança e Privacidade em Nuvem**.

A prática relacionou hospedagem de aplicações com SSL/TLS, certificados digitais, HTTPS e redirecionamento de requisições.