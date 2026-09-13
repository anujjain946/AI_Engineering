-- Creation of a database name "edtech"
CREATE DATABASE IF NOT EXISTS edtech;

-- List all the available databases in MySQL Workbench
SHOW DATABASES;

-- Use the desired database out of the available DBs
USE edtech;

-- Check which specific DB I am currently working
SELECT database();

-- Create table name "employee" working in edtech firm
CREATE TABLE employee(
	empID		int 		auto_increment,
    firstName	varchar(20)	NOT NULL,
    lastName	varchar(20)	NOT NULL,
    Age			int			NOT NULL,
    Salary		int			NOT NULL,
    Location	varchar(20)	NOT NULL,
    PRIMARY KEY(empID)
);

-- Show the tables inside the edtech database
SHOW TABLES;

-- Schema of the table "employee"
DESC employee;
DESCRIBE employee;

-- Insert the records in the employee table
INSERT INTO employee(firstName, lastName, Age, Salary, Location) VALUES ("Priya", "Bhatia", 26, 100000, "Bengaluru");
INSERT INTO employee(firstName, lastName, Age, Salary, Location) VALUES
("Suchitra", "Behera", 24, 50000, "Bengaluru"),
("Palak", "Bhatt", 29, 90000, "Noida"),
("Amit", "Agarwal", 31, 150000, "Noida"), 
("Avneet", "Kaur", 23, 60000, "Bengaluru"),
("Rashmi", "Tanwar", 29, 95000, "Gurugram"),
("Rohan", "Kapoor", 35, 30000, "Pune"),
("Priya", "Sangwan", 26, 100000, "Pune"),
("Priyanshi", "Bhatia", 28, 10000, "Noida"),
("Sudhir", "Bhatt", 34, 200000, "Gurugram");

-- Read the records in the employee table
SELECT * FROM employee;

-- Access the records of the employees having age less than 29
-- WHERE clause which is used for filtering the records in the database
SELECT * FROM employee
WHERE Age < 29;

-- Access firstName, lastName and Salary of the employees which belongs to "Bengaluru"
SELECT firstName, lastName, Salary 
FROM employee 
WHERE Location='Bengaluru';

-- Access all the records where firstName is either Priya OR lastName is Kaur
SELECT * FROM employee 
WHERE firstName='Priya' OR lastName='Kaur';

-- CREATE a new table "courses'
CREATE TABLE courses (
	courseID		int			PRIMARY KEY		auto_increment,
    courseName		varchar(20)	NOT NULL,
    courseDurationMonths	int	NOT NULL,
    courseFee		decimal(10, 2) NOT NULL
);

DESC courses;

-- INSERT the records inside the "courses" table
-- Insert a few course records inside the course table
INSERT INTO courses(courseName,courseDurationMonths,courseFee) VALUES
("Excel Course", 3, 1499),
("DSA Course", 2, 4999),
("SQL Bootcamp", 1, 2999),
("Data Science", 10, 14999);

-- Read the records under courses table
SELECT * FROM courses;

-- Create a new table "Learners"
CREATE TABLE Learners(
Learner_Id INT AUTO_INCREMENT,
LearnerFirstName VARCHAR(50) NOT NULL,
LearnerLastName VARCHAR(50) NOT NULL,
LearnerPhoneNo VARCHAR(15) NOT NULL,
LearnerEmailID VARCHAR(50),
LearnerEnrollmentDate TIMESTAMP NOT NULL,
SelectedCourses INT NOT NULL,
YearsOfExperience INT NOT NULL,
LearnerCompany VARCHAR(50),
SourceOfJoining VARCHAR(50) NOT NULL,
Batch_Start_Date TIMESTAMP NOT NULL,
Location VARCHAR(50) NOT NULL,
PRIMARY KEY(Learner_Id),
UNIQUE KEY(LearnerEmailID),
FOREIGN KEY(SelectedCourses) REFERENCES courses(courseID));

