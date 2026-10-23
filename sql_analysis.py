
import sqlite3

# Connect to database
connection = sqlite3.connect("ecommerce_sales.db")
cursor = connection.cursor()

# 1. Count total orders
cursor.execute("""
    SELECT COUNT(DISTINCT Order_ID)
    FROM sales
""")
print("Total Orders:", cursor.fetchone()[0])

# 2. Count unique customers
cursor.execute("""
    SELECT COUNT(DISTINCT Customer_ID)
    FROM sales
""")
print("Total Customers:", cursor.fetchone()[0])

# 3. Find total sales by product
cursor.execute("""
    SELECT Product, SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY Product
    ORDER BY Total_Sales DESC
""")

print("\nSALES BY PRODUCT")
for row in cursor.fetchall():
    print(row)


# 4. Count orders by status
cursor.execute("""
    SELECT Order_Status, COUNT(DISTINCT Order_ID) AS Total_Orders
    FROM sales
    GROUP BY Order_Status
    ORDER BY Total_Orders DESC
""")

print("\nORDERS BY STATUS")
for row in cursor.fetchall():
    print(row)

# 5. Calculate sales by status
cursor.execute("""
    SELECT Order_Status, SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY Order_Status
    ORDER BY Total_Sales DESC
""")

print("\nSALES BY STATUS")
for row in cursor.fetchall():
    print(row)


# 6. Find sales of Electronics products
cursor.execute("""
    SELECT Product, SUM(Sales) AS Total_Sales
    FROM sales
    WHERE Category = 'Electronics'
    GROUP BY Product
    ORDER BY Total_Sales DESC
""")

print("\nELECTRONICS PRODUCT SALES")

for row in cursor.fetchall():
    print(row)


# 7. Count delivered orders
cursor.execute("""
    SELECT COUNT(DISTINCT Order_ID)
    FROM sales
    WHERE Order_Status = 'Delivered'
""")

print("\nDELIVERED ORDERS:", cursor.fetchone()[0])


# 8. Find products with sales above ₹5,00,000
cursor.execute("""
    SELECT Product, SUM(Sales) AS Total_Sales
    FROM sales
    GROUP BY Product
    HAVING SUM(Sales) > 500000
    ORDER BY Total_Sales DESC
""")

print("\nPRODUCTS WITH SALES ABOVE ₹5,00,000")

for row in cursor.fetchall():
    print(row)


# 9. Create a separate customers table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers AS
    SELECT DISTINCT
        Customer_ID,
        Customer_Name,
        Gender,
        Age,
        City,
        State
    FROM sales
""")

connection.commit()
print("\nCustomers table created successfully!")


# 10. Join sales with customer details
cursor.execute("""
    SELECT
        sales.Order_ID,
        sales.Product,
        sales.Sales,
        customers.Customer_Name,
        customers.City
    FROM sales
    JOIN customers
        ON sales.Customer_ID = customers.Customer_ID
    LIMIT 10
""")

print("\nSALES WITH CUSTOMER DETAILS")

for row in cursor.fetchall():
    print(row)