import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data.csv")

X = df.select_dtypes(include="number")

scaler = StandardScaler()
scaled_features = scaler.fit_transform(X)

print("Scaled Features (first 5 rows):")
print(scaled_features[:5])
