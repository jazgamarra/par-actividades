-- Permitir acceso remoto al usuario 'parfpuna' desde cualquier IP
GRANT ALL PRIVILEGES ON *.* TO 'parfpuna'@'%' IDENTIFIED BY 'parfpuna' WITH
GRANT OPTION;
FLUSH PRIVILEGES;