-- ✅ Criação do banco de dados
CREATE DATABASE LojaCarros;
USE LojaCarros;

-- ✅ Criação das tabelas
CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE Carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100),
    marca VARCHAR(50),
    ano INT,
    preco DECIMAL(10,2),
    vendido BOOLEAN DEFAULT FALSE
);

CREATE TABLE Vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    carro_id INT,
    data_venda DATE,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (carro_id) REFERENCES Carros(id)
);

-- ✅ Inserção de dados
INSERT INTO Clientes (nome, telefone) VALUES 
('João Silva', '11999999999'),
('Maria Oliveira', '21988887777');

INSERT INTO Carros (modelo, marca, ano, preco) VALUES 
('Corolla', 'Toyota', 2020, 95000.00),
('Civic', 'Honda', 2021, 105000.00);

-- ✅ Consulta simples (carros disponíveis)
SELECT * FROM Carros WHERE vendido = FALSE;

-- ✅ Atualização de dados (marcar carro como vendido)
UPDATE Carros SET vendido = TRUE WHERE id = 1;

-- ✅ Registrar venda
INSERT INTO Vendas (cliente_id, carro_id, data_venda) VALUES (1, 1, CURDATE());

-- ✅ Exclusão de dados (excluir cliente)
DELETE FROM Clientes WHERE id = 2;

-- ✅ Adição de coluna (cor do carro)
ALTER TABLE Carros ADD cor VARCHAR(30);

-- ✅ Remoção de coluna (cor do carro)
ALTER TABLE Carros DROP COLUMN cor;

-- ✅ Alteração de tipo de dados (preço com mais casas)
ALTER TABLE Carros MODIFY preco DECIMAL(12,2);

-- ✅ Renomear tabela
RENAME TABLE Carros TO Veiculos;

-- ✅ Exclusão de tabela
DROP TABLE Vendas;

-- ✅ Exclusão do banco de dados
-- DROP DATABASE LojaCarros;
