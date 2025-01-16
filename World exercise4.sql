SHOW TABLES;

DESCRIBE sakila.actor;

SHOW CREATE TABLE sakila.actor;

SELECT first_name, last_name FROM sakila.actor;

SELECT first_name, last_name FROM sakila.actor WHERE last_name = 'Johansson';

SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS "Actor Name" FROM sakila.actor;

SELECT actor_id, first_name, last_name FROM sakila.actor WHERE first_name = 'Joe';

SELECT last_name FROM sakila.actor GROUP BY last_name HAVING COUNT(*) = 1;

SELECT staff.first_name, staff.last_name, address.address 
FROM staff 
JOIN address ON staff.address_id = address.address_id;

-- WORLD DATABASE EXERCISE
SELECT * FROM city LIMIT 10;

SELECT * FROM city LIMIT 5 OFFSET 15;

SELECT COUNT(*) AS total_rows FROM city;

SELECT name, population 
FROM city 
ORDER BY population DESC 
LIMIT 1;

SELECT name 
FROM city 
WHERE population BETWEEN 670000 AND 700000;

SELECT name, population 
FROM city 
ORDER BY population DESC 
LIMIT 10;

SELECT district 
FROM world.city 
WHERE CountryCode = 'USA' AND population > 3000000;
