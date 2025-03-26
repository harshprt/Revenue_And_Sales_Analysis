
-- SQL Queries for Sales Analysis Project

-- 1. View the first few rows of the sales table
SELECT * FROM sales LIMIT 10;

-- 2. Total Revenue
SELECT SUM(Quantity * Price_Per_Unit) AS Total_Revenue
FROM sales;

-- 3. Revenue by Product
SELECT Product, SUM(Quantity * Price_Per_Unit) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC;

-- 4. Revenue by Region
SELECT Region, SUM(Quantity * Price_Per_Unit) AS Total_Revenue
FROM sales
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- 5. Monthly Revenue
SELECT DATE_TRUNC('month', Order_Date) AS Month, SUM(Quantity * Price_Per_Unit) AS Total_Revenue
FROM sales
GROUP BY DATE_TRUNC('month', Order_Date)
ORDER BY Month;

-- 6. Top Customers
SELECT Customer_Name, SUM(Quantity * Price_Per_Unit) AS Total_Revenue
FROM sales
GROUP BY Customer_Name
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 7. Detect Outliers in Price
SELECT * 
FROM sales
WHERE Price_Per_Unit > 1500 OR Price_Per_Unit < 50;

-- 8. Sales Growth Rate (Month over Month)
WITH Monthly_Revenue AS (
    SELECT DATE_TRUNC('month', Order_Date) AS Month, SUM(Quantity * Price_Per_Unit) AS Total_Revenue
    FROM sales
    GROUP BY DATE_TRUNC('month', Order_Date)
)
SELECT Month, 
       Total_Revenue, 
       LAG(Total_Revenue) OVER (ORDER BY Month) AS Previous_Revenue,
       (Total_Revenue - LAG(Total_Revenue) OVER (ORDER BY Month)) / LAG(Total_Revenue) OVER (ORDER BY Month) * 100 AS Growth_Rate
FROM Monthly_Revenue;
