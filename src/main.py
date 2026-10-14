
# Retail Sales Analysis
# Lesson 2 - Analysing Sales Data

products = ["Keyboard", "Mouse", "Monitor", "Headphones"]
prices = [499, 299, 2499, 899]
quantities = [12, 20, 5, 8]

revenues = []

print("RETAIL SALES REPORT")
print("-------------------")

for i in range(len(products)):
    revenue = prices[i] * quantities[i]
    revenues.append(revenue)

    print(f"{products[i]}: {revenue} SEK")

# 1. Calculate total revenue
total_revenue = sum(revenues)

# 2. Calculate total items sold
total_items = sum(quantities)

# 3. Calculate average revenue per product
average_revenue = total_revenue / len(products)

# 4. Find the product with highest revenue
highest_index = revenues.index(max(revenues))
highest_product = products[highest_index]

# 5. Find the product with most units sold
most_sold_index = quantities.index(max(quantities))
most_sold_product = products[most_sold_index]

print("\nSALES ANALYSIS")
print("-------------------")

print(f"Total Revenue: {total_revenue} SEK")
print(f"Total Items Sold: {total_items}")
print(f"Average Revenue: {average_revenue:.2f} SEK")
print(f"Highest Revenue Product: {highest_product}")
print(f"Most Units Sold: {most_sold_product}")