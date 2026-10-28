const botoes = document.querySelectorAll('.btn-jogada');
const mensagem = document.getElementById('mensagem');
const placar = document.getElementById('placar');
const btnReiniciar = document.getElementById('reiniciar');

let pontosJogador = 0;
let pontosComputador = 0;
const opcoes = ['pedra', 'papel', 'tesoura'];

botoes.forEach(botao => {
    botao.addEventListener('click', (evento) => {
        jogar(evento.target.id);
    });
});

btnReiniciar.addEventListener('click', () => {
    pontosJogador = 0;
    pontosComputador = 0;
    atualizarPlacar();
    mensagem.textContent = "Aguardando jogada...";
    btnReiniciar.classList.add('oculto');
});

function jogar(escolhaJogador) {
    const escolhaComputador = opcoes[Math.floor(Math.random() * 3)];
    
    if (escolhaJogador === escolhaComputador) {
        mensagem.textContent = `Empate! Ambos escolheram ${escolhaJogador}.`;
    } else if (
        (escolhaJogador === 'pedra' && escolhaComputador === 'tesoura') ||
        (escolhaJogador === 'papel' && escolhaComputador === 'pedra') ||
        (escolhaJogador === 'tesoura' && escolhaComputador === 'papel')
    ) {
        mensagem.textContent = `Vitória! ${escolhaJogador} ganha de ${escolhaComputador}.`;
        pontosJogador++;
    } else {
        mensagem.textContent = `Derrota! ${escolhaComputador} ganha de ${escolhaJogador}.`;
        pontosComputador++;
    }
    
    atualizarPlacar();
    btnReiniciar.classList.remove('oculto');
}

function atualizarPlacar() {
    placar.textContent = `Jogador ${pontosJogador} x ${pontosComputador} Computador`;
}