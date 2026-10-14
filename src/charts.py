from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = BASE_DIR / "images"

IMAGE_DIR.mkdir(exist_ok=True)

import matplotlib.pyplot as plt

# Fictional retail sales data
products = ["Keyboard", "Mouse", "Monitor", "Headphones"]
prices = [499, 299, 2499, 899]
quantities = [12, 20, 5, 8]

# Calculate revenue
revenues = []

for i in range(len(products)):
    revenue = prices[i] * quantities[i]
    revenues.append(revenue)

# Create a bar chart
plt.figure(figsize=(9, 5))

plt.bar(products, revenues, color="mediumpurple")

plt.title("Retail Sales Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (SEK)")

plt.tight_layout()

# For your revenue chart
plt.savefig(IMAGE_DIR / "revenue_chart.png", dpi=300)

# Display the chart
plt.show()


# Second chart - Units sold

plt.figure(figsize=(9, 5))

plt.bar(products, quantities, color="skyblue")

plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")

plt.tight_layout()

# For your units sold chart
plt.savefig(IMAGE_DIR / "units_sold_chart.png", dpi=300)

# Display second chart
plt.show()