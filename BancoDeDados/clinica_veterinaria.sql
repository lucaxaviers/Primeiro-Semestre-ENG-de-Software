-- Criação das tabelas

-- Tabela: tutores
CREATE TABLE tutores (
  id_tutor INT PRIMARY KEY,
  nome VARCHAR(100),
  telefone VARCHAR(20),
  cidade VARCHAR(50)
);

-- Tabela: pacientes
CREATE TABLE pacientes (
  id_paciente INT PRIMARY KEY,
  nome VARCHAR(100),
  especie VARCHAR(50),
  idade INT,
  peso DECIMAL(5,2),
  tutor_id INT,
  FOREIGN KEY (tutor_id) REFERENCES tutores(id_tutor)
);

-- Tabela: consultas
CREATE TABLE consultas (
  id_consulta INT PRIMARY KEY,
  id_paciente INT,
  data DATE,
  valor DECIMAL(8,2),
  procedimento VARCHAR(100),
  FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente)
);

-- Inserção de dados na tabela tutores
INSERT INTO tutores VALUES
(1, 'Ana Silva', '11999999999', 'São Paulo'),
(2, 'Carlos Lima', '11888888888', 'Campinas'),
(3, 'João Souza', '11777777777', 'Sorocaba'),
(4, 'Beatriz Ramos', '11911111111', 'Campinas'),
(5, 'Marcos Tadeu', '11922222222', 'Osasco'),
(6, 'Luciana Costa', '11788888888', 'São Paulo'),
(7, 'Daniel Rocha', '11944444444', 'Jundiaí'),
(8, 'Fernanda Torres', '11666666666', 'Campinas'),
(9, 'Juliano Nogueira', '11955555555', 'Sorocaba'),
(10, 'Marta Fernandes', '11977777777', 'Campinas');

-- Inserção de dados na tabela pacientes
INSERT INTO pacientes VALUES
(1, 'Luna', 'Cachorro', 5, 12.5, 1),
(2, 'Mingau', 'Gato', 3, 4.8, 2),
(3, 'Bob', 'Cachorro', 8, 20.1, 3),
(4, 'Frajola', 'Gato', 2, 3.7, 4),
(5, 'Rex', 'Cachorro', 6, 18.4, 5),
(6, 'Tom', 'Gato', 9, 5.2, 6),
(7, 'Bella', 'Cachorro', 4, 9.5, 7),
(8, 'Nina', 'Gato', 7, 4.3, 8),
(9, 'Pingo', 'Coelho', 1, 2.0, 9),
(10, 'Spike', 'Cachorro', 10, 25.0, 10);

-- Inserção de dados na tabela consultas
INSERT INTO consultas VALUES
(1, 1, '2024-01-10', 120.00, 'Vacinação'),
(2, 2, '2024-01-15', 180.00, 'Exame de sangue'),
(3, 3, '2024-02-01', 250.00, 'Cirurgia'),
(4, 4, '2024-02-20', 100.00, 'Consulta geral'),
(5, 5, '2024-03-05', 300.00, 'Internação'),
(6, 6, '2024-03-10', 180.00, 'Ultrassom'),
(7, 7, '2024-03-12', 120.00, 'Vacinação'),
(8, 8, '2024-04-01', 150.00, 'Consulta geral'),
(9, 9, '2024-04-10', 90.00, 'Curativo'),
(10, 10, '2024-04-15', 200.00, 'Raio-X');

-- Exercícios de SELECT com funções e filtros avançados

-- 1. Liste o nome e idade dos pacientes com idade maior que 5:
SELECT nome, idade
FROM pacientes
WHERE idade > 5;

-- 2. Mostre os nomes dos pacientes ordenados do mais pesado para o mais leve:
SELECT nome, peso
FROM pacientes
ORDER BY peso DESC;

-- 3. Exiba a quantidade de pacientes por espécie:
SELECT especie, COUNT(*) AS total
FROM pacientes
GROUP BY especie;

-- 4. Liste os pacientes com suas respectivas classificações (Felino, Canino ou Outro) usando CASE:
SELECT nome,
  CASE
    WHEN especie = 'Gato' THEN 'Felino'
    WHEN especie = 'Cachorro' THEN 'Canino'
    ELSE 'Outro'
  END AS classificacao
FROM pacientes;

-- 5. Mostre o total de consultas realizadas por paciente:
SELECT id_paciente, COUNT(*) AS total_consultas
FROM consultas
GROUP BY id_paciente;

-- Exercícios de SELECT com JOIN

-- 6. Liste o nome de todos os pacientes e a cidade em que seus tutores moram.
SELECT p.nome AS paciente, t.cidade
FROM pacientes AS p
JOIN tutores AS t ON p.tutor_id = t.id_tutor;

-- 7. Mostre o nome do paciente, a data da consulta e o procedimento realizado.
SELECT p.nome AS paciente, c.data, c.procedimento
FROM consultas AS c
JOIN pacientes AS p ON c.id_paciente = p.id_paciente;

-- 8. Traga o nome do tutor, nome do paciente e o valor das consultas.
SELECT t.nome AS tutor, p.nome AS paciente, c.valor
FROM consultas AS c
JOIN pacientes AS p ON c.id_paciente = p.id_paciente
JOIN tutores AS t ON p.tutor_id = t.id_tutor;

-- 9. Exiba os nomes dos pacientes que tiveram consultas com valor acima de R$ 150,00, junto com o nome de seus tutores.
SELECT p.nome AS paciente, t.nome AS tutor
FROM consultas AS c
JOIN pacientes AS p ON c.id_paciente = p.id_paciente
JOIN tutores AS t ON p.tutor_id = t.id_tutor
WHERE c.valor > 150;

-- 10. Mostre o total de consultas realizadas por cada tutor.
SELECT t.nome AS tutor, COUNT(*) AS total_consultas
FROM consultas AS c
JOIN pacientes AS p ON c.id_paciente = p.id_paciente
JOIN tutores AS t ON p.tutor_id = t.id_tutor
GROUP BY t.nome;
