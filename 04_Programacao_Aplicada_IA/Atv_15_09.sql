-- 1. Criar o banco loja
CREATE DATABASE loja;
USE loja;

-- 2. Criar a tabela produtos
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco DECIMAL(10,2),
    estoque INT
);

-- 3. Inserir pelo menos 5 produtos
INSERT INTO produtos (nome, categoria, preco, estoque) VALUES
('Notebook Gamer', 'Eletrônicos', 4500.00, 10),
('Smartphone X', 'Eletrônicos', 2500.00, 25),
('Mouse Sem Fio', 'Acessórios', 89.90, 50),
('Teclado Mecânico', 'Acessórios', 150.00, 30),
('Cadeira Ergonômica', 'Móveis', 1200.00, 5);

-- 4. Listar todos os produtos
SELECT * FROM produtos;

-- 5. Buscar produtos com preço maior que R$ 100
SELECT * FROM produtos 
WHERE preco > 100.00;

-- 6. Atualizar o preço de um produto
UPDATE produtos 
SET preco = 95.00 
WHERE id = 3;

-- 7. Atualizar o estoque
UPDATE produtos 
SET estoque = 8 
WHERE id = 1;

-- 8. Excluir um produto
DELETE FROM produtos 
WHERE id = 4;

-- 9. Ordenar pelo preço (do mais barato ao mais caro)
SELECT * FROM produtos 
ORDER BY preco ASC;


-- DESAFIO EXTRA:

-- Criar a tabela categorias
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50)
);

-- Inserir algumas categorias de exemplo
INSERT INTO categorias (nome) VALUES 
('Eletrônicos'), 
('Acessórios'), 
('Móveis');

-- Adicionar categoria_id INT em produtos
ALTER TABLE produtos 
ADD COLUMN categoria_id INT;

-- Declarar a FOREIGN KEY relacionando as duas tabelas
ALTER TABLE produtos 
ADD CONSTRAINT fk_produtos_categorias
FOREIGN KEY (categoria_id) REFERENCES categorias(id);

-- (Opcional) Remover a coluna antiga de texto 'categoria' para limpar o banco
ALTER TABLE produtos 
DROP COLUMN categoria;
