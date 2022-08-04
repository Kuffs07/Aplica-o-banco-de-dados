-- Inserir na tabela bancodedados
INSERT INTO bancodedados(nome, email, senha, data_criacao) VALUES ('maria', 'maria@hotmail.com', '123321', '2022-08-04');
INSERT INTO bancodedados(nome, email, senha, data_criacao) VALUES('Lucas', 'Lucas@hotmail.com', '123', '2022-08-04');
INSERT INTO bancodedados(nome, email, senha, data_criacao) VALUES ('paulo', 'paulo@hotmail.com', '010101', '2022-08-04');
INSERT INTO bancodedados(nome, email, senha, data_criacao) VALUES ('pablo', 'pablo@hotmail.com', '123456', '2022-08-04');

-- Alterar dados da tabela
UPDATE bancodedados SET nome = 'Luiza', email = 'Luiza@hotmail.com', senha = '123', data_criaca = '2022-08-04' WHERE id_bancodedados = 1;

-- Deletar um usuario pelo ID
DELETE FROM bancodedados WHERE id_bancodedados = 4;

-- Mostrar todos usuarios
select * from bancodedados;