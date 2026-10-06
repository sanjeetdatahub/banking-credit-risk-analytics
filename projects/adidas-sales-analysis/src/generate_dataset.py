"""
Dataset Generator for Adidas US Sales Analysis.
Generates an authentic, high-quality sales dataset modeled after the standard Adidas US Sales benchmark.
Includes real-world nuances: raw currency strings ($), commas in numbers, percentages, and dates.
"""

import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_adidas_sales_data(num_records=9648, random_state=42):
    np.random.seed(random_state)

    retailers = {
        "Foot Locker": 1185732,
        "Walmart": 1197831,
        "Sports Direct": 1128299,
        "West Gear": 1189833,
        "Kohl's": 1185732,
        "Amazon": 1185732
    }

    regions_data = {
        "Northeast": [
            ("New York", "New York"), ("Maine", "Portland"), ("Massachusetts", "Boston"),
            ("Pennsylvania", "Philadelphia"), ("Rhode Island", "Providence"),
            ("Vermont", "Burlington"), ("Connecticut", "Hartford"), ("New Hampshire", "Manchester")
        ],
        "South": [
            ("Texas", "Houston"), ("Texas", "Dallas"), ("Louisiana", "New Orleans"),
            ("Mississippi", "Jackson"), ("Arkansas", "Little Rock"), ("Oklahoma", "Oklahoma City"),
            ("Alabama", "Birmingham"), ("Tennessee", "Knoxville")
        ],
        "West": [
            ("California", "San Francisco"), ("California", "Los Angeles"), ("Washington", "Seattle"),
            ("Oregon", "Portland"), ("Nevada", "Las Vegas"), ("Colorado", "Denver"),
            ("Utah", "Salt Lake City"), ("Idaho", "Boise"), ("Arizona", "Phoenix"),
            ("New Mexico", "Albuquerque"), ("Montana", "Billings"), ("Wyoming", "Cheyenne"),
            ("Alaska", "Anchorage"), ("Hawaii", "Honolulu")
        ],
        "Midwest": [
            ("Illinois", "Chicago"), ("Michigan", "Detroit"), ("Ohio", "Columbus"),
            ("Indiana", "Indianapolis"), ("Wisconsin", "Milwaukee"), ("Minnesota", "Minneapolis"),
            ("Missouri", "St. Louis"), ("Iowa", "Des Moines"), ("Kansas", "Wichita"),
            ("Nebraska", "Omaha"), ("North Dakota", "Fargo"), ("South Dakota", "Sioux Falls")
        ],
        "Southeast": [
            ("Florida", "Miami"), ("Florida", "Orlando"), ("Georgia", "Atlanta"),
            ("North Carolina", "Charlotte"), ("South Carolina", "Charleston"),
            ("Virginia", "Richmond")
        ]
    }

    products = [
        ("Men's Street Footwear", 50, 75),
        ("Men's Athletic Footwear", 45, 65),
        ("Women's Street Footwear", 40, 70),
        ("Women's Athletic Footwear", 40, 60),
        ("Men's Apparel", 55, 80),
        ("Women's Apparel", 50, 75)
    ]

    sales_methods = ["In-store", "Outlet", "Online"]
    method_weights = [0.35, 0.35, 0.30]

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2021, 12, 31)
    total_days = (end_date - start_date).days

    records = []
    region_names = list(regions_data.keys())
    region_weights = [0.20, 0.20, 0.26, 0.16, 0.18]

    retailer_names = list(retailers.keys())
    retailer_weights = [0.30, 0.12, 0.20, 0.22, 0.08, 0.08]

    for _ in range(num_records):
        ret = np.random.choice(retailer_names, p=retailer_weights)
        ret_id = retailers[ret]

        day_offset = np.random.randint(0, total_days + 1)
        invoice_date = start_date + timedelta(days=int(day_offset))
        is_q4 = invoice_date.month in [10, 11, 12]

        reg = np.random.choice(region_names, p=region_weights)
        state, city = regions_data[reg][np.random.randint(0, len(regions_data[reg]))]

        prod_idx = np.random.randint(0, len(products))
        prod_name, min_price, max_price = products[prod_idx]

        price_per_unit = float(np.random.randint(min_price, max_price + 1))
        method = np.random.choice(sales_methods, p=method_weights)
        if method == "Outlet":
            price_per_unit = round(price_per_unit * 0.85, 2)
        elif method == "Online":
            price_per_unit = round(price_per_unit * 0.95, 2)

        if method == "In-store":
            units = int(np.random.gamma(shape=4.0, scale=80)) + 30
        elif method == "Outlet":
            units = int(np.random.gamma(shape=3.5, scale=70)) + 20
        else: # Online
            units = int(np.random.gamma(shape=3.0, scale=60)) + 15

        if is_q4:
            units = int(units * np.random.uniform(1.2, 1.5))

        total_sales = round(price_per_unit * units, 2)

        base_margin = 0.42 if "Apparel" in prod_name else 0.36
        margin = round(np.clip(np.random.normal(loc=base_margin, scale=0.08), 0.15, 0.65), 2)
        operating_profit = round(total_sales * margin, 2)

        date_str = invoice_date.strftime("%Y-%m-%d")

        records.append({
            "Retailer": ret,
            "Retailer ID": ret_id,
            "Invoice Date": date_str,
            "Region": reg,
            "State": state,
            "City": city,
            "Product": prod_name,
            "Price per Unit": f"${price_per_unit:,.2f}",
            "Units Sold": f"{units:,}",
            "Total Sales": f"${total_sales:,.2f}",
            "Operating Profit": f"${operating_profit:,.2f}",
            "Operating Margin": f"{int(margin*100)}%",
            "Sales Method": method
        })

    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    raw_path = os.path.join(project_root, "data", "raw", "adidas_sales.csv")
    
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    df = generate_adidas_sales_data()
    df.to_csv(raw_path, index=False)
    print(f"Success! Generated {len(df)} records saved to {raw_path}")
