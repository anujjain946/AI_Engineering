USE edtech;

SHOW TABLES;

SELECT * FROM products;
SELECT * FROM returns;

-- Query to display the ProductName and the ModelName that have been returned more than 50 times.
-- Approach 1 using subqueries
SELECT p.ProductName, p.ModelName
FROM products p
WHERE (
	SELECT SUM(r.ReturnQuantity)
	FROM Returns r
	WHERE r.ProductKey = p.ProductKey
) > 50;

-- Approach 2 using joins
SELECT P.ProductName, P.ModelName
FROM Products P
JOIN
(SELECT ProductKey, COUNT(*) AS ReturnQuantity
FROM Returns
GROUP BY ProductKey) R
ON R.ProductKey = P.ProductKey
WHERE R.ReturnQuantity > 50;

SELECT P.ProductName, P.ModelName
FROM Products P
JOIN
(SELECT ProductKey, COUNT(*) AS ReturnQuantity
FROM Returns
GROUP BY ProductKey
HAVING ReturnQuantity > 50) R
ON R.ProductKey = P.ProductKey;


/* Query to create the view which contains the records of customerkey, firstname and lastname of 
the customers having totalchildren more than 3
*/
SELECT * FROM customers;

CREATE VIEW big_family AS
(SELECT CustomerKey, FirstName, LastName
FROM customers
WHERE TotalChildren > 3);

-- Retrieve the records from the view
SELECT * FROM big_family;

-- Check the internal query of the view
SHOW CREATE VIEW big_family;

-- Drop the view
DROP VIEW IF EXISTS big_family;

-- Index in Databases
SHOW INDEX FROM customers;

-- Retrieve the CustomerKey, Prefix, FirstName, LastName of those customers whose maritalstatus is 'M'.
SELECT CustomerKey, Prefix, FirstName, LastName
FROM customers
WHERE MaritalStatus = 'M';

-- MySQL scans the whole table to find the customers whose maritalstatus is M and represents married.
EXPLAIN SELECT CustomerKey, Prefix, FirstName, LastName
FROM customers
WHERE MaritalStatus = 'M';

-- Optimization => Create an index for a customerkey column 
CREATE INDEX CustomerKey ON customers (CustomerKey);
SHOW INDEX FROM customers;

-- Drop the indexes
ALTER TABLE customers
DROP INDEX CustomerKey;

DESC customers;

SELECT * FROM courses;
SELECT * FROM learners;

/* In future, if I update any record in the main table of courses
For example if we change the price of the courseID 1 from 1499 to 2499
				OR
For example if we want to delete the courseID 1*/