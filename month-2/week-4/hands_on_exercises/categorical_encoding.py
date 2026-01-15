import pandas as pd

df = pd.read_csv("data.csv")

encoded_df = pd.get_dummies(df, drop_first=True)

print("Encoded DataFrame:")
print(encoded_df.head())
