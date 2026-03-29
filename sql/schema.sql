CREATE DATABASE IF NOT EXISTS estoque_db;
USE estoque_db;

-- USERS
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('admin','funcionario') DEFAULT 'funcionario',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PRODUTOS
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT DEFAULT 0,
    vendidos INT DEFAULT 0,
    reservados INT DEFAULT 0,
    encomendados INT DEFAULT 0,
    status ENUM('ativo','inativo') DEFAULT 'ativo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- VENDAS
CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    user_id INT,
    quantidade INT,
    valor_total DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
