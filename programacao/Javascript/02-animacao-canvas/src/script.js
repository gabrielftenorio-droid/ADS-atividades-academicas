const canvas = document.getElementById("meuCanvas");
const ctx = canvas.getContext("2d");

const particulas = [
    {
        x: 100,
        y: 100,
        raio: 20,
        velocidadeX: 2,
        velocidadeY: 1.5,
        matiz: 0
    },
    {
        x: 300,
        y: 200,
        raio: 30,
        velocidadeX: -1.5,
        velocidadeY: 2,
        matiz: 220
    },
    {
        x: 500,
        y: 150,
        raio: 25,
        velocidadeX: 2,
        velocidadeY: -1,
        matiz: 120
    }
];

function desenharParticula(particula) {
    ctx.beginPath();

    ctx.arc(
        particula.x,
        particula.y,
        particula.raio,
        0,
        Math.PI * 2
    );

    ctx.fillStyle = `hsl(${particula.matiz}, 85%, 60%)`;
    ctx.fill();
}

function atualizar() {

    particulas.forEach(function(particula) {

        particula.x += particula.velocidadeX;
        particula.y += particula.velocidadeY;

        if (
            particula.x + particula.raio > canvas.width ||
            particula.x - particula.raio < 0
        ) {
            particula.velocidadeX *= -1;
        }

        if (
            particula.y + particula.raio > canvas.height ||
            particula.y - particula.raio < 0
        ) {
            particula.velocidadeY *= -1;
        }

        particula.matiz = (particula.matiz + 1) % 360;
    });
}

function animar() {

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    atualizar();

    particulas.forEach(function(particula) {
        desenharParticula(particula);
    });

    requestAnimationFrame(animar);
}

canvas.addEventListener("click", function(event) {

    const rect = canvas.getBoundingClientRect();

    const mouseX = (event.clientX - rect.left) *
        (canvas.width / rect.width);

    const mouseY = (event.clientY - rect.top) *
        (canvas.height / rect.height);

    let particulaSelecionada = null;
    let menorDistancia = Infinity;

    particulas.forEach(function(particula) {

        const dx = mouseX - particula.x;
        const dy = mouseY - particula.y;

        const distancia = Math.sqrt(dx * dx + dy * dy);

        if (
            distancia <= particula.raio + 15 &&
            distancia < menorDistancia
        ) {
            menorDistancia = distancia;
            particulaSelecionada = particula;
        }
    });

    if (particulaSelecionada) {

        particulaSelecionada.matiz =
            Math.floor(Math.random() * 360);

        console.log("Cor da partícula alterada!");
    }
});

animar();
