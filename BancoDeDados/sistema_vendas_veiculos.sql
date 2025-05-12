-- Criação da tabela 'clientes' para armazenar informações sobre os clientes
CREATE TABLE clientes(
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,  -- Identificador único do cliente (auto incrementa)
    cpf VARCHAR(14) UNIQUE NOT NULL,            -- CPF do cliente, único e não nulo
    nome VARCHAR(100) NOT NULL,                 -- Nome do cliente, obrigatório
    email VARCHAR(100),                         -- Email do cliente (opcional)
    telefone VARCHAR(20),                       -- Telefone do cliente (opcional)
    cidade VARCHAR(50),                         -- Cidade onde o cliente reside (opcional)
    idade INT                                   -- Idade do cliente (opcional)
);

-- Criação da tabela 'veiculos' para armazenar informações sobre os veículos disponíveis
CREATE TABLE veiculos(
    id_veiculo INT PRIMARY KEY AUTO_INCREMENT,  -- Identificador único do veículo (auto incrementa)
    chassi VARCHAR(20) UNIQUE NOT NULL,         -- Chassi do veículo, único e não nulo
    modelo VARCHAR(50) NOT NULL,                -- Modelo do veículo, obrigatório
    marca VARCHAR(50) NOT NULL,                 -- Marca do veículo, obrigatório
    ano INT,                                    -- Ano do veículo (opcional)
    preco DECIMAL(10,2),                        -- Preço do veículo, com 2 casas decimais
    cor VARCHAR(30),                            -- Cor do veículo (opcional)
    vendido BOOLEAN DEFAULT FALSE              -- Indica se o veículo foi vendido, padrão é FALSE
);

-- Criação da tabela 'vendas' que armazena informações sobre as transações de venda
CREATE TABLE vendas (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,   -- Identificador único da venda (auto incrementa)
    id_cliente INT,                             -- Referência ao cliente que fez a compra
    id_veiculo INT,                             -- Referência ao veículo comprado
    data_venda DATE,                            -- Data da venda
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),  -- Relacionamento com a tabela 'clientes'
    FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo)   -- Relacionamento com a tabela 'veiculos'
);

-- Inserção de dados na tabela 'clientes'
INSERT INTO clientes (cpf, nome, email, telefone, cidade, idade) VALUES
('111.111.111-11', 'João Silva', 'joao@email.com', '11999999999', 'São Paulo', 35),
('222.222.222-22', 'Ana Lima', 'ana@email.com', '11988888888', 'Campinas', 28),
('333.333.333-33', 'Carlos Souza', 'carlos@email.com', '11977777777', 'Sorocaba', 42),
('444.444.444-44', 'Bruna Dias', 'bruna@email.com', '11966666666', 'Jundiaí', 31),
('555.555.555-55', 'Tiago Ramos', 'tiago@email.com', '11955555555', 'Santos', 50),
('666.666.666-66', 'Lara Monteiro', 'lara@email.com', '11944444444', 'Guarulhos', 27),
('777.777.777-77', 'Marcos Paulo', 'marcos@email.com', '11933333333', 'São Paulo', 29),
('888.888.888-88', 'Beatriz Leal', 'beatriz@email.com', '11922222222', 'Campinas', 33),
('999.999.999-99', 'Rafael Nunes', 'rafael@email.com', '11911111111', 'Osasco', 38),
('000.000.000-00', 'Fernanda Rocha', 'fernanda@email.com', '11900000000', 'Sorocaba', 45);

-- Inserção de dados na tabela 'veiculos'
INSERT INTO veiculos (chassi, modelo, marca, ano, preco, cor) VALUES
('CH001', 'Civic', 'Honda', 2020, 95000.00, 'Preto'),
('CH002', 'Corolla', 'Toyota', 2021, 98000.00, 'Branco'),
('CH003', 'Onix', 'Chevrolet', 2019, 65000.00, 'Prata'),
('CH004', 'HB20', 'Hyundai', 2020, 72000.00, 'Vermelho'),
('CH005', 'Gol', 'Volkswagen', 2018, 58000.00, 'Cinza'),
('CH006', 'Argo', 'Fiat', 2021, 70000.00, 'Azul'),
('CH007', 'Ka', 'Ford', 2019, 60000.00, 'Branco'),
('CH008', 'Tracker', 'Chevrolet', 2022, 120000.00, 'Preto'),
('CH009', 'Renegade', 'Jeep', 2021, 110000.00, 'Verde'),
('CH010', 'Fusion', 'Ford', 2017, 85000.00, 'Prata');

-- Exercício 1: Atualiza o telefone de um cliente específico (Carlos Souza)
UPDATE clientes SET telefone = '11988887777' WHERE cpf = '333.333.333-33';

-- Exercício 2: Marca o veículo com chassi 'CH001' como vendido
UPDATE veiculos SET vendido = TRUE WHERE chassi = 'CH001';

-- Exercício 3: Registra uma venda do cliente com ID 1 (João Silva) e veículo com ID 1 (Civic)
INSERT INTO vendas (id_cliente, id_veiculo, data_venda) VALUES (1, 1, '2025-05-05');

-- Exercício 4: Aplica um aumento de 10% no preço de todos os veículos da marca 'Chevrolet'
UPDATE veiculos SET preco = preco * 1.10 WHERE marca = 'Chevrolet';

-- Exercício 5: Atualiza a cidade de todos os clientes com mais de 40 anos para 'São Paulo'
UPDATE clientes SET cidade = 'São Paulo' WHERE idade > 40;

-- Exercício 6: Deleta o cliente com o CPF '000.000.000-00' (Fernanda Rocha)
DELETE FROM clientes WHERE cpf = '000.000.000-00';

-- Exercício 7: Deleta todos os veículos com ano anterior a 2020
DELETE FROM veiculos WHERE ano < 2020;

-- Exercício 8: Atualiza a cor de todos os veículos da marca 'Ford' para 'Grafite'
UPDATE veiculos SET cor = 'Grafite' WHERE marca = 'Ford';

-- Exercício 9: Deleta todas as vendas feitas antes de 2024
DELETE FROM vendas WHERE data_venda < '2024-01-01';

-- Exercício 10: Limpa completamente a tabela 'vendas', excluindo todos os registros
TRUNCATE TABLE vendas;
