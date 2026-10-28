# Jokenpô Interativo ✊✋✌️

## 📖 Sobre o Projeto
Este projeto é um jogo web clássico de Jokenpô (Pedra, Papel e Tesoura) desenvolvido como atividade prática para a disciplina de **Programação Orientada a Eventos** do curso de Análise e Desenvolvimento de Sistemas (ADS). 

O foco da aplicação foi consolidar conhecimentos em desenvolvimento Front-end, com ênfase na escuta de eventos do usuário, lógica condicional e manipulação direta do Document Object Model (DOM).

## 📜 Regras do Jogo
- **Pedra:** ganha da tesoura, perde para o papel.
- **Papel:** ganha da pedra, perde para a tesoura.
- **Tesoura:** ganha do papel, perde para a pedra.

## 🚀 Tecnologias Utilizadas
- **HTML5:** Estruturação semântica da interface.
- **CSS3:** Estilização, layout com Flexbox e eventos visuais de animação (`transition`, `:hover`).
- **JavaScript:** Lógica de decisão (`Math.random`, `if/else`), captura de cliques (`addEventListener`) e injeção de dados no DOM em tempo real (`classList`, `textContent`).

## ⚙️ Funcionalidades
- Escolha interativa de jogadas com feedback visual imediato.
- Motor de jogo que processa rodadas aleatórias do computador.
- Placar dinâmico que mantém o estado da pontuação sem recarregar a página.
- Sistema de reinício de partida ocultado/revelado dinamicamente.

## 📁 Estrutura de Arquivos
- `index.html`: Estrutura da página.
- `style.css`: Folhas de estilo e animações.
- `script.js`: Inteligência do jogo.
- `Relatorio_Aula_Pratica.pdf`: Documentação acadêmica completa da atividade.

## 🖥️ Como Executar
1. Clone este repositório em sua máquina local.
2. Abra a pasta do projeto em seu editor de código ou IDE favorita (Visual Studio Code, PyCharm, WebStorm, Sublime Text, etc.).
3. Abra o arquivo `index.html` diretamente no seu navegador web para iniciar o jogo.
4. *(Opcional)* Caso utilize o VS Code, você pode usar a extensão **Live Server** para rodar o projeto em um servidor local.