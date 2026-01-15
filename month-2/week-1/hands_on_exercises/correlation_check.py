import pandas as pd

df = pd.read_csv("data.csv")

correlation = df.corr(numeric_only=True)

print("\n--- Correlation Matrix ---")
print(correlation)
