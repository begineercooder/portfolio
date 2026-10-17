CREATE TABLE EnderecoPessoa
(
cpfPessoaEndereco CHAR NOT NULL ,
logradouroEndereco VARCHAR (20) NOT NULL ,
nroEndereco CHAR (5) NOT NULL ,
complementoEndereco VARCHAR (20) NOT NULL ,
BairroEndereco VARCHAR (40) NOT NULL ,
cidadeEnderco VARCHAR (40) NOT NULL ,
ufEndereco CHAR (2) NOT NULL ,
cepEndereco CHAR (8) NOT NULL ,
siglaUfEndereco CHAR (2) NOT NULL,
PRIMARY KEY (cpfPessoaEndereco),
FOREIGN KEY (siglaUfEndereco) REFERENCES UfEndereco (siglaUf)
);
