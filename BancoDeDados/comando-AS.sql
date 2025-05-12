-- Aula Comando AS ( ALIAS ) 
-- Criação da tabela 'produtos' com as colunas id_produto, nome, preco e categoria
CREATE TABLE produtos (
    id_produto INT PRIMARY KEY,  -- Identificador único para cada produto
    nome VARCHAR(100),           -- Nome do produto (máximo de 100 caracteres)
    preco DECIMAL(10,2),         -- Preço do produto com 2 casas decimais
    categoria VARCHAR(50)        -- Categoria do produto (máximo de 50 caracteres)
);

-- Inserção de dados na tabela 'produtos'
INSERT INTO produtos VALUES
(1, 'Notebook', 3500.00, 'Informática'),  -- Produto 1: Notebook, preço 3500.00, categoria Informática
(2, 'Mouse', 80.00, 'Acessórios'),       -- Produto 2: Mouse, preço 80.00, categoria Acessórios
(3, 'Teclado', 150.00, 'Acessórios'),    -- Produto 3: Teclado, preço 150.00, categoria Acessórios
(4, 'Monitor', 1200.00, 'Informática'),  -- Produto 4: Monitor, preço 1200.00, categoria Informática
(5, 'Cadeira Gamer', 850.00, 'Móveis'); -- Produto 5: Cadeira Gamer, preço 850.00, categoria Móveis

-- Selecionando todos os dados da tabela 'produtos'
SELECT * FROM produtos;

-- Selecionando o nome e o preço de todos os produtos
SELECT nome, preco FROM produtos;

-- Usando alias para renomear as colunas, nomeando 'produto' para o nome do produto e 'valor' para o preço
SELECT nome AS produto, preco AS valor FROM produtos;

-- Seleção dos dados com alias para a tabela (usando 'p' como alias para a tabela 'produtos')
SELECT p.nome AS produto_nome, p.preco AS valor
FROM produtos AS p;

-- Seleção do nome e da categoria dos produtos, com alias para a tabela 'produtos'
SELECT p.nome AS item, p.categoria AS tipo
FROM produtos AS p;

-- Seleção do nome do produto e do preço final, com alias para a coluna 'preco' como 'preco_final'
SELECT nome AS item, preco AS preco_final 
FROM produtos;

-- Seleção do nome e da categoria, mas com alias para a tabela não é necessário
SELECT nome, categoria FROM produtos AS p; 

-- Seleção do nome do produto e o preço com um reajuste de 10%, usando o alias 'valor_ajustado' para o preço reajustado
SELECT nome , preco * 1.10 AS valor_ajustado
FROM produtos;
