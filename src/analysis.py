
import pandas as pd
from pathlib import Path

# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Locate the CSV dataset
file_path = BASE_DIR / "data" / "retail_sales.csv"

df = pd.read_csv(file_path)

print("RETAIL SALES DATA")
print("----------------------")
print(df.head())

# Explore the dataset
print("\nDATASET INFORMATION")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Check for missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Calculate revenue for each sale
df["Revenue"] = df["Price"] * df["Quantity"]

# Total revenue
total_revenue = df["Revenue"].sum()

# Total units sold
total_units = df["Quantity"].sum()

# Revenue by product
product_revenue = df.groupby("Product")["Revenue"].sum()

# Units sold by product
product_units = df.groupby("Product")["Quantity"].sum()

# Revenue by category
category_revenue = df.groupby("Category")["Revenue"].sum()

print("\nSALES SUMMARY")
print("----------------------")
print("Total Revenue:", total_revenue, "SEK")
print("Total Units Sold:", total_units)

print("\nREVENUE BY PRODUCT")
print(product_revenue.sort_values(ascending=False))

print("\nUNITS SOLD BY PRODUCT")
print(product_units.sort_values(ascending=False))

print("\nREVENUE BY CATEGORY")
print(category_revenue)

# Save the analysed dataset
output_path = BASE_DIR / "data" / "analysed_sales.csv"
df.to_csv(output_path, index=False)

print("\nAnalysis complete!")
print("Saved:", output_path.name)