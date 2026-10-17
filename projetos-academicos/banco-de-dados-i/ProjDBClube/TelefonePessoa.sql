CREATE TABLE TelefonePessoa
(
cpfPessoaTelefone CHAR (11) NOT NULL ,
dddTelefone CHAR (2) NOT NULL ,
nroTelefone CHAR (10) NOT NULL,
PRIMARY KEY (cpfPessoaTelefone, dddTelefone, nroTelefone),
FOREIGN KEY (cpfPessoaTelefone) REFERENCES Pessoa (cpfPessoa)
);