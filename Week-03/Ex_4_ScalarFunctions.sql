USE sakila;

-- Warm-up: scalar vs. aggregate
SELECT AVG(rental_rate) FROM film;

SELECT title, rental_rate, ROUND(rental_rate) AS rounded_rate
FROM film;

-- Part A: Conversion functions

-- Step 1
SELECT rental_id, rental_date,
	CAST(rental_date AS DATE) AS rental_day,
	CAST(rental_date AS TIME) AS rental_time
FROM rental
limit 10;

-- Step 2
SELECT title,
CONVERT(rental_rate, CHAR) AS rate_as_text,
	CAST(rental_duration AS DECIMAL(5,2)) AS duration_decimal,
	CAST(rental_rate AS SIGNED) AS rate_as_integer
    FROM film
    LIMIT 10;

-- Step 3
SELECT film_id,
	CONV(film_id, 10, 2) AS binary_id,
    CONV(film_id, 10, 16) AS hex_id
FROM film
WHERE film_id IN (10, 255);

-- Part B: String functions

-- Step 1. Combine and clean names and emails
SELECT customer_id,
	CONCAT_WS(' ', first_name, last_name) AS full_name,
	CONCAT_WS(', ', last_name, first_name) AS directory_name,
	LOWER(email) AS clean_email
FROM customer
LIMIT 10;

-- Step 2. Pull apart and reshape film titles
SELECT title,
	SUBSTRING(title, 1, 3) AS first_three,
	LOWER(title) AS lower_title,
	REPLACE(title, ' ', '_') AS file_name,
	REVERSE(title) AS backwards
FROM film
LIMIT 10;

-- Step 3. Try the remaining string functions on literal values
SELECT TRIM('    Sakila    ') AS trimmed,
		INSERT('ACADEMY DINOSAUR', 1, 7, 'MUSEUM') AS inserted,
		STRCMP('ALIEN', 'ZORRO') AS compare_1,
        STRCMP('ACE', 'ACE') AS compare_2,
        FORMAT(1234567.891, 2) AS formatted;
        
-- Step 4. Proper case. Nest functions to turn MARY into Mary: the first letter upper-case, the rest lower-case.
SELECT first_name,
	CONCAT(UPPER(SUBSTRING(fisrt_name, 1, 1)),
			LOWER(SUBSTRING(first_name, 2))) AS proper_first
	FROM customer
    LIMIT 10;
    
    
    
    






