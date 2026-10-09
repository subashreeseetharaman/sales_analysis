# Task 5: Data Analysis on CSV Files

Sales data analysis using **Python, Pandas and Matplotlib** (Python Developer Internship, Elevate Labs).

## What I did
- Loaded `sales_data.csv` (1,000 orders, Jan–Dec 2024) with `pd.read_csv()`
- Explored it with `head()`, `info()`, `describe()` and `shape`
- Found and handled missing values (NaN) with `isna()` and `fillna()`
- Filtered rows and compared `loc[]` vs `iloc[]`
- Used `groupby()`, `sum()` and `plot()` to build charts
- Wrote quick answers to the 10 interview questions at the end of the notebook

## Project structure
```
sales-data-analysis/
├── sales_analysis.ipynb   # main notebook (already executed, charts visible)
├── sales_data.csv         # dataset
├── generate_data.py       # script that created the dataset
├── requirements.txt
├── charts/                # saved chart images
└── README.md
```

## How to run
```bash
pip install -r requirements.txt
jupyter notebook sales_analysis.ipynb
```
Then click **Kernel → Restart & Run All**. Charts are re-saved into `charts/`.

Or upload `sales_analysis.ipynb` and `sales_data.csv` to Google Colab and run all cells.

## Charts
| Chart | File |
|---|---|
| Sales by Product | `charts/sales_by_product.png` |
| Sales by Region | `charts/sales_by_region.png` |
| Sales share by Category | `charts/sales_by_category.png` |
| Monthly sales trend | `charts/monthly_trend.png` |
| Region × Category (stacked) | `charts/region_category_stacked.png` |
| Orders by Payment Method | `charts/payment_methods.png` |

## Key insights
- **Top product:** Laptop (about 1.53 crore in sales)
- **Top region:** West
- **Top category:** Electronics, about 85% of total sales
- **Best month:** July 2024; **weakest month:** September 2024
- **Most used payment method:** UPI
- **Average customer rating:** 3.80 / 5

## Tools
Python · Pandas · Matplotlib · Jupyter Notebook
