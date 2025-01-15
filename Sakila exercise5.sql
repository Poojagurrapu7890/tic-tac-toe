SHOW TABLES;
DESCRIBE sakila.actor;
SHOW CREATE TABLE sakila.actor;
SELECT first_name, last_name FROM sakila.actor;

SELECT first_name, last_name FROM sakila.actor WHERE last_name = 'Johansson';
SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS "Actor Name" FROM sakila.actor;