-- Insert a few learners in the courses
INSERT INTO Learners(LearnerFirstName,LearnerLastName,LearnerPhoneNo,LearnerEmailID,LearnerEnrollmentDate,SelectedCourses,YearsOfExperience,LearnerCompany,SourceOfJoining,Batch_Start_Date,Location) VALUES ("Akash", "Mishra", '9998887776', "akash@gmail.com", '2024-01-21', 1, 4, "Amazon", "LinkedIn", '2024-02-29', "Bengaluru");
INSERT INTO Learners(LearnerFirstName,LearnerLastName,LearnerPhoneNo,LearnerEmailID,LearnerEnrollmentDate,SelectedCourses,YearsOfExperience,LearnerCompany,SourceOfJoining,Batch_Start_Date,Location) VALUES("Rishikesh","Joshi","9950192388", "carjkop@gmail.com", '2024-03-19', 3, 2, "HCL", "Youtube", '2024-03-25', "Chennai");
INSERT INTO Learners(LearnerFirstName,LearnerLastName,LearnerPhoneNo,LearnerEmailID,LearnerEnrollmentDate,SelectedCourses,YearsOfExperience,LearnerCompany,SourceOfJoining,Batch_Start_Date,Location) VALUES("Jeevan","Hegde", "9657856732","jeevanhegdek@yahoo.co.in", '2024-01-15', 2, 0, "", "Linkedin", '2024-01-16', "Noida");
INSERT INTO Learners(LearnerFirstName,LearnerLastName,LearnerPhoneNo,LearnerEmailID,LearnerEnrollmentDate,SelectedCourses,YearsOfExperience,LearnerCompany,SourceOfJoining,Batch_Start_Date,Location) VALUES("Akhil","George","7689558930", "akhil.george.8743@gmail.com", '2024-03-13', 3, 4, "Accenture", "Community", '2024-03-25', "Bengaluru");
INSERT INTO Learners(LearnerFirstName,LearnerLastName,LearnerPhoneNo,LearnerEmailID,LearnerEnrollmentDate,SelectedCourses,YearsOfExperience,LearnerCompany,SourceOfJoining,Batch_Start_Date,Location)VALUES("Sidhish","Kumar","6475765443", "sidhishkumar@gmail.com",'2024-01-10', 1, 4, "Meta", "Youtube", '2024-03-29', "Bengaluru");
INSERT INTO Learners(LearnerFirstName,LearnerLastName,LearnerPhoneNo,LearnerEmailID,LearnerEnrollmentDate,SelectedCourses,YearsOfExperience,LearnerCompany,SourceOfJoining,Batch_Start_Date,Location) VALUES("NagaSai","Sreedhar","9182937061", "saisreedhar2001@gmail.com", '2024-03-17', 3, 4, "TCS", "Community", '2024-03-25', "Mumbai");

SELECT * FROM learners;

-- Update the salary of the empID 1 as 200000
UPDATE employee
SET Salary = 200000
WHERE empID = 1;

-- Delete the record having empID as 10
DELETE FROM employee
WHERE empID = 10;

-- Read all the records in the customers table
SELECT * FROM customers;

-- Rename the column name to CustomerKey
ALTER TABLE customers
RENAME COLUMN ï»¿CustomerKey TO CustomerKey;

-- Drop the column named "MyUnknownColumn"
ALTER TABLE customers
DROP COLUMN MyUnknownColumn;

-- Query to find the customers who have more than 2 children
SELECT * 
FROM customers
WHERE TotalChildren>2;

-- Query to find the customers with education level of Bachelors, graduate degrees and High School
SELECT * FROM customers
WHERE EducationLevel IN ("Bachelors", "Graduate Degree", "High School");

-- Query to find the customers with a total number of children between 0 to 2
SELECT * FROM customers
WHERE TotalChildren BETWEEN 0 AND 2;

-- DROP TABLE table_name;

-- Access the record of the employee getting the highest salary and the age is bigger than 25
SELECT * FROM employee
WHERE Age > 25
ORDER BY salary DESC
LIMIT 1;

-- Access the record of the employee getting the second highest salary and the age is bigger than 25
SELECT * FROM employee
WHERE Age > 25
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

