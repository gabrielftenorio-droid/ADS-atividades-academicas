<?php
include('layouts/header.php');

$data_nascimento = $_POST['data_nascimento'];
$signos = simplexml_load_file("signos.xml");

$data = DateTime::createFromFormat('Y-m-d', $data_nascimento);
$anoReferencia = 2000;

$dataComparacao = DateTime::createFromFormat(
    'd/m/Y',
    $data->format('d/m') . '/' . $anoReferencia
);

$signoEncontrado = null;

foreach ($signos->signo as $signo) {
    $inicio = DateTime::createFromFormat(
        'd/m/Y',
        $signo->dataInicio . '/' . $anoReferencia
    );

    $fim = DateTime::createFromFormat(
        'd/m/Y',
        $signo->dataFim . '/' . $anoReferencia
    );

    if ($fim < $inicio) {
        if ($dataComparacao >= $inicio || $dataComparacao <= $fim) {
            $signoEncontrado = $signo;
            break;
        }
    } else {
        if ($dataComparacao >= $inicio && $dataComparacao <= $fim) {
            $signoEncontrado = $signo;
            break;
        }
    }
}

$simbolos = [
    'Áries' => '♈',
    'Touro' => '♉',
    'Gêmeos' => '♊',
    'Câncer' => '♋',
    'Leão' => '♌',
    'Virgem' => '♍',
    'Libra' => '♎',
    'Escorpião' => '♏',
    'Sagitário' => '♐',
    'Capricórnio' => '♑',
    'Aquário' => '♒',
    'Peixes' => '♓'
];
?>

<body>
    <div class="container min-vh-100 d-flex align-items-center justify-content-center py-5">

        <div class="zodiac-card p-4 p-md-5 text-center">

            <?php if ($signoEncontrado): ?>

                <p class="zodiac-subtitle mb-3">
                    Resultado da consulta
                </p>

                <div class="zodiac-symbol mb-3">
                    <?php
                    echo $simbolos[(string) $signoEncontrado->signoNome];
                    ?>
                </div>

                <h1 class="mb-3 text-white">
                    Seu signo é
                </h1>

                <h2 class="display-4 sign-name mb-3">
                    <?php echo $signoEncontrado->signoNome; ?>
                </h2>

                <p class="zodiac-subtitle fs-5 mb-4">
                    <?php echo $signoEncontrado->descricao; ?>
                </p>

            <?php else: ?>

                <div class="alert alert-warning">
                    Não foi possível identificar o signo.
                </div>

            <?php endif; ?>

            <div class="d-grid mt-4">
                <a href="index.php"
                   class="btn btn-zodiac btn-lg">
                    Fazer nova consulta
                </a>
            </div>

        </div>

    </div>
</body>
</html>