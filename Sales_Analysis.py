# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('C:/tmp/sales_project_export.csv')

# Display the structure of the dataset
print("Dataset Info:")
df.info()

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics of numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Calculate Total Revenue
df['Total_Revenue'] = df['quantity'] * df['price_per_unit']

# Total Revenue by Region
print("\nRevenue by Region:")
revenue_by_region = df.groupby('region')['Total_Revenue'].sum()
print(revenue_by_region)

# Plot Revenue by Region
plt.figure(figsize=(10, 6))
revenue_by_region.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.show()

# Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'], format='%d/%m/%Y')

# Monthly Revenue
print("\nMonthly Revenue:")
monthly_revenue = df.groupby(df['order_date'].dt.to_period('M'))['Total_Revenue'].sum()
print(monthly_revenue)

# Plot Monthly Revenue Trends
plt.figure(figsize=(12, 6))
monthly_revenue.plot(kind='line', marker='o', color='orange')
plt.title('Monthly Revenue Trends')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()

# Top 10 Customers
print("\nTop 10 Customers:")
top_customers = df.groupby('customer_name')['Total_Revenue'].sum().sort_values(ascending=False)
print(top_customers.head(10))

# Plot Top 10 Customers
plt.figure(figsize=(12, 6))
top_customers.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Customers by Total Revenue')
plt.xlabel('Customer Name')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Revenue by Product
print("\nRevenue by Product:")
revenue_by_product = df.groupby('product')['Total_Revenue'].sum().sort_values(ascending=False)
print(revenue_by_product)

# Plot Revenue by Product
plt.figure(figsize=(10, 6))
revenue_by_product.plot(kind='bar', color='purple')
plt.title('Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Detect Outliers in Price Per Unit
print("\nOutliers in Price Per Unit:")
outliers = df[(df['price_per_unit'] < 50) | (df['price_per_unit'] > 1500)]
print(outliers)

# Plot Boxplot for Price Per Unit
plt.figure(figsize=(8, 6))
plt.boxplot(df['price_per_unit'], vert=False, patch_artist=True)
plt.title('Boxplot of Price Per Unit')
plt.xlabel('Price Per Unit')
plt.show()

# Save Outliers to CSV
outliers.to_csv('price_outliers.csv', index=False)
print("Outliers saved to price_outliers.csv")
