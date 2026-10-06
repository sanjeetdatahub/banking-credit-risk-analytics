"""
Sample Retail Dataset Generator for Python Practice Notebooks.
"""
import pandas as pd
import numpy as np

def generate_sample_data():
    np.random.seed(42)
    n = 500

    cities = ["Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai", "Hyderabad", "Pune", "Patna", "Jaipur", "Lucknow"]
    categories = {
        "Electronics": ["Smartphone", "Laptop", "Headphones", "Smartwatch"],
        "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers"],
        "Home & Kitchen": ["Mixer Grinder", "Cookware Set", "Water Purifier", "Air Fryer"],
        "Footwear": ["Formal Shoes", "Running Shoes", "Sandals", "Casual Loafers"]
    }

    dates = pd.date_range(start="2023-01-01", end="2023-12-31", periods=n)

    records = []
    for i in range(n):
        cat = np.random.choice(list(categories.keys()))
        sub_cat = np.random.choice(categories[cat])
        city = np.random.choice(cities)
        qty = np.random.randint(1, 10)
        
        # Base prices
        price_map = {"Smartphone": 22000, "Laptop": 55000, "Headphones": 2500, "Smartwatch": 4000,
                     "T-Shirt": 800, "Jeans": 2200, "Jacket": 3500, "Sneakers": 3200,
                     "Mixer Grinder": 3000, "Cookware Set": 2400, "Water Purifier": 12000, "Air Fryer": 6500,
                     "Formal Shoes": 2800, "Running Shoes": 3600, "Sandals": 1200, "Casual Loafers": 2100}
        
        base_price = price_map[sub_cat]
        price = round(base_price * np.random.uniform(0.9, 1.15), 2)
        discount = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], p=[0.3, 0.25, 0.25, 0.15, 0.05])
        
        total_amount = round((price * qty) * (1 - discount), 2)
        cost_price = round(price * np.random.uniform(0.60, 0.75), 2)
        profit = round(total_amount - (cost_price * qty), 2)

        records.append({
            "Transaction_ID": f"TXN-{10000+i}",
            "Date": dates[i].strftime("%Y-%m-%d"),
            "Customer_Name": f"Customer_{i+1}",
            "City": city,
            "Category": cat,
            "Sub_Category": sub_cat,
            "Price": price,
            "Quantity": qty,
            "Discount_Pct": discount,
            "Total_Amount": total_amount,
            "Cost_Price": cost_price,
            "Profit": profit
        })

    df = pd.DataFrame(records)
    out_path = "/Users/sanjeetkumar/Desktop/banking-credit-risk-analytics/python-masterclass/data/sample_retail_data.csv"
    df.to_csv(out_path, index=False)
    print(f"Sample dataset saved to {out_path} with {len(df)} rows.")

if __name__ == "__main__":
    generate_sample_data()
