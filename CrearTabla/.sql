

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS planilla_db;

-- Usar la base de datos
USE planilla_db;

-- Crear tabla empleados
CREATE TABLE IF NOT EXISTS empleados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    edad INT,
    ciudad VARCHAR(100),
    salario DECIMAL(10, 2)
);

-- Insertar datos
INSERT INTO empleados (nombre, edad, ciudad, salario) VALUES 
('Juan', 30, 'Lima', 1500.00),
('Ana', 25, 'Cusco', 1800.00),
('Pedro', 35, 'Arequipa', 2000.00),
('Maria', 40, 'Lima', 2100.00),
('Jose', 28, 'Cusco', 1600.00);


