"""
Coffee sales analysis (coffee_sales.csv).
This script calculates: the best-selling products, the average order value,
and the average order value broken down by month.
"""

import pandas as pd

df = pd.read_csv('coffee_sales.csv')

# Top 5 best-selling products
product_counts = df["coffee_name"].value_counts()
top_5_products = product_counts.head()
print(f"Top 5 products:\n{top_5_products}")
top_5_products.to_csv('top_5_products.csv')

# Average order value
mean_order_value = round(df["money"].mean(),2)
print(f"Average order value: {mean_order_value}")
pd.Series({"average_order_value": mean_order_value}).to_csv('mean_order_value.csv', header=False)

# Average order value by month
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month_name()

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                'September', 'October', 'November', 'December']

df['month'] = pd.Categorical(df['month'], categories=months_order, ordered=True)

monthly_mean_value = round(df.groupby("month")["money"].mean(),2)
print(f"\nAverage order value by month:\n {monthly_mean_value}")
monthly_mean_value.to_csv('monthly_mean_value.csv')
