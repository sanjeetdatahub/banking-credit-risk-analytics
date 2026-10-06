# 🐍 Python Data Analytics Master Handbook & Cheatsheet

Created specifically for **Sanjeet Kumar** as a lifelong reference and interview revision guide.

---

## 📂 Folder Structure

```text
Python-Data-Analytics-Masterclass/
│
├── Python_Data_Analytics_Complete_Guide.ipynb   # Master interactive Jupyter Notebook (Hindi + English)
│
├── data/
│   ├── sample_retail_data.csv                   # 500 rows practice dataset (Electronics, Clothing, Footwear, etc.)
│   └── generate_sample.py                       # Script to regenerate practice data anytime
│
└── README.md                                    # This handbook guide
```

---

## 📑 Topics Covered Inside the Notebook (Module-by-Module)

### 🔹 Module 1: Python Core Foundations for Analysts
- **Variables & Data Types**: `int`, `float`, `str`, `bool`
- **String Cleaning**: `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.split()`, f-strings
- **Data Structures**: Lists (`.append()`, slicing), Dictionaries (`key-value`, `.get()`)
- **Loops & Comprehensions**: `for`, `while`, List & Dict Comprehensions
- **Functions & Lambda**: Custom `def`, Lambda one-liners for `.apply()`

### 🔹 Module 2: NumPy for Numerical Computing & Vectorization
- **1D & 2D Arrays**: Array shapes, dimensions, types
- **Vectorization**: Why NumPy is 50x faster than Python loops
- **Statistical Functions**: `np.mean()`, `np.median()`, `np.std()`, `np.percentile()`
- **Conditional Logic**: `np.where(condition, if_true, if_false)`

### 🔹 Module 3: Pandas Data Wrangling Mastery
- **Data Loading & Inspection**: `.read_csv()`, `.head()`, `.info()`, `.describe()`
- **Filtering**: Multi-condition filtering `&`, `|`, `.isin()`
- **Feature Engineering**: Creating profit margins, binning with `pd.cut()`
- **DateTime Operations**: `pd.to_datetime()`, `.dt.year`, `.dt.month`, `.dt.quarter`, `.dt.day_name()`
- **GroupBy & Aggregations**: `.groupby(['Category']).agg(...)`
- **Pivot Tables**: Cross-tabulating rows and columns (`pd.pivot_table()`)

### 🔹 Module 4: Publication-Grade Visualizations (Matplotlib & Seaborn)
- **Horizontal Bar Charts**: Comparing categories with custom value annotations
- **Time Series Line Charts**: Monthly revenue & profit trajectories with shaded fill
- **Donut Charts**: Category revenue market share
- **Correlation Heatmaps**: Statistical relationships between financial drivers

### 🔹 Module 5: Real-World Business Metrics & Formulas
- **Gross Profit & Gross Margin %**
- **Average Order Value (AOV)**
- **Year-over-Year (YoY) Growth %**
- **Banking Credit Risk Expected Loss**: `EL = PD * LGD * EAD`

### 🔹 Module 6: Top 10 Data Analyst Interview Questions
- `loc` vs `iloc`
- `groupby` vs `pivot_table`
- Handling missing data & outliers (IQR method)
- Vectorization vs `.apply()`

---

## 🚀 Kaise Padhein / Practice Kaise Karein?

Apna Terminal open karein aur yeh command chalayein:

```bash
cd /Users/sanjeetkumar/Desktop/Python-Data-Analytics-Masterclass
jupyter notebook Python_Data_Analytics_Complete_Guide.ipynb
```

Notebook open ho jayegi. Har cell me cursor rakh kar **`Shift + Enter`** dabate jayein aur padhte jayein!
