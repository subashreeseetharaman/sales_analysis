"""Generates a realistic sample sales dataset -> sales_data.csv"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 1000

products = {
    "Laptop": ("Electronics", 55000),
    "Smartphone": ("Electronics", 22000),
    "Headphones": ("Electronics", 2500),
    "Office Chair": ("Furniture", 7500),
    "Desk": ("Furniture", 12000),
    "Notebook": ("Stationery", 120),
    "Pen Set": ("Stationery", 250),
    "Backpack": ("Accessories", 1800),
    "Water Bottle": ("Accessories", 600),
}
names = list(products)
product = rng.choice(names, n, p=[.08, .14, .16, .06, .05, .17, .14, .1, .1])
dates = pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 366, n), unit="D")

df = pd.DataFrame({
    "Order_ID": [f"ORD{1000 + i}" for i in range(n)],
    "Date": dates,
    "Region": rng.choice(["North", "South", "East", "West"], n, p=[.22, .3, .2, .28]),
    "Product": product,
    "Category": [products[p][0] for p in product],
    "Quantity": rng.integers(1, 8, n),
    "Unit_Price": [round(products[p][1] * rng.uniform(0.9, 1.1), 2) for p in product],
    "Payment_Method": rng.choice(["UPI", "Credit Card", "Debit Card", "Cash"], n, p=[.4, .25, .2, .15]),
    "Customer_Rating": rng.choice([1, 2, 3, 4, 5], n, p=[.05, .08, .17, .4, .3]).astype(float),
})
df["Sales"] = (df["Quantity"] * df["Unit_Price"]).round(2)

# Add a few missing values (NaN) so the notebook can demonstrate handling them
df.loc[rng.choice(n, 40, replace=False), "Customer_Rating"] = np.nan
df.loc[rng.choice(n, 15, replace=False), "Payment_Method"] = np.nan

df = df.sort_values("Date").reset_index(drop=True)
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
df.to_csv("sales_data.csv", index=False)
print(f"Saved sales_data.csv with {len(df)} rows")
