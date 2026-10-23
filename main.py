import pandas as pd

# Load the dataset
data = pd.read_csv("ecommerce_sales_data.csv")

# ==============================
# BASIC BUSINESS KPIs
# ==============================

# Total Sales
total_sales = data["Sales"].sum()

# Total Orders
total_orders = data["Order_ID"].nunique()

# Total Customers
total_customers = data["Customer_ID"].nunique()

# Average Order Value
average_order_value = total_sales / total_orders

# Display results
print("\n" + "=" * 50)
print("       E-COMMERCE BUSINESS KPIs")
print("=" * 50)

print("Total Sales       :", round(total_sales, 2))
print("Total Orders      :", total_orders)
print("Total Customers   :", total_customers)
print("Average Order Value:", round(average_order_value, 2))

print("=" * 50)

import pandas as pd

# Load the dataset
data = pd.read_csv("ecommerce_sales_data.csv")

# ==============================
# PRODUCT SALES ANALYSIS
# ==============================

product_sales = data.groupby("Product")["Sales"].sum()

# Sort from highest sales to lowest sales
product_sales = product_sales.sort_values(ascending=False)

print("\n" + "=" * 50)
print("          PRODUCT SALES ANALYSIS")
print("=" * 50)

print(product_sales)

print("=" * 50)

# ==============================
# CATEGORY SALES ANALYSIS
# ==============================

category_sales = data.groupby("Category")["Sales"].sum()

# Sort from highest to lowest
category_sales = category_sales.sort_values(ascending=False)

print("\n" + "=" * 50)
print("          CATEGORY SALES ANALYSIS")
print("=" * 50)

print(category_sales)

print("=" * 50)


# ==============================
# MONTHLY SALES ANALYSIS
# ==============================

# Convert Order_Date into a date format
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

# Extract the month from each order date
data["Month"] = data["Order_Date"].dt.month_name()

# Calculate total sales for each month
monthly_sales = data.groupby("Month")["Sales"].sum()

# Arrange months in calendar order
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_sales = monthly_sales.reindex(month_order).dropna()

print("\n" + "=" * 50)
print("          MONTHLY SALES ANALYSIS")
print("=" * 50)

print(monthly_sales)

print("=" * 50)


# ==============================
# BEST AND WORST SALES MONTH
# ==============================

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

worst_month = monthly_sales.idxmin()
worst_month_sales = monthly_sales.min()

print("\n" + "=" * 50)
print("       BEST AND WORST SALES MONTH")
print("=" * 50)

print("Best Sales Month :", best_month)
print("Best Month Sales : ₹", round(best_month_sales, 2))

print("Lowest Sales Month:", worst_month)
print("Lowest Month Sales: ₹", round(worst_month_sales, 2))

print("=" * 50)


import matplotlib.pyplot as plt

# Check monthly sales data
print("\nMonthly sales data:")
print(monthly_sales)

