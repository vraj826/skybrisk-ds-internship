import pandas as pd

df = pd.read_csv("data.csv")

print("\nMissing Values Before:")
print(df.isnull().sum())

df_filled = df.fillna(df.mean(numeric_only=True))

print("\nMissing Values After Fill:")
print(df_filled.isnull().sum())
