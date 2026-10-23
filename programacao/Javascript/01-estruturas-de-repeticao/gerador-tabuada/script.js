const campoNumero = document.getElementById("numero");
const botaoGerar = document.getElementById("gerar");
const areaResultado = document.getElementById("resultado");

botaoGerar.addEventListener("click", function () {
    const numero = Number(campoNumero.value);

    areaResultado.innerHTML = "";

    if (!Number.isInteger(numero) || numero < 1 || numero > 10) {
        areaResultado.innerHTML =
            '<p class="mensagem-erro">Digite um número inteiro de 1 a 10.</p>';
        return;
    }

    const titulo = document.createElement("h2");
    titulo.textContent = "Tabuada do " + numero;
    areaResultado.appendChild(titulo);

    for (let i = 1; i <= 10; i++) {
        const resultado = numero * i;
        const linha = document.createElement("p");

        linha.textContent = numero + " x " + i + " = " + resultado;
        areaResultado.appendChild(linha);
    }
});
