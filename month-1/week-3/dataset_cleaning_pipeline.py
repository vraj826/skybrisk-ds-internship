# ----------------------------------------------------
# CLIENT PROJECT – DATA CLEANING & AGGREGATION PIPELINE
# Week 3: NumPy and Pandas Only
# ----------------------------------------------------

import pandas as pd
import numpy as np

# Load dataset (ensure "data.csv" exists in same folder)
df = pd.read_csv("data.csv")

print("\n--- Original Dataset ---")
print(df.head())

# Step 1: Remove duplicate rows
df = df.drop_duplicates()


# Step 2: Remove rows with missing values
df = df.dropna()


# Step 3: Compute mean of all numeric columns using Pandas + NumPy
numeric_cols = df.select_dtypes(include=[np.number])
column_means = numeric_cols.mean()

print("\n--- Column-wise Means ---")
print(column_means)


# Step 4: Optional aggregation (if dataset contains a 'Category' column)
if "Category" in df.columns:
    grouped = df.groupby("Category").mean(numeric_only=True)
    print("\n--- Grouped Averages by Category ---")
    print(grouped)

print("\n--- Cleaned Dataset Preview ---")
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)
