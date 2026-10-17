CREATE TABLE Titular
(
cpfTitular CHAR (11) NOT NULL,
cpfPessoaTitular CHAR (11) NOT NULL,
vlrMensalidade NUMERIC (10,2) NOT NULL,
PRIMARY KEY (cpfTitular),
FOREIGN KEY (cpfPessoaTitular) REFERENCES Pessoa (cpfPessoa)
);