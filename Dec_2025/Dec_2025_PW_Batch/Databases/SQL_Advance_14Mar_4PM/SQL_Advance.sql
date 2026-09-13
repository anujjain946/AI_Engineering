USE edtech;

SHOW TABLES;

SELECT * FROM courses;
SELECT * FROM learners;

-- learnerFirstName, learnerLastName, selectedcourse, courseName
-- INNER JOIN
SELECT LearnerFirstName, LearnerLastName, SelectedCourses, CourseName
FROM learners l
INNER JOIN courses c
ON l.SelectedCourses = c.courseID;

-- RIGHT JOIN
SELECT LearnerFirstName, LearnerLastName, SelectedCourses, CourseName
FROM learners l
RIGHT JOIN courses c
ON l.SelectedCourses = c.courseID;

-- LEFT JOIN
SELECT LearnerFirstName, LearnerLastName, SelectedCourses, CourseName
FROM learners l
LEFT JOIN courses c
ON l.SelectedCourses = c.courseID;


SELECT * FROM customers;

DESC customers;

-- Subqueries
-- Convert the dtype of AnnualIncome to numeric type
-- Step 1: Data preprocessing
SET SQL_SAFE_UPDATES = 0;

UPDATE customers
SET AnnualIncome = REPLACE(REPLACE(AnnualIncome, '$', ''), ',', '');

UPDATE customers
SET AnnualIncome = null
WHERE AnnualIncome IN ('N/A', 'NA', 'unknown', '');


-- Step 2: Dtype conversion
ALTER TABLE customers
MODIFY COLUMN AnnualIncome DECIMAL(10,2);

/* Filter the records based on the annualincome of the customers where the annualincome 
is more than the average income */
-- 
SELECT CustomerKey, FirstName, LastName, AnnualIncome
FROM customers
WHERE AnnualIncome > (SELECT AVG(AnnualIncome) AS avg_income FROM customers);

SELECT * FROM products;

/* Filter the records of the products which are more expensive than the average price 
of the product */
SELECT * FROM products
WHERE 
ProductCost > (SELECT AVG(ProductPrice) FROM products);

-- Margin => ProductPrice - ProductCost
/* Calculate the margin of each product and then filter the records where the margin is more
than 100 */
SELECT * 
FROM
(SELECT ProductKey, ProductName, ProductPrice, ProductCost, 
ROUND((ProductPrice - ProductCost), 2) AS ProductMargin
FROM products) as PMargin
WHERE ProductMargin > 100;

-- Window Functions
SELECT * FROM employee;

-- Query to get the maximum salary per location
SELECT Location, MAX(Salary) AS max_salary
FROM Employee
GROUP BY Location;


INSERT INTO employee(firstName, lastName, Age, Salary, Location) VALUES ("Atul", "Bhatt", 26, 200000, "Bengaluru");

/* Query to get the maximum salary per location with the details of the employee
FirstName	LastName	Location	Salary
Priya		Bhatia		Bengaluru	200000
Atul		Bhatt		Bengaluru 	200000
Amit		Agarwal		Noida		150000
....
*/
-- Approach 1: This is a big failure
SELECT firstName, lastName, Location, MAX(salary) AS max_salary
FROM employee
GROUP BY firstName, lastName, Location;

-- Approach 2: Subquery 
SELECT firstName, lastName, Location, Salary
FROM employee e
WHERE Salary = (SELECT MAX(Salary) FROM employee WHERE Location = e.Location);

-- Approach 3: via Inner Join
SELECT 
    e.FirstName,
    e.LastName,
    e.Salary AS Max_Salary,
    e.Location
FROM Employee e
JOIN (
    SELECT Location, MAX(Salary) AS Max_Salary
    FROM Employee
    GROUP BY Location
) m
ON e.Location = m.Location
AND e.Salary = m.Max_Salary;


-- Window Functions
SELECT firstName, lastName, Location, Salary,
ROW_NUMBER() OVER (PARTITION BY Location ORDER BY Salary DESC)
AS row_num
FROM employee;

SELECT firstName, lastName, Location, Salary,
RANK() OVER (PARTITION BY Location ORDER BY Salary DESC)
AS rank_salary
FROM employee;


SELECT firstName, lastName, Location, Salary,
DENSE_RANK() OVER (PARTITION BY Location ORDER BY Salary DESC)
AS rank_salary
FROM employee;

-- CTE => Common Table Expression
WITH ranked_employee AS (
SELECT firstName, lastName, Location, Salary,
DENSE_RANK() OVER (PARTITION BY Location ORDER BY Salary DESC)
AS rank_salary
FROM employee)
SELECT * FROM ranked_employee
WHERE rank_salary = 1;
