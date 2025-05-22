-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         11.7.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.10.0.7000
-- --------------------------------------------------------

CREATE DATABASE IF NOT EXISTS telemedicine_db;
USE telemedicine_db;

CREATE TABLE IF NOT EXISTS telemedicine_app_paciente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    symptoms TEXT NOT NULL,
    diagnosis TEXT NOT NULL,
    treatment TEXT NOT NULL
);

INSERT INTO telemedicine_app_paciente (name, age, symptoms, diagnosis, treatment) VALUES
('Juan Perez', 45, 'Fiebre, tos', 'Gripe común', 'Reposo y líquidos'),
('Maria Lopez', 30, 'Dolor de cabeza', 'Migraña', 'Medicamentos analgésicos');
