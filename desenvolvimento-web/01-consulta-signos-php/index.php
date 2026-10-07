<?php include('layouts/header.php'); ?>

<body>
    <div class="container min-vh-100 d-flex align-items-center justify-content-center py-5">

        <div class="zodiac-card p-4 p-md-5">
            <div class="text-center mb-4">
                <div class="zodiac-symbol mb-3">✦</div>

                <h1 class="zodiac-title">
                    Descubra seu signo
                </h1>

                <p class="zodiac-subtitle mt-3">
                    Informe sua data de nascimento e descubra
                    qual signo do zodíaco corresponde a você.
                </p>
            </div>

            <form id="signo-form" method="POST" action="show_zodiac_sign.php">

                <div class="mb-4">
                    <label for="data_nascimento" class="form-label">
                        Data de nascimento
                    </label>

                    <input type="date"
                           class="form-control form-control-lg"
                           id="data_nascimento"
                           name="data_nascimento"
                           required>
                </div>

                <div class="d-grid">
                    <button type="submit"
                            class="btn btn-zodiac btn-lg">
                        Descobrir meu signo
                    </button>
                </div>

            </form>
        </div>

    </div>
</body>
</html>