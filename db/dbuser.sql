CREATE USER IF NOT EXISTS 'appuser'@'10.0.%' IDENTIFIED BY 'yourpassword';

GRANT ALL PRIVILEGES ON employee_db.* TO 'appuser'@'10.0.%';

FLUSH PRIVILEGES;
