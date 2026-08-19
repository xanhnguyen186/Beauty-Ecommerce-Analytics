import pandas as pd

# 1. load
FILE = "data/raw/Global skincare and Beauty e-store_E-commerce Analysis_English.xlsx"
xls = pd.ExcelFile(FILE)
print("Sheets:", xls.sheet_names)

# 2. check data
df = pd.read_excel(FILE, sheet_name=0)
print("\nshape:", df.shape)
print("\n--- columns & types ---")
print(df.dtypes)
print("\n--- missing values ---")
print(df.isnull().sum())
print("\n--- first rows ---")
print(df.head())

# 3. fix dates
df["Order Date"] = pd.to_datetime(df["Order Date"])

# 4. drop missing values and duplicate rows
df = df.dropna().drop_duplicates()

# 5. save clean version
df.to_csv("data/clean/beauty_clean.csv", index=False)
print("\nsaved -> data/clean/beauty_clean.csv")