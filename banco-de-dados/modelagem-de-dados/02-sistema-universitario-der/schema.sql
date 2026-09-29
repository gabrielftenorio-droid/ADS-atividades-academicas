CREATE TABLE curso (
    codigo_curso INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria_total INTEGER NOT NULL
);

CREATE TABLE aluno (
    ra INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    codigo_curso INTEGER NOT NULL,

    FOREIGN KEY (codigo_curso)
        REFERENCES curso(codigo_curso)
);

CREATE TABLE departamento (
    codigo_departamento INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sigla VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE professor (
    matricula INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    titulacao VARCHAR(50) NOT NULL,
    codigo_departamento INTEGER NOT NULL,

    FOREIGN KEY (codigo_departamento)
        REFERENCES departamento(codigo_departamento)
);

CREATE TABLE disciplina (
    codigo_disciplina INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INTEGER NOT NULL,
    periodo INTEGER NOT NULL,
    codigo_curso INTEGER NOT NULL,
    matricula_professor INTEGER NOT NULL,

    FOREIGN KEY (codigo_curso)
        REFERENCES curso(codigo_curso),

    FOREIGN KEY (matricula_professor)
        REFERENCES professor(matricula)
);

CREATE TABLE historico_matricula (
    ra_aluno INTEGER NOT NULL,
    codigo_disciplina INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    semestre INTEGER NOT NULL,
    nota_final DECIMAL(4,2),
    frequencia DECIMAL(5,2),

    PRIMARY KEY (
        ra_aluno,
        codigo_disciplina,
        ano,
        semestre
    ),

    FOREIGN KEY (ra_aluno)
        REFERENCES aluno(ra),

    FOREIGN KEY (codigo_disciplina)
        REFERENCES disciplina(codigo_disciplina),

    CHECK (nota_final BETWEEN 0 AND 10),
    CHECK (frequencia BETWEEN 0 AND 100),
    CHECK (semestre IN (1, 2))
);

CREATE TABLE disciplina_prerequisito (
    codigo_disciplina INTEGER NOT NULL,
    codigo_prerequisito INTEGER NOT NULL,

    PRIMARY KEY (
        codigo_disciplina,
        codigo_prerequisito
    ),

    FOREIGN KEY (codigo_disciplina)
        REFERENCES disciplina(codigo_disciplina),

    FOREIGN KEY (codigo_prerequisito)
        REFERENCES disciplina(codigo_disciplina),

    CHECK (codigo_disciplina <> codigo_prerequisito)
);

CREATE TABLE bolsa (
    id_bolsa INTEGER PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    ra_aluno INTEGER NOT NULL,

    FOREIGN KEY (ra_aluno)
        REFERENCES aluno(ra),

    CHECK (valor >= 0)
);