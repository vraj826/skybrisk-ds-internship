import pandas as pd

df = pd.read_csv("data.csv")

print("Dataset Loaded")
print(df.head())
print("\nTarget distribution:")
print(df.iloc[:, -1].value_counts())
