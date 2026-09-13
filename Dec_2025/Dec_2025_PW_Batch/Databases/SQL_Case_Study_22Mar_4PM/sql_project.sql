CREATE DATABASE retail_analytics;

USE retail_analytics;

-- Data loaded
SELECT * FROM customer_profiles;
SELECT * FROM product_inventory;
SELECT * FROM sales_transaction;

-- Data Cleaning
-- Step 1: Remove the duplicate values from the above three tables
ALTER TABLE sales_transaction
RENAME COLUMN ï»¿TransactionID TO TransactionID;

ALTER TABLE customer_profiles
RENAME COLUMN ï»¿CustomerID TO CustomerID;

ALTER TABLE product_inventory
RENAME COLUMN ï»¿ProductID TO ProductID;

-- To detect the duplicate records
SELECT TransactionID, count(*) FROM sales_transaction_nodup
GROUP BY TransactionID
HAVING COUNT(*) > 1;

-- Select only distinct records
CREATE TABLE sales_transaction_nodup AS
SELECT DISTINCT * FROM sales_transaction;

DROP TABLE sales_transaction;

ALTER TABLE sales_transaction_nodup
RENAME TO sales_transaction;

-- Write a query to identify the discrepancies in the price of the same product in "sales_transaction" and "product_inventory". 
-- Also, update those discrepancies to match the price in both the tables.
SELECT pi.productID, st.TransactionID, st.Price AS TransactionPrice, pi.Price AS InventoryPrice
FROM sales_transaction st
JOIN product_inventory pi
ON st.ProductID = pi.ProductID
WHERE st.Price <> pi.Price;

-- Update the sales transaction prices to match the inventory prices where discrepancies are found.
SET SQL_SAFE_UPDATES = 0;

UPDATE sales_transaction st
SET Price = (SELECT pi.Price FROM product_inventory pi WHERE st.ProductID = pi.ProductID)
WHERE st.ProductID IN (SELECT ProductID FROM product_inventory pi WHERE st.Price <> pi.Price);

-- NULL values in the dataset
-- Identify the columns which contains null values in the customer_profiles dataset.
-- no missing values 
SELECT count(*) FROM customer_profiles 
WHERE location is NULL;

SELECT count(*) FROM customer_profiles 
WHERE location = '';

-- Replace all the empty location values with unknown
UPDATE customer_profiles
SET location = 'Unknown'
WHERE location = '';


DESC customer_profiles;
DESC sales_transaction;
DESC product_inventory;

-- Change the type of Date-specific columns from text to DATE type
ALTER TABLE sales_transaction
MODIFY COLUMN TransactionDate datetime;

ALTER TABLE customer_profiles
MODIFY JoinDate DATE;

-- Exploratory Data Analysis
-- Write a SQL query to summarize the total sales and quantities sold per product by the company. 
-- ProductID  TotalUnitsSold, TotalSales
SELECT ProductID, SUM(QuantityPurchased) AS TotalUnitsSold, SUM(QuantityPurchased * Price) AS TotalSales
FROM sales_transaction
GROUP BY ProductID
ORDER BY TotalSales DESC;

-- Customer Purchase Frequency
-- Write a SQL query to count the number of transactions per customer to understand purchase frequency. 
SELECT CustomerID, COUNT(TransactionID) AS NumOfTransactions
FROM sales_transaction
GROUP BY CustomerID
ORDER BY NumOfTransactions DESC;

-- Product Categories Performance
-- Write a SQL query to evaluate the performance of the product categories based on the total sales 
-- which help us understand the product categories which needs to be promoted in the marketing campaigns.
-- category		totalunitssold		totalsales
SELECT PI.Category AS Category, SUM(ST.QuantityPurchased) AS Total_Unit_Sold, 
ROUND(SUM(ST.QuantityPurchased * ST.Price), 2) AS Total_Sales
FROM product_inventory PI
JOIN sales_transaction ST
ON PI.ProductID = ST.ProductID
GROUP BY PI.Category
ORDER BY Total_Sales DESC;

-- High Sales Products
-- Write a SQL query to find the top 10 products with the highest total sales revenue from the sales 
-- transactions. This will help the company to identify the High sales products which needs to be focused 
-- to increase the revenue of the company.
-- ProductID	TotalRevenue
SELECT 
    ProductID,
    SUM(QuantityPurchased * Price) AS TotalRevenue
FROM sales_transaction
GROUP BY ProductID
ORDER BY TotalRevenue DESC
LIMIT 10;


-- High Purchase Frequency and Revenue
-- Write a SQL query that describes the number of transaction along with the total amount spent by 
-- each customer which are on the higher side and will help us understand the customers who are the high 
-- frequency purchase customers in the company.
-- The resulting table must have number of transactions more than 10 and TotalSpent more than 1000 on 
-- those transactions by the corresponding customers. 

-- CustomerID	NumberOfTransactions	TotalSpent
SELECT CustomerID, COUNT(*) AS NumberOfTransactions, SUM(Price * QuantityPurchased) AS TotalSpent
FROM sales_transaction
GROUP BY CustomerID 
HAVING NumberOfTransactions > 10 AND TotalSpent > 1000
ORDER BY TotalSpent DESC;

-- Task 1
/* Loyality Indicators
Write a SQL query that describes the duration between the first and the last purchase of the customer 
in that particular company to understand the loyalty of the customer.
Hint: 
1. Use the sales_transaction table.
2. The DATE column will be majorly in use in the question and the TransactionDate column in Sales_transaction is in text format. Thus, the format of the TransactionDate column should be changed.
3. The resulting table must have the first date of purchase, the last date of purchase and the difference between the first and the last date of purchase. 
4. Return the table in descending order.
*/ 

-- Task 2
/* Customer Segmentation based on quantity purchased 
Write a SQL query that segments customers based on the total quantity of products they have purchased. 
Also, count the number of customers in each segment. 
Hint:
1. Use the customer_profiles and sales_transaction tables.
2. To segment customers based on their purchasing behavior for targeted marketing campaigns. Create Customer segments - 

Total Quantity of Products Purchased     Customer Segment
1-10									 Low
11-30									 Mid
>30										 High
The resulting table should be counting the number of customers in different customer segments.
Return the result table in any order.
*/ 








