CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE livros (
    titulo VARCHAR(255),
    autor VARCHAR(255)
);

SELECT * FROM livros;


CREATE TABLE unidades (
    nome_unidade VARCHAR(255),
    endereco VARCHAR(255)
);

SELECT * FROM unidades;

CREATE TABLE emprestimos (
    livro VARCHAR(255),
    usuario VARCHAR(255),
    data_emprestimo DATE
);

SELECT * FROM emprestimos;