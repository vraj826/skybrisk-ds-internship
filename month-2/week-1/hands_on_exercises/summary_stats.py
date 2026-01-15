import pandas as pd

df = pd.read_csv("data.csv")

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Data Info ---")
print(df.info())
