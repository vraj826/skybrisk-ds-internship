# ----------------------------------------------------
# CLIENT PROJECT – DATA CLEANING & AGGREGATION PIPELINE
# Week 3: NumPy and Pandas Only
# ----------------------------------------------------

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

print("\n--- Original Dataset ---")
print(df.head())

df = df.drop_duplicates()
df = df.dropna()

numeric_cols = df.select_dtypes(include=[np.number])
column_means = numeric_cols.mean()

print("\n--- Column-wise Means ---")
print(column_means)

if "Category" in df.columns:
    grouped = df.groupby("Category").mean(numeric_only=True)
    print("\n--- Grouped Averages by Category ---")
    print(grouped)

print("\n--- Cleaned Dataset Preview ---")
print(df.head())

df.to_csv("cleaned_data.csv", index=False)
