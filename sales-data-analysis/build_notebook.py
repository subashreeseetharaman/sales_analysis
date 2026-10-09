import nbformat as nbf
nb = nbf.v4.new_notebook()
M = lambda s: nbf.v4.new_markdown_cell(s.strip())
C = lambda s: nbf.v4.new_code_cell(s.strip())
nb.cells = [
M("""
# Task 5: Data Analysis on CSV Files
**Objective:** Analyze sales data using Pandas  
**Tools:** Python, Pandas, Matplotlib, Jupyter Notebook  
**Dataset:** `sales_data.csv` (1,000 orders, Jan–Dec 2024)
"""),
M("## 1. Import libraries"),
C("""
import os
import pandas as pd
import matplotlib.pyplot as plt
os.makedirs("charts", exist_ok=True)
plt.rcParams.update({"figure.figsize": (9, 5), "axes.grid": True, "grid.alpha": 0.3})
"""),
M("## 2. Load the CSV file"),C("""
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df.head()
"""),
M("## 3. Explore the data"),
C("""
print("Shape (rows, columns):", df.shape)
print()
df.info()
"""),
C("df.describe()"),
M("## 4. Handle missing values (NaN)"),
C("""
print("Missing values per column:")
print(df.isna().sum())
# Fill missing ratings with the median, missing payment method with 'Unknown'
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].median())
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")
print("\\nMissing values after cleaning:", df.isna().sum().sum())
"""),
M("## 5. Filtering rows, `loc[]` and `iloc[]`"),
C("""
# Filter: high-value orders in the South region
south_big = df[(df["Region"] == "South") & (df["Sales"] > 100000)]
print("South orders above 1,00,000:", len(south_big))
south_big.head()
"""),
C("""
# loc  -> label based  |  iloc -> position based
print(df.loc[0:2, ["Order_ID", "Product", "Sales"]])
print()
print(df.iloc[0:3, 0:4])
"""),
M("## 6. Key metrics"),
C("""
total_sales = df["Sales"].sum()
avg_order = df["Sales"].mean()
total_units = df["Quantity"].sum()
print(f"Total Sales        : {total_sales:,.2f}")
print(f"Average Order Value: {avg_order:,.2f}")
print(f"Total Units Sold   : {total_units:,}")
print(f"Total Orders       : {len(df):,}")
"""),
M("## 7. Sales by Product (`groupby` + `sum` + `plot`)"),
C("""
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print(product_sales)
ax = product_sales.plot(kind="bar", color="#4C78A8")
ax.set_title("Total Sales by Product")
ax.set_xlabel("Product"); ax.set_ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/sales_by_product.png", dpi=150)
plt.show()
"""),
M("## 8. Sales by Region"),
C("""
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)
ax = region_sales.plot(kind="bar", color="#F58518")
ax.set_title("Total Sales by Region")
ax.set_xlabel("Region"); ax.set_ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/sales_by_region.png", dpi=150)
plt.show()
"""),
M("## 9. Sales share by Category"),
C("""
category_sales = df.groupby("Category")["Sales"].sum()
category_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90, ylabel="")
plt.title("Sales Share by Category")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png", dpi=150)
plt.show()
"""),
M("## 10. Monthly sales trend"),
C("""
df["Month"] = df["Date"].dt.to_period("M")
monthly = df.groupby("Month")["Sales"].sum()
monthly.index = monthly.index.astype(str)
ax = monthly.plot(kind="line", marker="o", color="#54A24B")
ax.set_title("Monthly Sales Trend (2024)")
ax.set_xlabel("Month"); ax.set_ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_trend.png", dpi=150)
plt.show()
"""),
M("## 11. Region × Category (stacked bar)"),
C("""
pivot = df.pivot_table(index="Region", columns="Category", values="Sales", aggfunc="sum")
ax = pivot.plot(kind="bar", stacked=True)
ax.set_title("Sales by Region and Category")
ax.set_ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/region_category_stacked.png", dpi=150)
plt.show()
"""),
M("## 12. Payment method usage"),
C("""
df["Payment_Method"].value_counts().plot(kind="bar", color="#B279A2")
plt.title("Orders by Payment Method")
plt.xlabel("Payment Method"); plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/payment_methods.png", dpi=150)
plt.show()
"""),
M("## 13. Insights"),
C("""
top_product = product_sales.idxmax()
top_region = region_sales.idxmax()
top_category = category_sales.idxmax()
best_month = monthly.idxmax()
worst_month = monthly.idxmin()
top_payment = df["Payment_Method"].value_counts().idxmax()
print("KEY INSIGHTS")
print("-" * 50)
print(f"1. Top product        : {top_product} ({product_sales.max():,.0f})")
print(f"2. Top region         : {top_region} ({region_sales.max():,.0f})")
print(f"3. Top category       : {top_category} ({category_sales.max() / total_sales:.1%} of sales)")
print(f"4. Best month         : {best_month} ({monthly.max():,.0f})")
print(f"5. Weakest month      : {worst_month} ({monthly.min():,.0f})")
print(f"6. Most used payment  : {top_payment}")
print(f"7. Average rating     : {df['Customer_Rating'].mean():.2f} / 5")
"""),
M("""
## 14. Interview Questions: quick answers
1. **What is Pandas used for?** Data loading, cleaning, analysis and manipulation of structured (tabular) data.
2. **What's a DataFrame?** A 2-D labelled table with rows and columns, where each column can have a different type.
3. **How do you read a CSV file?** `pd.read_csv("file.csv")`
4. **What is groupby()?** Splits data into groups by a column, applies a function (sum, mean, count) and combines the result: `df.groupby("Region")["Sales"].sum()`
5. **How do you filter rows?** Boolean indexing: `df[df["Sales"] > 1000]`, combine conditions with `&` and `|`.
6. **loc[] vs iloc[]?** `loc` selects by label/condition; `iloc` selects by integer position.
7. **What does .head() do?** Shows the first 5 rows (or `n` rows) of a DataFrame.
8. **How to create a bar chart?** `df.groupby("Region")["Sales"].sum().plot(kind="bar")`
9. **Shape of a DataFrame?** `df.shape` returns `(rows, columns)`.
10. **What is NaN?** "Not a Number": Pandas' marker for missing values. Detect with `isna()`, handle with `fillna()` or `dropna()`.
"""),
]
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nbf.write(nb, "sales_analysis.ipynb")
print("notebook built")