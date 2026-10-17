CREATE TABLE Pessoa
(
cpfPessoa CHAR (11) NOT NULL ,
nomePessoa VARCHAR (60) NOT NULL ,
dataNascimentoPessoa DATE NOT NULL,
PRIMARY KEY (cpfPessoa),
FOREIGN KEY (cpfPessoa) REFERENCES EnderecoPessoa (cpfPessoaEndereco)
);
