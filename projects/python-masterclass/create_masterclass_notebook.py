"""
Script to generate the comprehensive, masterclass Python Data Analytics Notebook.
Formatted with structured modules, detailed Hindi+English (Hinglish) explanations,
code examples, exercises, and interview Q&As.
"""

import json
import os

def build_masterclass_notebook():
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    def add_md(content):
        notebook["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in content.split("\n")]
        })

    def add_code(content):
        notebook["cells"].append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in content.split("\n")]
        })

    # Header
    add_md("""# 🐍 Python for Data Analysis: The Complete Master Handbook & Cheatsheet
### *By Sanjeet Kumar — Data Analyst & Business Intelligence Specialist*

---
## 📖 Is Notebook Ka Maksad (Purpose):
Agar aap Python ka syntax, functions, ya methods bhool jate hain, toh yeh notebook aapka **Ultimate Revision Companion** hai.
Isme **Basic Python se lekar Advanced Data Analytics (NumPy, Pandas, Matplotlib, Seaborn, Business KPIs, Interview Q&A)** tak sab kuch structured format me **Hinglish (Hindi + English)** me detail me samjhaya gaya hai.

---
## 📑 Index / Vishay-Suchi:
1. **Module 1**: Python Core Foundations for Data Analysts (Variables, Strings, Lists, Dicts, Loops, Functions, Lambda)
2. **Module 2**: NumPy Masterclass (Arrays, Vectorization, Indexing, Slicing, Statistics, np.where)
3. **Module 3**: Pandas Data Wrangling Mastery (DataFrames, Cleaning, Missing Values, Filtering, GroupBy, Pivot, DateTime)
4. **Module 4**: Publication-Grade Visualization (Matplotlib & Seaborn: Line, Bar, Donut, Heatmaps, Subplots)
5. **Module 5**: Real-World Business Analytics Formulas (Margin %, YoY Growth, AOV, Banking Expected Loss)
6. **Module 6**: Interview Revision & Top 10 Data Analyst Q&A with Hinglish Explanations
""")

    # Module 1: Python Core Foundations
    add_md("""---
# 🧩 MODULE 1: Python Core Foundations for Data Analysts
Data analysis me Python ka sabse bada kaam data clean karna aur logic build karna hota hai.

### 1.1 Variables & Data Types (Variables aur Data Types)
- **int**: Integer (Pura number) jaise `10`, `500`
- **float**: Decimal number jaise `10.5`, `99.99`
- **str**: String (Text) single `'...'` ya double `"..."` quotes me
- **bool**: Boolean (`True` ya `False`)""")

    add_code("""# Variables and Data Types Example
age = 26                     # int
salary = 45000.75            # float
name = "Sanjeet Kumar"       # str
is_analyst = True            # bool

# type() function se kisi bhi variable ka type pata chalta hai
print(f"Name: {name} | Type: {type(name)}")
print(f"Age: {age} | Type: {type(age)}")
print(f"Salary: {salary} | Type: {type(salary)}")
print(f"Is Analyst?: {is_analyst} | Type: {type(is_analyst)}")""")

    add_md("""### 1.2 String Manipulation (Data Cleaning Me Sabse Zyada Kaam Aane Wale String Methods)
Raw data me aksar space, dollar signs, ya mixed case hote hain. Unhe clean karne ke liye:
- `.strip()`: Shuru aur aakhiri ke extra spaces hatata hai.
- `.lower()` / `.upper()`: Text ko chhota ya bada karta hai.
- `.replace(old, new)`: Kisi character ko dusre se replace karta hai (jaise `$` ya `,` hatana).
- `.split(delimiter)`: Text ko tukdo me tod kar list banata hai.
- **f-strings**: Text ke andar variable inject karne ka sabse aasan tareeqa: `f"Hello {name}"`""")

    add_code("""messy_price = "   $1,250.50   "

# Step 1: Strip extra whitespace
clean_step1 = messy_price.strip()

# Step 2: Replace dollar sign and comma
clean_step2 = clean_step1.replace("$", "").replace(",", "")

# Step 3: Convert string to float
final_price = float(clean_step2)

print(f"Original String: '{messy_price}'")
print(f"Cleaned Number:  {final_price} (Type: {type(final_price)})")

# Split example: Full name se First and Last name nikalna
full_name = "Sanjeet Kumar Aryan"
parts = full_name.split(" ")
print(f"First Name: {parts[0]}, Last Name: {parts[-1]}")""")

    add_md("""### 1.3 Lists & Dictionaries (Data Structures Jo Roz Use Hote Hain)
- **List `[...]`**: Ordered collection jisme items add (`.append()`), remove, ya modify kiye ja sakte hain.
- **Dictionary `{key: value}`**: Key-Value pairs jisme row/column ka data map hota hai.""")

    add_code("""# 1. LIST OPERATIONS
sales = [1200, 1500, 1800, 2200, 2600]

sales.append(3100)        # Naya sale add kiya
first_sale = sales[0]     # Pehla element (0-indexed)
last_sale = sales[-1]     # Aakhiri element
slice_sales = sales[1:4]  # Index 1 se 3 tak

print(f"Total elements: {len(sales)}")
print(f"First: {first_sale}, Last: {last_sale}")
print(f"Sliced List: {slice_sales}")

# 2. DICTIONARY OPERATIONS
customer_profile = {
    "customer_id": "C-101",
    "name": "Sanjeet Kumar",
    "city": "Bengaluru",
    "credit_score": 750,
    "annual_income": 850000
}

# Accessing values
print(f"Customer Name: {customer_profile['name']}")
print(f"City: {customer_profile.get('city')}")

# Adding new key-value pair
customer_profile["risk_tier"] = "Prime"
print("Updated Dictionary:", customer_profile)""")

    add_md("""### 1.4 Loops & List Comprehensions (Loops Aur Fast One-Liners)
Jab list ke har item par koi calculation karni ho, tab hum Loops ya **List Comprehension** use karte hain.
- Normal loop: 3-4 lines leta hai.
- List comprehension: 1 single line me fast execute hota hai.""")

    add_code("""# Problem: Har price par 18% GST add karna hai

prices = [100, 250, 500, 1200, 2000]

# Tareeqa 1: Normal For Loop
prices_with_tax_loop = []
for p in prices:
    prices_with_tax_loop.append(round(p * 1.18, 2))

# Tareeqa 2: List Comprehension (Pythonic & Fast!)
# Syntax: [expression for item in list]
prices_with_tax_comp = [round(p * 1.18, 2) for p in prices]

print("Loop Output:         ", prices_with_tax_loop)
print("Comprehension Output:", prices_with_tax_comp)

# Filtering with List Comprehension: Sirf wo prices lo jo 500 se zyada hain
high_value_prices = [p for p in prices if p >= 500]
print("High Value Items:    ", high_value_prices)""")

    add_md("""### 1.5 Custom Functions & Lambda Functions (Code Ko Reusable Banana)
- **`def function_name(args):`**: Bada logic bar-bar likhne se bachata hai.
- **`lambda arguments: expression`**: Chhota anonymous 1-line function jo Pandas ke `.apply()` me bohot use hota hai.""")

    add_code("""# 1. Custom Function: Credit Risk Tier categorize karna
def assign_risk_tier(credit_score, dti_ratio):
    \"\"\"
    Borrower ka credit score aur DTI ratio dekhkar Risk Tier batata hai.
    \"\"\"
    if credit_score >= 750 and dti_ratio <= 35:
        return "Low Risk (Prime)"
    elif credit_score >= 650 and dti_ratio <= 45:
        return "Medium Risk (Near Prime)"
    else:
        return "High Risk (Subprime)"

# Test function
print("Applicant 1:", assign_risk_tier(780, 28))
print("Applicant 2:", assign_risk_tier(610, 52))

# 2. Lambda Function (Chhota 1-liner function)
# Syntax: lambda x: calculation
calculate_margin = lambda revenue, profit: round((profit / revenue) * 100, 2)
print(f"Profit Margin: {calculate_margin(100000, 38500)}%")""")

    # Module 2: NumPy
    add_md("""---
# 🔢 MODULE 2: NumPy for Numerical Computing & Vectorization
**NumPy (Numerical Python)** data science ki foundation hai. Yeh normal Python lists se **50x zyada fast** hoti hai kyunki yeh C-language me optimized array operations use karti hai.

### 2.1 NumPy Arrays Create Karna
- `np.array(list)`: List ko NumPy array me convert karta hai.
- `np.arange(start, stop, step)`: Sequence of numbers banata hai.
- `np.zeros(shape)` / `np.ones(shape)`: Zero ya One se bhari array.
- `np.random.normal(mean, std, size)`: Bell-curve normal distribution generate karta hai.""")

    add_code("""import numpy as np

# 1D Array
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr_1d)
print("Shape:", arr_1d.shape, "| Data Type:", arr_1d.dtype)

# 2D Array (Matrix - Rows and Columns)
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("\\n2D Array (2 Rows, 3 Columns):\\n", arr_2d)
print("Shape:", arr_2d.shape)

# Random numbers for simulations
sales_samples = np.random.normal(loc=5000, scale=800, size=5)
print("\\nRandom Sales Samples:\\n", np.round(sales_samples, 2))""")

    add_md("""### 2.2 Vectorization (Kyun NumPy Python Loops Se 50x Fast Hai?)
Normal Python me agar list ke sabhi numbers ko 2 se multiply karna ho toh loop chalana padta hai.
NumPy me direct `arr * 2` likh sakte hain — isko **Vectorization** bolte hain.""")

    add_code("""# Vectorization Example:
prices = np.array([100, 200, 300, 400, 500])
quantities = np.array([2, 5, 1, 4, 3])

# Vectorized Multiplication: Har index ke elements aapas me multiply honge
total_revenues = prices * quantities
print("Prices:       ", prices)
print("Quantities:   ", quantities)
print("Total Revenue:", total_revenues)  # Output: [ 200 1000  300 1600 1500]""")

    add_md("""### 2.3 Statistical Functions & `np.where()` (Interview Ka Favorite!)
Data analysis me descriptive statistics nikalne ke liye:
- `np.mean()`, `np.median()`, `np.std()` (Standard Deviation)
- `np.percentile(arr, 95)` (95th percentile nikalna)
- `np.where(condition, value_if_true, value_if_false)` (Excel ke `IF()` jaisa)""")

    add_code("""loan_amounts = np.array([5000, 12000, 25000, 45000, 80000, 150000, 250000])

print("Mean Loan Amount:  $", np.mean(loan_amounts))
print("Median Loan Amount:$", np.median(loan_amounts))
print("Standard Deviation: ", round(np.std(loan_amounts), 2))
print("90th Percentile:   $", np.percentile(loan_amounts, 90))

# np.where() Example:
# Agar loan amount 50,000 se zyada hai toh "Large Exposure", warna "Standard Exposure"
exposure_category = np.where(loan_amounts > 50000, "Large Exposure", "Standard Exposure")
print("\\nExposure Categories:")
for amt, cat in zip(loan_amounts, exposure_category):
    print(f"  ${amt:<8} -> {cat}")""")

    # Module 3: Pandas
    add_md("""---
# 🐼 MODULE 3: Pandas Data Wrangling Mastery (The Core Tool)
Pandas data analyst ka sabse important tool hai. Real-world business data tabular format (**DataFrame**) me hota hai.

### 3.1 Data Load Karna Aur First Look Inspection
- `pd.read_csv('filepath')`: CSV file load karta hai.
- `.head(n)`: Pehle n rows dikhata hai.
- `.info()`: Column names, non-null counts, aur data types batata hai.
- `.describe()`: Mean, min, max, 25%, 50%, 75% summary deta hai.""")

    add_code("""import pandas as pd

# Load practice dataset
data_path = 'data/sample_retail_data.csv'
df = pd.read_csv(data_path)

print(f"Shape: {df.shape[0]} Rows, {df.shape[1]} Columns\\n")
display(df.head(3))""")

    add_code("""# Data Structure & Summary
print("--- DataFrame Info ---")
df.info()

print("\\n--- Numerical Statistics Summary ---")
display(df.describe())""")

    add_md("""### 3.2 Filtering & Subsetting Data (Data Ko Filter Karna)
- **Single condition**: `df[df['Category'] == 'Electronics']`
- **Multiple conditions**: `df[(df['City'] == 'Delhi') & (df['Total_Amount'] > 20000)]`
  - Note: Multiple conditions me `and` ki jagah `&` aur `or` ki jagah `|` use karte hain, aur brackets `(...)` lagana zaroori hota hai!
- **`.isin(['val1', 'val2'])`**: Multiple values match karne ke liye.""")

    add_code("""# Example 1: Sirf Electronics Category ka data
electronics_df = df[df['Category'] == 'Electronics']
print(f"Electronics records: {len(electronics_df)}")

# Example 2: Delhi ya Mumbai me 15,000 se zyada ke transactions
metro_high_sales = df[
    (df['City'].isin(['Delhi', 'Mumbai'])) & 
    (df['Total_Amount'] > 15000)
]
print(f"High-Value Metro Sales: {len(metro_high_sales)}")
display(metro_high_sales[['Date', 'City', 'Sub_Category', 'Quantity', 'Total_Amount', 'Profit']].head(3))""")

    add_md("""### 3.3 Feature Engineering & `.apply()` (Naye Columns Banana)
Naye columns banana business insights ke liye bohot zaroori hota hai:
1. **Profit Margin %**: `(Profit / Total_Amount) * 100`
2. **Profitability Status**: `.apply()` use karke "High Profit", "Moderate", "Loss" tag karna.""")

    add_code("""# 1. Vectorized Calculation (Fast!)
df['Margin_Pct'] = ((df['Profit'] / df['Total_Amount']) * 100).round(2)

# 2. .apply() with custom function
def tag_performance(margin):
    if margin >= 30:
        return 'High Margin'
    elif margin >= 15:
        return 'Healthy Margin'
    elif margin >= 0:
        return 'Low Margin'
    else:
        return 'Loss Making'

df['Performance_Tier'] = df['Margin_Pct'].apply(tag_performance)

print("Distribution of Performance Tiers:")
print(df['Performance_Tier'].value_counts())""")

    add_md("""### 3.4 DateTime Mastery (Dates Ko Analyze Karna)
Dates string format me hoti hain (`"2023-05-14"`). Pehle unhe datetime object banate hain:
`df['Date'] = pd.to_datetime(df['Date'])`
Iske baad hum asaani se `.dt.year`, `.dt.month`, `.dt.day_name()`, `.dt.quarter` nikaal sakte hain.""")

    add_code("""# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract temporal dimensions
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%b')
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)
df['Day_of_Week'] = df['Date'].dt.day_name()

display(df[['Date', 'Month_Name', 'Quarter', 'Day_of_Week']].head(3))""")

    add_md("""### 3.5 GroupBy & Aggregations (Pandas Ka Sabse Powerful Feature!)
Business me sawal hote hain:
- *"Kaunse category ka total revenue aur average margin sabse zyada hai?"*
- *"Kaunsi city me sabse zyada orders aaye?"*
Iske liye hum `df.groupby('Column').agg(...)` use karte hain.""")

    add_code("""# Category Performance Summary
category_summary = df.groupby('Category').agg(
    Total_Revenue=('Total_Amount', 'sum'),
    Total_Profit=('Profit', 'sum'),
    Total_Units=('Quantity', 'sum'),
    Average_Margin=('Margin_Pct', 'mean'),
    Order_Count=('Transaction_ID', 'count')
).reset_index()

category_summary['Profit_Margin_Pct'] = ((category_summary['Total_Profit'] / category_summary['Total_Revenue']) * 100).round(2)
category_summary = category_summary.sort_values(by='Total_Revenue', ascending=False)

print("--- Category Performance Table ---")
display(category_summary)""")

    add_md("""### 3.6 Pivot Tables (Excel Pivot Table Ka Python Version)
Jab rows aur columns dono me categories ko cross-tabulate karna ho:
`pd.pivot_table(df, index='City', columns='Category', values='Total_Amount', aggfunc='sum')`""")

    add_code("""# City vs Category Revenue Matrix
pivot_city_cat = pd.pivot_table(
    df,
    index='City',
    columns='Category',
    values='Total_Amount',
    aggfunc='sum',
    fill_value=0
)

print("--- City vs Category Revenue Pivot Table ($) ---")
display(pivot_city_cat.round(0).head(5))""")

    # Module 4: Data Visualization
    add_md("""---
# 📊 MODULE 4: Data Visualization Mastery with Matplotlib & Seaborn
Charts dekhkar business stakeholders ko turant samajh aata hai.
- **Matplotlib**: Core chart framework (axes, titles, figure size, annotations).
- **Seaborn**: Statistical styling, palettes, heatmaps, and distributions.

### 4.1 Global Visual Style Setup
Hamesha clean professional aesthetic use karein.""")

    add_code("""import matplotlib.pyplot as plt
import seaborn as sns

# Styling Setup
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['figure.dpi'] = 110

# Coordinated Color Palette
PALETTE = {
    'primary': '#0055A5',    # Adidas Royal Blue
    'secondary': '#0D9488',  # Teal
    'accent': '#E63946',     # Coral Red
    'dark': '#1E293B',       # Dark Slate
    'amber': '#F59E0B'       # Amber Gold
}

print("✅ Visualization styling initialized!")""")

    add_md("""### 4.2 Bar Charts With Value Annotations (Horizontal Bar Chart)
Bar charts categories ko compare karne ke liye best hote hain. Value labels add karne se chart self-explanatory ban jata hai.""")

    add_code("""# Top Cities by Total Revenue
city_rev = df.groupby('City')['Total_Amount'].sum().sort_values(ascending=True) / 1e5  # in Lakhs

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(city_rev.index, city_rev.values, color=PALETTE['primary'], alpha=0.85, height=0.6)

ax.set_xlabel('Total Sales in Lakhs (INR)')
ax.set_title('City-Wise Total Sales Performance')
ax.grid(axis='x', linestyle='--', alpha=0.5)

# Value annotations on each bar
for bar in bars:
    w = bar.get_width()
    ax.annotate(f'₹{w:.1f}L', 
                xy=(w, bar.get_y() + bar.get_height()/2),
                xytext=(5, 0), textcoords='offset points', 
                va='center', fontweight='bold', fontsize=9)

ax.set_xlim(0, city_rev.max() * 1.15)
plt.tight_layout()
plt.show()""")

    add_md("""### 4.3 Time Series Line Chart (Monthly Sales & Profit Trend)
Waqt ke sath sales badh rahi hai ya ghat rahi hai, yeh dekhne ke liye Line Plot best hai.""")

    add_code("""# Monthly Aggregation
monthly = df.groupby(['Month', 'Month_Name']).agg(
    Revenue=('Total_Amount', 'sum'),
    Profit=('Profit', 'sum')
).reset_index().sort_values(by='Month')

fig, ax = plt.subplots(figsize=(11, 4.5))

ax.plot(monthly['Month_Name'], monthly['Revenue'] / 1e3, marker='o', color=PALETTE['primary'], linewidth=2.5, label='Monthly Revenue (k)')
ax.plot(monthly['Month_Name'], monthly['Profit'] / 1e3, marker='s', color=PALETTE['accent'], linewidth=2, linestyle='--', label='Monthly Profit (k)')
ax.fill_between(monthly['Month_Name'], monthly['Revenue'] / 1e3, color=PALETTE['primary'], alpha=0.1)

ax.set_ylabel('Amount in Thousands (INR)')
ax.set_title('Monthly Revenue & Profitability Trajectory (2023)')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
plt.tight_layout()
plt.show()""")

    add_md("""### 4.4 Donut Chart (Category Share Distribution)
Market share ya revenue composition dikhane ke liye Donut Chart standard hota hai.""")

    add_code("""cat_rev = df.groupby('Category')['Total_Amount'].sum()

fig, ax = plt.subplots(figsize=(7, 5))
colors = [PALETTE['primary'], PALETTE['secondary'], PALETTE['accent'], PALETTE['amber']]

wedges, texts, autotexts = ax.pie(
    cat_rev,
    labels=cat_rev.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2),
    pctdistance=0.75
)

for at in autotexts:
    at.set_fontweight('bold')
    at.set_color('white')

ax.set_title('Revenue Contribution by Product Category', pad=15)
plt.tight_layout()
plt.show()""")

    add_md("""### 4.5 Correlation Heatmap (Seaborn Heatmap)
Kaunse numeric variables aapas me correlated hain (Price, Quantity, Discount, Profit) dekhne ke liye Heatmap use karte hain.""")

    add_code("""numeric_cols = ['Price', 'Quantity', 'Discount_Pct', 'Total_Amount', 'Profit', 'Margin_Pct']
corr = df[numeric_cols].corr()

plt.figure(figsize=(7.5, 5.5))
sns.heatmap(
    corr,
    annot=True,
    fmt='.2f',
    cmap='Blues',
    square=True,
    linewidths=1.2,
    cbar_kws={'label': 'Correlation Coefficient'}
)
plt.title('Correlation Matrix: Financial & Operational Drivers', pad=15)
plt.xticks(rotation=30, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()""")

    # Module 5: Real-World Business Formulas
    add_md("""---
# 💼 MODULE 5: Real-World Business Analytics Formulas & Metrics
Interview me aur corporate analysis me yeh formulas sabse zyada puche jate hain:

| Metric Name | Business Meaning | Exact Formula |
| :--- | :--- | :--- |
| **Gross Profit** | Bikri se direct cost hatane ke baad bacha munafa | `Revenue - COGS (Cost of Goods Sold)` |
| **Gross Margin %** | Har 100 rupaye ki bikri me kitna % profit bacha | `(Gross Profit / Revenue) * 100` |
| **Average Order Value (AOV)** | Ek customer ek order me average kitna kharch karta hai | `Total Revenue / Total Number of Orders` |
| **YoY Growth %** | Pichle saal ke mukable is saal kitni growth hui | `((Current Year - Last Year) / Last Year) * 100` |
| **Expected Loss (Banking)** | Loan portfolio me kitna loss hone ka risk hai | `EL = PD * LGD * EAD` |
""")

    add_code("""# Calculating Business Metrics in Code:
total_rev = df['Total_Amount'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
total_units = df['Quantity'].sum()

overall_margin = (total_profit / total_rev) * 100
aov = total_rev / total_orders
units_per_order = total_units / total_orders

print("="*55)
print("          EXECUTIVE BUSINESS PERFORMANCE SCORECARD")
print("="*55)
print(f"💰 Total Gross Revenue:     ₹{total_rev:,.2f}")
print(f"📈 Total Operating Profit:  ₹{total_profit:,.2f}")
print(f"🎯 Overall Profit Margin:   {overall_margin:.2f}%")
print(f"🛒 Average Order Value:     ₹{aov:,.2f}")
print(f"📦 Average Basket Size:     {units_per_order:.1f} items / order")
print("="*55)""")

    # Module 6: Interview Questions
    add_md("""---
# 🎯 MODULE 6: Top 10 Python Data Analyst Interview Questions (With Hinglish Answers)

### Q1: `loc` aur `iloc` me kya antar hai?
- **Answer**: 
  - `loc`: **Label-based** hota hai (Column ka naam aur Index label leta hai). Jaise: `df.loc[0, 'City']`.
  - `iloc`: **Integer index-based** hota hai (Rows aur columns ke numeric positions leta hai). Jaise: `df.iloc[0, 3]`.

### Q2: `groupby` aur `pivot_table` me kya farak hai?
- **Answer**:
  - `groupby`: Data ko 1D summary table me summarize karta hai (Series ya standard DataFrame).
  - `pivot_table`: Data ko 2D matrix me cross-tabulate karta hai (Rows me ek category aur Columns me doosri category).

### Q3: Missing values ko handle karne ke kya rules hain?
- **Answer**:
  1. Agar data 5% se kam missing hai aur row drop karne se fark nahi padta, toh `.dropna()` kar sakte hain.
  2. Numerical columns me Mean (agar normal ho) ya Median (agar outliers hon) se fill karte hain: `.fillna(df['Price'].median())`.
  3. Categorical columns me Mode (most frequent value) ya `'Unknown'` se fill karte hain.

### Q4: Outliers kaise detect karte hain?
- **Answer**:
  1. **Visual method**: Box Plot draw karke.
  2. **IQR Method (Interquartile Range)**: $Q1$ (25th percentile) aur $Q3$ (75th percentile) nikaalte hain. $IQR = Q3 - Q1$. Jo values $Q1 - 1.5 \\times IQR$ se chhoti ya $Q3 + 1.5 \\times IQR$ se badi hoti hain, wo outliers hoti hain.

### Q5: Pandas me `.apply()` aur Vectorization me kya difference hai?
- **Answer**:
  - **Vectorization**: Direct array mathematics use karta hai (e.g., `df['A'] * df['B']`), yeh C-level par run hota hai aur fastest hota hai.
  - **`.apply()`**: Python level par har row/element par function loop chalata hai, isliye yeh thoda slow hota hai lekin complex `if-else` logic ke liye useful hai.
""")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Python_Data_Analytics_Complete_Guide.ipynb")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2)
    print(f"✅ Masterclass Jupyter Notebook created successfully at: {out_path}")

if __name__ == "__main__":
    build_masterclass_notebook()
