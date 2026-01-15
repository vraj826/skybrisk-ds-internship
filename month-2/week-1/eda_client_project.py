import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sample_data.csv")

print("\n--- EDA Report ---")

# Shape & Info
print("\nDataset Shape:", df.shape)
print("\nColumn Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary Stats
print("\nSummary Statistics:")
print(df.describe())

# Correlation
num_df = df.select_dtypes(include="number")
print("\nCorrelation Matrix:")
print(num_df.corr())

# Simple Histogram
plt.hist(num_df.iloc[:,0], bins=15)
plt.title("Distribution of First Numeric Column")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
