CREATE DATABASE IF NOT EXISTS employee_db;

USE employee_db;

CREATE TABLE IF NOT EXISTS employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  skill VARCHAR(50),
  location VARCHAR(50),
  experience_years INT,
  available BOOLEAN
);