# Create the chart
plt.figure(figsize=(10, 5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("monthly_sales_chart.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()


# ==========================================
# CHART 2: TOP PRODUCT SALES
# ==========================================

product_sales = data.groupby("Product")["Sales"].sum()
product_sales = product_sales.sort_values(ascending=True)

plt.figure(figsize=(10, 6))
product_sales.plot(kind="barh")
plt.title("Sales by Product")
plt.xlabel("Total Sales (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("product_sales_dashboard.png", dpi=300)
plt.show()


# ==========================================
# CHART 3: ORDER STATUS
# ==========================================

order_status = data["Order_Status"].value_counts()

plt.figure(figsize=(7, 5))
order_status.plot(kind="pie", autopct="%1.1f%%")
plt.title("Order Status Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("order_status_dashboard.png", dpi=300)
plt.show()


# ==========================================
# CHART 4: SALES BY CATEGORY
# ==========================================

category_sales = data.groupby("Category")["Sales"].sum()
category_sales = category_sales.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("category_sales_dashboard.png", dpi=300)
plt.show()

print("All dashboard charts created successfully!")



# ==============================
# PRODUCT SALES CHART
# ==============================

plt.figure(figsize=(10, 6))

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("product_sales_chart.png", dpi=300, bbox_inches="tight")

plt.show()


# ==============================
# CUSTOMER SALES ANALYSIS
# ==============================

customer_sales = data.groupby("Customer_Name")["Sales"].sum()

# Sort from highest to lowest
customer_sales = customer_sales.sort_values(ascending=False)

print("\n" + "=" * 50)
print("          CUSTOMER SALES ANALYSIS")
print("=" * 50)

print(customer_sales)

print("=" * 50)

# ==============================
# TOP CUSTOMER ANALYSIS
# ==============================

top_customer = customer_sales.idxmax()
top_customer_sales = customer_sales.max()

print("\n" + "=" * 50)
print("            TOP CUSTOMER")
print("=" * 50)

print("Customer Name :", top_customer)
print("Total Sales   : ₹", round(top_customer_sales, 2))

print("=" * 50)


# ==============================
# CUSTOMER SALES CHART
# ==============================

plt.figure(figsize=(10, 6))

customer_sales.plot(kind="bar")

plt.title("Total Sales by Customer")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "customer_sales_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==============================
# ORDER STATUS ANALYSIS
# ==============================

order_status = data["Order_Status"].value_counts()

print("\n" + "=" * 50)
print("          ORDER STATUS ANALYSIS")
print("=" * 50)

print(order_status)

print("=" * 50)

# Calculate percentages
status_percentage = data["Order_Status"].value_counts(normalize=True) * 100

print("\nORDER STATUS PERCENTAGES")
print(status_percentage.round(2))


# ==============================
# ORDER STATUS CHART
# ==============================

plt.figure(figsize=(7, 5))

order_status.plot(kind="bar")

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "order_status_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# ==============================
# SALES BY ORDER STATUS
# ==============================

status_sales = data.groupby("Order_Status")["Sales"].sum()

print("\n" + "=" * 50)
print("          SALES BY ORDER STATUS")
print("=" * 50)

print(status_sales)

print("=" * 50)

# Calculate cancelled order percentage by count
cancelled_orders = (data["Order_Status"] == "Cancelled").sum()
total_orders = data["Order_ID"].nunique()

cancellation_rate = (cancelled_orders / total_orders) * 100

print("Cancelled Orders :", cancelled_orders)
print("Total Orders     :", total_orders)
print("Cancellation Rate:", round(cancellation_rate, 2), "%")


# ==============================
# ORDER STATUS PIE CHART
# ==============================

plt.figure(figsize=(7, 7))

order_status.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Delivered vs Cancelled Orders")
plt.ylabel("")

plt.tight_layout()

plt.savefig(
    "order_status_pie_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


import pandas as pd

# Load the dataset
data = pd.read_csv("ecommerce_sales_data.csv")

# 1. Check missing values
print("\nMISSING VALUES")
print(data.isnull().sum())

# 2. Check duplicate rows
print("\nDUPLICATE ROWS")
print(data.duplicated().sum())

# 3. Check dataset size
print("\nDATASET SHAPE")
print(data.shape)

# 4. Check data types
print("\nDATA TYPES")
print(data.dtypes)

# 5. Check duplicate Order IDs
print("\nDUPLICATE ORDER IDs")
print(data["Order_ID"].duplicated().sum())

# 6. Check invalid quantities
print("\nINVALID QUANTITIES")
print((data["Quantity"] <= 0).sum())

# 7. Check invalid prices
print("\nINVALID PRICES")
print((data["Unit_Price"] <= 0).sum())

# 8. Check discount values
print("\nINVALID DISCOUNTS")
print(
    ((data["Discount_Percent"] < 0) |
     (data["Discount_Percent"] > 100)).sum()
)

# 9. Check order status values
print("\nORDER STATUS COUNTS")
print(data["Order_Status"].value_counts())


# ==========================================
# FINAL BUSINESS KPI REPORT
# ==========================================

total_sales = data["Sales"].sum()
total_orders = data["Order_ID"].nunique()
total_customers = data["Customer_ID"].nunique()
average_order_value = total_sales / total_orders

cancelled_orders = data.loc[
    data["Order_Status"] == "Cancelled", "Order_ID"
].nunique()

cancellation_rate = (cancelled_orders / total_orders) * 100

print("\n" + "=" * 45)
print(" E-COMMERCE SALES ANALYTICS REPORT")
print("=" * 45)

print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Cancelled Orders: {cancelled_orders}")
print(f"Cancellation Rate: {cancellation_rate:.2f}%")

print("=" * 45)


# ==========================================
# BUSINESS INSIGHTS REPORT
# ==========================================

print("\n" + "=" * 55)
print("       E-COMMERCE BUSINESS INSIGHTS")
print("=" * 55)

# 1. Best-selling product by recorded sales value
product_sales = data.groupby("Product")["Sales"].sum()
top_product = product_sales.idxmax()
top_product_sales = product_sales.max()

print("\n1. TOP PRODUCT")
print("Product:", top_product)
print(f"Recorded Sales Value: Rs. {top_product_sales:,.2f}")

# 2. Highest-performing category
category_sales = data.groupby("Category")["Sales"].sum()
top_category = category_sales.idxmax()
top_category_sales = category_sales.max()

category_share = (top_category_sales / data["Sales"].sum()) * 100

print("\n2. TOP CATEGORY")
print("Category:", top_category)
print(f"Recorded Sales Value: Rs. {top_category_sales:,.2f}")
print(f"Share of Recorded Sales: {category_share:.2f}%")

# 3. Best month
data["Order_Date"] = pd.to_datetime(data["Order_Date"])
monthly_sales = data.groupby(
    data["Order_Date"].dt.to_period("M")
)["Sales"].sum()

best_month = monthly_sales.idxmax()
worst_month = monthly_sales.idxmin()

print("\n3. MONTHLY PERFORMANCE")
print("Best Month:", best_month)
print(f"Best Month Sales: Rs. {monthly_sales.max():,.2f}")
print("Lowest Month:", worst_month)
print(f"Lowest Month Sales: Rs. {monthly_sales.min():,.2f}")

# 4. Order status analysis
status_counts = data.groupby("Order_Status")["Order_ID"].nunique()

print("\n4. ORDER STATUS")
for status, count in status_counts.items():
    print(f"{status} Orders: {count}")

# 5. Customer with the highest recorded sales value
customer_sales = data.groupby("Customer_Name")["Sales"].sum()
top_customer = customer_sales.idxmax()

print("\n5. TOP CUSTOMER BY RECORDED SALES VALUE")
print("Customer:", top_customer)
print(f"Recorded Sales Value: Rs. {customer_sales.max():,.2f}")

print("\n" + "=" * 55)
print("       END OF BUSINESS INSIGHTS")
print("=" * 55)
