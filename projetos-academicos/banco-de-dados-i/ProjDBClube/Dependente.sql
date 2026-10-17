CREATE TABLE Dependente
(
cpfDependente CHAR (11) NOT NULL,
cpfTitularDependente CHAR (11) NOT NULL ,
grauParentesco SMALLINT NOT NULL,
PRIMARY KEY (cpfDependente, cpfTitularDependente),
FOREIGN KEY (cpfDependente) REFERENCES Pessoa (cpfPessoa),
FOREIGN KEY (cpfTitularDependente) REFERENCES Titular (cpfTitular),
FOREIGN KEY (grauParentesco) REFERENCES Parentesco (grauParentesco)
) ;